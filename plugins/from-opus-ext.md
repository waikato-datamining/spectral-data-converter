# from-opus-ext

* generates: sdc.api.Spectrum2D

Loads the spectra in Bruker OPUS (extended) format.

```
usage: from-opus-ext [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                     [-N LOGGER_NAME] [--instrument INSTRUMENT]
                     [--format FORMAT] [--keep_format] [-i [INPUT ...]]
                     [-I [INPUT_LIST ...]] [--resume_from RESUME_FROM]
                     [--spectrum_block_type SPECTRUM_BLOCK_TYPE]
                     [--operation OPERATION] [--key KEY] [--all_spectra]
                     [--add_command_lines] [--add_log]

Loads the spectra in Bruker OPUS (extended) format.

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
                        Path to the OPUS file(s) to read; glob syntax is
                        supported; Supported placeholders: {HOME}, {CWD},
                        {TMP} (default: None)
  -I [INPUT_LIST ...], --input_list [INPUT_LIST ...]
                        Path to the text file(s) listing the OPUS files to
                        use; Supported placeholders: {HOME}, {CWD}, {TMP}
                        (default: None)
  --resume_from RESUME_FROM
                        Glob expression matching the file to resume from,
                        e.g., '*/012345.0' (default: None)
  --spectrum_block_type SPECTRUM_BLOCK_TYPE
                        The block type of the spectrum to extract, in hex
                        notation (default: 100f)
  --operation OPERATION
                        The command-line operation to get the sample ID from,
                        e.g., 'MeasureSample' (default: MeasureSample)
  --key KEY             The command-line key to get the sample ID from, e.g,
                        'NAM' (default: -1)
  --all_spectra         If enabled, all spectra stored in the file are loaded.
                        (default: False)
  --add_command_lines   If enabled, the other command-lines extracted from the
                        file gets added to the report. (default: False)
  --add_log             If enabled, the entire log extracted from the file
                        gets added to the report. (default: False)
```

Available placeholders:

* `{HOME}`: The home directory of the current user.
* `{CWD}`: The current working directory.
* `{TMP}`: The temp directory.
