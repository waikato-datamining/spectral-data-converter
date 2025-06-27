# from-csv-sd

* generates: sdc.api.SampleData

Loads the sample data in CSV format (row-wise).

```
usage: from-csv-sd [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                   [-N LOGGER_NAME] [-i [INPUT ...]] [-I [INPUT_LIST ...]]
                   [--resume_from RESUME_FROM] [--sample_id SAMPLE_ID]
                   [--sample_data SAMPLE_DATA]
                   [--sample_data_prefix SAMPLE_DATA_PREFIX]

Loads the sample data in CSV format (row-wise).

options:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
  -N LOGGER_NAME, --logger_name LOGGER_NAME
                        The custom name to use for the logger, uses the plugin
                        name by default (default: None)
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
  --sample_data SAMPLE_DATA
                        The range of columns containing the reference values
                        (1-based). (default: 2-last)
  --sample_data_prefix SAMPLE_DATA_PREFIX
                        The prefix used by the sample data columns. (default:
                        None)
```

Available placeholders:

* `{HOME}`: The home directory of the current user.
* `{CWD}`: The current working directory.
* `{TMP}`: The temp directory.
