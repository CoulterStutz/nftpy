import os
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nftpy",
    version="1.2.0.post4",
    author="CoulterStutz",
    author_email="coultercash@gmail.com",
    description="A NFT specific Python library for easy NFT integration in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CoulterStutz/nftpy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=[
        "web3>=6.2.0,<7.0.0",
        "requests>=2.28.1,<3.0.0",
        "aiohttp==3.9.5",
        "eth-abi>=4.0.0",
        "eth-account<0.13,>=0.8.0",
        "eth-hash>=0.5.1",
        "eth-typing!=4.2.0,>=3.0.0",
        "eth-utils>=2.1.0",
        "hexbytes<0.4.0,>=0.1.0",
        "jsonschema>=4.0.0",
        "lru-dict<1.3.0,>=1.1.6",
    ],
    extras_require={
        "dev": [
            "twine>=5.1.0"
        ]
    },
)
