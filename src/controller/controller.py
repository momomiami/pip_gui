import json
from src.controller.subprocess import Subprocess
from src.model.package import PipPackage
from src.view.main_window import MainWindow
from src.controller.command import *


class Controller:
    '''
    Controller class, to coordinate suprocess, ui and model.
    '''
    def __init__(self):
        self.pip_subprocess = Subprocess()
        self.get_pip_version()
        self.createUI()

    def get_pip_version(self):
        command_general = General()
        command_general.version()
        self.version = self.pip_subprocess.run_subprocess(command_general).decode("utf-8")
        self.version = self.version[4:self.version.find(" from")]

    def createUI(self):
        self.main_window = MainWindow(self)

    def get_pck_list_name(self):
        command_list = List()
        command_list.format_json()
        self.pck_list_name = []
        pip_list_pck = json.loads(self.pip_subprocess.run_subprocess(command_list))
        for pck in pip_list_pck:
            self.pck_list_name.append(pck['name'])
        return self.pck_list_name

    def get_pck_info(self, pck_name):
        pck = PipPackage(self.pip_subprocess.run_subprocess(Show(pck_name)))
        return pck

    def get_option(self,command):
        if(command == "List"):
            return List().available_option