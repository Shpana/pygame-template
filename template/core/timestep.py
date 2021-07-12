from typing import NoReturn


class Timestep:

    def __init__(self, delta_time: float) -> NoReturn:
        self.__delta_time = delta_time

    def __mul__(self, value: float) -> float:
        return self.__delta_time * value

    def __imul__(self, value: float):
        self.__delta_time *= value
        return self

    def __div__(self, value: float) -> float:
        if value == 0:
            raise ZeroDivisionError()
        else:
            return self.__delta_time / value

    def __idiv__(self, value: float):
        if value == 0:
            raise ZeroDivisionError()
        else:
            self.__delta_time /= value
        return self

    @property
    def delta_time_in_seconds(self) -> float:
        return self.__delta_time / 1000

    @property
    def delta_time_in_milliseconds(self) -> float:
        return self.__delta_time

    @property
    def frames_per_second(self) -> float:
        if self.__delta_time != 0:
            return 1 / self.delta_time_in_seconds
        else:
            return self.__max_possible_frames_per_second

    @property
    def __max_possible_frames_per_second(self) -> float:
        return 10.0**6
