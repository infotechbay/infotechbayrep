tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        if tasks:
            print("\nYour tasks:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
        else:
            print("No tasks yet.")
    elif choice == "2":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")
    elif choice == "3":
        task_num = int(input("Enter task number to remove: "))
        if 0 < task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")


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

