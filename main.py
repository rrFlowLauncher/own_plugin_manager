import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from hawkcatcher import Hawk
hawk = Hawk("eyJpbnRlZ3JhdGlvbklkIjoiODc4OGU4MGEtYzEwMy00ZTMzLTg2MzYtNzkwMWRkNzQ1NGEwIiwic2VjcmV0IjoiZDNlZmI3NjMtMmEyYi00ODdlLTg4YzItZmViZTVhY2RmYzRlIn0=")

try:
    from plugin.main import PluginManager


    if __name__ == "__main__":
        plugin_manager = PluginManager()
        plugin_manager.run()
except:
    hawk.send()
