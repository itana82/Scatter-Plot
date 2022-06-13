PLOT_TITLE = "Life Style and Life Expectancy"

# Path of CSV file from which to load data (note
# that example.csv was created to demonstrate this
# program and does not contain real world data).
CSV_PATH = 'example.csv'

# Positions of the columns in the CSV file (where the 1st column is
# column 0) from which to obtain the data.
X_COL = 1
Y_COL = 2
Z_COL = 3

# If plot file name does not have an extension then an extension such
# as .png will be added automatically when the plot is saved.
PLOT_FILE_NAME = 'scatter_plot'

DOT_COLOUR_MAP = 'jet'
DOT_SIZE = 10


import matplotlib.pyplot as plt
import pandas as pd


def main():
    return_code = 0
    try:
        df = pd.read_csv(CSV_PATH)
        df.plot(kind='scatter',
                      title=PLOT_TITLE,
                      x=X_COL,
                      y=Y_COL,
                      c=Z_COL, # Colour values.
                      s=DOT_SIZE,
                      colormap=DOT_COLOUR_MAP,
                      colorbar=True)

        plt.savefig(PLOT_FILE_NAME)
        print("Saved plot in '{}'".format(PLOT_FILE_NAME))
        
        plt.show()
    except Exception as e:
        print("Error: {}".format(str(e)))
        return_code = 1
    return return_code


if __name__ == '__main__':
    exit_code = main()
    exit(exit_code)