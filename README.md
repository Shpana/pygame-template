# pygame-template

### Run Application


Before starting the application, you need to create an application context:
```
context = ApplicationContext()
context.config.from_ini("project.config")
```

And then run the application:
```
app = context.get_instance()
app.run()
```

Now you can add several layers to customize the behavior of your application:
```
app.add_layer(TemplateLayer(context))
```

So you get: 
```
from core.application_context import ApplicationContext


if __name__ == "__main__":
    from assets.scripts.template_layer import TemplateLayer
    
    context = ApplicationContext()
    context.config.from_ini("project.config")
    
    app = context.get_instance()
    app.add_layer(TemplateLayer(context))
    app.run()
```
