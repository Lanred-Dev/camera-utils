from sys import modules
from os import path, listdir
from json import load
from importlib import util
from threading import Thread

PLUGIN_DIRECTORY = "camera\\plugins"


class PluginController:
    def __init__(self):
        self.plugins = {}
        self.groups = {}
        self.__active = {}
        self.__loadPluginCallbacks = {}
        self.__unloadPluginCallbacks = {}

        self.__register(PLUGIN_DIRECTORY)

    def isActive(self, name):
        return name in self.__active

    def load(self, name):
        if name in self.__active:
            return

        plugin = self.plugins[name]

        try:
            spec = util.spec_from_file_location(name, plugin["main"])
            module = util.module_from_spec(spec)
            spec.loader.exec_module(module)

            pluginClass = module.Plugin()
            pluginThread = Thread(target=pluginClass.load).start()

            self.__active[name] = {"class": pluginClass, "thread": pluginThread}

            for callback in self.__loadPluginCallbacks.values():
                callback()
        except ImportError as error:
            print(f"Failed to import plugin: {name}\n{error}")

    def unload(self, name):
        if not (name in self.__active):
            return

        self.__active[name]["class"].unload()
        del self.__active[name]

        for callback in self.__unloadPluginCallbacks.values():
            callback()

    def addLoadCallback(self, name, callback):
        self.__loadPluginCallbacks[name] = callback

    def removeLoadCallback(self, name):
        del self.__loadPluginCallbacks[name]

    def addUnloadCallback(self, name, callback):
        self.__unloadPluginCallbacks[name] = callback

    def removeUnloadCallback(self, name):
        del self.__unloadPluginCallbacks[name]

    def __register(self, directory, group="none"):
        for folder in listdir(directory):
            folderPath = path.join(directory, folder)

            if not path.isdir(folderPath):
                continue

            infoPath = path.join(folderPath, "info.json")

            if not path.isdir(infoPath):
                continue

            with open(infoPath, "r") as file:
                info = load(file)

                if info["type"] == "group":
                    self.__registerGroup(info)
                    self.__register(folderPath, info["name"])
                elif info["type"] == "plugin":
                    self.__registerPlugin(info, folderPath, group)

    def __registerGroup(self, info):
        self.groups[info["name"]] = []

    def __registerPlugin(self, info, directory, group):
        info["main"] = path.join(directory, "main.py")

        self.plugins[info["name"]] = info
        self.groups[group].append(info["name"])


modules[__name__] = PluginController()
