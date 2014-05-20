__author__ = 'wybe'

import os
import fnmatch
import logging

import pygame


DATA_DIR = "Data/"


class Item(object):

    sprite = 0

    def __init__(self, f):
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line == "end":
                return
            elif 'sprite = ' in line:
                unpacked_line = str.split(line, ' = ')
                sprite_path = DATA_DIR + unpacked_line[1]

                if os.path.isfile(sprite_path):
                    self.sprite = pygame.image.load(sprite_path).convert()
                    self.sprite.set_colorkey((255, 0, 255))
                else:
                    logging.warning("Sprite does not exist")
                    logging.warning(sprite_path)


def load_objects():
    items = dict()
    matches = []
    for root, dir_name, file_name in os.walk(DATA_DIR):
        for file in fnmatch.filter(file_name, '*.aof'):
            matches.append(os.path.join(root, file))

    # Go through each .aof file found.
    for file in matches:

        # Open the file
        with open(file, 'r') as f:

            # Check lines until one with a ':' at the end is found.
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line[-1] == ':':

                    # Split the line in the type and the name. Lines look like this -> type:name:
                    unpacked_line = str.split(line, ':')
                    object_type = unpacked_line[0]
                    object_name = unpacked_line[1]

                    if " " in object_type or " " in object_name:
                        logging.warning("In " + file)
                        logging.warning("Spaces are not allowed in object names or types \"" + line + "\"")

                    if object_type == "item":
                        # Check for doubles and log an error when one is found.
                        if not object_name in items:
                            logging.info("Adding " + object_type + " \"" + object_name + "\"")
                            items[object_name] = Item(f)
                        else:
                            logging.warning("In " + file)
                            logging.warning("Encountered double " + object_type + " \"" +
                                            object_name + "\"")

    return items