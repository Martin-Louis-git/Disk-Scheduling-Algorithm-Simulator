from setuptools import find_packages, setup

setup(
    name="os-disk-scheduling",
    version="0.1.0",
    py_modules=["simulator"],
    packages=["src"],
    entry_points={
        "console_scripts": [
            "run-simulator=simulator:main",
        ],
    },
)
