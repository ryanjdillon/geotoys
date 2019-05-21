"""
Methods for generating simple plots of data from NetCDF and GeoTIFF data
"""
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import netCDF4
import os
import rasterio

def add_geotiff_ax(ax, fp, band, index, crs):
    """
    Add a projected GeoTIFF raster to the Axes instance
    """

    src = rasterio.open(fp)

    extent = (src.bounds.left, src.bounds.right, src.bounds.bottom, src.bounds.top)
    ax.imshow(src.read()[0], transform=crs, extent=extent, origin="upper")

    return ax


def add_netcdf_ax(ax, fp, band_name, index, crs):
    """
    Add a projected NetCDF raster to the Axes instance
    """

    nc = netCDF4.Dataset(fp)

    var = nc[band_name][0,:,:]
    lons, lats = get_lons_lats(nc)

    ax.contourf(lons, lats, var, 60, transform=crs)

    return ax


def quickplot(fp, band, index=0, crs=None, coast_res="50m"):
    """
    Generate a projected plot the first timestep of data for a NetCDF or GeoTIFF file
    """

    ext = os.path.splitext(fp)[1]

    # Set plotting function
    if "nc" in ext:
        plt_func = add_netcdf_ax
    elif "tif" in ext:
        plt_func = add_geotiff_ax
    else:
        raise ValueError(f"File extensions {ext} not recognized")

    # Set CRS
    if crs is None:
        crs = ccrs.PlateCarree()

    ax = plt.axes(projection=crs)
    ax = plt_func(ax, fp, band, index, crs)
    ax.coastlines(resolution=coast_res, color="black", linewidth=1)

    plt.show()
