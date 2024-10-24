import pandas as pd
from src.preprocessing.preprocessing import combine_train_test
from src.features.feature_engineering import add_family_size, add_age_interval, add_fare_interval_column, add_sex_pclass
from src.eda.eda import perform_eda
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def main():
    # Load the data
    train_df = pd.read_csv('data/train.csv')
    test_df = pd.read_csv('data/test.csv')
    
    # Combine train and test datasets
    all_df = combine_train_test(train_df, test_df, target_col='Survived')

    # Feature Engineering
    all_df = add_family_size(all_df)
    all_df = add_age_interval(all_df)
    all_df = add_fare_interval_column(all_df)
    all_df = add_sex_pclass(all_df)

    # Perform exploratory data analysis
    perform_eda(all_df)
    
    # Split combined data back into train and test sets
    train = all_df[all_df['set'] == 'train']
    test = all_df[all_df['set'] == 'test']

    # Define target and predictors
    predictors = ['Family Size', 'Age Interval', 'Fare Interval', 'Pclass', 'Sex']
    target = 'Survived'

    # Train/validation split
    train_X, valid_X, train_Y, valid_Y = train_test_split(train[predictors], train[target], test_size=0.2, random_state=42)

    # Train a model (Random Forest in this case)
    clf = RandomForestClassifier(n_jobs=-1, random_state=42, criterion="gini", n_estimators=100)
    clf.fit(train_X, train_Y)

    # Make predictions and evaluate
    preds = clf.predict(valid_X)
    accuracy = accuracy_score(valid_Y, preds)
    
    print(f"Validation Accuracy: {accuracy:.4f}")

    # Predict on the test set (Optional)
    test_preds = clf.predict(test[predictors])

if __name__ == '__main__':
    main()