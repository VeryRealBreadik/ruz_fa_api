from setuptools import setup
from os import path


current_directory = path.abspath(path.dirname(__file__))
with open(path.join(current_directory, "README.md"), encoding="utf-8") as file:
    long_description = file.read()

setup(
    name="fu-ruz-api",
    version="0.1.0",    
    description="Small API wrapper for ruz.fa.ru",
    url="https://github.com/XJIE6yIlIek/fu-ruz-api",
    author="Stankovskiy Aleksey",
    author_email="aleksey_stankovskiy@rambler.ru",
    license="GNU GPLv3",
    packages=["fu_ruz_api"],
    install_requires=[
                    "requests",
                    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
