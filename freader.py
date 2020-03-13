import decorators


class FileReader:
    """ Read a file line by line, optionally searching for a regular expression. """

    def __init__(self, fname: str):
        """Initialize a FileReader.

            :param fname: the full path to the file
        """
        self.__fname = fname
        self.__grep_str = ""

    @staticmethod
    @decorators.RegExp
    def print_line(*args) -> str:
        pass

    def read_file(self):
        """Reads the file, searching for the pattern in self.grep_str."""
        with open(self.fname, "r") as f:

            while True:
                line = f.readline()
                if line != "":
                    x = self.print_line(self. grep_str, line)
                    print(x, end="")

    def __repr__(self):
        return f"FileReader('{self.__fname}')"

    def __str__(self):
        return f"file to parse:  {self.__fname}"

    # region properties
    @property
    def fname(self) -> str:
        return self.__fname

    @fname.setter
    def fname(self, fname: str):
        self.__fname = fname

    @property
    def grep_str(self) -> str:
        return self.__grep_str

    @grep_str.setter
    def grep_str(self, grep_str: str):
        self.__grep_str = grep_str
    # endregion


if __name__ == "__main__":
    reader = FileReader(r'C:\Users\rwragg\Desktop\u_ex200220.log')
    print(reader)

    # reader.grep_str = "error"
    # reader.read_file()
