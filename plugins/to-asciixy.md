# to-asciixy

* accepts: sdc.api.Spectrum2D
* default extension: .txt

Saves the spectrum in ASCII XY format.

```
usage: to-asciixy [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                  [-N LOGGER_NAME] [--skip]
                  [--split_ratios SPLIT_RATIOS [SPLIT_RATIOS ...]]
                  [--split_names SPLIT_NAMES [SPLIT_NAMES ...]]
                  [--split_group SPLIT_GROUP] [-o OUTPUT] [-s SEPARATOR]

Saves the spectrum in ASCII XY format.

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
                        The directory to store the ASCII XY .txt files in. Any
                        defined splits get added beneath there. Supported
                        placeholders: {INPUT_PATH}, {INPUT_NAMEEXT},
                        {INPUT_NAMENOEXT}, {INPUT_EXT}, {INPUT_PARENT_PATH},
                        {INPUT_PARENT_NAME} (default: None)
  -s SEPARATOR, --separator SEPARATOR
                        The separator to use for identifying X and Y columns.
                        (default: ;)
```

Available placeholders:

* `{INPUT_PATH}`: The directory part of the current input, i.e., `/some/where` of input `/some/where/file.txt`.
* `{INPUT_NAMEEXT}`: The name (incl extension) of the current input, i.e., `file.txt` of input `/some/where/file.txt`.
* `{INPUT_NAMENOEXT}`: The name (excl extension) of the current input, i.e., `file` of input `/some/where/file.txt`.
* `{INPUT_EXT}`: The extension of the current input (incl dot), i.e., `.txt` of input `/some/where/file.txt`.
* `{INPUT_PARENT_PATH}`: The directory part of the parent directory of the current input, i.e., `/some` of input `/some/where/file.txt`.
* `{INPUT_PARENT_NAME}`: The name of the parent directory of the current input, i.e., `where` of input `/some/where/file.txt`.
