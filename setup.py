from setuptools import setup

setup(
    # TODO: Write a globally unique name which will be listed on PyPI
    name="CI-CD-Homework-Dictionary-dgndds",
    author="Muhammed Doğancan Yılmazoğlu",  # TODO: Write your name
    version="2.0.4",
    packages=["dictionary"],
    install_requires=[
        "requests>=2.23.0",
    ],
    python_requires=">=3.8",
)
