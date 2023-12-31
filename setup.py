from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(filename: str) -> List[str]:
    """Get list of requirements from a file"""
    with open(filename) as f:
        requirements = f.read().splitlines()

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="IML-Project",
    version="0.0.1",
    packages=find_packages(exclude=["tests*"]),
    author="Shahil Kumar, Manu Pande, Gourav Rawat",
    license="MIT",
    long_description=open("README.md").read(),
    install_requires=get_requirements("requirements.txt"),
)
