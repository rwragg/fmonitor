import time


class FileTester:
    def __init__(self, fname):
        self.fname = fname

    def writefile(self, count):
        with open(self.fname, "w") as f:
            for x in range(count):
                f.write("line " + str(x) + "\n")
                f.flush()

                time.sleep(5)


if __name__ == "__main__":
    file_test = FileTester(r'C:\Users\rwragg\Desktop\fun.txt')
    file_test.writefile(25)
