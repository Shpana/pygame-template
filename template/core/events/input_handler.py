import pygame

from typing import NoReturn


class InputHandler:

    def __init__(self) -> NoReturn:
        self.__key_state = pygame.key.get_pressed()
        self.__mouse_button_state = pygame.mouse.get_pressed()

    def is_key_pressed(self, key: int)-> bool:
        return self.__key_state[key]

    def is_mouse_button_pressed(self, button: int)-> bool:
        return self.__mouse_button_state[button]
