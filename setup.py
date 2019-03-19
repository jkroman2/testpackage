from setuptools import setup, find_packages

setup(
    name='testpackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Hackathon python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/jkroman2/testpackage',
    author='Jason Kannemeyer',
    author_email='vonhitl@gmail.com'
)
