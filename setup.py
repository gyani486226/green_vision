# Setuptools is a package development and distribution library.
# find_packages() finds all packages in the current directory.
# setup() is the main function for setting up a package.

from setuptools import   find_packages, setup
setup(
    name = "Green_Vision_Project",
    version = "0.1.0",
    author="gyanendra singh",
    author_email="gyani486226@gmail.com",
    packages = find_packages(), # it find all the packages in the current project
    install_requires = []
)


