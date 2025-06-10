from setuptools import setup, find_packages
from typing import List

requirement_lst:List[str]=[]
def get_requirements() -> List[str]:
    """
    Reads the requirements.txt file and returns a list of requirements.
    """
    try:
        with open('requirements.txt', 'r') as file: 
            lines=file.readlines()
            for line in lines:
                requirements=line.strip()
                #ignore empty lines -e .
                if requirements and requirements!='-e .': 
                    requirement_lst.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found. Please create it with the necessary dependencies.")
    return requirement_lst

setup(
    name='Network Security',
    version='0.0.1',
    author='Koushik',
    author_email='koushikvardhanbandi@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
    description='A package for network security analysis and tools.'
)