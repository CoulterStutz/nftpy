from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="nftpy",
    version="1.2.0post1",
    author="CoulterStutz",
    author_email="coultercash@gmail.com",
    description="A NFT specific Python library for easy NFT integration in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/coulterstutz/nftpy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=requirements,
)
