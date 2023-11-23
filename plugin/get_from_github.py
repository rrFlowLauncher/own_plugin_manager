import json
import requests


def get_plugin_json_file_content_from_github(repo_url, branch):
    # Get the 'plugin.json' content as dictionary
    plugin_json_url = "{}/blob/{}/plugin.json".format(repo_url, branch)
    res = requests.get(plugin_json_url)
    plugin_json_list = res.json()["payload"]["blob"]["rawLines"]
    plugin_json_str = " ".join(plugin_json_list)
    plugin_json_dict = json.loads(plugin_json_str)

    return plugin_json_dict


def get_plugin_release_info_from_github(repo_url):
    # Get the Filename + URL for the newest release .zip file
    release_base_url = "https://api.github.com/repos/{}/releases/latest".format(repo_url.split("github.com/")[1])
    release_informatoin = requests.get(release_base_url, headers={"Accept": "application/vnd.github+json"})
    release_informatoin_json = release_informatoin.json()
    plugin_file_name = release_informatoin_json["assets"][0]["name"]
    download_url = release_informatoin_json["assets"][0]["browser_download_url"]

    return plugin_file_name, download_url
