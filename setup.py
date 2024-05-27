# setup.py
from setuptools import setup, find_packages

setup(
    name="drhyme",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "pymorphy3>=2.0.1",
        "rusyllab @ git+https://github.com/Koziev/rusyllab@c5d0ea405e9cc8233bd65503c26c0d2ad8b5cb57"
    ],
    author="zxolad",
    description="Simple lib for generate rhymes",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)