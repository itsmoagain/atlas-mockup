# Dataset Overview & Indicator Logic

This document summarizes the datasets and indicator logic used in the Atlas Mockup project.

## 🌍 Data Sources

- **ERA5 (ECMWF Reanalysis)** – Temperature, precipitation, wind
- **NDVI (MODIS or Sentinel-2)** – Vegetation index (greenness)
- **SPI (calculated)** – Standardized Precipitation Index
- **Land Cover (Copernicus or USGS)** – Classification overlays (optional)

## 🧠 Indicator Logic

| Indicator | Purpose | Method |
|----------|---------|--------|
| **SPI** | Drought risk | Rolling z-score of rainfall |
| **NDVI anomaly** | Vegetation stress | Current NDVI minus long-term average |
| **Temperature anomaly** | Heat signal | Current value minus climatology |
| **Precipitation anomaly** | Rainfall trend | Deviation from baseline |

## 🧪 Notes

- Data is stored locally in `netcdf/` and loaded with xarray
- Time series are visualized in `notebooks/`
- Functions live in `utils/preprocessing.py`

---

_Last updated: July 2025_
