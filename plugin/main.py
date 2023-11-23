import json
import os
import time

import requests

from flox import Flox

INSTALL_QUERY = "install <GitHub_Repo_URL> <Branch>"

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
        query_splitted = query.split()
        if len(query_splitted) <= 3:
            title = ""
            for nr, q in enumerate(INSTALL_QUERY.split()):
                try:
                    title += "{} ".format(query_splitted[nr])
                except:
                    title += "{} ".format(q)
            self.add_item(
                title=title,
                subtitle="<GitHub Repo URL> => The URL to the Repository\n"
                         "<BRANCH> => The Branch, which will be used for this plugin".format(query),
                method=self.install_plugin_from_github,
                parameters=[query],
                dont_hide=True
            )
        else:
            self.add_item(
                title="install - to many parameters",
                subtitle=INSTALL_QUERY,
                dont_hide=True
            )

    def update(self, query):
        if "OwnPluginLauncher" not in self.settings.keys():
            self.settings.update({self.manifest["Name"]: {"Version": self.manifest["Version"],
                                                          "Website": self.manifest["Website"],
                                                          "Branch": "main"}})
            self.add_item(
                title="OwnPluginLauncher not available",
                subtitle="asdf",
                dont_hide=True
            )
        #for key, values in self.settings.items():
        #    newest_version = self.get_info_from_github(values["Website"])

    def uninstall(self, query):
        pass

    def install_plugin_from_github(self, query):
        if len(query.split()) != 3:
            self.show_msg("Your query is not correct", "Your query => '{}'\nExpected '{}'".format(query,
                                                                                                  INSTALL_QUERY))
        else:
            cmd, url, branch = query.split()
            self.get_info_from_github(url, branch)

    @staticmethod
    def get_info_from_github(repo_url, branch):
        # Get the 'plugin.json' content as dictionary
        plugin_json_url = "{}/blob/{}/plugin.json".format(repo_url, branch)
        res = requests.get(plugin_json_url)
        plugin_json_list = res.json()["payload"]["blob"]["rawLines"]
        plugin_json_str = " ".join(plugin_json_list)
        plugin_json_dict = json.loads(plugin_json_str)

        # Get the URL for the newest release .zip file
        "https://github.com/rrFlowLauncher/own_plugin_manager/releases"



if __name__ == "__main__":
    plugin_manager = PluginManager()
    #plugin_manager.run()
    query = "install https://github.com/rrFlowLauncher/own_plugin_manager main"
    plugin_manager.install_plugin_from_github(query)
