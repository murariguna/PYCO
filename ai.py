import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
# Load the Iris dataset
iris = load_iris()

# Convert to a pandas DataFrame for better visualization
data = pd.DataFrame(iris.data, columns=iris.feature_names)
data["target"] = iris.target

# Display the first 5 rows
print(data.head())

# Features (X) and target (y)
X = data.drop("target", axis=1)
y = data["target"]
# Split the data: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training set size: {X_train.shape[0]}")
print(f"Testing set size: {X_test.shape[0]}")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
new_sample = [[5.1, 3.5, 1.4, 0.2]]  
predicted_class = model.predict(new_sample)
print(f"Predicted class: {iris.target_names[predicted_class][0]}")
