class General:
    def __init__(self):
        self.command = []
        self.available_option = []

    def version(self):
        self.command.append("-V")


class List:
    def __init__(self):
        self.command = []
        self.available_option = {"-o": "List outdated packages",
                                 "-u": "List uptodate packages",
                                 "-e": "List editable projects"}
        self.command.append("list")

    def format_json(self):
        self.command.append("--format=json")

    def outdated_pck(self):
        self.command.append("-o")

    def uptodate_pck(self):
        self.command.append("-u")

    def editable_projects(self):
        self.command.append("-e")


class Show:
    def __init__(self, pck_name):
        self.command = []
        self.available_option = []
        self.command.append("show")
        self.command.append(pck_name)
