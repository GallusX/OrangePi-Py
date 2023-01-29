import os
import subprocess
def gpio_out(text):
    return os.system("gpio -1 mode " + str(text) + " out")
def gpio_up(text):
    return os.system("gpio -1 write " + str(text) + " 1")
def gpio_down(text):
    return os.system("gpio -1 write " + str(text) + " 0")
def gpio_rele(text):
    return os.system("gpio -1 mode " + str(text) + " out")
    return os.system("gpio -1 mode " + str(text) + " out")
def gpio_rup(text):
    return os.system("gpio -1 write " + str(text) + " 0")
def gpio_rdown(text):
    return os.system("gpio -1 write " + str(text) + " 1")
def gpio_button(text):
    return os.system("gpio -1 mode " + str(text) + " input")
def gpio_pull_up(text):
    return os.system("gpio -1 mode " + str(text) + " up")
def gpio_pull_down(text):
    return os.system("gpio -1 mode " + str(text) + " down")
def butclick(text):
    с = subprocess.run(["gpio","-1", "read", str(text)], stdout=subprocess.PIPE, text=True)
    return int(с.stdout)
    click = int(с.stdout)
