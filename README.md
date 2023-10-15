# AirBnB Clone - The Console

# Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Available Commands](#available-commands)
- [Author](#author)

# Description

The AirBnB Clone - The Console is a Command Line Interface (CLI) that serves as a simplified version of the AirBnB web application. It allows users to interact with data models through the command-line interface. This project is part of a larger effort to create a complete AirBnB clone and acts as the backend for managing data and models.

# Features

- Create, read, update, and delete instances of various data models (e.g., User, State, City, Place, Review, Amenity, etc.).
- Support for complex commands and queries through the CLI.
- Data persistence with JSON file storage.
- Easily extendable to support new data models.

# Installation

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

# Execution
Your could work like this in interactive mode:

	$ ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb) 
	(hbnb) 
	(hbnb) quit
	$

But also in non-interactive mode: (like the Shell project in C)

	$ echo "help" | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$

# Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* update - Updates an instance based on the class name and id
* quit/EOF - quit the console
* help - see descriptions of commands

To start console type in shell

    AirBnB_clone$ ./console.py
    (hbnb) 

## Create
To create an object use format "create <ClassName>" ex:

	(hbnb) create BaseModel

## Show
To show an instance based on the class name and id. Ex: 

	(hbnb) show BaseModel 1234-1234-1234.

## Destroy
To Delete an instance of an object use "destroy <ClassName> id". Ex: 

	(hbnb) destroy BaseModel 1234-1234-1234.

## All
all or all <class name> Ex: 

	(hbnb) all or all State

## Update
Updates an instance based on the class name and id:

	(hbnb) update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"

## Quit
quit or EOF

## Help
help or help <command> Ex: 

	(hbnb) help or help quit
	 Defines quit option
	(hbnb) 

# Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

# Author
Emmanuel Ntaadu Gyamfi
Email: <engyamfi@st.ug.edu.gh>
