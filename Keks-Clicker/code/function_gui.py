from tkinter import StringVar


def more_cookies(kekse: StringVar, multiplicator: StringVar):
    try:
        # get, because it takes the value
        temp = int(kekse.get())
        kekse.set(int(temp + int(multiplicator.get())))

    except ValueError:
        pass


def upgrade(kekse: StringVar, upgrade: StringVar, multiplicator: StringVar, info: StringVar):
    try:
        curr = int(kekse.get())
        prize = int(upgrade.get())

        if curr > prize:
            multiplicator.set(int(multiplicator.get()) * 2)
            kekse.set(curr - prize)
            upgrade.set(prize * 2)
            info.set("Erfolgreich")

        else:
            info.set("Nicht genug Geld")

    except ValueError:
        pass
