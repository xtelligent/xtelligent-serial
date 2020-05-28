import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

buildnumber = os.environ.get('BUILDNUMBER') or 1

setuptools.setup(
    name="xtelligent-serial", # Replace with your own username
    version=f'0.0.{buildnumber}',
    author="Xtelligent",
    author_email="development@xtelligent.io",
    description="Serialization, especially for JSON",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
