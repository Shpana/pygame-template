import pygame

from typing import NoReturn

from core.application_startup_options import ApplicationStartupOptions

from core.timestep import Timestep
from core.renderer.window import Window
from core.renderer.window_viewport import WindowViewSpecification
from core.renderer.window_toolkit import WindowToolkit
from core.events.event_dispatcher import EventDispatcher
from core.layers.layer import Layer
from core.layers.layer_stack import LayerStack


class Application:

    def __init__(self, options: ApplicationStartupOptions) -> NoReturn:
        self.__options = options

        self.__prepare_platform()

        self.__clock = pygame.time.Clock()

        self.__layer_stack = LayerStack()
        self.__running = True
        self.__title = self.__options.title

        self.__window = Window(
            self.__title,
            WindowViewSpecification(
                self.__options.resolution, self.__options.is_smoothed), self.__options.viewport_resolution
        )

        # TODO: Избавиться от WindowToolkit.
        self.__window_toolkit = WindowToolkit(self.__window)

    @property
    def window_toolkit(self) -> WindowToolkit:
        return self.__window_toolkit

    def add_layer(self, layer: Layer) -> NoReturn:
        self.__layer_stack.add_layer(layer)

    def run(self) -> NoReturn:
        self.__begin_session()
        while self.__running:
            self.__process_main_loop()
        self.__finish_session()

    @property
    def __max_frame_rate(self) -> float:
        return 60

    def __process_main_loop(self) -> NoReturn:
        render_context = self.__window.render_context

        self.__clock.tick(self.__max_frame_rate)

        self.__window.update(self.__on_event)
        self.__window.prepare(pygame.Color(18, 18, 18))

        time_step = Timestep(self.__clock.get_time())
        self.__layer_stack.on_(lambda layer: layer.on_update(time_step))
        self.__layer_stack.on_(lambda layer: layer.on_render(render_context))

        self.__window.render()

    def __on_resize(self, event: pygame.event.Event) -> NoReturn:
        self.__window.on_resize(event)

    def __on_close(self, event: pygame.event.Event) -> NoReturn:
        self.__running = False

    def __on_event(self, event: pygame.event.Event) -> NoReturn:
        dispatcher = EventDispatcher(event)

        dispatcher.dispatch(pygame.VIDEORESIZE, self.__on_resize)
        dispatcher.dispatch(pygame.QUIT, self.__on_close)
        dispatcher.dispatch_key_down(pygame.K_ESCAPE, self.__on_close)

        self.__layer_stack.on_(lambda layer: layer.on_event(event))

    def __prepare_platform(self) -> NoReturn:
        pygame.init()
        pygame.key.set_repeat(1000, 50)

    def __shutdown_platform(self) -> NoReturn:
        pygame.quit()

    def __begin_session(self) -> NoReturn:
        self.__layer_stack.on_(lambda layer: layer.on_attach())

    def __finish_session(self) -> NoReturn:
        self.__shutdown_platform()
        self.__layer_stack.on_(lambda layer: layer.on_detach())
