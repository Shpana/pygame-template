import pygame

from typing import Callable, NoReturn


class EventDispatcher:

    def __init__(self, handle: pygame.event.Event) -> NoReturn:
        self.__handle = handle

    def dispatch(self, event_type: int, callback: Callable, **kwargs) -> NoReturn:
        if self.__is_correct_type(event_type):
            callback(self.__handle, **kwargs)

    def dispatch_mouse_button_up(self, button: int, callback: Callable, **kwargs) -> NoReturn:
        if self.__is_correct_type(pygame.MOUSEBUTTONUP) and self.__handle.button == button:
            callback(self.__handle, **kwargs)

    def dispatch_mouse_button_down(self, button: int, callback: Callable, **kwargs) -> NoReturn:
        if self.__is_correct_type(pygame.MOUSEBUTTONDOWN) and self.__handle.button == button:
            callback(self.__handle, **kwargs)

    def dispatch_key_up(self, key: int, callback: Callable, **kwargs) -> NoReturn:
        if self.__is_correct_type(pygame.KEYUP) and self.__handle.key == key:
            callback(self.__handle, **kwargs)

    def dispatch_key_down(self, key: int, callback: Callable, **kwargs) -> NoReturn:
        if self.__is_correct_type(pygame.KEYDOWN) and self.__handle.key == key:
            callback(self.__handle, **kwargs)

    def dispatch_keyboard_shortcut(self, keymod: int, key: int, callback: Callable, **kwargs) -> NoReturn:
        if self.__is_correct_type(pygame.KEYDOWN) and self.__handle.key == key and self.__handle.mod & keymod:
            callback(self.__handle, **kwargs)

    def __is_correct_type(self, type: int) -> bool:
        return self.__handle.type == type
