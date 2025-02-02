import pandas as pd

# Step 1: Load the dataset
try:
    # Attempt to read the CSV file with encoding handling
    df = pd.read_csv("netflix_titles.csv", encoding="ISO-8859-1")
    print("Dataset loaded successfully!")
except Exception as e:
    print(f"Error loading file: {e}")
    exit()

# Step 2: Data Preprocessing
# 2.1 Explode 'listed_in' (genre) column
df['listed_in'] = df['listed_in'].str.split(', ')
genre_exploded = df.explode('listed_in')

# 2.2 Explode 'cast' column
df['cast'] = df['cast'].fillna('').str.split(', ')
cast_exploded = df.explode('cast')

# Step 3: Save cleaned data to new CSV files
# Save genre-exploded data
genre_exploded.to_csv("netflix_genre_cleaned.csv", index=False)
print("Genre-exploded data saved to 'netflix_genre_cleaned.csv'.")

# Save cast-exploded data
cast_exploded.to_csv("netflix_cast_cleaned.csv", index=False)
print("Cast-exploded data saved to 'netflix_cast_cleaned.csv'.")

# Step 4: Combine the cleaned datasets if needed
# Optional: Create a dataset with both genres and cast exploded
combined_exploded = cast_exploded.copy()
combined_exploded['listed_in'] = combined_exploded['listed_in'].str.split(', ')
combined_exploded = combined_exploded.explode('listed_in')

# Save combined data
combined_exploded.to_csv("netflix_combined_cleaned.csv", index=False)
print("Combined exploded data saved to 'netflix_combined_cleaned.csv'.")
