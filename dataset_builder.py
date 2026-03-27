import numpy as np
from feature_extraction import extract_features

signals = np.load("signals.npy")
labels = np.load("labels.npy")
snr = np.load("snr.npy")

X = []
for s in signals:
    X.append(extract_features(s))

X = np.array(X)

np.save("X.npy", X)
np.save("y.npy", labels)
np.save("snr.npy", snr)

print("Features extracted!")
