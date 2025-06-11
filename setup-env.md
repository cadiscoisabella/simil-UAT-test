# Python Environment Management Script

This project provides a Python environment management script (`setup.py`) to automate the setup and management of virtual environments for Python 3.9 and 3.11 using `uv`.

## Prerequisites

- **Windows OS**
- **PowerShell**
- **uv package manager** (installed automatically if not found)

## Installation & Setup

- To set up 3.8, 3.9 & 3.11 projects, open the terminal and run:

```bash
python setup.py setup all
```
- To set up particular projects for e.g 3.9 or 3.11, open the terminal and run:

``` bash
python setup.py setup <3.9> or <3.11>
```

This will:

1. Check for `uv` and install it if missing.
2. Create virtual environments:
    - `.venv38` for Python 3.8
    - `.venv39` for Python 3.9
    - `.venv311` for Python 3.11
3. Install dependencies from:
    - `requirements/py38.txt`
    - `requirements/py39.txt`
    - `requirements/py311.txt`

## Activating Virtual Environments

To activate a specific virtual environment, run:

# Python 3.8 Virtual Environment Activation

## Version: 1.0.0

### Windows CMD
```cmd
call .venv39\Scripts\activate.bat && set VERSION=1.0.0
```

### Windows PowerShell
```powershell
# First check the execution policy
Get-ExecutionPolicy
# if it's restricted, then run the following command and then set env and version

Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force

# if is' bypass, run the following command directly
.\.venv38\Scripts\Activate.ps1; $env:VERSION = "1.0.0"
```

### Git Bash
```bash
source .venv38/Scripts/activate && export VERSION="1.0.0"
```

### Nushell
```nu
overlay use .venv38/Scripts/activate.nu; $env.VERSION = "1.0.0"
```
### WSL
```WSL
source .venv38/bin/activate && export VERSION="1.0.0"
```

# Python 3.9 Virtual Environment Activation

## Version: 1.0.0

### Windows CMD
```cmd
call .venv39\Scripts\activate.bat && set VERSION=1.0.0
```

### Windows PowerShell
```powershell
# First check the execution policy
Get-ExecutionPolicy
# if it's restricted, then run the following command and then set env and version

Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force

# if is' bypass, run the following command directly
.\.venv39\Scripts\Activate.ps1; $env:VERSION = "1.0.0"
```

### Git Bash
```bash
source .venv39/Scripts/activate && export VERSION="1.0.0"
```

### Nushell
```nu
overlay use .venv39/Scripts/activate.nu; $env.VERSION = "1.0.0"
```
### WSL
```WSL
source .venv39/bin/activate && export VERSION="1.0.0"
```

# Python 3.11 Virtual Environment Activation

## Version: 1.0.0

### Windows CMD
```cmd
call .venv311\Scripts\activate.bat && set VERSION=1.0.0
```

### Windows PowerShell
```powershell
# First check the execution policy
Get-ExecutionPolicy
# if it's restricted, then run the following command and then set env and version

Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force

# if is' bypass, run the following command directly
.\.venv311\Scripts\Activate.ps1; $env:VERSION = "1.0.0"
```

### Git Bash
```bash
source .venv311/Scripts/activate && export VERSION="1.0.0"
```

### Nushell
```nu
overlay use .venv311/Scripts/activate.nu; $env.VERSION = "1.0.0"
```

### WSL
```WSL
source .venv311/bin/activate && export VERSION="1.0.0"
```

## Verification
After activation, verify the environment:

```sh
python --version
echo $VERSION  # or %VERSION% in CMD
```

This will:

- Activate the environment in **CMD/ Nushell/ Powershell/ Git Bash**.
- Display the Python version.


## Installing package

- To install packages with uv
```
uv pip install <package_name>
```

## Deactivating the venv

- To deactivate the venv

```
deactivate
```

## Cleaning Up

- To remove all virtual environments, run:

### bash/cmd/Powershell/Nushell
```bash
python setup.py clean all
```
### WSL
```WSL
python3 setup.py clean all
```

- To remove a particular virtual environment, run :

### bash/cmd/Powershell/Nushell
```bash
python setup.py clean <3.8>, <3.9> or <3.11>
```

### WSL

```WSL
python3 setup.py clean <3.8>, <3.9> or <3.11>
```

This will delete the `.venv38` `.venv39` and `.venv311` directories.

## Notes

- Ensure **Python** is installed on your system.
- Modify `requirements/py38.txt`, `requirements/py39.txt` and `requirements/py311.txt` to manage dependencies.
- `setup.py` installs `setuptools==68.0.0` to ensure compatibility.
