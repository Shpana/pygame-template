from typing import Callable, NoReturn


class Event:

    def __init__(self) -> NoReturn:
        self.__listeners = list()

    def add_listener(self, listener: Callable) -> NoReturn:
        if listener not in self.__listeners:
            self.__listeners.append(listener)

    def remove_listener(self, listener: Callable) -> NoReturn:
        if listener in self.__listeners:
            self.__listeners.pop(self.__listeners.index(listener))

    def invoke(self, *args) -> NoReturn:
        for listener in self.__listeners:
            listener(*args)
