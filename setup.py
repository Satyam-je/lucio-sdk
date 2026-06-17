from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="lucio-sdk",
    version="0.1.0",
    author="Artéfacts, Inc.",
    author_email="partnerships@artefacts.ai",
    description="Lucio SDK for token-based authorization and agent authentication.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/artefacts-inc/lucio-sdk",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests>=2.31.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "authentication",
        "authorization",
        "tokenization",
        "ai",
        "agents",
        "security",
        "lucio",
    ],
)
