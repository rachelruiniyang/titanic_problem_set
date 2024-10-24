# Plot count pairs of "Age Interval" grouped by "Pclass"

def plot_age_interval_by_pclass(df):
    """
    Plot count of 'Age Interval' grouped by 'Pclass'.

    Parameters:
    df (pd.DataFrame): The DataFrame containing 'Age Interval' and 'Pclass' columns.
    """
    # Group by 'Pclass' and 'Age Interval' and count occurrences
    count_data = df.groupby(['Pclass', 'Age Interval']).size().reset_index(name='Count')

    # Create the plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Pclass', y='Count', hue='Age Interval', data=count_data, palette='viridis')
    
    # Adding title and labels
    plt.title('Count of Age Intervals by Passenger Class')
    plt.xlabel('Passenger Class')
    plt.ylabel('Count')
    plt.legend(title='Age Interval')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

# Plot count pairs of "Age Interval" grouped by "Embarked"

def plot_age_interval_by_embarked(df):
    """
    Plot count of 'Age Interval' grouped by 'Embarked'.

    Parameters:
    df (pd.DataFrame): The DataFrame containing 'Age Interval' and 'Embarked' columns.
    """
    # Group by 'Embarked' and 'Age Interval' and count occurrences
    count_data = df.groupby(['Embarked', 'Age Interval']).size().reset_index(name='Count')

    # Create the plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Embarked', y='Count', hue='Age Interval', data=count_data, palette='viridis')
    
    # Adding title and labels
    plt.title('Count of Age Intervals by Embarkation Point')
    plt.xlabel('Embarkation Point')
    plt.ylabel('Count')
    plt.legend(title='Age Interval')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

# Plot count pairs of "Pclass" grouped by "Fare Interval"

def plot_pclass_by_fare_interval(df):
    """
    Plot count of 'Pclass' grouped by 'Fare Interval'.

    Parameters:
    df (pd.DataFrame): The DataFrame containing 'Pclass' and 'Fare Interval' columns.
    """
    # Group by 'Fare Interval' and 'Pclass' and count occurrences
    count_data = df.groupby(['Fare Interval', 'Pclass']).size().reset_index(name='Count')

    # Create the plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Fare Interval', y='Count', hue='Pclass', data=count_data, palette='viridis')
    
    # Adding title and labels
    plt.title('Count of Passenger Class by Fare Interval')
    plt.xlabel('Fare Interval')
    plt.ylabel('Count')
    plt.legend(title='Pclass')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

