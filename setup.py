from setuptools import setup, find_packages

setup(
    name='convertex',
    version='0.1.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'convertex = main:main',
        ],
    },
    install_requires=[
        'argparse',
        'pathlib',
        'marvin',
        'rich',
    ],
)
