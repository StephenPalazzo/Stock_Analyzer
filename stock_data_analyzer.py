from io import StringIO
import csv
import pandas as pd
import matplotlib.pyplot as plt

def plot_data(df):
    selected_columns = df.iloc[:, 1:6]

    selected_columns = selected_columns.apply(pd.to_numeric, errors='coerce')

    fcf_row = df.loc[df.index == 'FCF']
    selected_columns.T.plot(kind='bar', legend=False)
    plt.title('Free Cash Flow (FCF)')
    plt.xlabel('Years')
    plt.ylabel('FCF Value')
    plt.show()


stock_fundamentals = pd.read_csv('stock_fundamentals.csv')

print(stock_fundamentals)
plot_data(stock_fundamentals)


