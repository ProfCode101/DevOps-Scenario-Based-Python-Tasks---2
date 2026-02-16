# DevOps Scenario-Based Python Tasks

A collection of practical Python exercises designed to build foundational DevOps skills through hands-on scenarios. This project contains three progressive tasks that cover essential programming concepts including conditional logic, module imports, error handling, and data processing.

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Tasks](#tasks)
  - [Task 1: The Logic Master (FizzBuzz)](#task-1-the-logic-master-fizzbuzz)
  - [Task 2: Port Scanner Module](#task-2-port-scanner-module)
  - [Task 3: Server Data Processor](#task-3-server-data-processor)
- [Usage](#usage)
- [Learning Objectives](#learning-objectives)
- [Contributing](#contributing)

## 🎯 Overview

This repository contains three scenario-based Python tasks that simulate real-world DevOps challenges. Each task builds upon previous concepts while introducing new programming patterns and best practices.

## 📁 Project Structure

```
DevOps-Scenario-Based-Python-Tasks---2/
│
├── Task1/
│   ├── task1.py          # FizzBuzz implementation
│   └── task1.txt         # Task 1 requirements
│
├── Task2/
│   ├── task2.py          # Port scanner module
│   ├── app.py            # Main execution script
│   └── task2.txt         # Task 2 requirements
│
├── Task3/
│   ├── task3.py          # JSON server data processor
│   └── task3.txt         # Task 3 requirements
│
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```

## 🔧 Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

## 💻 Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd DevOps-Scenario-Based-Python-Tasks---2
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies** (if any):
   ```bash
   pip install -r requirements.txt
   ```

   Note: This project uses only Python standard library modules, so no external dependencies are required.

## 📚 Tasks

### Task 1: The Logic Master (FizzBuzz)

**Objective:** Master conditional logic and loops.

**Description:** Implement a classic FizzBuzz algorithm that processes numbers from 1 to a given limit, applying specific rules based on divisibility.

**Features:**
- Conditional logic with `if/elif/else` statements
- Loop iteration using `for` loops
- Modulo operator for divisibility checks

**File:** `Task1/task1.py`

**Usage:**
```python
from Task1.task1 import fizbuzz_checker

fizbuzz_checker(15)
```

**Output:**
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

### Task 2: Port Scanner Module

**Objective:** Practice cross-file imports and using immutable data types.

**Description:** Create a modular port scanner that checks for dangerous ports in a network environment. This task demonstrates Python module structure and the use of tuples for immutable data.

**Features:**
- Module creation and organization
- Cross-file imports
- Tuple data structure for immutable constants
- Function-based architecture

**Files:**
- `Task2/task2.py` - Port scanner module
- `Task2/app.py` - Main execution script

**Usage:**
```bash
cd Task2
python app.py
```

**Output:**
```
Port 21 is dangerous!
Port 23 is dangerous!
```

### Task 3: Server Data Processor

**Objective:** Safely handle external data strings using JSON and exception handling.

**Description:** Process JSON-formatted server status data from API responses with proper error handling. This task emphasizes robust error handling and data parsing.

**Features:**
- JSON parsing with `json.loads()`
- Exception handling with `try/except` blocks
- Error handling for malformed JSON
- Iteration over nested data structures

**File:** `Task3/task3.py`

**Usage:**
```bash
cd Task3
python task3.py
```

**Or programmatically:**
```python
from Task3.task3 import process_server_data

json_data = '{"servers": [{"name": "web-01", "status": "up"}, {"name": "db-01", "status": "down"}]}'
process_server_data(json_data)
```

**Output:**
```
{'servers': [{'name': 'web-01', 'status': 'up'}, {'name': 'db-01', 'status': 'down'}]}
Server Status: up
Server Status: down
```

## 🚀 Usage

Each task can be run independently:

1. **Task 1:**
   ```bash
   cd Task1
   python -c "from task1 import fizbuzz_checker; fizbuzz_checker(20)"
   ```

2. **Task 2:**
   ```bash
   cd Task2
   python app.py
   ```

3. **Task 3:**
   ```bash
   cd Task3
   python task3.py
   ```

## 🎓 Learning Objectives

By completing these tasks, you will gain proficiency in:

- ✅ **Conditional Logic**: Using `if/elif/else` statements effectively
- ✅ **Loops**: Implementing `for` loops for iteration
- ✅ **Functions**: Creating reusable, well-structured functions
- ✅ **Modules**: Organizing code into modules and packages
- ✅ **Imports**: Understanding Python's import system
- ✅ **Data Types**: Working with tuples, lists, and dictionaries
- ✅ **Error Handling**: Implementing try/except blocks for robust code
- ✅ **JSON Processing**: Parsing and processing JSON data
- ✅ **Code Organization**: Structuring projects for maintainability

## 🤝 Contributing

Contributions are welcome! If you'd like to improve these tasks or add new scenarios:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is provided for educational purposes.

## 👤 Author : Tasnim Rahmatullah

DevOps Learning Project

---

**Note:** This project is designed for educational purposes to help developers learn Python fundamentals through practical DevOps scenarios.

