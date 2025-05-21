'''
The setup.py file is an essential part of a Python project
that defines the project's metadata and dependencies.
It is a Python script that is used to configure and install 
the project.
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function returns the list of requirements
    '''
    try:
        requirements=[]
        HYPEN_E_DOT='-e .'
        with open(file_path) as file_obj:
            requirements=file_obj.readlines()
            requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    except FileNotFoundError:
        print("File not found")

    return requirements

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Badara Diallo",
    author_email="diallodouba17@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)