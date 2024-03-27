## Development

### Prerequisites

* Windows 10 / 11 (64-bit)
* git
* Python 3.11.8 (64-bit) - use [Pyenv](https://github.com/pyenv-win/pyenv-win)
to set correct version
* [PDM](https://github.com/pdm-project/pdm)

### Developing 

Clone the git repository into a directory of your choice:

```bash
git clone git@github.com:stefanoschalkidis/esign-myphoto.git
```

Enter the created directory and set up a development virtual environment:

```bash
pdm install
```

Run the app via:

```bash
pdm main
```

To format the code run:

```bash
pdm fmt
```

To lint the code run:

```bash
pdm lint
```

```bash
pdm lint-mypy
```

```bash
pdm lint-vulture
```

### Dependencies

To check the project's dependencies for updates run:

```bash
pdm update --dry-run --unconstrained --top
```

To apply the updates run:

```bash
pdm update --unconstrained --top
```

The ***requirements.txt*** file is required for the trivy scanner.
To update the ***requirements.txt*** file run:

```bash
pdm export -f requirements --without-hashes -o requirements.txt
```

### Vulnerabilities

To check for vulnerabilities run:

```bash
pdm trivy
```

The vulnerability report ***trivy-report.html*** can be found in the **target**
directory.

### Pre release

Update the program version in ***pyproject.toml*** and ***version_info.yml***.
To update the version in the ***version_info.txt*** file run:

```bash
pdm version-info
```

### Building

Open *PowerShell* and clone the git repository into the
*Windows root directory* **C:\\**:

```bash
git clone git@github.com:stefanoschalkidis/esign-myphoto.git
```

Enter the created directory:

```bash
cd C:\esign-myphoto
```

Create a virtual environment and install the packaging dependencies:

```bash
pdm install -G dev_package
```

The *typing* package needs to be removed as it clashes with *PyInstaller*:

```bash
.venv\Scripts\python -m pip uninstall typing
```

Build the application via:

```bash
pdm run pyinstaller -n amy_e-sign_myphoto -F --add-data src/data:data --version-file=src/data/version/version_info.txt .\src\main.py
```

The application is bundled into the **amy_e-sign_myphoto** directory and can be
found in the **dist** directory.
To remove the build directories run:

```bash
pdm clean
```

## Configuration

Create a directory named **config** in the project root and create a file named
***config.toml*** in there.
Populate the ***config.toml*** file with the following content and adjust it
according to your needs.

```toml
language = "el"

[signature]
license = "sdk_license"
reason = "signing_reason"
```
