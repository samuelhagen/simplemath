from setuptools import setup, find_packages

setup(
    name='simplemath',
    version='0.1',
    packages=find_packages(),
    description='A simple math library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/simplemath',
    install_requires=[
        # Any dependencies, if you have them, like 'numpy>=1.18.1'
    ],
)
