# FL_plugin_manager

# FlowLauncher documentation about Plugins in Python
https://www.flowlauncher.com/docs/#/py-develop-plugins?id=about-flow39s-python-plugins

# Flox lib
https://github.com/Garulf/Flox


# The `plugin.json` file
```json
{
  "ID":"",             //Plugin ID，32 bit UUID
  "ActionKeyword":"",  //Plugin default action keyword (* means no specific action keyword)
  "Name":"",           //Plugin name
  "Description":"",    //Plugin description
  "Author":"",         //Plugin Author
  "Version":"",        //Plugin version (e.g. 1.0.0). It is important for plugin update checking.
  "Language":"",       //Plugin language，available fields are csharp, fsharp, python, javascript, typescript and executable. Make sure you put the correct field for your plugin language, this is important so that the required runtime environment can be setup automatically.
  "Website":"",        //Plugin website or author website
  "IcoPath": "",       //Plugin icon, relative path to the plugin folder
  "ExecuteFileName":"" //Execution entry. dll extension for C#/F# plugin, .py for python plugin, .js/.ts for JS/TS plugins and .exe or other executable for executable plugin. Path examples include "main.py" or "./dist/main.js"
}
```

