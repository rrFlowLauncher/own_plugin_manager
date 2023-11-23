import json
import os
import shutil
import time
import zipfile

import requests
from flox import Flox

from get_from_github import *

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
                                                          "Branch": "main",
                                                          "Path": self.plugindir}})
            self.add_item(
                title="OwnPluginLauncher not available",
                subtitle="asdf",
                dont_hide=True
            )
        for key, values in self.settings.items():
            plugin_json_content = get_plugin_json_file_content_from_github(values["Website"], values["Branch"])
            if values["Version"] != plugin_json_content["Version"]:
                self.add_item(
                    title=key,
                    subtitle="{} => {}".format(values["Version"], plugin_json_content["Version"]),
                    method=self.install_plugin_from_github,
                    parameters=["install {} {}".format(values["Website"], values["Branch"])],
                    dont_hide=True
                )

    def uninstall(self, query):
        for key, value in self.settings.items():
            self.add_item(
                title="{}".format(key),
                subtitle=value,
                method=self.uninstall_plugin,
                parameters=[key]
            )

    def uninstall_plugin(self, plugin_name):
        if plugin_name == self.manifest["Name"]:
            self.show_msg(plugin_name, "Is not allowed to uninstall\nBecause it is this Plugin Manager")
        else:
            try:
                shutil.rmtree(self.settings[plugin_name]["path"])
                del self.settings[plugin_name]
                self.show_msg(plugin_name, "Uninstall successfully")
            except Exception as e:
                self.show_msg("Exception during uninstallation", e)

    def install_plugin_from_github(self, query):
        if len(query.split()) != 3:
            self.show_msg("Your query is not correct", "Your query => '{}'\nExpected '{}'".format(query,
                                                                                                  INSTALL_QUERY))
        else:
            cmd, url, branch = query.split()
            plugin_file_name, download_url = get_plugin_release_info_from_github(url)

            # Download last release file
            download_path_with_filename = os.path.join(self.plugindir, "downloads", plugin_file_name)
            plugin_binary = requests.get(download_url, allow_redirects=True)
            with open(download_path_with_filename, "wb") as release_file:
                release_file.write(plugin_binary.content)

            # unzip release file into plugins folder
            destination_path = os.path.join(self.user_dir, "Plugins", plugin_file_name.split(".zip")[0])
            with zipfile.ZipFile(download_path_with_filename, "r") as zip_ref:
                zip_ref.extractall(destination_path)

            # update settings with new plugin
            new_plugin_json_file = os.path.join(destination_path, "plugin.json")
            with open(new_plugin_json_file, "r") as plugin_file:
                new_plugin_json_file_str = plugin_file.read()
            new_plugin_json_file_dict = json.loads(new_plugin_json_file_str)
            plugin_name = new_plugin_json_file_dict["Name"]
            plugin_version = new_plugin_json_file_dict["Version"]
            plugin_website = new_plugin_json_file_dict["Website"]
            self.settings.update({plugin_name:
                {
                    "Branch": branch,
                    "Version": plugin_version,
                    "Website": plugin_website,
                    "path": destination_path
                }
            })

            # success message
            self.show_msg("Installation of '{}' => success".format(plugin_name), "Please restart FlowLauncher")


if __name__ == "__main__":
    plugin_manager = PluginManager()
    #plugin_manager.run()
    query = "install https://github.com/rrFlowLauncher/own_plugin_manager main"
    plugin_manager.update(query)
