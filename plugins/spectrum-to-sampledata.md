# spectrum-to-sampledata

* accepts: sdc.api.Spectrum2D
* generates: sdc.api.SampleData

Extracts the sample data from the spectrum and forwards it. Ensures that the sample ID is present.

```
usage: spectrum-to-sampledata [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                              [-N LOGGER_NAME] [--skip]

Extracts the sample data from the spectrum and forwards it. Ensures that the
sample ID is present.

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
