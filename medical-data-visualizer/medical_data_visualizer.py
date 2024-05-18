import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
bmi = df['weight']/((df['height']/100)**2)
bm=[]
for value in bmi:
  if(value>25.0):
    bm.append(1)
  else:
    bm.append(0)

df['overweight'] = bm

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
check = []
for val in df['cholesterol']:
  if(val<=1):
    check.append(0)
  else:
    check.append(1)

df['cholesterol'] = check

gluc = []
for value in df['gluc']:
  if(value<=1):
    gluc.append(0)
  else:
    gluc.append(1)

df['gluc'] = gluc

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(id_vars=['cardio'], value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])
    df_cat['value'] = df_cat['value'].astype(str)

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    #df_cat = None
    

    # Draw the catplot with 'sns.catplot()'
    plot = sns.catplot(data=df_cat,x='variable',kind='count',hue='value',col='cardio')
    plot.set_axis_labels("variable", "total")


    # Get the figure for the output
    fig = plot.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.loc[(df['ap_lo']<=df['ap_hi']) &
              (df['height']>=df['height'].quantile(0.025)) &
              (df['height']<=df['height'].quantile(0.975)) &
              (df['weight']>=df['weight'].quantile(0.025)) &
              (df['weight']<=df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr =df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr))
    #print(corr)


    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12,6))
    #annot_kws = {"size": 12}
    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(data=corr, mask=mask, annot=True, linewidths=0.5, fmt='0.1f')

    # Do not modify the next two lines
    fig.savefig('heatmap.png', bbox_inches='tight')
    #plt.show()
    plt.close(fig)
    
    return fig
