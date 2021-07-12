import pygame

from typing import NoReturn

from core.renderer.window import Window


class WindowToolkit:

    def __init__(self, handle: Window) -> NoReturn:
        self.__handle = handle

    @property
    def handle(self) -> Window:
        return self.__handle

    @property
    def normolized_mouse_position(self) -> pygame.Vector2:
        scaled_mouse_position = pygame.Vector2(pygame.mouse.get_pos()) \
            / self.__handle.scale_factor

        return scaled_mouse_position - self.__handle.view_surface_blend / self.__handle.scale_factor
