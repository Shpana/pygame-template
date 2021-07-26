from dataclasses import dataclass


@dataclass
class ApplicationStartupOptions:
    title: str
    is_smoothed: bool
    resolution: tuple[int, int]
    viewport_resolution: tuple[int, int]
