class PipPackage:
    """
    Class representing information about a pip package.
    """

    def __init__(self, pck_string_info):
        """
        :param pck_string_info: It represents information (byte type) about a
        particular package retrieved by the subprocess Module.
        """
        pck_string_info = pck_string_info.decode("utf-8")
        self.name = ""
        self.version = ""
        self.summary = ""
        self.home_page = ""
        self.author = ""
        self.author_email = ""
        self.license_type = ""
        self.location = ""
        self.require_list = []
        self.require_by_list = []
        self.pck_files = []
        self.string_info_to_object(pck_string_info)

    def string_info_to_object(self, pck_string_info):
        """
        Function used to parse the information given by the subprocess and fill the package object with the
        corresponding string information.
        :param pck_string_info: It represents information (byte type) about a
        particular package retrieved by the subprocess Module.
        """
        index = self.get_index_from_string(pck_string_info, "Name:", "Version:")
        self.name = pck_string_info[index[0]:index[1]].strip()
        pck_string_info = pck_string_info[index[1]:]

        index = self.get_index_from_string(pck_string_info, "Version:", "Summary:")
        self.version = pck_string_info[index[0]:index[1]].strip()
        pck_string_info = pck_string_info[index[1]:]

        index = self.get_index_from_string(pck_string_info, "Summary:", "Home-page:")
        self.summary = pck_string_info[index[0]:index[1]].strip()
        pck_string_info = pck_string_info[index[1]:]

        index = self.get_index_from_string(pck_string_info, "Home-page:", "Author:")
        self.home_page = pck_string_info[index[0]:index[1]].strip()
        pck_string_info = pck_string_info[index[1]:]

        index = self.get_index_from_string(pck_string_info, "Author:", "Author-email:")
        self.author = pck_string_info[index[0]:index[1]].strip()
        pck_string_info = pck_string_info[index[1]:]

        index = self.get_index_from_string(pck_string_info, "Author-email:", "License:")
        self.author_email = pck_string_info[index[0]:index[1]].strip()
        pck_string_info = pck_string_info[index[1]:]

        index = self.get_index_from_string(pck_string_info, "License:", "Location:")
        self.license_type = pck_string_info[index[0]:index[1]].strip()
        pck_string_info = pck_string_info[index[1]:]

        index = self.get_index_from_string(pck_string_info, "Location:", "Requires:")
        self.location = pck_string_info[index[0]:index[1]].strip()
        pck_string_info = pck_string_info[index[1]:]

        index = self.get_index_from_string(pck_string_info, "Requires:", "Required-by:")
        tmp_require_list = pck_string_info[index[0]:index[1]]
        self.require_list = [x.strip() for x in tmp_require_list.split(',')]
        pck_string_info = pck_string_info[index[1]:]

        index = self.get_index_from_string(pck_string_info, "Required-by:")
        tmp_require_list_by = pck_string_info[index[0]:index[1]]
        self.require_by_list = [x.strip() for x in tmp_require_list_by.split(',')]
        pck_string_info = pck_string_info[index[1]:]

        self.pck_files = pck_string_info.splitlines()
        del self.pck_files[0:2]

    def get_index_from_string(self, string_to_search, search_word, next_stop_word="\r\n"):
        """
        Used to retrieve the information contained between two words in a string
        :param string_to_search: The complete string to search.
        :param search_word: The starting delimiter of the string
        :param next_stop_word: The ending delimiter of the string
        :return: A array of two index. The information is present between these two index.
        """
        index_start = string_to_search.find(search_word)
        index_stop = string_to_search.find(next_stop_word)
        return [index_start + len(search_word) + 1, index_stop]
