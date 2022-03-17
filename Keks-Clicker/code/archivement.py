from tkinter import StringVar


def archivements(kekse: StringVar, multiplicator: StringVar, msg: StringVar):
    arch_kekse = int(kekse.get())
    arch_mult = int(multiplicator.get())
    try:
        if arch_kekse == 1000000 and arch_mult == 1:
            msg.set("Du Hobbyloser")

    except TypeError:
        pass
