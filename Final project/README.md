# PlayStation Store

## Description

PlayStation Store is a Python console application that can simulate an interactive PlayStation Store environment directly inside the terminal. The application allows users to browse a catalog of video games, view exclusive PlayStation Plus subscription deals, search for specific titles, and add items to either a shopping cart (for paid games) or a personal game library (for free games).
The project is built around real-world software engineering practices in Python. It interacts dynamically with a structured CSV dataset (`store.csv`) to store and fetch game information, subscription tiers, and pricing details. Through clear interactive menu options, the program guides the user through browsing, searching, and managing their cart and library seamlessly.
Furthermore, the application features a robust checkout simulation system. It validates user inputs (such as payment method details and user responses) using Regular Expressions (Regex) and conditional checks, calculates the total price of selected items, and provides interactive feedback for both successful transactions and invalid inputs.

## Features

- Browse catalog:  Display available paid and free games retrieved from the CSV database.
- PlayStation Plus Deals: Show current subscription options and special offers.
- Search Functionality: Search for games by name with instant feedback on availability.
- Cart and Library: Add paid games to a shopping cart and free games directly to the library.
- Checkout Process: Calculate total costs and validate user input cleanly.
- Robust Error Handling: Handle unexpected or invalid user inputs gracefully without crashing.

## Files

- `projet.py`: The main Python script containing the core application logic, menu navigation loop, CSV data parsing, input validation, and checkout handling.

- `test_projet.py`: The test suite written with `pytest` to perform unit testing on key functions in `projet.py` to ensure high code quality and reliability.

- `store.csv`: A structured CSV file containing the dataset for games, categories, prices, and PlayStation Plus offers.

## How to Run

```bash
python projet.py
```

## How to Test

```bash
python -m pytest
```

## Technologies

- Python
- CSV
- Regular Expressions
- Pytest

## Video Demo

[CS50P Final Project](https://www.youtube.com/watch?v=oWFAZIPHMiw&t=11s)
