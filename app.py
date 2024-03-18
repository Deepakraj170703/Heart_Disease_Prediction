import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, mean_absolute_error, accuracy_score

# Load the dataset
@st.cache
def load_data():
    df = pd.read_csv(r"C:/Users/Deepak Raj/Downloads/heart.csv")
    return df

df = load_data()

# Split the dataset into features and target
X = df.drop('target', axis=1)
y = df['target']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the Random Forest classifier
rf_classifier.fit(X_train, y_train)

# Predict on the test set
y_pred = rf_classifier.predict(X_test)

# Calculate RMSE
rmse = mean_squared_error(y_test, y_pred, squared=False)

# Calculate MAPE
mape = mean_absolute_error(y_test, y_pred)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Display metrics
st.write("RMSE:", rmse)
st.write("MAPE:", mape)
st.write("Accuracy:", accuracy)

# Predict function
def predict(model, input_df):
    predictions_df = model.predict(input_df)
    predictions = predictions_df.tolist()
    return predictions

# Collect user input
def user_input_features():
    input_dict = {}
    for column in df.columns:
        if column != 'target':
            input_dict[column] = st.sidebar.slider(f'{column}', int(df[column].min()), int(df[column].max()), int(df[column].mean()))
    features = pd.DataFrame([input_dict])
    return features


input_df = user_input_features()

# Display user input
st.subheader('User Input features')
st.write(input_df)

# Predict and display output
if st.button("Predict"):
    output = predict(rf_classifier, input_df)
    st.success(f'The predicted target is {output}')
