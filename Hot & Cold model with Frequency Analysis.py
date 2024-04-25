import pandas as pd
from collections import defaultdict

# Load the cleaned and preprocessed dataset
df = pd.read_csv('Lottery_Powerball_Cleaned.csv')

# Convert the 'Draw Date' column to datetime format
df['Draw Date'] = pd.to_datetime(df['Draw Date'])

# Initialize dictionaries to store the frequency of each number
main_freq = defaultdict(int)
powerball_freq = defaultdict(int)

# Count the frequency of each number in the entire dataset
for _, row in df.iterrows():
    for i in range(1, 6):
        main_freq[row[f'Number {i}']] += 1
    powerball_freq[row['Powerball']] += 1

# Function to get the hot and cold numbers based on the specified number of recent draws
def get_hot_cold_numbers(recent_draws):
    # Get the most recent draw date
    latest_draw_date = df['Draw Date'].max()

    # Filter the dataset to include only the recent draws
    recent_df = df[df['Draw Date'] > latest_draw_date - pd.Timedelta(days=recent_draws)]

    # Initialize dictionaries to store the frequency of each number in the recent draws
    recent_main_freq = defaultdict(int)
    recent_powerball_freq = defaultdict(int)

    # Count the frequency of each number in the recent draws
    for _, row in recent_df.iterrows():
        for i in range(1, 6):
            recent_main_freq[row[f'Number {i}']] += 1
        recent_powerball_freq[row['Powerball']] += 1

    # Sort the numbers based on their frequency in descending order
    hot_main_numbers = sorted(recent_main_freq, key=recent_main_freq.get, reverse=True)
    hot_powerball_numbers = sorted(recent_powerball_freq, key=recent_powerball_freq.get, reverse=True)

    # Get the cold numbers (numbers that haven't been drawn recently)
    all_main_numbers = set(range(1, 70))
    all_powerball_numbers = set(range(1, 27))
    cold_main_numbers = list(all_main_numbers - set(hot_main_numbers))
    cold_powerball_numbers = list(all_powerball_numbers - set(hot_powerball_numbers))

    return hot_main_numbers, hot_powerball_numbers, cold_main_numbers, cold_powerball_numbers

# Function to update the frequency analysis and hot/cold numbers with new draw data
def update_analysis(new_data):
    global main_freq, powerball_freq

    # Update the frequency dictionaries with the new draws
    for _, row in new_data.iterrows():
        for i in range(1, 6):
            main_freq[row[f'Number {i}']] += 1
        powerball_freq[row['Powerball']] += 1

    # Append the new draw data to the existing dataset
    global df
    df = pd.concat([df, new_data], ignore_index=True)

# Get user input for the number of recent draws to consider
recent_draws = int(input("Enter the number of recent draws to consider for hot and cold numbers: "))

# Get the hot and cold numbers based on the user-specified recent draws
hot_main, hot_powerball, cold_main, cold_powerball = get_hot_cold_numbers(recent_draws)

# Print the frequency analysis results
print("Frequency Analysis:")
print("Main Numbers:")
for number, freq in sorted(main_freq.items(), key=lambda x: x[1], reverse=True):
    print(f"Number {number}: Frequency = {freq}")

print("\nPowerball Numbers:")
for number, freq in sorted(powerball_freq.items(), key=lambda x: x[1], reverse=True):
    print(f"Number {number}: Frequency = {freq}")

# Print the hot and cold numbers
print(f"\nHot Main Numbers (last {recent_draws} draws):")
print(hot_main)

print(f"\nHot Powerball Numbers (last {recent_draws} draws):")
print(hot_powerball)

print(f"\nCold Main Numbers (not drawn in the last {recent_draws} draws):")
print(cold_main)

print(f"\nCold Powerball Numbers (not drawn in the last {recent_draws} draws):")
print(cold_powerball)

# Example usage of updating the analysis with new draw data
new_draws = pd.DataFrame({'Draw Date': ['2023-06-01', '2023-06-03'],
                          'Number 1': [1, 10], 'Number 2': [2, 20], 'Number 3': [3, 30],
                          'Number 4': [4, 40], 'Number 5': [5, 50], 'Powerball': [6, 7]})
update_analysis(new_draws)

# Get the updated hot and cold numbers after adding new draws
hot_main, hot_powerball, cold_main, cold_powerball = get_hot_cold_numbers(recent_draws)

print(f"\nUpdated Hot Main Numbers (last {recent_draws} draws):")
print(hot_main)

print(f"\nUpdated Hot Powerball Numbers (last {recent_draws} draws):")
print(hot_powerball)

print(f"\nUpdated Cold Main Numbers (not drawn in the last {recent_draws} draws):")
print(cold_main)

print(f"\nUpdated Cold Powerball Numbers (not drawn in the last {recent_draws} draws):")
print(cold_powerball)