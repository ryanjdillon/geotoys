from setuptools import setup, find_packages

install_requires = [
    "Cartopy>=0.17.0",
    "descartes>=1.1.0",
    "geopandas>=0.4.1",
    "netCDF4==1.5.0.1",
    "numpy>=1.16.2",
    "matplotlib>=3.0.3",
    "pandas>=0.24.2",
    "pyproj>=2.1.2",
    "rasterio>=1.0.22",
    "requests>=2.21.0",
    "sentinelsat>=0.13",
    "scipy>=1.2.1",
    "Shapely>=1.6.4",
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
