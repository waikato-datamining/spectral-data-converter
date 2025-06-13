# pyfunc-filter

* accepts: sdc.api.Spectrum2D
* generates: sdc.api.Spectrum2D

The declared Python function processes spectrum containers. The function must handle a single spectrum container or an iterable of spectrum containers and return a single spectrum container or an iterable of spectrum containers.

```
usage: pyfunc-filter [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                     [-N LOGGER_NAME] [--skip] -f FUNCTION

The declared Python function processes spectrum containers. The function must
handle a single spectrum container or an iterable of spectrum containers and
return a single spectrum container or an iterable of spectrum containers.

options:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
  -N LOGGER_NAME, --logger_name LOGGER_NAME
                        The custom name to use for the logger, uses the plugin
                        name by default (default: None)
  --skip                Disables the plugin, removing it from the pipeline.
                        (default: False)
  -f FUNCTION, --function FUNCTION
                        The Python function to use, format:
                        module_name:function_name (default: None)
```
