from abc import abstractmethod
from typing import Protocol, NoReturn, Callable

from core.layers.layer import Layer


class ILayerCollection(Protocol):

    @abstractmethod
    def add_layer(self, layer: Layer) -> NoReturn:
        raise NotImplementedError()

    @abstractmethod
    def remove_layer(self, layer: Layer) -> NoReturn:
        raise NotImplementedError()

    # NOTE: Может этому методу здесь не место. Мб надо выделить новый интерфейс.
    @abstractmethod
    def on_(self, action: Callable) -> NoReturn:
        raise NotImplementedError()
