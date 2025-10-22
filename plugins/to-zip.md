# to-zip

* accepts: sdc.api.Spectrum2D, sdc.api.SampleData
* default extension: .zip

Saves the spectra or sample data in a zip file using the specified direct writer.

```
usage: to-zip [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-N LOGGER_NAME]
              [--skip] -o OUTPUT [-c {stored,deflated,bzip2,lzma}] -w WRITER
              [-e EXTENSION]

Saves the spectra or sample data in a zip file using the specified direct
writer.

options:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
  -N LOGGER_NAME, --logger_name LOGGER_NAME
                        The custom name to use for the logger, uses the plugin
                        name by default (default: None)
  --skip                Disables the plugin, removing it from the pipeline.
                        (default: False)
  -o OUTPUT, --output OUTPUT
                        The zip file to store the spectra or sample data files
                        in. Supported placeholders: {HOME}, {CWD}, {TMP}
                        (default: None)
  -c {stored,deflated,bzip2,lzma}, --compression {stored,deflated,bzip2,lzma}
                        The compression to use. (default: stored)
  -w WRITER, --writer WRITER
                        The direct writer to use for writing the data in the
                        zip file. (default: None)
  -e EXTENSION, --extension EXTENSION
                        The extension to use for the files in the zip file,
                        overrides any default extension that the direct writer
                        may provide. (default: None)
```

Available placeholders:

* `{HOME}`: The home directory of the current user.
* `{CWD}`: The current working directory.
* `{TMP}`: The temp directory.
