# center

* accepts: sdc.api.Spectrum2D
* generates: sdc.api.Spectrum2D

Subtracts the column mean from the columns. Requires multiple spectra as input.

```
usage: center [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-N LOGGER_NAME]
              [--skip] [-k METADATA_KEY] [--always_reset]

Subtracts the column mean from the columns. Requires multiple spectra as
input.

options:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
  -N LOGGER_NAME, --logger_name LOGGER_NAME
                        The custom name to use for the logger, uses the plugin
                        name by default (default: None)
  --skip                Disables the plugin, removing it from the pipeline.
                        (default: False)
  -k METADATA_KEY, --metadata_key METADATA_KEY
                        The key in the meta-data that identifies the batches.
                        NB: sorts the batch names alphabetically. (default:
                        None)
  --always_reset        If enabled, the filter's 'trained' flag gets reset
                        with every batch (default: False)
```
