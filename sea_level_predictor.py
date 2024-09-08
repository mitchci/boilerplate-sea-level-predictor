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
    fit_1 = linregress(x=df['CSIRO Adjusted Sea Level'], y=df['Year'])
    x_fit = np.arange(df['Year'].min(), 2051,1)
    y_fit = fit_1.slope + fit_1.intercept*x_fit

    plt.plot(x_fit,y_fit)

    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()