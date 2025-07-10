# to-arff

* accepts: sdc.api.Spectrum2D
* default extension: .arff

Saves the spectra in ARFF format (row-wise).

```
usage: to-arff [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-N LOGGER_NAME]
               [--skip] [--split_ratios SPLIT_RATIOS [SPLIT_RATIOS ...]]
               [--split_names SPLIT_NAMES [SPLIT_NAMES ...]]
               [--split_group SPLIT_GROUP] [-o OUTPUT] [--sample_id SAMPLE_ID]
               [--sample_data [SAMPLE_DATA ...]]
               [--sample_data_prefix SAMPLE_DATA_PREFIX]
               [--wave_numbers_format WAVE_NUMBERS_FORMAT]

Saves the spectra in ARFF format (row-wise).

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
                        The ARFF file to store the spectra in. (default: None)
  --sample_id SAMPLE_ID
                        The name to use for the sample ID attribute. (default:
                        sample_id)
  --sample_data [SAMPLE_DATA ...]
                        The sample data names to store in ARFF file. (default:
                        [])
  --sample_data_prefix SAMPLE_DATA_PREFIX
                        The prefix to use for the sample data attributes.
                        (default: )
  --wave_numbers_format WAVE_NUMBERS_FORMAT
                        The format to use for the spectral data columns, the
                        following placeholders are available: {WAVE}|{INDEX}
                        (default: {WAVE})
```

Available placeholders:

* `{INPUT_PATH}`: The directory part of the current input, i.e., `/some/where` of input `/some/where/file.txt`.
* `{INPUT_NAMEEXT}`: The name (incl extension) of the current input, i.e., `file.txt` of input `/some/where/file.txt`.
* `{INPUT_NAMENOEXT}`: The name (excl extension) of the current input, i.e., `file` of input `/some/where/file.txt`.
* `{INPUT_EXT}`: The extension of the current input (incl dot), i.e., `.txt` of input `/some/where/file.txt`.
* `{INPUT_PARENT_PATH}`: The directory part of the parent directory of the current input, i.e., `/some` of input `/some/where/file.txt`.
* `{INPUT_PARENT_NAME}`: The name of the parent directory of the current input, i.e., `where` of input `/some/where/file.txt`.
