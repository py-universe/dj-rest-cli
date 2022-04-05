from django_rest_cli.engine import raise_error_message
from .plugin_django_environ.generator import DjangoEnviron


class PluginFacade():

    @staticmethod
    def add_django_environ():
        DjangoEnviron()


def plugin_trigger(plugin_name: str) -> None:
    """ Initiates the process of adding the specified plugin """

    plugin_name: str = plugin_name.replace('-', '_') # Function names can't have hyphens
    function_name: str = f"add_{plugin_name}"

    if hasattr(PluginFacade, function_name) \
        and callable(getattr(PluginFacade, function_name)):
        func = getattr(PluginFacade, function_name)
        func()
    else:
        error_text: str =  f"'{plugin_name}'currently not supported :( " \
                "Make sure it's spelt correctly though "

        raise_error_message(error_text)