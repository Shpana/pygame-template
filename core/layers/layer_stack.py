from typing import Callable, NoReturn

from core.layers.layer import Layer


class LayerStack:

    def __init__(self) -> NoReturn:
        self.__layers = list()

    @property
    def layers(self) -> list[Layer]:
        return self.__layers

    def add_layer(self, layer: Layer) -> NoReturn:
        self.__layers.append(layer)

    def on_(self, action: Callable) -> NoReturn:
        for layer in self.__layers:
            action(layer)
