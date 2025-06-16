# row-norm

* accepts: sdc.api.Spectrum2D
* generates: sdc.api.Spectrum2D
* alias(es): standard-normal-variate

Subtracts mean and divides by standard deviation. Also known as standard normal variate.

```
usage: row-norm [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-N LOGGER_NAME]
                [--skip]

Subtracts mean and divides by standard deviation. Also known as standard
normal variate.

options:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
  -N LOGGER_NAME, --logger_name LOGGER_NAME
                        The custom name to use for the logger, uses the plugin
                        name by default (default: None)
  --skip                Disables the plugin, removing it from the pipeline.
                        (default: False)
```
