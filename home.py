!/usr/bin/env python
-*- coding: utf-8 -*-


install_requires=requires,
    extras_require=extras,
    include_package_data=True,
    license=about["__license__"],
    classifiers=[
        Trove classifiers

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

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "pbipy", "__version__.py"), "r", encoding="utf-8") as f:
    exec(f.read(), about)

with open("README.md", "r", encoding="utf-") as f:
    readme = f.read()

import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command
from setuptools.command.test import test as TestCommand

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
            return attempts

def main():
    name = input("Enter your name: ")
    scores = load_scores()

    attempts = play_game()

    if name not in scores or attempts < scores[name]:
        scores[name] = attempts
        save_scores(scores)
        print(f"🏆 New personal best, {name}! Saved your score.\n")
    else:
        print(f"Your best record is {scores[name]} tries.\n")

if __name__ == "__main__":
    main()

output = net_connect.send_command("show ip interface brief")
print(output)

# Close connection
net_connect.disconnect()

