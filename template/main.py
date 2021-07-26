from core.application_builder import ApplicationBuilder

from assets.scripts.template_layer import TemplateLayer


if __name__ == "__main__":
    ApplicationBuilder() \
        .use_layer(TemplateLayer).build().run()
