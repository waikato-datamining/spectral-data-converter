# downsample

* accepts: sdc.api.Spectrum2D
* generates: sdc.api.Spectrum2D

Picks every n-th wave number.

```
usage: downsample [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                  [-N LOGGER_NAME] [--skip] [-s START_INDEX] [-n STEP]

Picks every n-th wave number.

options:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
  -N LOGGER_NAME, --logger_name LOGGER_NAME
                        The custom name to use for the logger, uses the plugin
                        name by default (default: None)
  --skip                Disables the plugin, removing it from the pipeline.
                        (default: False)
  -s START_INDEX, --start_index START_INDEX
                        The index to start sampling from. (default: 0)
  -n STEP, --step STEP  The step-size between samples. (default: 1)
```
