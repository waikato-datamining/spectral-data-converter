# simpls

* accepts: sdc.api.Spectrum2D
* generates: sdc.api.Spectrum2D

Applies SIMPLS to the batches of spectra.

```
usage: simpls [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-N LOGGER_NAME]
              [--skip] [-k METADATA_KEY] [--always_reset]
              [-p {none,center,standardize}] [-n NUM_COMPONENTS] -r RESPONSE
              [-c NUM_COEFFICIENTS]

Applies SIMPLS to the batches of spectra.

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
  -p {none,center,standardize}, --preprocessing {none,center,standardize}
                        The type of preprocessing to apply. (default: none)
  -n NUM_COMPONENTS, --num_components NUM_COMPONENTS
                        The number of PLS components. (default: 5)
  -r RESPONSE, --response RESPONSE
                        The name of the sample data field to use as response.
                        (default: None)
  -c NUM_COEFFICIENTS, --num_coefficients NUM_COEFFICIENTS
                        The number of coefficients of W to keep, 0 for all.
                        (default: 0)
```
