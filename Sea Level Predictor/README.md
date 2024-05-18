# Sea Level Predictor

This is the boilerplate for the Sea Level Predictor project.

## Project Description
The Sea Level Predictor project aims to analyze historical data of global average sea level changes and predict future sea level rise using linear regression. The analysis utilizes data from the US Environmental Protection Agency (EPA), which includes global average absolute sea level changes from 1880 to 2014. The project involves creating visualizations to understand the historical trends and making predictions about future sea level changes through the year 2050.

## Data Source
The dataset used in this project is the "Global Average Absolute Sea Level Change, 1880-2014" from the US Environmental Protection Agency, which includes data from CSIRO (2015) and NOAA (2015).

## Project Tasks
Data Importation: Use Pandas to import the sea level data from the epa-sea-level.csv file.
Scatter Plot Creation: Use Matplotlib to create a scatter plot with the Year column on the x-axis and the CSIRO Adjusted Sea Level column on the y-axis.
Linear Regression (1880-2050):
Use the linregress function from scipy.stats to calculate the slope and y-intercept of the line of best fit for the entire dataset (from 1880).
Plot the line of best fit extending through the year 2050 to predict the sea level rise.
Linear Regression (2000-2050):
Perform linear regression using only the data from the year 2000 to the most recent year in the dataset.
Plot a second line of best fit extending through the year 2050 to predict the sea level rise if the current trend continues.
Visualization:
Label the x-axis as "Year" and the y-axis as "Sea Level (inches)".
Title the plot as "Rise in Sea Level".
Saving and Returning the Plot: Save the final plot as an image file and ensure it is displayed correctly.

## Files in the Repository
sea_level_predictor.py: Contains the main code for data analysis and visualization.
main.py: Used for testing and running the code during development.
test_module.py: Contains unit tests to validate the implementation.
epa-sea-level.csv: The dataset used for the project.

Results
The project generates a scatter plot of the historical sea level data with two lines of best fit:

One line predicting sea level rise through 2050 using data from 1880 to the present.
A second line predicting sea level rise through 2050 using data from 2000 to the present.
These visualizations help in understanding the trend in sea level changes and provide a basis for future predictions.

## Acknowledgments
* US Environmental Protection Agency (EPA)
* CSIRO (2015)
* NOAA (2015)
* freeCodeCamp for providing the project guidelines and dataset

replit link to run the project: https://replit.com/@rahulramakrish2/boilerplate-sea-level-predictor
