# NETFLIX-ANALYSIS
Tableau Project

[![Image alt](https://github.com/Nikhil414/NETFLIX-ANALYSIS/blob/280878af3ebd622e58843d9b0c6cc16fc0c5983c/Capture.PNG)](https://public.tableau.com/views/NETFLIXANALYSIS_17378071257360/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)


# Netflix Data Analysis and Visualization in Tableau

## Project Overview

This project explores a Netflix dataset containing information about movies and TV shows. The objective is to clean the data, preprocess it using Python, and create interactive Tableau dashboards to gain insights into Netflix's content distribution, popular genres, actors, and filming locations.

## Dataset

The dataset consists of 12 columns and 8,807 rows, including:

- **Title**
- **Director**
- **Cast**
- **Country filmed**
- **Release year**
- **Rating**
- **Genre**
- **Description**

## Data Preprocessing

To prepare the dataset for Tableau visualizations:

- **Genre Cleanup**: Split multiple genres into separate rows.
- **Cast Cleanup**: Split multiple actors into separate rows.
- Used **Python** for data transformation.

## Visualizations in Tableau

### 1. Total Movie KPI

- Created a sparkline to display yearly movie releases.
- Compared current and previous year’s data.

### 2. Country Filmed

- Designed a map visualization highlighting top filming locations.

### 3. Most Frequent Genres

- Created bar charts showcasing the most popular genres.

### 4. Top 10 Cast Members

- Visualized the most frequent actors/actresses in Netflix content.

### 5. Movie Rating Analysis

- Bar charts analyzing rating trends over time.

### 6. Select Year Parameter

- Implemented an interactive parameter to filter data by year.

## Calculated Fields in Tableau

### Movies Dashboard:

- **CY Movies**: Count of distinct movies for the selected year.
- **PY Movies**: Count of distinct movies for the previous year.
- **% Diff Movies**: Percentage change in movie count.
- **Min/Max Movies**: Window function to find min/max movie count.

### TV Shows Dashboard:

- **CY TV Shows**: Count of distinct TV shows for the selected year.
- **PY TV Shows**: Count of distinct TV shows for the previous year.
- **% Diff TV Shows**: Percentage change in TV show count.
- **Min/Max TV Shows**: Window function to find min/max TV show count.

## Interactive Dashboards

- Combined all visualizations into an intuitive Tableau dashboard.
- Included filters and parameters for dynamic exploration.

## Storytelling with Data

- Used **titles, tooltips, and legends** for clarity.
- Applied **color coding** for genres, ratings, and countries.

## Dashboard Design Principles

- Kept layout **clean and visually appealing**.
- Ensured smooth **user experience with logical arrangements** of visuals.

## How to Use

1. Load the cleaned dataset into Tableau.
2. Open the provided Tableau dashboard.
3. Interact with filters, parameters, and tooltips to explore insights.

## Tools Used

- **Python** (for data preprocessing)
- **Tableau** (for visualizations)
- **Excel/CSV** (for data storage and modifications)

