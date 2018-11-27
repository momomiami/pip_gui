class General:
    def __init__(self):
        self.command = []
        self.available_option = {}

    def version(self):
        self.command.append("-V")


class Uninstall:

    def __init__(self, pck_name):
        self.command = []
        self.available_option = {}
        self.command.append("uninstall")
        self.command.append(pck_name)
        self.command.append("-y")


class List:
    def __init__(self):
        self.command = []
        self.available_option = {"-o": "List outdated packages",
                                 "-u": "List uptodate packages",
                                 "-e": "List editable projects",
                                 "-l": "If in a virtualenv that has global access"
                                       ", do not list globally-installed packages",
                                 "--user": "Only output packages installed in user-site",
                                 "--pre": "Include pre-release and development versions. "
                                          "By default, pip only finds stable versions",
                                 "--not-required": "List packages that are not dependencies of installed packages",
                                 "--exclude-editable": "Exclude editable package from output",
                                 "--include-editable": "Include editable package from output"}
        self.command.append("list")

    def format_json(self):
        self.command.append("--format=json")

    def outdated_pck(self):
        self.command.append("-o")

    def uptodate_pck(self):
        self.command.append("-u")

    def editable_projects(self):
        self.command.append("-e")

    def user_site(self):
        self.command.append("--user")

    def local(self):
        self.command.append("-l")

    def pre(self):
        self.command.append("--pre")

    def not_required(self):
        self.command.append("--not-required")

    def exclude_editable(self):
        self.command.append("--exclude-editable")

    def include_editable(self):
        self.command.append("--include-editable")


class Show:
    def __init__(self, pck_name):
        self.command = []
        self.available_option = []
        self.command.append("show")
        self.command.append(pck_name)
        self.command.append("-f")
