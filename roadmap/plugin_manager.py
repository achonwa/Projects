# plugin_manager.py
import importlib
import os
import sys

class PluginManager:
    def __init__(self, plugins_directory):
        self.plugins_directory = plugins_directory
        self.plugins = {}

    def load_plugins(self):
        # Add plugins directory to the Python path
        if self.plugins_directory not in sys.path:
            sys.path.append(self.plugins_directory)

        for file_name in os.listdir(self.plugins_directory):
            if file_name.endswith(".py") and not file_name.startswith("__"):
                module_name = file_name[:-3]
                try:
                    module = importlib.import_module(module_name)
                    if hasattr(module, "Plugin"):
                        plugin_instance = module.Plugin()
                        self.plugins[module_name] = plugin_instance
                        print(f"Loaded plugin: {module_name}")
                except Exception as e:
                    print(f"Failed to load plugin {module_name}: {e}")

    def execute_plugin(self, plugin_name, *args, **kwargs):
        if plugin_name in self.plugins:
            try:
                self.plugins[plugin_name].execute(*args, **kwargs)
            except Exception as e:
                print(f"Error executing plugin {plugin_name}: {e}")
        else:
            print(f"Plugin {plugin_name} not found.")
