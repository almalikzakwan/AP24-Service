import random

class random:
    """ get random number range """
    def range(file_path, start, stop, step):
        """ get new default random port, and save into storage file."""
        random_port = random.randrange(start, stop, step)

        # save random default port into file.
        rdp = open(file_path,"w")
        rdp.write(str(random_port))

        return random_port