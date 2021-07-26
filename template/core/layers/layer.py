import pygame

from typing import NoReturn
from abc import abstractmethod

from core.timestep import Timestep


class Layer:

    @abstractmethod
    def on_attach(self) -> NoReturn:
        pass

    @abstractmethod
    def on_detach(self) -> NoReturn:
        pass

    @abstractmethod
    def on_event(self, event: pygame.event.Event) -> NoReturn:
        pass

    @abstractmethod
    def on_update(self, ts: Timestep) -> NoReturn:
        pass

    @abstractmethod
    def on_render(self, context: pygame.Surface) -> NoReturn:
        pass
