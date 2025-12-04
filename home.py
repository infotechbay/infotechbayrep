import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 30
        self.inventory = []

    def is_alive(self):
        return self.health > 0


class Enemy:
    def __init__(self, name, health, dmg_range):
        self.name = name
        self.health = health
        self.dmg_range = dmg_range

    def attack(self):
        return random.randint(*self.dmg_range)


def slow_print(text, delay=0.03):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()


def battle(player, enemy):
    slow_print(f"\n⚔️ A wild {enemy.name} appears!")
    while enemy.health > 0 and player.is_alive():
        slow_print(f"\nYour HP: {player.health} | {enemy.name} HP: {enemy.health}")
        slow_print("Choose an action:\n1. Attack\n2. Heal\n> ", 0.01)
        choice = input()

        if choice == "1":
            dmg = random.randint(4, 8)
            enemy.health -= dmg
            slow_print(f"You strike the {enemy.name} for {dmg} damage!")
        elif choice == "2":
            heal = random.randint(5, 10)
            player.health += heal
            slow_print(f"You heal yourself for {heal} HP.")
        else:
            slow_print("Invalid choice, turn wasted...")

        if enemy.health > 0:
            edmg = enemy.attack()
            player.health -= edmg
            slow_print(f"The {enemy.name} hits you for {edmg} damage!")

    return player.is_alive()


def game():
    slow_print("🗺️ Welcome, traveler. What is your name?")
    name = input("> ")
    player = Player(name)
    slow_print(f"Greetings, {name}. Your journey begins...\n")

    time.sleep(1)

    slow_print("You enter a dark forest. The wind whispers your name.")
    time.sleep(1)

    enemies = [
        Enemy("Goblin", 15, (3, 6)),
        Enemy("Wolf", 18, (2, 8)),
        Enemy("Forest Spirit", 22, (4, 9))
    ]

    for enemy in enemies:
        alive = battle(player, enemy)
        if not alive:
            slow_print("\n💀 You have fallen... The forest claims another soul.")
            return
        else:
            slow_print(f"\n🏆 You defeated the {enemy.name}!")
            item = random.choice(["Healing Potion", "Magic Leaf", "Iron Dagger"])
            player.inventory.append(item)
            slow_print(f"You found a {item}!")

    slow_print("\n🌟 After defeating all foes, you find a glowing portal.")
    slow_print("You step through it and vanish into legend...")
    slow_print("\n🎉 THE END 🎉")


if __name__ == "__main__":
    game()

from netmiko import ConnectHandler

cisco_device = {
    "device_type": "cisco_ios",
    "host": "10.10.10.1",
    "username": "admin",
    "password": "password123",
    "secret": "password123"
}

net_connect = ConnectHandler(**cisco_device)
net_connect.enable()

output = net_connect.send_command("show ip interface brief")
print(output)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, username=username, password=password)

stdin, stdout, stderr = ssh.exec_command("show ip interface brief")
print(stdout.read().decode())

ssh.close()



    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

    import random

def roll_dice():
    return random.randint(1, 6)

for i in range(5):
    print(f"Roll {i+1}: {roll_dice()}")

    ],
    tests_require=test_requirements,
    # $ setup.py publish support.
    cmdclass={
        "upload": UploadCommand,
        "test": PyTest,
    },
)

requires = [
    "python-dateutil==2.8.2",
    "requests>=2.28.1",
]

extras = {"dev":["black"]}

test_requirements = [
    "pytest==7.1.3",
    "responses==0.21.0",
]

class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        self.status("Pushing git tags…")
        os.system("git tag v{0}".format(about["__version__"]))
        os.system("git push --tags")

        sys.exit()

Note: To use the 'upload' functionality of this file, you must:
pipenv install twine --dev

import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command
from setuptools.command.test import test as TestCommand

from netmiko import ConnectHandler

cisco_switch = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.10',
    'username': 'admin',
    'password': 'your_password',
}

net_connect = ConnectHandler(**cisco_switch)
output = net_connect.send_command("show interfaces")
net_connect.disconnect()

with open("interfaces_output.txt", "w") as file:
    file.write(output)

print("Interface details saved to interfaces_output.txt")

    ),


requires = [
    "python-dateutil==2.8.2",
    "requests>=2.28.1",
]

extras = {"dev":["black"]}

test_requirements = [
    "pytest==7.1.3",
    "responses==0.21.0",
]

class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        self.status("Pushing git tags…")
        os.system("git tag v{0}".format(about["__version__"]))
        os.system("git push --tags")

        sys.exit()


setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    python_requires=">=3.10",
    url=about["__url__"],
    packages=find_packages(
        exclude=[
            "tests",
            "*.tests",
            "*.tests.*",
            "tests.*",
            "tests/*"
        ]
    ),


requires = [
    "python-dateutil==2.8.2",
    "requests>=2.28.1",
]

extras = {"dev":["black"]}

test_requirements = [
    "pytest==7.1.3",
    "responses==0.21.0",
]

from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=('calibri', 50, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center')

time()
root.mainloop()
import requests

city = "London"
url = f"https://api.open-meteo.com/v1/forecast?latitude=51.5072&longitude=-0.1276&current_weather=true"

res = requests.get(url)
data = res.json()
print("Temperature:", data['current_weather']['temperature'], "°C")
print("Wind speed:", data['current_weather']['windspeed'], "km/h")


import random
import json

FILE = "scores.json"

def load_scores():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_scores(scores):
    with open(FILE, "w") as f:
        json.dump(scores, f, indent=4)

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("\n🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = input("Enter your guess: ")
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        guess = int(guess)
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} tries.\n")
    import random

num = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number (1–100): "))
    attempts += 1
    if guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} tries.")
        break

