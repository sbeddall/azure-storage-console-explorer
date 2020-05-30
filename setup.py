from setuptools import setup, find_packages
import os, re

PACKAGE_NAME = "azure-storage-console-explorer"

DESCRIPTION = (
    "A console application that interacts with azure blob storage."
)

with open(os.path.join("asce", "_version.py"), "r") as fd:
    version = re.search(
        r'^VERSION\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE
    ).group(1)

if not version:
    raise RuntimeError("Cannot find version information")

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name=PACKAGE_NAME,
    description=DESCRIPTION,
    version=version,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sbeddall/azure-storage-console-explorer",
    author="sbeddall",
    author_email="sbeddall@gmail.com",
    license="MIT License",
    packages=find_packages(),
    install_requires=[
      "azure-storage-blob==12.3.1"
    ],
    python_requires=">=3.5.0"
)
