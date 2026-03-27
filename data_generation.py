import numpy as np
from scipy.signal import hilbert


def generate_bits(n_bits):
    return np.random.randint(0, 2, n_bits)

def ask_modulate(bits, fs=1000, carrier_freq=10):
    t = np.arange(len(bits)) / fs
    signal = (bits * 1.0) * np.cos(2 * np.pi * carrier_freq * t)
    return signal

def fsk_modulate(bits, fs=1000, f0=5, f1=15):
    t = np.arange(len(bits)) / fs
    signal = np.where(bits == 0,
                      np.cos(2 * np.pi * f0 * t),
                      np.cos(2 * np.pi * f1 * t))
    return signal

def psk_modulate(bits, fs=1000, carrier_freq=10):
    t = np.arange(len(bits)) / fs
    phase = np.pi * bits
    signal = np.cos(2 * np.pi * carrier_freq * t + phase)
    return signal

def add_awgn(signal, snr_db):
    signal_power = np.mean(signal**2)
    snr_linear = 10**(snr_db / 10)
    noise_power = signal_power / snr_linear

    noise = np.sqrt(noise_power) * np.random.randn(len(signal))
    return signal + noise

def get_iq(signal):
    analytic_signal = hilbert(signal)
    I = np.real(analytic_signal)
    Q = np.imag(analytic_signal)
    return np.stack([I, Q], axis=-1)

def generate_dataset(num_samples=5000):
    signals = []
    labels = []
    snrs = []

    for _ in range(num_samples):
        bits = generate_bits(128)
        mod_type = np.random.choice(["ASK", "FSK", "PSK", "NOISE"])
        snr = np.random.randint(-5, 21)

        if mod_type == "ASK":
            signal = ask_modulate(bits)
        elif mod_type == "FSK":
            signal = fsk_modulate(bits)
        elif mod_type == "PSK":
            signal = psk_modulate(bits)
        else:
            signal = np.random.randn(128)

        signal = add_awgn(signal, snr)
        iq = get_iq(signal)

        signals.append(iq)
        labels.append(mod_type)
        snrs.append(snr)

    np.save("signals.npy", np.array(signals))
    np.save("labels.npy", np.array(labels))
    np.save("snr.npy", np.array(snrs))

    print("Dataset generated!")
    
    
if __name__ == "__main__":
    generate_dataset(50000)
