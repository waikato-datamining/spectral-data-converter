# apply-cleaner

* accepts: seppl.AnyData
* generates: seppl.AnyData

Applies the specified cleaner to the batches of data it receives.

```
usage: apply-cleaner [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                     [-N LOGGER_NAME] [--skip] [-k METADATA_KEY]
                     [--batch_order [BATCH_ORDER ...]] [-c CLEANER]

Applies the specified cleaner to the batches of data it receives.

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
  -c CLEANER, --cleaner CLEANER
                        The command-line defining the cleaner. (default: None)
```
