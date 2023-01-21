import os
def gpout(text):
    return os.system("gpio -1 mode " + str(text) + " out")
def gpup(text):
    return os.system("gpio -1 write " + str(text) + " 1")
def gpdown(text):
    return os.system("gpio -1 write " + str(text) + " 0")
def gprele(text):
    return os.system("gpio -1 mode " + str(text) + " out")
    return os.system("gpio -1 mode " + str(text) + " out")
def gprup(text):
    return os.system("gpio -1 write " + str(text) + " 0")
def gprdown(text):
    return os.system("gpio -1 write " + str(text) + " 1")
