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

    plt.figure(figsize=(16, 10))
    plt.grid(color='gray', linestyle='-', linewidth=0.5)
    plt.plot(time, high, color='crimson')
    plt.plot(time, low, color='cornflowerblue')
    plt.xlabel('Dates', color='black', fontsize=18)
    plt.ylabel('Temperature in degree F°', color='black', fontsize=18)

    plt.title(station[0], color='black', fontsize=22)

    high_legend = mpatches.Patch(color='crimson', label='High')
    low_legend = mpatches.Patch(color='cornflowerblue', label='Low')

    plt.legend(handles=[high_legend,low_legend])

    plt.show()
    return

def plot_hist(df):
    df.hist(figsize=(16, 14))
    
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

def join_plot_hue(df, x, y, hue):
    sns.set_theme(style="whitegrid")
    plt.rc("legend", fontsize=12)
    palette = sns.color_palette("husl", 5)
    j_plot = sns.jointplot(x = x, y = y, data=df, hue = hue, palette=palette, height=12,s=60)
    
def join_plot_kind(df, x, y, kind):
    sns.set_theme(style="whitegrid")
    plt.rc("legend", fontsize=12)
    j_plot = sns.jointplot(x = x, y = y, data=df, kind=kind, height=10)
    
def plot_many(df, base, cat_name, feature_list, ylabel):
    plt.figure(figsize=(16, 10))
    plt.grid(color='gray', linestyle='-', linewidth=0.5)
    
    for feature in feature_list:
        plt.plot(df[base], df[feature], label=f'{feature}')
    
    font = {
        'size'   : 22}

    plt.rc('font', **font)
    
    name = df[cat_name].unique()

    plt.xlabel(base, color='black', fontsize=18)
    plt.ylabel(ylabel, color='black', fontsize=18)

    plt.title(name[0], color='black', fontsize=22)

    plt.show()
    return
    
    
    
    
    
    
    