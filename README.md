# Subfiles

subfiles is a python script for list all files with relative path from a main dir.

### How use

#### From CLI

```bash
$ git clone https://github.com/eddynelson/subfiles.git
$ sudo chmod 744 ./subfiles/subfiles.py
$ ./subfiles/subfiles.py
```

#### From python

``` pyhon
from subfiles import get_subfiles

subfiles = get_subfiles() # get list of file with relative path
print(subfiles) # print list of file with relative path
```