import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, mean_absolute_error, accuracy_score

#Load the dataset
df=pd.read_csv(r"C:/Users/Deepak Raj/Downloads/heart.csv")

df.head()

df.tail()

#Info abt dataset
df.info()

#Description of dataset
df.describe()

df.columns

df.shape

#Missing values
df.isnull().sum()

#Visualization
import seaborn as sns

df.corr()
sns.heatmap(df.corr())

sns.jointplot(x='age',y='target',data=df,kind='reg')

sns.boxplot(df['target'])

sns.pairplot(df)

sns.pairplot(df,hue='target')


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

print("RMSE:", rmse)
print("MAPE:", mape)
print("Accuracy:", accuracy)



