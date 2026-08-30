# alche-back-end

This repository contains backend engineering projects, including work with
APIs, data structures, and Python scripting for system administration
tasks (SRE-style).

## Background

Old-school system administrators usually only know Bash scripting. While
Bash is fine for a lot of things, it can get messy and inefficient
compared to other programming languages. This project focuses on using
Python to interact with a REST API instead of Bash, since accessing and
transforming JSON data is not well suited to shell scripting.

## api/

Python scripts that interact with a REST API (JSONPlaceholder) to
retrieve and export employee TODO list data.

- `0-gather_data_from_an_API. Given an employee ID, prints theirpy` 
  TODO list completion progress to standard output.
- `1-export_to_CSV. Exports a given employee's TODO list data to apy` 
  CSV file named `USER_ID.csv`.
- `2-export_to_JSON. Exports a given employee's TODO list data to apy` 
  JSON file named `USER_ID.json`.
- `3-dictionary_of_list_of_dictionaries. Exports TODO list data forpy` 
  all employees into a single JSON file named `todo_all_employees.json`.

### Requirements

- All files are interpreted on Ubuntu 14.04 LTS using `python3` (3.4.3)
- Every file starts with `#!/usr/bin/python3` on the first line
- All files end with a new line
- Imported libraries are organized in alphabetical order
- Code follows PEP 8 style
- All files are executable
- All modules are documented
- Dictionary values are accessed with `.get()`
- Code does not execute on import (`if __name__ == "__main__":`)

### Usage

```bash
python3 api/0-gather_data_from_an_API.py <employee_id>
python3 api/1-export_to_CSV.py <employee_id>
python3 api/2-export_to_JSON.py <employee_id>
python3 api/3-dictionary_of_list_of_dictionaries.py
```
