import sys, os

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from plugin.main import PluginManager


if __name__ == "__main__":
    plugin_manager = PluginManager()
#    plugin_manager.run(["install", "a", "b"])
    plugin_manager.run()
