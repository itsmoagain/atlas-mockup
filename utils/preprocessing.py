"""
preprocessing.py

Reusable functions for loading and cleaning climate data
(NetCDF, raster, geospatial time series).
"""

import xarray as xr
import pandas as pd

def load_netcdf(filepath):
    """Load NetCDF file and return an xarray Dataset."""
    ds = xr.open_dataset(filepath)
    return ds

def extract_timeseries(ds, var, lat=None, lon=None):
    """
    Extract time series from a gridded xarray Dataset.

    Args:
        ds (xarray.Dataset): Input dataset
        var (str): Variable name (e.g., 'temperature')
        lat (float): Optional latitude
        lon (float): Optional longitude

    Returns:
        pandas.Series: Time series at selected point or average over grid
    """
    if lat and lon:
        ts = ds[var].sel(lat=lat, lon=lon, method="nearest").to_series()
    else:
        ts = ds[var].mean(dim=['lat', 'lon']).to_series()
    return ts
