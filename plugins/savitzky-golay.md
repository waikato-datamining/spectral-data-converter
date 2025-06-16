# savitzky-golay

* accepts: sdc.api.Spectrum2D
* generates: sdc.api.Spectrum2D

Applies the Savitzky-Golay smoothing filter. For more details see: https://en.wikipedia.org/wiki/Savitzky-Golay_filter

```
usage: savitzky-golay [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                      [-N LOGGER_NAME] [--skip] [-p POLYNOMIAL_ORDER]
                      [-d DERIVATIVE_ORDER] [-L NUM_POINTS_LEFT]
                      [-R NUM_POINTS_RIGHT]

Applies the Savitzky-Golay smoothing filter. For more details see:
https://en.wikipedia.org/wiki/Savitzky-Golay_filter

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
  -L NUM_POINTS_LEFT, --num_points_left NUM_POINTS_LEFT
                        The number of points to the left from the current
                        point. (default: 3)
  -R NUM_POINTS_RIGHT, --num_points_right NUM_POINTS_RIGHT
                        The number of points to the right from the current
                        point. (default: 3)
```
