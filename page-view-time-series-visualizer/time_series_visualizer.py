import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
#df1 = df.copy()
df.index = df['date']
#df = df.drop('date',axis='columns')


# Clean data
top_percentile = df['value'].quantile(0.975)
bottom_percentile = df['value'].quantile(0.025)
df = df[df['value']<top_percentile]
df = df[df['value']>bottom_percentile]
#print(df)
#df1.index = pd.to_datetime(df1.index)

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(20,8))
    plt.plot(df.index,df['value'], scalex=True)
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df2=df.copy()
    #df2['date'] = pd.to_datetime(df2['date'])
    #df2.reset_index()
    df2['Year'] = df2['date'].dt.year
    df2['Month'] = df2['date'].dt.strftime('%B')
    avg_values = df2.groupby(['Year', 'Month'])['value'].mean().unstack(fill_value=0)
     
    # Copy and modify data for monthly bar plot
    df_bar = avg_values[['January','February','March','April','May','June',
                                    'July','August','September','October','November','December']]

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, 6))
    width = 0.5
    df_bar.plot(kind='bar',ax=ax ,width=width)

    plt.title('Monthly Values by Year')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    #df_box['date'] = pd.to_datetime(df_box['date'])
    #df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['Month_no'] = df_box['date'].dt.month
    df_box = df_box.sort_values(by='Month_no')

    # Draw box plots (using Seaborn)
    fig,ax1 =plt.subplots(1,2, figsize=(30, 10))

    sns.boxplot(ax=ax1[0],x=df_box['year'],y=df_box['value'])
    ax1[0].set(xlabel ="Year", ylabel = "Page Views", title ='Year-wise Box Plot (Trend)')
    ax1[0].set_yticks(range(0,int(df_box["value"].max())+40000, 20000))
    
    sns.boxplot(ax=ax1[1],x=df_box['month'],y=df_box['value'])
    ax1[1].set(xlabel ="Month", ylabel = "Page Views", title ='Month-wise Box Plot (Seasonality)')
    ax1[1].set_yticks(range(0,int(df_box["value"].max())+40000, 20000))


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig