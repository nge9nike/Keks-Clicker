import json

values_path = "C:\\Users\\legen\\OneDrive\\Dokumente\\Privat\\Games\\Keks-Clicker\\data.json"


class class_values:
    @staticmethod
    def read():
        # read values from txt file
        with open(values_path, "r") as file:
            temp = json.load(file)

        for key in temp:
            temp = []
            temp.append(temp[key])

        kekse = int(temp[0])
        mult_upgrades = int(temp[1])
        mult_kekse = int(temp[2])

    @staticmethod
    def save(kekse, mult_upgrades, mult_kekse):
        # save variable values
        with open(values_path, 'w') as f:
            pass
