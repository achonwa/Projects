# main.py
import sys
import os
from plugin_manager import PluginManager

# Add the project directory to sys.path
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    plugins_directory = "plugins"  # Adjust to the actual path of the plugins folder
    if not os.path.exists(plugins_directory):

        print(f"Error: Plugins directory '{plugins_directory}' does nor exist.")
        return
    
    manager = PluginManager(plugins_directory)

    # Load all plugins in the directory
    manager.load_plugins()

    # Execute plugins dynamically
    manager.execute_plugin("hello_plugin")
    manager.execute_plugin("goodbye_plugin")
    #manager.execute_plugin("non_existent_plugin")  # Test with an invalid plugin name

print("Current working directory:", os.getcwd())

if __name__ == "__main__":
    main()
