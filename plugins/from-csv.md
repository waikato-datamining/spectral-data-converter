# from-csv

* generates: sdc.api.Spectrum2D

Loads the spectra in CSV format (row-wise).

```
usage: from-csv [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-N LOGGER_NAME]
                [--instrument INSTRUMENT] [--format FORMAT] [--keep_format]
                [-i [INPUT ...]] [-I [INPUT_LIST ...]]
                [--resume_from RESUME_FROM] [--sample_id SAMPLE_ID]
                [--spectral_data SPECTRAL_DATA] [--sample_data SAMPLE_DATA]
                [--sample_data_prefix SAMPLE_DATA_PREFIX]
                [--wave_numbers_in_header]
                [--wave_numbers_regexp WAVE_NUMBERS_REGEXP]

Loads the spectra in CSV format (row-wise).

options:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
  -N LOGGER_NAME, --logger_name LOGGER_NAME
                        The custom name to use for the logger, uses the plugin
                        name by default (default: None)
  --instrument INSTRUMENT
                        The instrument this data is from (default: unknown)
  --format FORMAT       The spectral data format to set (default: NIR)
  --keep_format         Will keep the format that the reader determines rather
                        than the supplied one. (default: False)
  -i [INPUT ...], --input [INPUT ...]
                        Path to the CSV file(s) to read; glob syntax is
                        supported; Supported placeholders: {HOME}, {CWD},
                        {TMP} (default: None)
  -I [INPUT_LIST ...], --input_list [INPUT_LIST ...]
                        Path to the text file(s) listing the CSV files to use;
                        Supported placeholders: {HOME}, {CWD}, {TMP} (default:
                        None)
  --resume_from RESUME_FROM
                        Glob expression matching the file to resume from,
                        e.g., '*/012345.csv' (default: None)
  --sample_id SAMPLE_ID
                        The 1-based index of the sample ID column. (default:
                        1)
  --spectral_data SPECTRAL_DATA
                        The range of columns containing the spectral data
                        (1-based). (default: 2-last)
  --sample_data SAMPLE_DATA
                        The range of columns containing the reference values
                        (1-based). (default: None)
  --sample_data_prefix SAMPLE_DATA_PREFIX
                        The prefix used by the sample data columns. (default:
                        None)
  --wave_numbers_in_header
                        Whether the wave numbers are encoded in the column
                        name. (default: False)
  --wave_numbers_regexp WAVE_NUMBERS_REGEXP
                        The regular expression for extracting the wave numbers
                        from the column names (1st group is used). (default:
                        (.*))
```

Available placeholders:

* `{HOME}`: The home directory of the current user.
* `{CWD}`: The current working directory.
* `{TMP}`: The temp directory.
