from setuptools import setup

setup(
    name="os-disk-scheduling",
    version="0.1.0",
    py_modules=["simulator"],
    entry_points={
        "console_scripts": [
            "run-simulator=simulator:main",
        ],
    },
)
