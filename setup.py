from struct import pack
from setuptools import setup, find_packages
setup(
    name='nanoquant',
    packages=find_packages(exclude=['figures', 'act_scales'])
)
