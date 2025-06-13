# ADAMS

Simple, plain-text based file format with a default file extension of `.spec`.

## Spectral data

The spectral data is stored in two, comma-separated columns, e.g.:

```
waveno,amplitude
600.0,1.61972
602.0,1.61423
604.0,1.61561
606.0,1.62065
```

## Meta-data

Additionally, meta-data can be placed at the start of the file. The format
is that of [Java properties](https://en.wikipedia.org/wiki/.properties), 
each line prefixed with `# `. In order to specify the data type of values,
additional properties with the name suffix of `\tDataType` are added. The available
options for the data type are:

* `B` - boolean
* `N` - number
* `S` - string
* `U` - unknown

Here is an example:

```
# #Thu Jun 12 16:22:24 NZST 2025
# Format=MIR
# Format\tDataType=S
# Parent\ ID=3
# Sample\ ID=03bbd570dfd399bfd866ebcdf860de39
# Sample\ ID\tDataType=S
# Sample\ Type=soil
# Sample\ Type\tDataType=S
# al.ext_usda.a1056_mg.kg=1020.0
# al.ext_usda.a1056_mg.kg\tDataType=N
waveno,amplitude
600.0,1.61972
602.0,1.61423
604.0,1.61561
606.0,1.62065
```

## Multiple spectra

The .spec format also supports storing multiple spectra. In such a case, the
spectra a separated by a line of `---`.
