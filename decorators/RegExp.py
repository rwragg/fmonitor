import re


class RegExp(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args):
        """
        Overload of the __call__ method.

        :param *args:
        :param args[0] = pattern to search for.
        :param args[1] = string to search in.
        :return: string passed in if there is a match.
        :rtype: string
        """
        pattern, line = args

        match = re.search(pattern, line)
        if match:
            return line

        # self.f(line)
        return ""
