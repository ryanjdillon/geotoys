from setuptools import setup, find_packages

install_requires = [
    "numpy>=1.16.2",
    "pandas>=0.24.2",
    "rasterio>=1.0.22",
]


setup(
    name="geotoys",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    version="0.0.0",
    url="https://github.com/ryanjdillon/geotoys",
    license="MIT",
    author="Ryan J. Dillon",
    author_email="ryanjamesdillon.gmail.com",
    description="Tools for working with geospatial data in python",
    install_requires=install_requires,
    test_suite="tests",
)
