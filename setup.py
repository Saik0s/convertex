from setuptools import setup, find_packages

setup(
    name='Convertex',
    version='0.1.0',
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
