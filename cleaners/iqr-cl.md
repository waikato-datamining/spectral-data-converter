# iqr-cl

* accepts: sdc.api.Spectrum2D
* generates: sdc.api.Spectrum2D

Calculates for each wave number the inter-quartile range and removes any spectra that have any amplitudes that fall outside the ranges: lower = q1 - factor * iqr, upper = q3 + factor * iqr

```
usage: iqr-cl [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-N LOGGER_NAME]
              [-f FACTOR]

Calculates for each wave number the inter-quartile range and removes any
spectra that have any amplitudes that fall outside the ranges: lower = q1 -
factor * iqr, upper = q3 + factor * iqr

options:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
  -N LOGGER_NAME, --logger_name LOGGER_NAME
                        The custom name to use for the logger, uses the plugin
                        name by default (default: None)
  -f FACTOR, --factor FACTOR
                        The factor to apply to the IQR range to determine
                        outliers. (default: 4.25)
```
