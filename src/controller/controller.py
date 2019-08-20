import json
import urllib.request
import re
import os
from urllib.error import URLError
from src.controller.subprocess import Subprocess
from src.model.package import PipPackage
from src.view.main_window import MainWindow
from src.controller.command import *


class Controller:
    """
    Controller class, to coordinate suprocess, ui and model.
    """

    def __init__(self):
        self.pip_subprocess = Subprocess()
        self.get_pip_version()
        self.create_ui()

    def get_pip_version(self):
        command_general = General()
        command_general.version()
        self.version = self.pip_subprocess.run_subprocess(command_general).decode("utf-8")
        self.version = self.version[4:self.version.find(" from")]

    def create_ui(self):
        self.main_window = MainWindow(self)

    def get_pck_list_name(self, option):
        command_list = List()
        command_list.format_json()
        if option == "-o":
            command_list.outdated_pck()
        elif option == "-e":
            command_list.editable_projects()
        elif option == "-u":
            command_list.uptodate_pck()
        elif option == "-l":
            command_list.local()
        elif option == "--user":
            command_list.user_site()
        elif option == "--pre":
            command_list.pre()
        elif option == "--not-required":
            command_list.not_required()
        elif option == "--exclude-editable":
            command_list.exclude_editable()
        elif option == "--include-editable":
            command_list.include_editable()
        pck_list_name = []
        pip_list_pck = json.loads(self.pip_subprocess.run_subprocess(command_list))
        for pck in pip_list_pck:
            pck_list_name.append(pck['name'])
        return pck_list_name

    def get_pck_info(self, pck_name):
        pck = PipPackage(self.pip_subprocess.run_subprocess(Show(pck_name)))
        return pck

    def search_pck(self, pck_search):
        conn = ConnectionCheck()
        if conn.request_pypi():
            search_info = self.parse_search_query(self.pip_subprocess.run_subprocess(Search(pck_search)))
            if search_info is not None:
                return search_info
            else:
                return None
        else:
            return None

    def parse_search_query(self, cmd_output):
        if cmd_output:
            output = cmd_output.decode("utf-8")
            output = re.sub(r'((\r\n  INSTALLED:.+?\r\n)?(LATEST:(.+?\r\n))?)*', r'', output)
            search_info = {}
            while output:
                search_info[output[:output.find(" - ")]] = output[output.find(" - ")+2:output.find("\r\n")]
                output = output[output.find("\r\n")+2:]
            return search_info
        else:
            return None

    def uninstall_pck(self, pck_name):
        self.pip_subprocess.run_subprocess(Uninstall(pck_name))

    def get_option(self, command):
        if command == "List":
            return List().available_option


class ConnectionCheck:

    def request_pypi(self):
        '''
        This method is intended to check if the user has a working internet connection (specifically to hit the python package index)
        :return: boolean depending if the connection is working
        '''
        try:
            with urllib.request.urlopen('https://pypi.org/') as response:
                return True
        except URLError as e:
            return False
