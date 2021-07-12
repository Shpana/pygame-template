from dependency_injector import containers, providers

from core.application import Application


def _parse_bool(value: str) -> bool:
    if value != "true" and value != "false":
        raise ValueError(f"Field must be 'true' or 'false', not '{value}'.")
    else:
        return value == "true"


class ApplicationContext(containers.DeclarativeContainer):

    config = providers.Configuration()

    get_instance: providers.Singleton[Application] = providers.Singleton(
        Application,
        title=config.window.title.required(),
        width=config.window_spec.width.required().as_int(),
        height=config.window_spec.height.required().as_int(),
        smoothed=config.window_spec.smoothed.required().as_(_parse_bool),
        viewport_width=config.viewport_spec.width.required().as_int(),
        viewport_height=config.viewport_spec.height.required().as_int(),
    )
