from setuptools import setup

setup(
    name='minined',
    version='0.1',
    description='Minimal Entity Linking',
    url='http://github.com/anon93559236/miniNED',
    author='Anonymous',
    license='MIT',
    packages=['minined'],
    zip_safe=False,
    entry_points={ 'console_scripts': ['minined = minined.__main__:main'] },
)