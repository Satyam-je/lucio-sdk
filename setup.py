from setuptools import setup, find_packages

setup(
    name="lucio-sdk",
    version="0.1.0",
    description="Lucio by Darpan — AI credential tokenization. No vault. Nothing stored. Nothing to steal.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Darpan, Inc.",
    author_email="partnerships@darpan.io",
    url="https://github.com/darpan-inc/lucio-sdk",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
    ],
)
