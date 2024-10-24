# Missing data
def missing_data_summary(df):
    """
    Generate a summary of missing data in the dataframe.

    Parameters:
    df (pd.dataframe): The dataframe to analyze.

    Returns:
    pd.dataframe: A dataframe summarizing the total and percentage of missing values
                  and the data types of each column.
    """
    total = df.isnull().sum()
    percent = (df.isnull().sum() / df.count() * 100)  # Use df.count() instead of isnull().count()
    summary = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    
    # Getting the data types
    summary['Types'] = df.dtypes.values  # Get data types directly from the DataFrame
    
    # Transpose the summary DataFrame for better readability
    return summary.transpose()

# Most frequent data
def frequency_summary(df):
    """
    Generate a summary of the frequency of the most common item in each column.

    Parameters:
    df (pd.DataFrame): The DataFrame to analyze.

    Returns:
    pd.DataFrame: A DataFrame summarizing the most frequent item, its frequency, 
                  and the percentage from the total for each column.
    """
    total = df.count()  # Count of non-null values per column
    summary = pd.DataFrame(total, columns=['Total'])

    items = []
    vals = []

    for col in df.columns:
        try:
            itm = df[col].value_counts().index[0]  # Most frequent item
            val = df[col].value_counts().values[0]  # Frequency of the most frequent item
        except Exception as ex:
            print(f"Error processing column {col}: {ex}")
            itm, val = 0, 0  # In case there's an exception, default to 0
        items.append(itm)
        vals.append(val)

    summary['Most frequent item'] = items
    summary['Frequence'] = vals
    summary['Percent from total'] = np.round(np.array(vals) / total * 100, 3)

    # Transpose the summary for better readability
    return summary.transpose()

# Unique values
def unique_values_summary(df):
    """
    Generate a summary of the total and unique values for each column in the DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to analyze.

    Returns:
    pd.DataFrame: A DataFrame summarizing the total count and number of unique values
                  for each column.
    """
    total = df.count()  # Count of non-null values per column
    summary = pd.DataFrame(total, columns=['Total'])

    uniques = [df[col].nunique() for col in df.columns]  # Number of unique values per column
    summary['Uniques'] = uniques

    # Transpose the summary DataFrame for better readability
    return summary.transpose()

