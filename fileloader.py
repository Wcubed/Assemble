__author__ = 'wybe'

import glob
import logging


def load_objects():
    folder = "Data/"
    items = set()

    for file in glob.glob(folder + "*.aof"):
        with open(file, 'r') as f:
            for line in f:
                line = line.rstrip('\n')

                if line[-1] == ':':
                    unpacked_line = str.split(line, ':')
                    object_type = unpacked_line[0]
                    object_name = unpacked_line[1]

                    if object_type == "item":
                        if not object_name in items:
                            items.add(object_name)
                        else:
                            logging.warning("Encountered double " + object_type + ": \"" +
                                            object_name + "\" in file: \"" + file + "\".")








    return items