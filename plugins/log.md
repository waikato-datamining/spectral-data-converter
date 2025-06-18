# log

* accepts: sdc.api.Spectrum2D
* generates: sdc.api.Spectrum2D

Log-transforms the spectra.

```
usage: log [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-N LOGGER_NAME]
           [--skip] [-b BASE] [-o OFFSET]

Log-transforms the spectra.

options:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
  -N LOGGER_NAME, --logger_name LOGGER_NAME
                        The custom name to use for the logger, uses the plugin
                        name by default (default: None)
  --skip                Disables the plugin, removing it from the pipeline.
                        (default: False)
  -b BASE, --base BASE  The base for the logarithm. (default:
                        2.718281828459045)
  -o OFFSET, --offset OFFSET
                        The offset for the spectra. (default: 1.0)
```
