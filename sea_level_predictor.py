import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Create first line of best fit (using all data)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_levels_all = res_all.intercept + res_all.slope * years_extended
    ax.plot(years_extended, sea_levels_all, 'r', label='Fit: 1880-2050')

    # Create second line of best fit (using data from year 2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    sea_levels_recent = res_recent.intercept + res_recent.slope * years_recent
    ax.plot(years_recent, sea_levels_recent, 'green', label='Fit: 2000-2050')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return ax.get_figure()
