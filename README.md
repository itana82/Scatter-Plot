# Scatter Plot Program

This program generates a scatter plot from the data in a CSV (comma separated values) file. The path of this file is
specified by the value of the **CSV_PATH** constant near the top of the file **ScatterPlotFromCSV.py**. Each row in the
CSV file specifies the x, y and colour values of a dot in the plot. The **X_COL_NAME**, **Y_COL_NAME** and
**Z_COL_NAME** constants near the top of **ScatterPlotFromCSV.py** specify the names of the columns in the CSV file to
be be used for the x values, y values and colour values respectively.

The program will display the plot on the screen and save it to the file whose name is specified by the
**PLOT_FILE_NAME** constant near the top of **ScatterPlotFromCSV.py**. If this file name does not have an extension
then an extension such as .png will be automatically added when the plot is saved. Note that this file will be
overwritten if it already exists when the plot is saved.

Note that the file **example.csv** was created to demonstrate the program and does not contain real world data.

Note that Python 3 must be installed. The **pandas** and **matplotlib** python libraries must also be installed.