PLOT_TITLE = "Life Style and Life Expectancy"

# Path of CSV file from which to load data (note
# that example.csv was created to demonstrate this
# program and does not contain real world data).
CSV_PATH = 'example.csv'

# Columns in the CSV file to be used for the x and y coordinate values 
# of each dot in the plot.
X_COL_NAME = "Mean hours exercise per week"
Y_COL_NAME = "Mean units alcohol consumed per week"

# Column in the CSV file to be used for the colour value of each dot in
# the plot.
Z_COL_NAME = "Life expectancy years"

# If plot file name does not have an extension then an extension such
# as .png will be automatically added when the plot is saved.
PLOT_FILE_NAME = 'scatter_plot'

DOT_COLOUR_MAP = 'jet'
DOT_SIZE = 10


import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd


def save_plot(filename):
    plt.savefig(filename)

    ext = mpl.rcParams["savefig.format"]
    print("Saved plot as {}.{}".format(filename, ext))


def main():
    return_code = 0
    try:
        df = pd.read_csv(CSV_PATH)
        df.plot(kind='scatter',
                      title=PLOT_TITLE,
                      x=X_COL_NAME,
                      y=Y_COL_NAME,
                      c=Z_COL_NAME,
                      s=DOT_SIZE,
                      colormap=DOT_COLOUR_MAP,
                      colorbar=True)

        save_plot(PLOT_FILE_NAME)
        plt.show()
    except Exception as e:
        print("Error: {}".format(str(e)))
        return_code = 1
    return return_code


if __name__ == '__main__':
    exit_code = main()
    exit(exit_code)