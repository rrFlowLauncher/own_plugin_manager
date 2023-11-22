import time

import requests

from flox import Flox



class PluginManager(Flox):
    def __init__(self):
        super().__init__()
    def query(self, query):
        if query.startswith("install"):
            self.add_item(
                title="install",
                subtitle="install <Name> <GitHub Repo URL>",
                method=self.installa,
                parameters=["pmr install"],
                dont_hide=True
            )
        elif query.startswith("update"):
            pass
        elif query.startswith("uninstall"):
            pass
        else:
            self.add_item(
                title="install",
                method=self.change_query,
                parameters=["pmr install"],
                dont_hide=True
            )
            self.add_item(
                title="update",
                method=self.change_query,
                parameters=["pmr update"],
                dont_hide=True
            )
            self.add_item(
                title="uninstall",
                method=self.change_query,
                parameters=["pmr uninstall"],
                dont_hide=True
            )
#        #self.browser.open("https://github.com/rrFlowLauncher/amazing_marvin/blob/main/plugin.json")
#        url =              "https://github.com/rrFlowLauncher/amazing_marvin"
#        res = requests.get("https://github.com/rrFlowLauncher/amazing_marvin/raw/main/plugin.json")
#        print(res.json())
#        res_j = res.json()
#        print(type(res_j))


    def context_menu(self, data):
        self.add_item(
            title=data,
            subtitle=data,
            context=["jip"]
        )

#    def install(self, cmd, title=str, url=str, *args):
    def installa(self, *args):
        self.start_loadingbar()
        self.add_item(
            title="installing",
            subtitle="install <Name> <GitHub Repo URL>",
#            method=self.install,
#            parameters=["pmr install"],
            dont_hide=True
        )
        time.sleep(1)
        self.add_item(
            title="install finished",
            subtitle="install <Name> <GitHub Repo URL>",
          #  method=self.install,
         #   parameters=["pmr install"],
            dont_hide=True
        )
        self.stop_loadingbar()



if __name__ == "__main__":
    plugin_manager = PluginManager()
    plugin_manager.run()