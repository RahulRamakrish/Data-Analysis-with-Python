# Page View Time Series Visualizer

This is the boilerplate for the Page View Time Series Visualizer project. 

The goal of this project is to visualize the daily page views of the FreeCodeCamp.org forum over a specified period. The visualizations help in understanding the trends and patterns in the data. The project includes:

* Line Plot: Displays daily page views over time.
* Bar Plot: Shows average daily page views for each month, grouped by year.
* Box Plots: Illustrate the distribution of page views within a given year and month, highlighting trends and seasonality.

## Data Cleaning
The dataset fcc-forum-pageviews.csv is cleaned by removing days with page views in the top 2.5% and bottom 2.5% to eliminate outliers. The cleaned data is then used to create the visualizations.

## Visualizations
Line Plot
The draw_line_plot function creates a line chart to visualize daily page views over time. The chart has the following characteristics:

Title: Daily freeCodeCamp Forum Page Views 5/2016-12/2019
X-axis Label: Date
Y-axis Label: Page Views
Bar Plot
The draw_bar_plot function generates a bar chart to show average daily page views for each month, grouped by year. The chart includes:

Legend: Month labels with the title "Months"
X-axis Label: Years
Y-axis Label: Average Page Views
Box Plots
The draw_box_plot function creates two adjacent box plots to display the distribution of page views:

Year-wise Box Plot: Shows the trend of page views for each year.
Month-wise Box Plot: Illustrates the seasonality of page views for each month.
Both plots have correctly labeled axes and month labels starting from January.

replit link to run the project: https://replit.com/@rahulramakrish2/boilerplate-page-view-time-series-visualizer#time_series_visualizer.py
