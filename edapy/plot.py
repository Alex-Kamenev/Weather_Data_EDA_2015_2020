from IPython.display import display
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import seaborn as sns

def plot_temp_high_low(df):
        high = df['TMAX'] 
        low = df['TMIN']
        time = df['DATE']
        station = df['NAME'].unique()
        
        plt.figure(figsize=(20, 12))
        plt.grid(color='gray', linestyle='-', linewidth=0.5)
        plt.plot(time, high, color='crimson')
        plt.plot(time, low, color='cornflowerblue')
        plt.xlabel('Dates', color='black')
        plt.ylabel('Temperature in degree F°', color='black')
        
        plt.title(station[0], color='black')
        
        high_legend = mpatches.Patch(color='crimson', label='High')
        low_legend = mpatches.Patch(color='cornflowerblue', label='Low')
        
        plt.legend(handles=[high_legend,low_legend])
        
        plt.show()
        return

def plot_hist(df):
    df.hist(figsize=(18, 14))
    
def plot_outliers(df):
    try:
        dims = (16, 12)
        fig, ax = plt.subplots(figsize=dims)
        sns.boxplot(ax=ax, data=df)
    except NameError as e:
        print("Wrong name of something? Error: ", e)
    return

def plot_outlier_single_col_for_all(df):
    for i, col in enumerate(df.select_dtypes(include=np.number).columns.tolist()):
        plt.figure(i)
        dims = (10, 8)
        fig, ax = plt.subplots(figsize=dims)
        sns.boxplot(ax=ax, x=col, data=df)
    return

def plot_heat_map_per_feature(df, type_of_corr):
    for i, col in enumerate(df.select_dtypes(include=np.number).columns.tolist()):
        plt.figure(i)
        dims = (10, 8)
        fig, ax = plt.subplots(figsize=dims)
        sns.heatmap(ax = ax, data = df.corr(type_of_corr).abs()[[col]].sort_values(col))
    return

def heat_map(df):
    # Correlation matrix heat map
    plt.figure(figsize=(28,28))
    cmap = sns.diverging_palette(309, 10, 30, center="light", as_cmap=True)
    sns.set(font_scale = 2)
    mask = np.zeros_like(df.corr())
    mask[np.triu_indices_from(mask)] = True
    sns.heatmap(df.corr(), mask=mask, linewidths=.1 ,cmap=cmap, annot=True)
    plt.yticks(rotation=0);
    return
    
    
    
    
    
    
    
    
    