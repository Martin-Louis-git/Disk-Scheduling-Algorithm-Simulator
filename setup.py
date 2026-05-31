from setuptools import setup, find_packages

setup(
    name="os-disk-scheduling",
    version="0.1.0",
    packages=find_packages(),
    entrypoints={
        "console_scripts": [
            "run-simulator=simulator:main",
        ],
    },
)
