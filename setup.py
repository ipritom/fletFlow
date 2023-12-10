from setuptools import setup

VERSION = "0.1.4"

setup(
    name="fletFlow",
    version=VERSION,
    description="Tiny Framework for Flet based application development with ease",
    url="https://github.com/ipritom/fletFlow",
    author='Pritom Mojumder',
    author_email='pritom.blue2@gmail.com',
    license='MIT',
    packages=['fletFlow'],
    install_requires=[
        "flet>=0.11.0",
    ],
    python_requires='>=3.9',
    zip_safe=False
)
