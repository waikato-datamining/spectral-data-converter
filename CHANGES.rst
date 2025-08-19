Changelog
=========

0.0.4 (????-??-??)
------------------

- `split-records` filter now allows specifying the meta-data field in which to store the split name
- the `tee` meta-filter can now forward or drop the incoming data based on a meta-data evaluation
- the `sub-process` filter can be used for processing data with sub-flow of filters, can be conditional based on meta-data evaluation
- the `metadata-from-name` filter can work on the path now as well (must be present)
- switched to `kasperl` library for base API and generic pipeline plugins
- requiring seppl>=0.2.21 now


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

