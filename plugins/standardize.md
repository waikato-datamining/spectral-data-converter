# standardize

* accepts: sdc.api.Spectrum2D
* generates: sdc.api.Spectrum2D

Column-wise subtracts the column mean and divides by the column stdev.

```
usage: standardize [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                   [-N LOGGER_NAME] [--skip] [-k METADATA_KEY]
                   [--batch_order [BATCH_ORDER ...]] [--always_reset]
                   [--save_to FILE] [--load_from FILE]

Column-wise subtracts the column mean and divides by the column stdev.

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
                        NB: sorts the batch names alphabetically by default.
                        (default: None)
  --batch_order [BATCH_ORDER ...]
                        Lists the names of the batches to enforce an order
                        other than alphabetical. Batches that do not appear in
                        this list get appended to the order. (default: None)
  --always_reset        If enabled, the filter's 'trained' flag gets reset
                        with every batch and the filter retrained each time,
                        rather than only getting trained on the 1st batch and
                        then applied in that form to subsequent batches.
                        (default: False)
  --save_to FILE        The file to save the trained filter to. (default:
                        None)
  --load_from FILE      The file to load a trained filter from (instead of
                        training it on the first batch). (default: None)
```
