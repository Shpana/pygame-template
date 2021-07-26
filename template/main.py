from core.application import Application
from core.application_startup_options import ApplicationStartupOptions

from assets.scripts.template_layer import TemplateLayer


if __name__ == "__main__":
    app = Application(
        ApplicationStartupOptions(
            title="pygame-template",
            is_smoothed=False,
            resolution=(1000, 600),
            viewport_resolution=(900, 600),
        )
    )
    app.run()
