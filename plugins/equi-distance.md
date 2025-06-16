# equi-distance

* accepts: sdc.api.Spectrum2D
* generates: sdc.api.Spectrum2D

Generates a spectrum with the specified number of equally spaced wave numbers. The amplitudes gets interpolated accordingly.

```
usage: equi-distance [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                     [-N LOGGER_NAME] [--skip] -n NUM_WAVENOS

Generates a spectrum with the specified number of equally spaced wave numbers.
The amplitudes gets interpolated accordingly.

options:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
  -N LOGGER_NAME, --logger_name LOGGER_NAME
                        The custom name to use for the logger, uses the plugin
                        name by default (default: None)
  --skip                Disables the plugin, removing it from the pipeline.
                        (default: False)
  -n NUM_WAVENOS, --num_wavenos NUM_WAVENOS
                        The number of wavenumbers to resample to. (default:
                        None)
```
