import subprocess
import sys


class Subprocess:
    """
    The class will use the subprocess module to call the pip module of the python installation
    """

    def __init__(self):
        try:
            self.check_sys_exe()
            self.python_path = sys.executable
        except AssertionError as error:
            print(error)
            sys.exit()

    def run_subprocess(self, command):
        """
        Call a process to execute the given command
        :return: the output of the subprocess
        """
        return subprocess.check_output([self.python_path, '-m', 'pip']+command.command)

    def check_sys_exe(self):
        """
        raise an AssertionError if Python is unable to retrieve
        the absolute path of the executable binary for the Python interpreter
        """
        assert sys.executable is not None or sys.executable != "", "Python is unable to retrieve absolute path of " \
                                                                   "the executable binary for the Python interpreter"
