import numpy as np
from scipy.stats import skew, kurtosis

def extract_features(iq_signal):
    I = iq_signal[:, 0]
    Q = iq_signal[:, 1]

    features = []

    # Time features
    features += [np.mean(I), np.mean(Q)]
    features += [np.var(I), np.var(Q)]
    features += [np.sqrt(np.mean(I**2 + Q**2))]

    # Stats
    features += [skew(I), kurtosis(I)]

    # Frequency features
    fft_vals = np.fft.fft(I)
    power = np.abs(fft_vals)**2
    features += [np.mean(power), np.max(power)]

    # Phase features
    phase = np.arctan2(Q, I + 1e-8)
    features += [np.var(phase), np.mean(np.diff(phase))]

    return np.array(features)
