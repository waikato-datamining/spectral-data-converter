# savitzky-golay2

* accepts: sdc.api.Spectrum2D
* generates: sdc.api.Spectrum2D

Applies the Savitzky-Golay smoothing filter, using a centered window of the specified size. For more details see: https://en.wikipedia.org/wiki/Savitzky-Golay_filter

```
usage: savitzky-golay2 [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                       [-N LOGGER_NAME] [--skip] [-p POLYNOMIAL_ORDER]
                       [-d DERIVATIVE_ORDER] [-n NUM_POINTS]

Applies the Savitzky-Golay smoothing filter, using a centered window of the
specified size. For more details see: https://en.wikipedia.org/wiki/Savitzky-
Golay_filter

options:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
  -N LOGGER_NAME, --logger_name LOGGER_NAME
                        The custom name to use for the logger, uses the plugin
                        name by default (default: None)
  --skip                Disables the plugin, removing it from the pipeline.
                        (default: False)
  -p POLYNOMIAL_ORDER, --polynomial_order POLYNOMIAL_ORDER
                        The polynomial order to use. (default: 2)
  -d DERIVATIVE_ORDER, --derivative_order DERIVATIVE_ORDER
                        The derivative order to use. (default: 1)
  -n NUM_POINTS, --num_points NUM_POINTS
                        The size of the window (left + center + right), must
                        be an odd number. (default: 7)
```
