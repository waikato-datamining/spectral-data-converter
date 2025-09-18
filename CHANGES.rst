Changelog
=========

0.1.0 (????-??-??)
------------------

- `split-records` filter now allows specifying the meta-data field in which to store the split name
- the `tee` meta-filter can now forward or drop the incoming data based on a meta-data evaluation
- the `sub-process` filter can be used for processing data with sub-flow of filters, can be conditional based on meta-data evaluation
- the `metadata-from-name` filter can work on the path now as well (must be present)
- switched to `kasperl` library for base API and generic pipeline plugins
- requiring seppl>=0.2.21 now
- added `@abc.abstractmethod` decorator where appropriate
- the `sdc-exec` tool now uses all remaining parameters as the pipeline components rather than having
  to specify them via the `-p/--pipeline` parameter, making it easy to simply prefix the `sdc-exec`
  command to an existing `sdc-convert` command-line
- added the `text-file` and `csv-file` generators that work off files to populate the variable(s)
- `sdc-exec` can load pipelines from file now as well, useful when dealing with large pipelines
- added `--load_pipeline` option to `sdc-convert`
- added `from-text-file` reader and `to-text-file` writer
- readers now locate files the first time the `read()` method gets called rather than in the
  `initialized()`, to allow more dynamic placeholders
- added `from-text-file` reader and `to-text-file` writer
- added `block`, `stop` filters for controlling the flow of data (via meta-data conditions)
- added email support with `get-email` reader and `send-email` writer
- added `list-files` reader for listing files in a directory
- added `list-to-sequence` stream filter that forwards list items one by one
- added `console` writer for outputting the data on stdout that is coming through
- added `watch-dir` meta-reader that uses the watchdog library to react to file-system events
  rather than using fixed-interval polling like `poll-dir`
- added `delete-files` writer
- added `copy-files` filter


0.0.3 (2025-07-15)
------------------

- requiring seppl>=0.2.20 now for improved help requests in `sdc-convert` tool


0.0.2 (2025-07-11)
------------------

- wai.spectralio-based readers now instantiate the wai.spectralio reader in the `initialize` method
- wai.spectralio-based writers now instantiate the wai.spectralio writer in the `initialize` method
- introduced `SpectralIOBased`, `SpectralIOReader` and `SpectralIOWriter` mixins to wai.spectralio-based
  readers/writers for a cleaner class hierarchy
- requiring wai-spectralio>=0.0.5 now
- requiring seppl>=0.2.19 now
- added experimental support for direct read/write operations using file-like objects
- fixed initialization of sample ID and sample data prefix in `CSVSampleDataWriter`
- fixed initialization of None values of `OPUSExtReader`, aligning it with the command-line args
- added `from-zip` meta-reader for reading spectra and sample data from zip files
- added `to-zip` meta-writer for writing spectra and sample data to zip files


0.0.1 (2025-06-27)
------------------

- initial release

