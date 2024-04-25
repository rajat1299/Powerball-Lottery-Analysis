import pandas as pd
import numpy as np

# Load the dataset from a CSV file
df = pd.read_csv('Lottery_Powerball_Winning_Numbers__Beginning_2010.csv')

# Convert the 'Draw Date' column to datetime type
df['Draw Date'] = pd.to_datetime(df['Draw Date'])

# Split the 'Winning Numbers' column into individual columns for each number
winning_numbers = df['Winning Numbers'].str.split(expand=True)
winning_numbers.columns = ['Number 1', 'Number 2', 'Number 3', 'Number 4', 'Number 5', 'Powerball']

# Convert the winning numbers columns to integer type
winning_numbers = winning_numbers.astype(int)

# Combine the winning numbers columns with the original DataFrame
df = pd.concat([df, winning_numbers], axis=1)

# Drop the original 'Winning Numbers' column
df = df.drop('Winning Numbers', axis=1)

# Check for missing values
print("Missing values:")
print(df.isnull().sum())

# Handle missing values (if any)
df = df.dropna()  # Drop rows with missing values

# Check for duplicates
print("\nDuplicate rows:")
print(df.duplicated().sum())

# Remove duplicates (if any)
df = df.drop_duplicates()

# Rename columns for clarity
df = df.rename(columns={'Multiplier': 'Power Play'})

# Reorder the columns
column_order = ['Draw Date', 'Number 1', 'Number 2', 'Number 3', 'Number 4', 'Number 5', 'Powerball', 'Power Play']
df = df[column_order]

# Reset the index
df = df.reset_index(drop=True)

# Save the cleaned and preprocessed dataset to a new CSV file
df.to_csv('Lottery_Powerball_Cleaned.csv', index=False)

print("\nCleaned and preprocessed dataset saved to 'Lottery_Powerball_Cleaned.csv'.")