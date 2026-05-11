class files:
    """
    class for read and write file.

    read(path: str)
    write(path: str)
    """
    def init(self, path: str):
        self.path = path

    def read(self, mode:str = "r"):
        """ read a file. """
        file = open(self.path, mode)
        value = file.read()
        file.close()
        self.close(file)

        return value
    
    def write(self, string: str, mode:str ="w"):
        """ write into file. """
        file = open(self.path, mode)
        file.write(string)
        self.close(file)

        return True

    def close(file):
        """ close file after execution """
        file.close()


