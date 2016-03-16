from setuptools import setup

setup(
    name='ivsort',
    version='0.2',
    description='proper sorting of pointed Hebrew texts',
    long_description=open('README.rst').read(),
    url='https://github.com/ninjaaron/ivsort',
    author='Aaron Christianson',
    author_email='ninjaaron@gmail.com',
    keywords='Hebrew sorting niqqud vowels',
    py_modules=['ivsort'],
    entry_points={'console_scripts': ['ivsort=ivsort:main']},
    install_requires=['six']
)
