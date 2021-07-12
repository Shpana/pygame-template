from core.application_context import ApplicationContext

from assets.scripts.template_layer import TemplateLayer


if __name__ == "__main__":
    context = ApplicationContext()
    context.config.from_ini("project.config")

    app = context.get_instance()
    app.add_layer(TemplateLayer(context))
    app.run()
