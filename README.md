# trucks-x-cargo

- Author: [Jorge Feldmann](https://github.com/jotafeldmann)
- Purpose: load cargos and trucks data (.csv files), pick the closest truck for each cargo, and output in the stdout.

## Requirements

- [Python 3.8](https://docs.python.org/3/whatsnew/3.8.html)
- [PipEnv](https://github.com/pypa/pipenv)

## Setup

- Start virutal env
```bash
make env
```

- Install dependencies
```bash
make install
```

## How to run

- Load default CSVs from `input` folder, with default options

```bash
make run
```

## More details

- For more details about the solution and options to run, please check [how-it-works](docs/how-it-works.md).
