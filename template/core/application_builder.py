from typing import NoReturn

from core.layers.layer import Layer
from core.layers.layer_stack import LayerStack

from core.application import Application
from core.application_startup_options import ApplicationStartupOptions


class ApplicationBuilder:

    def __init__(self) -> NoReturn:
        self.__layers_to_instantiate = list()
        self.__options = self.__default_application_options

    def build(self) -> Application:
        layer_stack = LayerStack()

        for layer in self.__layers_to_instantiate:
            layer_stack.add_layer(layer())

        return Application(self.__options, layer_stack)

    def use_layer(self, layer: Layer) -> 'ApplicationBuilder':
        self.__layers_to_instantiate.append(layer)
        return self

    def enable_smoothing(self) -> 'ApplicationBuilder':
        self.__options.is_smoothing = True
        return self

    def disable_smoothing(self) -> 'ApplicationBuilder':
        self.__options.is_smoothing = False
        return self

    def with_title(self, title: str) -> 'ApplicationBuilder':
        self.__options.title = title
        return self

    def with_resolution(self, resolution: tuple[int, int]) -> 'ApplicationBuilder':
        self.__options.resolution = resolution
        return self

    def with_viewport_resolution(self, resolution: tuple[int, int]) -> 'ApplicationBuilder':
        self.__options.viewport_resolution = resolution
        return self

    @property
    def __default_application_options(self) -> ApplicationStartupOptions:
        return ApplicationStartupOptions(
            title="pygame-template",
            is_smoothed=False,
            resolution=(1000, 600),
            viewport_resolution=(900, 600),
        )
