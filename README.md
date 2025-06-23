# README for App Console Python

## Description
This project is a simple console application that greets the user based on the time of day. It will say "Bonjour" if the time is before 6 PM and "Bonsoir" otherwise. The application also echoes back any input provided by the user.

## Project Structure
```
app-console-python
├── src
│   ├── main.py          # Entry point of the application
│   └── utils
│       └── time_greeting.py  # Contains the greeting logic based on time
├── requirements.txt     # Lists the dependencies required for the project
└── README.md            # Documentation for the project
```

## Requirements
To run this project, you need to have Python installed. You can install the required dependencies by running:

```
pip install -r requirements.txt
```

## Usage
To start the application, navigate to the `src` directory and run:

```
python main.py
```

Follow the prompts in the console to interact with the application. The application will greet you based on the current time and will repeat any input you provide.