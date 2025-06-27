# ADAMS Report

Simple, plain-text based file format with a default file extension of `.report`.

The format is that of [Java properties](https://en.wikipedia.org/wiki/.properties) files.
In order to specify the data type of values, additional properties with the name 
suffix of `\tDataType` are added. The available options for the data type are:

* `B` - boolean
* `N` - number
* `S` - string
* `U` - unknown

Here is an example:

```
#Fri Jun 27 14:33:19 NZST 2025
Format=NIR
Format\tDataType=S
Parent\ ID=3
Parent\ ID\tDataType=S
Sample\ ID=03bbd570dfd399bfd866ebcdf860de39
Sample\ ID\tDataType=S
Sample\ Type=soil
Sample\ Type\tDataType=S
al.ext_usda.a1056_mg.kg=1020.0
al.ext_usda.a1056_mg.kg\tDataType=N
b.ext_mel3_mg.kg=0.001
b.ext_mel3_mg.kg\tDataType=N
c.tot_usda.a622_w.pct=1.061671317
c.tot_usda.a622_w.pct\tDataType=N
```
