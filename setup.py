from setuptools import setup, find_packages

setup(
    name='basic-python-project',
    version='0.1.0',
    author='Atishay',
    author_email='atishay849@gmail.com',
    description='A basic Python project for mathematical operations.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    python_requires='>=3.6',
)