# from-multi

* generates: seppl.AnyData

Reads data using the specified base readers and combines their output.

```
usage: from-multi [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                  [-N LOGGER_NAME] [--instrument INSTRUMENT] [--format FORMAT]
                  [--keep_format] -r READER [READER ...]
                  [-o {sequential,interleaved}]

Reads data using the specified base readers and combines their output.

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
  -r READER [READER ...], --reader READER [READER ...]
                        The command-line defining the base reader. (default:
                        None)
  -o {sequential,interleaved}, --read_order {sequential,interleaved}
                        How to use the output from the readers. (default:
                        sequential)
```
