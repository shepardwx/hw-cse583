# 1. READING CSV

    Used pd.read_csv() function that I was already aware of.
    Renamed each column to total, east, and west for simplicity's sake.


# 2. COMMENT ON COLUMNS

    Added a triple-quote multi-line comment describing the names and types of each column.


# 3. NEW COLUMNS

    Added new 'hour' and 'year' columns by string-slicing from the 'Date' column. Didn't need a new total column, since one already existed.


# 4. DF WITH 2016 DATA

    Using prior knowledge, indexed my full df to only select row values where the entry for the 'year' column == '2016'


# 5. Only NaN value is at 03/13/2016 02:00:00 AM. I will use nanmax/nanmin in data analysis to prevent trouble.

    Used np.isnan() to find indexes where 'nan' bikes crossed. Only one timestamp. Also checked (did not leave in final version of code) for missing values marked with -1 or with very large value (999 or 9999).


# 6. PLOTTING TOTAL RIDERS AS A FUNCTION OF HOUR

    Used np.unique() to find an hour value, ordered them by extracting datetimes from the strings in 'Date' to sort hours for an x axis, then sum and order 'total' crossings. Plotted this 'y' as a function of 'x' and used plt.savefig().


# 7. BUSIEST HOUR

    Used np.argmax() to find the index with the highest total, then indexed our unique, sorted hours to find which hour that corresponded to.


# 8. EDITED README.MD