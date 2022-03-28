from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="magic-container",
    version="0.0.4",
    author="KingKevin23",
    author_email="code@kingkevin.de",
    description="Thread-safe, magical and persistent dict for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KingKevin23/container",
    project_urls={
        "Bug Tracker": "https://github.com/KingKevin23/container/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "sqlitedict>=1.7.0"
    ],
)