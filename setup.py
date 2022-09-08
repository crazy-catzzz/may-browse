import setuptools

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setuptools.setup(name='may_browse', packages=['may_browse'], install_requires=install_requires)