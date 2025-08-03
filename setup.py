from setuptools import setup, find_packages


setup(
    name='colorME',
    version='0.1.0',
    description='A simple coloring util for better output visibility',
    author='Abdulrahman Khaled',
    packages=find_packages(),
    install_requires=['termcolor'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Dependent'
    ],
    python_requires='>3.10'
)