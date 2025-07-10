# to-asc

* accepts: sdc.api.Spectrum2D
* default extension: .asc

Saves the spectrum in ASC format.

```
usage: to-asc [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-N LOGGER_NAME]
              [--skip] [--split_ratios SPLIT_RATIOS [SPLIT_RATIOS ...]]
              [--split_names SPLIT_NAMES [SPLIT_NAMES ...]]
              [--split_group SPLIT_GROUP] [-o OUTPUT]
              [--instrument_name INSTRUMENT_NAME]
              [--accessory_name ACCESSORY_NAME] [--data_points DATA_POINTS]
              [--first_x_point FIRST_X_POINT] [--last_x_point LAST_X_POINT]
              [--descending]

Saves the spectrum in ASC format.

options:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
  -N LOGGER_NAME, --logger_name LOGGER_NAME
                        The custom name to use for the logger, uses the plugin
                        name by default (default: None)
  --skip                Disables the plugin, removing it from the pipeline.
                        (default: False)
  --split_ratios SPLIT_RATIOS [SPLIT_RATIOS ...]
                        The split ratios to use for generating the splits
                        (must sum up to 100) (default: None)
  --split_names SPLIT_NAMES [SPLIT_NAMES ...]
                        The split names to use for the generated splits.
                        (default: None)
  --split_group SPLIT_GROUP
                        The regular expression with a single group used for
                        keeping items in the same split, e.g., for identifying
                        the base name of a file or the sample ID. (default:
                        None)
  -o OUTPUT, --output OUTPUT
                        The directory to store the .asc files in. Any defined
                        splits get added beneath there. Supported
                        placeholders: {INPUT_PATH}, {INPUT_NAMEEXT},
                        {INPUT_NAMENOEXT}, {INPUT_EXT}, {INPUT_PARENT_PATH},
                        {INPUT_PARENT_NAME} (default: None)
  --instrument_name INSTRUMENT_NAME
                        The instrument name to use in the header (default:
                        <not implemented>)
  --accessory_name ACCESSORY_NAME
                        The accessory name to use in the header (default: ABB-
                        BOMEM MB160D)
  --data_points DATA_POINTS
                        The number of data points to output, -1 for all
                        (default: -1)
  --first_x_point FIRST_X_POINT
                        The first wave number (default: 3749.3428948242)
  --last_x_point LAST_X_POINT
                        The last wave number (default: 9998.2477195313)
  --descending          Outputs the wave numbers in descending order (default:
                        False)
```

Available placeholders:

* `{INPUT_PATH}`: The directory part of the current input, i.e., `/some/where` of input `/some/where/file.txt`.
* `{INPUT_NAMEEXT}`: The name (incl extension) of the current input, i.e., `file.txt` of input `/some/where/file.txt`.
* `{INPUT_NAMENOEXT}`: The name (excl extension) of the current input, i.e., `file` of input `/some/where/file.txt`.
* `{INPUT_EXT}`: The extension of the current input (incl dot), i.e., `.txt` of input `/some/where/file.txt`.
* `{INPUT_PARENT_PATH}`: The directory part of the parent directory of the current input, i.e., `/some` of input `/some/where/file.txt`.
* `{INPUT_PARENT_NAME}`: The name of the parent directory of the current input, i.e., `where` of input `/some/where/file.txt`.
