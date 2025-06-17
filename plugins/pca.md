# pca

* accepts: sdc.api.Spectrum2D
* generates: sdc.api.Spectrum2D

Applies principal components analysis to the data for dimensionality reduction.

```
usage: pca [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-N LOGGER_NAME]
           [--skip] [-k METADATA_KEY] [--always_reset] [-v VARIANCE]
           [-m MAX_COLUMNS] [-c]

Applies principal components analysis to the data for dimensionality
reduction.

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
  -v VARIANCE, --variance VARIANCE
                        The variance to use. (default: 0.95)
  -m MAX_COLUMNS, --max_columns MAX_COLUMNS
                        The maximum number of columns to generate, use -1 for
                        unlimited. (default: -1)
  -c, --center          Centers the data before applying PCA. (default: False)
```
