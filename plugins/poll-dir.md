# poll-dir

* generates: sdc.api.Spectrum

Polls a directory for files and presents them to the base reader.

```
usage: poll-dir [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-N LOGGER_NAME]
                [--instrument INSTRUMENT] [--format FORMAT] [--keep_format] -i
                DIR_IN -o DIR_OUT [-w POLL_WAIT] [-W PROCESS_WAIT] [-d] -e
                EXTENSIONS [EXTENSIONS ...] [-O [OTHER_INPUT_FILES ...]]
                [-m MAX_FILES] [-b BASE_READER]

Polls a directory for files and presents them to the base reader.

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
  -i DIR_IN, --dir_in DIR_IN
                        The directory to poll; Supported placeholders: {HOME},
                        {CWD}, {TMP} (default: None)
  -o DIR_OUT, --dir_out DIR_OUT
                        The directory to move the files to; Supported
                        placeholders: {HOME}, {CWD}, {TMP} (default: None)
  -w POLL_WAIT, --poll_wait POLL_WAIT
                        The poll interval in seconds (default: 1.0)
  -W PROCESS_WAIT, --process_wait PROCESS_WAIT
                        The number of seconds to wait before processing the
                        polled files (e.g., waiting for files to be fully
                        written) (default: 0.0)
  -d, --delete_input    Whether to delete the input files rather than move
                        them to --dir_out directory (default: False)
  -e EXTENSIONS [EXTENSIONS ...], --extensions EXTENSIONS [EXTENSIONS ...]
                        The extensions of the files to poll (incl. dot)
                        (default: None)
  -O [OTHER_INPUT_FILES ...], --other_input_files [OTHER_INPUT_FILES ...]
                        The glob expression(s) for capturing other files apart
                        from the input files; use {NAME} in the glob
                        expression for the current name (default: None)
  -m MAX_FILES, --max_files MAX_FILES
                        The maximum number of files in a single poll; <1 for
                        unlimited (default: -1)
  -b BASE_READER, --base_reader BASE_READER
                        The command-line of the reader for reading the files
                        (default: None)
```

Available placeholders:

* `{HOME}`: The home directory of the current user.
* `{CWD}`: The current working directory.
* `{TMP}`: The temp directory.
