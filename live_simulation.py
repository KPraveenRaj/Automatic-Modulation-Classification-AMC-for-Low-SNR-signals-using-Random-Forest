import time
import numpy as np
import joblib
from data_generation import generate_bits, ask_modulate, fsk_modulate, psk_modulate, add_awgn, get_iq
from feature_extraction import extract_features

model = joblib.load("rf_model.pkl")

def generate_signal():
    bits = generate_bits(128)
    mod = np.random.choice(
        ["ASK", "FSK", "PSK", "NOISE"],
        p=[0.25, 0.25, 0.25, 0.25]
        )

    if mod == "ASK":
        signal = ask_modulate(bits)
    elif mod == "FSK":
        signal = fsk_modulate(bits)
    elif mod == "PSK":
        signal = psk_modulate(bits)
    else:
        signal = np.random.randn(128)  # 👈 pure noise

    snr = np.random.randint(-5, 20)
    signal = add_awgn(signal, snr)

    return get_iq(signal), mod, snr
    
print("Starting LIVE classification...\n")

while True:
    iq, true_label, snr = generate_signal()
    features = extract_features(iq).reshape(1, -1)

    pred = model.predict(features)[0]

    print(f"SNR: {snr} dB | Predicted: {pred} | Actual: {true_label}")

    time.sleep(1)
