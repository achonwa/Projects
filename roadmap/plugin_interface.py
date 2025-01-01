# plugin_interface.py
class PluginInterface:
    def execute(self, *args, **kwargs):
        raise NotImplementedError("Plugins must implement the 'execute' method.")
