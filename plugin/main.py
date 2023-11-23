import os
import time

import requests

from flox import Flox


class PluginManager(Flox):
    def __init__(self):
        super().__init__()

    def query(self, query):
        if query.startswith("install"):
            self.install(query)
        elif query.startswith("update"):
            self.update(query)
        elif query.startswith("uninstall"):
            self.uninstall(query)
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
        self.change_query("pmr install succ", True)

    def install(self, query):
        if len(query.split()) <=3:
            self.add_item(
                title="install",
                subtitle="install <Name> <GitHub Repo URL>",
                method=self.installa,
                parameters=[query],
                dont_hide=True
            )
        else:
            self.add_item(
                title="install - to many parameters",
                subtitle="install <Name> <GitHub Repo URL>",
                dont_hide=True
            )

    def update(self, query):
        if "OwnPluginLauncher" not in self.settings.keys():
            self.settings.update({self.manifest["Name"]: {"Version": self.manifest["Version"], "Website": self.manifest["Website"]}})
            self.add_item(
                title="OwnPluginLauncher not available",
                subtitle="asdf",
                dont_hide=True
            )
        for key, values in self.settings.items():
            newest_version = self.get_info_from_github(values["Website"])

    def uninstall(self, query):
        pass

#    def install(self, cmd, title=str, url=str, *args):
    def installa(self, *args):
        if self.settings["test"] == "jo":
            self.settings.update({"test": "no"})
        else:
            self.settings.update({"test": "jo"})

    @staticmethod
    def get_info_from_github(url):
        pass



if __name__ == "__main__":
    plugin_manager = PluginManager()
    plugin_manager.run()