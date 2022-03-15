import json

values_path = __file__.rsplit("\\", maxsplit=1)[0] + "\\data.json"


def read():
    """Reads the values from the json file

    Returns:
        list: list with values
    """
    with open(values_path, "r") as file:
        temp = json.load(file)

    kekse = int(temp["kekse"])
    mult_upgrades = int(temp["upgrades"])
    mult_kekse = int(temp["multiplicator"])

    templist = [kekse, mult_upgrades, mult_kekse]
    return templist


def save_values(templist):
    """Saves the values in the json file

    Args:
        templist(list): list with variable values used in main.py
    """
    tempdict = {
        "kekse": templist[0],
        "upgrades": templist[1],
        "multiplicator": templist[2]
    }
    with open(values_path, 'w') as f:
        json.dump(tempdict, f)
