import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="random-word",
    version="0.0.1",
    author="Vaibhav Singh",
    author_email="author@vaibhavsingh97.com",
    description="This is a simple python package to generate random english words",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vaibhavsingh97/random-word",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
