# AirBnB Clone - The Console
## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [#available-commands-and-what-they-doAvailable commands](#commands)
- [Contributing](#contributing)
- [Author](#author)

## Description

The AirBnB Clone-The console: A Command Line Interface (CLI) is a simplified version of the AirBnB web application that allows users to interact with data models through a command-line interface. This project is part of a larger project to create a complete AirBnB clone, and it serves as the backend for managing data and models.

## Features

- Create, read, update, and delete instances of various data models (e.g., User, State, City, Place, Review, Amenity, etc.).
- Support for complex commands and queries through the CLI.
- Data persistence with JSON file storage.
- Easily extendable to support new data models.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/KwameNtaadu007/AirBnB_clone
   ```

2. Change to the project directory:
   ```bash
   cd AirBnB_clone
   ```

3. Run the CLI:
   ```bash
   ./console.py
   ```

## Usage

The CLI provides a command-line interface for interacting with data models. To start the CLI, simply run `console.py` as described in the Installation section. The prompt `(hbnb)` will indicate that you are in the CLI.

For example, you can create a new User instance by running the following command:
```python
(hbnb) create User
```

You can also use the `show`, `all`, `update`, and `destroy` commands to manage instances. For a complete list of commands, please refer to the [Commands](#commands) section.

## Available commands and what they do

Here are some of the available commands and their usage:

- `create <class_name>`: Create a new instance of the specified class.
- `show <class_name> <id>`: Show information about a specific instance.
- `destroy <class_name> <id>`: Delete an instance based on the class name and ID.
- `all [<class_name>]`: Retrieve and print all instances or all instances of a specified class.
- `update <class_name> <id> <attribute_name> <attribute_value>`: Update an instance based on its ID with a specific attribute.
- `update <class_name> <id> <dictionary_representation>`: Update an instance based on its ID with a dictionary.

|Command| Description |
|--|--|
| **quit or EOF** | Exits the program |
| **Usage** | By itself |
| **-----** | **-----** |
| **help** | Provides a text describing how to use a command.  |
| **Usage** | By itself --or-- **help <command\>** |
| **-----** | **-----** |
| **create** | Creates a new instance of a valid `Class`, saves it (to the JSON file) and prints the `id`.  Valid classes are: BaseModel, User, State, City, Amenity, Place, Review. |
| **Usage** | **create <class name\>**|
| **-----** | **-----** |
| **show** | Prints the string representation of an instance based on the class name and `id`  |
| **Usage** | **show <class name\> <id\>** --or-- **<class name\>.show(<id\>)**|
| **-----** | **-----** |
| **destroy** | Deletes an instance based on the class name and `id` (saves the change into a JSON file).  |
| **Usage** | **destroy <class name\> <id\>** --or-- **<class name>.destroy(<id>)** |
| **-----** | **-----** |
| **all** | Prints all string representation of all instances based or not on the class name.  |
| **Usage** | By itself or **all <class name\>** --or-- **<class name\>.all()** |
| **-----** | **-----** |
| **update** | Updates an instance based on the class name and `id` by adding or updating attribute (saves the changes into a JSON file).  |
| **Usage** | **update <class name\> <id\> <attribute name\> "<attribute value\>"** ---or--- **<class name\>.update(<id\>, <attribute name\>, <attribute value\>)** --or-- **<class name\>.update(<id\>, <dictionary representation\>)**|
| **-----** | **-----** |
| **count** | Retrieve the number of instances of a class.  |
| **Usage** | **<class name\>.count()** |

## Contributing

This project is open for contributions. If you have ideas for improvements or bug fixes, feel free to fork the repository and submit a pull request.

1. Fork the project.
2. Create a new branch for your feature or bug fix.
3. Implement your changes.
4. Test your changes thoroughly.
5. Submit a pull request.



## Author

Emmanuel Ntaadu Gyamfi<engyamfi@st.ug.edu.gh>


