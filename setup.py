from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    """
    This function will return the requirements from the requirements.txt file
    """
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name='full_mlproject',
version='0.0.1',
author='Rahul',
author_email='rahulkrishlalwani@gmail.com', 
packages=find_packages(), #?it will search for all the packages in the directory with has __init__.py file
license='MIT',
install_requires=get_requirements('requirements.txt'),
)