# Luigi Training

## Environment setup

To run the project is required the `luigi` library.
In order to simplify project execution it is useful to setup a **python virtual environment**

A `Makefile` has been provided to speedup the setup project (requires the command `python3`)

To **initialize** the `.venv` folder and download the dependencies under `requirements.txt` run: 

```bash 
make setup
```

To **clean up** run:
```bash 
make clean
```

To **enable the virtual environment**:
```bash 
source .venv/bin/activate
```

To **disable the virtual environment**:
```bash 
deactivate
```