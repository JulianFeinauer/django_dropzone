from setuptools import setup, find_packages

setup(
    name="django_dropzone",
    version="0.1.0",
    description="Example",
    author="Julian Feinauer",
    author_email="jfeinauer@hey.com",
    packages=find_packages(include=["django_dropzone"]),
    install_requires=["django"],
)
