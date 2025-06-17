# from-mps

* generates: sdc.api.Spectrum2D

Loads the spectra in MPS format.

```
usage: from-mps [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-N LOGGER_NAME]
                [--instrument INSTRUMENT] [--format FORMAT] [--keep_format]
                [-i [INPUT ...]] [-I [INPUT_LIST ...]]
                [--resume_from RESUME_FROM]

Loads the spectra in MPS format.

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
                        Path to the ASC file(s) to read; glob syntax is
                        supported; Supported placeholders: {HOME}, {CWD},
                        {TMP} (default: None)
  -I [INPUT_LIST ...], --input_list [INPUT_LIST ...]
                        Path to the text file(s) listing the ASC files to use;
                        Supported placeholders: {HOME}, {CWD}, {TMP} (default:
                        None)
  --resume_from RESUME_FROM
                        Glob expression matching the file to resume from,
                        e.g., '*/012345.asc' (default: None)
```

Available placeholders:

* `{HOME}`: The home directory of the current user.
* `{CWD}`: The current working directory.
* `{TMP}`: The temp directory.
