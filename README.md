# Slice Code Challenge - Pizzabot

This script is written in [Python3](https://www.python.org)

##Getting started

Start by cloning the repo into a directory of your choice:
```sh
git clone https://github.com/alereynot/SliceCC.git
```

Move into the `py` directory where you will find 3 different approaches to the same challenge named:
```
/approach_1
/approach_2
/approach_3
```

No matter which approach you select, it's called using the same command line from within the approach's directory:

```commandline
./pizzabot [dimension] [coordinates]
```
Arguments are should be passed in this format inside **double quotes**:
```properties
dimension: nxm
coordinates: (x, y) ...
```

For example:
```commandline
./pizzabot "5x5 (3,4) (4,5)"
```