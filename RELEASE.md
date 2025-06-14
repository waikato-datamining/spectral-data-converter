PyPi
====

Preparation:

* update all help screens

  * `sdc-help -f markdown -o plugins -T pipeline -i README.md -l INFO`
  * `sdc-help -f markdown -o generators -T generator -i README.md -l INFO`
  
* update the help screen of `sdc-convert` in `README.md` to have the latest list of plugins
* update the help screen of `sdc-exec` in `README.md` to have the latest list of generators
* increment version in `setup.py`
* add new changelog section in `CHANGES.rst`
* align `DESCRIPTION.rst` with `README.md`  
* commit/push all changes

Commands for releasing on pypi.org (requires twine >= 1.8.0):

```
find -name "*~" -delete
rm dist/*
python3 setup.py clean
python3 setup.py sdist
twine upload dist/*
```


Github
======

Steps:

* start new release (version: `vX.Y.Z`)
* enter release notes, i.e., significant changes since last release
* upload `spectral_data_converter-X.Y.Z.tar.gz` previously generated with `setup.py`
* publish
