# from-cal

* generates: sdc.api.Spectrum2D

Loads the spectra in FOSS CAL format.

```
usage: from-cal [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-N LOGGER_NAME]
                [--instrument INSTRUMENT] [--format FORMAT] [--keep_format]
                [-i [INPUT ...]] [-I [INPUT_LIST ...]]
                [--resume_from RESUME_FROM] [--type_field TYPE_FIELD]
                [--id_field ID_FIELD] [-s START] [-m MAX]

Loads the spectra in FOSS CAL format.

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
                        Path to the NIR file(s) to read; glob syntax is
                        supported; Supported placeholders: {HOME}, {CWD},
                        {TMP} (default: None)
  -I [INPUT_LIST ...], --input_list [INPUT_LIST ...]
                        Path to the text file(s) listing the NIR files to use;
                        Supported placeholders: {HOME}, {CWD}, {TMP} (default:
                        None)
  --resume_from RESUME_FROM
                        Glob expression matching the file to resume from,
                        e.g., '*/012345.nir' (default: None)
  --type_field TYPE_FIELD
                        Code|Field1|Field2|Field3|ID|[sample_type] (default:
                        Code)
  --id_field ID_FIELD   ID|Field1|Field2|Field3|[prefix] (default: ID)
  -s START, --start START
                        The spectrum number to start loading from (default: 1)
  -m MAX, --max MAX     The maximum number of spectra to load, -1 for all
                        (default: -1)
```

Available placeholders:

* `{HOME}`: The home directory of the current user.
* `{CWD}`: The current working directory.
* `{TMP}`: The temp directory.
