from setuptools import setup
from setuptools import find_packages

setup(

	author='Slavik007',
	author_email='https://2ch.hk/',

    version="0.0.1",
    long_description_content_type="text/markdown",
    python_requires=">=3.7.0",

    packages=find_packages(),
    include_package_data=True,
    install_requires = requiered,
    entry_points={ 'console_scripts': ['abu = dvach.__main__:main','bitard = dvach.__main__:main' ] },

    license="MIT License",
    )
