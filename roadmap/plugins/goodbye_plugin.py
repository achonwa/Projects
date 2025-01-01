# plugins/goodbye_plugin.py
from plugin_interface import PluginInterface

class Plugin(PluginInterface):
    def execute(self, *args, **kwargs):
        print("Goodbye from GoodbyePlugin!")
