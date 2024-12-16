# Luigi Training

---

## Content table

- [Environment setup](#environment-setup)
- [Usage](#usage)
  - [Python Modules](#python-modules)

---

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
---

## Usage

The purpose of `luigi` is running tasks. The simplest way to do so is to import a **module** and scheduling one of its
task on a `local-scheduler`

```bash
PYTHONPATH='.' luigi --module <module-name> <task-name> --local-scheduler  --<param-name> <param-value>
```

where:
- `module-name`: the module you want to select the task from
- `task-name`: the task (specifically the class name of the Task as defined into the module) you want to run
- `param-name`: a parameter defined in the task (i.e.: `luigi.Parameter()`) assuming value `param-value`

### Python Modules

To define a _multi-file_ **python module**:
- a directory must be created (i.e.: `my_module`)
- inside the directory a `__init__.py` file must me created
- each file created inside the directory will be considered a **sub-module** (i.e.: `./my_module/hello_tasks.py`)
- to connect all sub-modules inside the module, `__init__.py` must define an **import clause**

    ```python
    #__init__.py
    from .hello_tasks import Task1
    from .hello_tasks import Task2
    from .other_tasks import OtherTask
    ```
### Multiple executions
To run a task accepting `luigi.DateParameter` multiple times passing a **range of dates** use the `DailyRangeBase` 
utility

```bash
PYTHONPATH='.' luigi --module <module-name> DailyRangeBase --of <task-name>  --start <start_date> --stop <stop_date> --local-scheduler
```