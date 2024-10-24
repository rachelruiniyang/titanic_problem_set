def parse_names(row):
    """
    Parse the 'Name' field of a DataFrame row to extract family name, title,
    given name, and maiden name.

    Parameters:
    row (pd.Series): A row of the DataFrame containing the 'Name' column.

    Returns:
    pd.Series: A Series containing family name, title, given name, and maiden name.
    """
    try:
        text = row["Name"]
        split_text = text.split(",")
        family_name = split_text[0].strip()
        next_text = split_text[1]
        split_text = next_text.split(".")
        title = (split_text[0] + ".").strip()
        next_text = split_text[1].strip()

        if "(" in next_text:
            split_text = next_text.split("(")
            given_name = split_text[0].strip()
            maiden_name = split_text[1].rstrip(")").strip()
            return pd.Series([family_name, title, given_name, maiden_name])
        else:
            given_name = next_text
            return pd.Series([family_name, title, given_name, None])
    except Exception as ex:
        print(f"Exception: {ex}")
        return pd.Series([None, None, None, None])  # Return None for all if an error occurs

## Extract names    
def extract_names(df):
    """
    Extract family name, title, given name, and maiden name from the 'Name' column 
    and add them as new columns to the DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the 'Name' column.

    Returns:
    pd.DataFrame: The original DataFrame with new columns added for Family Name, Title, 
                  Given Name, and Maiden Name.
    """
    # Apply the parse_names function to extract name components
    df[["Family Name", "Title", "Given Name", "Maiden Name"]] = df.apply(lambda row: parse_names(row), axis=1)
    return df
