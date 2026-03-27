import numpy as np
import joblib
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

X = np.load("X.npy")
y = np.load("y.npy")
snr = np.load("snr.npy")

model = joblib.load("rf_model.pkl")

snr_vals = sorted(set(snr))
accs = []

for s in snr_vals:
    idx = (snr == s)
    if np.sum(idx) == 0:
        continue

    pred = model.predict(X[idx])
    acc = accuracy_score(y[idx], pred)
    accs.append(acc)

plt.plot(snr_vals, accs)
plt.xlabel("SNR")
plt.ylabel("Accuracy")
plt.title("Accuracy vs SNR")
plt.show()
