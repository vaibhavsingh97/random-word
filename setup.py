import random_word
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=random_word.__name__,
    version=random_word.__version__,
    author=random_word.__author__,
    author_email="hi@vaibhavsingh97.com",
    description="This is a simple python package to generate random english words",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="package random words word of the day random word generator",
    url="https://github.com/vaibhavsingh97/random-word",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    test_suite="nose.collector",
    tests_require=["nose"],
    install_requires=["requests", "nose"],
    include_package_data=True,
    zip_safe=False,
)
