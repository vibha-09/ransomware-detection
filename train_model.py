import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load or create a dataset
data = {
    "entropy": [4.0, 7.2, 7.8, 6.1, 8.5],
    "modification_rate": [2, 10, 12, 4, 15],
    "is_encrypted": [0, 1, 1, 0, 1]
}
df = pd.DataFrame(data)

# Features and labels
X = df[["entropy", "modification_rate"]]
y = df["is_encrypted"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Evaluate the model
y_pred = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# Save the model
joblib.dump(clf, "models/classifier.pkl")
