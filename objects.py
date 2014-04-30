__author__ = 'wybe'


import os
import errorhandler


class Building:
    """
    Base building class.

    Children are instanced when a building is built.

    Building classes can have a number of parameters:

    size = (x, y)
        The size of the building in tiles.

    effect_radius = (width, height)
        The amount of tiles around the building this building can have effect on.
        When this does not exist, this building does only act on itself.

    item_name = "i_"
        Name of the item to drop when destroyed, always starts with "i_".



    inventory = []
        Inventory with specific size.

    input_tiles = [(x, y, "filter", (slot, slot, ...)), (x, y, "filter", (slot, slot, ...)]
        List of tiles, relative to the building, this building can take input from.
        If the filter starts with "i_" it only takes a specific item,
        else it takes any item that has a variable with that name.
        (slot, slot) specifies the slot the item can go into, when this is empty it can go anywhere.

    output_tiles = [(x, y, "filter", (slot, slot, ...), (x, y, "filter", (slot, slot, ...)]
        List of tiles, relative to the building, where output can be taken from.
        If the filter starts with "i_" that tile only outputs a specific item,
        else it outputs any item that has a variable with that name.
        (slot, slot) specifies the slot the item can be taken from, when it is empty it can be taken from anywhere.



    Other variables are special cases and will (hopefully) be self-explanatory.
    An example could be: "energy_value" in a class named "Coal"
    """

    size = (1, 1)

    def __init__(self, x, y):

        self.x = x
        self.y = y


class Item:
    """
    Base item class.

    Instanced when items lay on the ground.
    Queried when information about an item is needed
    """

    is_buildable = False
    # Specifies if an item can be built

    building_name = "b_"
    # Name of the building to be built, starts with "b_"

    def __init__(self, x, y):

        self.x = x
        self.y = y


def load(folder="objects"):
    """
    Loads all the objects and items in the files in the specified folder
    """

    try:
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    except FileNotFoundError:
        errorhandler.log("ERROR: Folder \"Objects\" does not exist.\n"
                         "The game is probably corrupted, a fresh install is advised.")
        return False

    return True