import pygame

from typing import Callable, NoReturn

from core.renderer.window_viewport import WindowViewport
from core.renderer.window_viewport import WindowViewFormat
from core.renderer.window_viewport import WindowViewSpecification


class Window:

    def __init__(self, title: str,
                 specification: WindowViewSpecification, viewport_resolution: tuple[int, int]) -> NoReturn:
        pygame.display.set_caption(title)
        self.__specification = specification
        self.__title = title
        self.__resolution = specification.resolution_as_vector

        self.__format = WindowViewFormat()
        self.__format.apply_pygame_format(pygame.RESIZABLE)

        self.__viewport = WindowViewport(pygame.Vector2(viewport_resolution))

        self.__native_surface = pygame.display.set_mode(specification.resolution, self.__format.format)
        self.__refresh_display()

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value: str) -> NoReturn:
        self.__title = value
        pygame.display.set_caption(value)

    @property
    def scale_factor(self) -> float:
        return self.__viewport.scale_factor

    @property
    def view_surface_blend(self) -> pygame.Vector2:
        return pygame.Vector2(self.__native_surface.get_rect().center) \
               - pygame.Vector2(self.__viewport.view_surface.get_rect().center)

    @property
    def render_context(self) -> pygame.Surface:
        return self.__viewport.render_context

    def on_resize(self, event: pygame.event.Event) -> NoReturn:
        self.__viewport.on_resize(event)

        self.__resolution = pygame.Vector2(event.w, event.h)
        self.__native_surface = pygame.display.set_mode(
            (int(self.__resolution.x), int(self.__resolution.y)), self.__format.format)

    def update(self, event_callback: Callable) -> NoReturn:
        pygame.display.update()

        # NOTE: Тут вот обрабатывается очередь событий
        # и эти события отправляются в event_callback, где после они будет обрабатываться.
        for event in pygame.event.get():
            event_callback(event)

    def prepare(self, color: pygame.Color = pygame.Color(0, 0, 0)) -> NoReturn:
        # NOTE: Тут подготавливаются поверхности к слудующему кадру,
        # потому что если этого не делать, то все, что было на предыдущем кадре
        # попадет и на этот, а это плохо.
        self.__viewport.prepare_context(color)

    def render(self) -> NoReturn:
        # NOTE: Здесь увеличенная поверхность рисуется на поверхности окна.
        if self.__specification.is_smoothed:
            self.__native_surface.blit(
                self.__viewport.smoothed_view_surface, self.view_surface_blend)
        else:
            self.__native_surface.blit(self.__viewport.view_surface, self.view_surface_blend)

    def __refresh_display(self) -> NoReturn:
        resolution = self.__specification.resolution

        self.on_resize(pygame.event.Event(
            pygame.VIDEORESIZE, size=resolution, w=resolution[0], h=resolution[1]))
