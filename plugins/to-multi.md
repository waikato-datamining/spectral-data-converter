# to-multi

* accepts: seppl.AnyData

Forwards the incoming data to all the base writers.

```
usage: to-multi [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-N LOGGER_NAME]
                [--skip] -w WRITER [WRITER ...]

Forwards the incoming data to all the base writers.

options:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
  -N LOGGER_NAME, --logger_name LOGGER_NAME
                        The custom name to use for the logger, uses the plugin
                        name by default (default: None)
  --skip                Disables the plugin, removing it from the pipeline.
                        (default: False)
  -w WRITER [WRITER ...], --writer WRITER [WRITER ...]
                        The command-line defining the base writer. (default:
                        None)
```
