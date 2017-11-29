import setuptools
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="ipython-IDV",
    version="0.1.8",
    url="https://github.com/piqueen314/drilsdown.git",

    author="Drilsdown team",
    author_email="cecehedrick@gmail.com",

    description="This project allows users to use Unidata's IDV with jupyter notebooks ",
    long_description=open('README.md').read(),

    packages=['drilsdown'],
    py_modules = ['drilsdown'],
    install_requires=['ipython'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    package_data={
        'drilsdown': [
            'drilsdownplugin.jar',
            'ramaddaplugin.jar',

        ],
    },
    package_dir={'drilsdown': 'drilsdown'},
    include_package_data=True,
)
