# ASC

Simple, plain-text format that contains some meta-data in its header section.

Meta-data consists of `key = value` pairs that are prefixed with `## `.

The spectral data is stored in two blank-separated columns, with the
first being the wave number and the second the amplitude.

Here is an example:

```
## Instrument Name = <not implemented>
## Accessory Name = ABB-BOMEM MB160D
## Product Name = 01
## Sample ID = 03bbd570dfd399bfd866ebcdf860de39
## Nr of data points = 1701
## First X Point = 3749.3428948242
## Last X Point = 9998.2477195313
## Wave number - Absorbance value
3749.34289482 1.61972
3753.01872119 1.61423
3756.69454756 1.61561
3760.37037393 1.62065
3764.04620029 1.62641
...
```
