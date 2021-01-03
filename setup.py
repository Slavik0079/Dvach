from setuptools import setup
from setuptools import find_packages

setup(

	author='Slavik007',
	author_email='https://2ch.hk/',

    packages=find_packages(),
    package_data={"dvach": ["*.txt"]},
    include_package_data=True,
    entry_points={ 'console_scripts': ['abu = dvach.__main__:main','bitard = dvach.__main__:main','2ch = dvach.__main__:main' ] },

    license="Bitard_License",
    )

