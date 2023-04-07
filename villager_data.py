"""Functions to parse a file containing villager data."""

# name|species|personality|hobby|motto


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    file = open(filename)
    species = set()

    for line in file:
        species.add(line.rstrip().split("|")[1])

    return species


# print(all_species("villagers.csv"))


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []
    file = open(filename)
    for line in file:
        name = line.rstrip().split("|")[0]
        animal = line.rstrip().split("|")[1]
        if search_string == "All":
            villagers.append(name)
        elif animal == search_string:
            villagers.append(name)

    return sorted(villagers)


# print(get_villagers_by_species("villagers.csv"))
# print(get_villagers_by_species("villagers.csv", "Pig"))


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    hobbies = {}

    for line in open(filename):
        name = line.rstrip().split("|")[0]
        hobby = line.rstrip().split("|")[3]

        if (hobby in hobbies):
            hobbies[hobby].append(name)
        else:
            hobbies[hobby] = [name]

    return [hobbies.values()]


# print(all_names_by_hobby("villagers_copy.csv"))


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []
    for line in open(filename):
        all_data.append(tuple(line.rstrip().split("|")))

    return all_data


# print(all_data("villagers_copy.csv"))


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    for line in all_data(filename):
        name, _, _, _, motto = line

        if villager_name == name:
            return motto


# print(find_motto("villagers_copy.csv", "Curt"))
# print(find_motto("villagers_copy.csv", "Haz"))
# print(find_motto("villagers.csv", "Hazel"))


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    villager_personality = None

    for line in all_data(filename):
        name, _, personality, _, _ = line

        if villager_name == name:
            villager_personality = personality
            break
    same_personality = set()

    if villager_personality is None:
        return same_personality

    for line in all_data(filename):
        name, _, personality, _, _ = line
        if personality == villager_personality:
            same_personality.add(name)

    return same_personality


print(find_likeminded_villagers("villagers_copy.csv", "Curt"))
