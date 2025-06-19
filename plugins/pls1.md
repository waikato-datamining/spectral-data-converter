# pls1

* accepts: sdc.api.Spectrum2D
* generates: sdc.api.Spectrum2D

Applies PLS1 to the batches of spectra. For more information see: https://en.wikipedia.org/wiki/Partial_least_squares_regression#PLS1

```
usage: pls1 [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-N LOGGER_NAME]
            [--skip] [-k METADATA_KEY] [--batch_order [BATCH_ORDER ...]]
            [--always_reset] [--save_to FILE] [--load_from FILE]
            [-p {none,center,standardize}] [-n NUM_COMPONENTS] [-r RESPONSE]

Applies PLS1 to the batches of spectra. For more information see:
https://en.wikipedia.org/wiki/Partial_least_squares_regression#PLS1

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
  -p {none,center,standardize}, --preprocessing {none,center,standardize}
                        The type of preprocessing to apply. (default: none)
  -n NUM_COMPONENTS, --num_components NUM_COMPONENTS
                        The number of PLS components. (default: 5)
  -r RESPONSE, --response RESPONSE
                        The name of the sample data field to use as response.
                        (default: None)
```
