# add-sampledata

* accepts: sdc.api.Spectrum2D
* generates: sdc.api.Spectrum2D

Loads sample data with the specified sample data reader and adds it to the spectra passing through based on matching sample ID.

```
usage: add-sampledata [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                      [-N LOGGER_NAME] [--skip] [-r READER]

Loads sample data with the specified sample data reader and adds it to the
spectra passing through based on matching sample ID.

options:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
  -N LOGGER_NAME, --logger_name LOGGER_NAME
                        The custom name to use for the logger, uses the plugin
                        name by default (default: None)
  --skip                Disables the plugin, removing it from the pipeline.
                        (default: False)
  -r READER, --reader READER
                        The sample data reader command-line. (default: None)
```
