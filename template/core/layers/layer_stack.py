from typing import Callable, NoReturn

from core.layers.layer import Layer
from core.layers.ilayer_collection import ILayerCollection


class LayerStack(ILayerCollection):

    def __init__(self) -> NoReturn:
        self.__layers = list()

    def add_layer(self, layer: Layer) -> NoReturn:
        self.__layers.append(layer)

    def remove_layer(self, layer: Layer) -> NoReturn:
        if not layer in self.__layers:
            raise ValueError(f"Layer Stack does not contain layer: {layer}. Yoc cannot remove it.")

        self.__layers.pop(self.__layers.index(layer))

    def on_(self, action: Callable) -> NoReturn:
        for layer in self.__layers:
            action(layer)
