import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=[0])
df.set_index('date', inplace=True)

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot

    fig = plt.figure(figsize=(32, 10))

    plt.plot(df.index, df["value"])

    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize=24)
    plt.xlabel('Date', fontsize=20)
    plt.ylabel('Page Views', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['year'] = [d.year for d in df_bar.date]
    df_bar['month'] = [d.strftime('%B') for d in df_bar.date]
    
    dfg_bar = df_bar.groupby(['year', 'month']).mean('value').reset_index()

    print(dfg_bar)

    dfg_bar["value"] = dfg_bar["value"].astype('int')

    #print(dfg_bar)

    dfg_bar = dfg_bar.pivot(index='year', columns='month', values='value')

    print(dfg_bar)
    
    width = 0.04

    x = dfg_bar.index

    fig = plt.figure(figsize=(15, 13))

    plt.bar(x - 6 * width, dfg_bar['January'], width) 
    plt.bar(x - 5 * width, dfg_bar['February'], width) 
    plt.bar(x - 4 * width, dfg_bar['March'], width) 
    plt.bar(x - 3 * width, dfg_bar['April'], width) 
    plt.bar(x - 2 * width, dfg_bar['May'], width) 
    plt.bar(x - 1 * width, dfg_bar['June'], width) 
    plt.bar(x + 0 * width, dfg_bar['July'], width) 
    plt.bar(x + 1 * width, dfg_bar['August'], width) 
    plt.bar(x + 2 * width, dfg_bar['September'], width) 
    plt.bar(x + 3 * width, dfg_bar['October'], width) 
    plt.bar(x + 4 * width, dfg_bar['November'], width) 
    plt.bar(x + 5 * width, dfg_bar['December'], width) 

    plt.xticks(x, dfg_bar.index) 
    plt.xlabel("Years") 
    plt.ylabel("Average Page Views") 
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], loc='upper left') 
    

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month_nr'] = [d.strftime('%m') for d in df_box.date]

    print(df_box)

    np.float = float    
    np.int = int   #module 'numpy' has no attribute 'int'
    np.object = object    #module 'numpy' has no attribute 'object'
    np.bool = bool    #module 'numpy' has no attribute 'bool'

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(32, 10))

    box_plot_year = sns.boxplot(data=df_box, x="year", y="value", ax=ax[0])
    ax[0].set_title('Year-wise Box Plot (Trend)', fontsize=20)
    ax[0].set_xlabel('Year', fontsize=16)
    ax[0].set_ylabel('Page Views', fontsize=16)
    ax[0].set_xticklabels(ax[0].get_xticklabels(), fontsize=16)
    ax[0].set_yticklabels(ax[0].get_yticklabels(), fontsize=16)

    box_plot_month = sns.boxplot(data=df_box.sort_values(by=["month_nr"]), x="month", y="value", ax=ax[1])
    ax[1].set_title('Month-wise Box Plot (Seasonality)', fontsize=20)
    ax[1].set_xlabel('Month', fontsize=16)
    ax[1].set_ylabel('Page Views', fontsize=16)
    ax[1].set_xticklabels(ax[1].get_xticklabels(), fontsize=16)
    ax[1].set_yticklabels(ax[1].get_yticklabels(), fontsize=16)
    
   
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig


#draw_line_plot()
#draw_bar_plot()
#draw_box_plot()