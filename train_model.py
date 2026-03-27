import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = np.load("X.npy")
y = np.load("y.npy")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

np.save("X_test.npy", X_test)
np.save("y_test.npy", y_test)
print("Data for Testing seperated from Training and Saved!")
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

joblib.dump(model, "rf_model.pkl")

print("Model trained and saved!")
