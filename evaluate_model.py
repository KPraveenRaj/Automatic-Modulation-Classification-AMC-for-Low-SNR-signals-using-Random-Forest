import numpy as np
import joblib
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

X_test = np.load("X_test.npy")
y_test = np.load("y_test.npy")

model = joblib.load("rf_model.pkl")

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nReport:\n", classification_report(y_test, y_pred))
