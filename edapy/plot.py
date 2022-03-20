from IPython.display import display
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_temp_high_low(df):
    high = df['TMAX'] 
    low = df['TMIN']
    time = df['DATE']
    station = df['NAME'].unique()
    plt.figure(figsize=(8, 8))
    plt.plot(time, high, 'm-.', time, low, 'c:')
    plt.ylabel('Temperature in degree F°', color='red', fontsize=12)
    plt.title(station, color='blue', fontsize=12)
    high_legend = mpatches.Patch(color='red', label='High')
    low_legend = mpatches.Patch(color='blue', label='Low')
    plt.legend(handles=[high_legend,low_legend])
    plt.show()