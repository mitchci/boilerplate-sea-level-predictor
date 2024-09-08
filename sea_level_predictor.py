import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    fit_1 = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    x_fit = np.arange(df['Year'].min(), 2051,1)
    y_fit = fit_1.intercept + fit_1.slope*x_fit

    plt.plot(x_fit,y_fit)

    # Create second line of best fit
    df_b = df.loc[df['Year'] >= 2000]

    fit_2 = linregress(x=df_b['Year'], y=df_b['CSIRO Adjusted Sea Level'])
    x_fit_2 = np.arange(df_b['Year'].min(), 2051,1)
    y_fit_2 = fit_2.intercept + fit_2.slope*x_fit_2

    plt.plot(x_fit_2,y_fit_2)

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()