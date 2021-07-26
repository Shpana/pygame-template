import pygame

from typing import NoReturn


class WindowViewFormat:

    def __init__(self) -> NoReturn:
        self.__format = 0

    @property
    def format(self) -> int:
        return self.__format

    def apply_pygame_format(self, format: int) -> NoReturn:
        self.__format |= format


class WindowViewport:

    def __init__(self, resolution: pygame.Vector2) -> NoReturn:
        self.__scale_factor = 1.0
        self.__resolution = resolution
        # NOTE: На этой поверхности будет рисоваться
        # вообще всё. А потом она увеличивается и рисуется на окне.
        self.__surface = pygame.Surface(resolution)

    @property
    def scale_factor(self) -> float:
        return self.__scale_factor

    @property
    def render_context(self) -> pygame.Surface:
        return self.__surface

    @property
    def view_surface(self) -> pygame.Surface:
        # NOTE: Тут как раз и изменяется размер
        # поверхности, причем поверхность увеличивается в scale_factor раз.
        scaled_resolution = self.__resolution * self.__scale_factor

        return pygame.transform.scale(
            self.__surface, (int(scaled_resolution.x), int(scaled_resolution.y))
        )

    @property
    def smoothed_view_surface(self) -> pygame.Surface:
        # NOTE: Очень затратная на вычисления функция,
        # для увеличения производительности можно использовать view_surface,
        # но получается не сглаженная поверхность.
        scaled_resolution = self.__resolution * self.__scale_factor

        return pygame.transform.smoothscale(
            self.__surface, (int(scaled_resolution.x), int(scaled_resolution.y))
        )

    def prepare_context(self, color: pygame.Color) -> NoReturn:
        self.__surface.fill(color)

    def on_resize(self, event: pygame.event.Event) -> NoReturn:
        factor_x = event.w / self.__resolution.x
        factor_y = event.h / self.__resolution.y
        # NOTE: Перещитывается scale_factor, чтобы
        # поверхность, которая будет показываться увеличивалась в
        # корректное количество раз. И это как раз минимум от отношения нового
        # размера окна и фиксированного, по горизонтали и вертикали.
        self.__scale_factor = min(factor_x, factor_y)
