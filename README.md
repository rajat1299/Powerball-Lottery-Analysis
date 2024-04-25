# Powerball Lottery Analysis

This repository contains a Python-based project that analyzes the historical data of the Powerball lottery. The project focuses on frequency analysis, hot and cold numbers, and providing insights to help users make informed decisions when playing the lottery.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Powerball Lottery Analysis project aims to provide a comprehensive analysis of the Powerball lottery results. By examining the historical data, the project identifies patterns, trends, and statistical insights that can be valuable for lottery enthusiasts and players.

## Features
- Frequency Analysis: The project performs a detailed frequency analysis of the main numbers and Powerball numbers, revealing the most frequently drawn numbers and their respective percentages.
- Hot and Cold Numbers: Users can specify the number of recent draws to consider and identify the hot numbers (frequently drawn in recent draws) and cold numbers (not drawn in recent draws).
- Automatic Updates: The project supports automatic updates of the analysis whenever new draw data is available, ensuring that the insights are always up to date.
- User-Friendly Interface: The project provides a user-friendly command-line interface that allows users to input their preferences and view the analysis results easily.

## Installation
To run the Powerball Lottery Analysis project locally, follow these steps:

1. Clone the repository: git clone https://github.com/your-username/powerball-lottery-analysis.git
2. Navigate to the project directory: cd powerball-lottery-analysis
3. Install the required dependencies: pip install -r requirements.txt
4. Prepare the data:
- Place the cleaned and preprocessed Powerball lottery dataset in CSV format in the project directory.
- Ensure that the dataset file is named `Lottery_Powerball_Cleaned.csv`.

## Usage
To use the Powerball Lottery Analysis project, follow these steps:

1. Run the main script:
2. Follow the prompts in the command-line interface to specify the number of recent draws to consider for hot and cold numbers.

3. View the analysis results, including the frequency analysis, hot numbers, and cold numbers.

4. To update the analysis with new draw data, provide the new data in the specified format and run the script again.

## Data
The project requires a cleaned and preprocessed Powerball lottery dataset in CSV format. The dataset should include the following columns:
- `Draw Date`: The date of each lottery draw.
- `Number 1` to `Number 5`: The five main numbers drawn in each draw.
- `Powerball`: The Powerball number drawn in each draw.

Please ensure that the dataset is properly formatted and placed in the project directory with the name `Lottery_Powerball_Cleaned.csv`.

## Contributing
Contributions to the Powerball Lottery Analysis project are welcome! If you have any ideas, suggestions, or improvements, please feel free to open an issue or submit a pull request. Make sure to follow the project's code of conduct and guidelines for contributing.

## License
This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code for both commercial and non-commercial purposes.
