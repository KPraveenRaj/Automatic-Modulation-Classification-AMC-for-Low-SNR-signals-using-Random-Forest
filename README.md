# 📡 Signal-Based Digital Modulation Recognition Using Machine Learning

## 👥 Team

* **Konatham Praveen Raj** (252SP014)
* **Rishabh Barwe** (252SP025)

---

# 🚀 How to Run the Project

## 🧰 1. Setup Environment (Conda - Recommended)

```bash
conda create -n amc_env python=3.10 -y
conda activate amc_env
```

---

## 📁 2. Navigate to Project Folder

```bash
cd AMC_Project
```

---

## 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ 4. Execute Pipeline (IMPORTANT ORDER)

### Step 1: Generate Dataset

```bash
python data_generation.py
```

### Step 2: Extract Features

```bash
python dataset_builder.py
```

### Step 3: Train Model

```bash
python train_model.py
```

### Step 4: Evaluate Model

```bash
python evaluate_model.py
```

### Step 5: Analyze SNR vs Accuracy

```bash
python snr_analysis.py
```

### Step 6: Run Live Simulation (Real-Time Demo)

```bash
python live_simulation.py
```

👉 Press `Ctrl + C` to stop live simulation

---

# 🧱 Project Architecture

```
Bit Stream (128 bits)
   ↓
Modulation (ASK / FSK / PSK)
   ↓
AWGN Channel (Noise)
   ↓
IQ Conversion (Hilbert Transform)
   ↓
Feature Extraction
   ↓
Random Forest Classifier
   ↓
Prediction (Modulation Type)
```
`Note: Code generates Random 128 bits to generate signals. you can give a file with custom bits and size and make few changes in data_generation.py to generate your custom signals data`

---

# 📘 Full Documentation

---

## 🎯 Problem Statement

This project implements an **Automatic Modulation Classification (AMC)** system to classify signals into:

* ASK (Amplitude Shift Keying)
* FSK (Frequency Shift Keying)
* PSK (Phase Shift Keying)
* NOISE (No Signal)

The system works even under varying noise conditions (SNR: -5 dB to 20 dB).

---

# 📡 Signal Generation (Mathematics)

## 🔹 Bit Stream

Random binary sequence:

```
b[n] ∈ {0,1}
```

---

## 🔹 ASK (Amplitude Shift Keying)

```
s(t) = A · b(t) · cos(2πf_c t)
```

* Bit 1 → signal present
* Bit 0 → no signal

---

## 🔹 FSK (Frequency Shift Keying)

```
s(t) = cos(2πf_0 t)   if b=0
s(t) = cos(2πf_1 t)   if b=1
```

* Frequency carries information

---

## 🔹 PSK (BPSK)

```
s(t) = A · (2b(t) - 1) · cos(2πf_c t)
```

* Phase shift encodes bits

---

## 🔹 NOISE (No Signal)

```
n(t) ~ N(0, σ²)
```

* Pure Gaussian noise

---

# 📡 Channel Model (AWGN)

```
r(t) = s(t) + n(t)
```

SNR:

```
SNR_dB = 10 log10(P_signal / P_noise)
```

---

# 📡 IQ Representation

Using Hilbert Transform:

```
z(t) = s(t) + j ŝ(t)
```

* I = Real part
* Q = Imaginary part

Stored as:

```
[I, Q]
```

---

# 📊 Feature Extraction

## 🔹 Time Domain

* Mean
* Variance
* RMS

## 🔹 Statistical Features

* Skewness
* Kurtosis

## 🔹 Frequency Domain

* FFT
* Power spectrum

## 🔹 Phase Features (Important for PSK)

```
θ = arctan(Q / I)
```

* Phase variance
* Phase difference

---

# 🌲 Machine Learning Model

## 🔹 Random Forest Classifier

* Ensemble of decision trees
* Uses majority voting

### Gini Index:

```
Gini = 1 - Σ(p_i²)
```

---

## 🔹 Why Random Forest?

* Handles non-linear patterns
* Robust to noise
* Works well with extracted features

---

# 📊 Results

## ✅ Accuracy

```
89.26%
```

---

## 📊 Classification Performance

| Class | Precision | Recall | Insight                              |
| ----- | --------- | ------ | ------------------------------------ |
| ASK   | 0.98      | 0.95   | Excellent                            |
| FSK   | 0.95      | 0.94   | Stable                               |
| PSK   | 0.94      | 0.75   | PSK is mistaken for Noise Frequently |
| NOISE | 0.74      | 0.93   | Model Correctly predicts Noise mostly but also mistake other Classes like PSK as Noise |

---

## 🔍 Key Observation

* PSK often misclassified as NOISE
* Due to sensitivity of phase features to noise

---

# 📈 SNR vs Accuracy

* -5 dB → ~88%
* > 5 dB → ~99%

👉 Model is robust to noise

---

# 🔴 Limitations

* PSK confusion with noise
* Synthetic dataset only
* Feature engineering dependent

---

# 🚀 Future Work

* CNN on raw IQ signals
* Higher-order modulation (QAM)
* Real-time SDR integration

---

# 🔥 Live Simulation

Simulates real-time classification:

```
SNR: 10 dB | Predicted: PSK (92%) | Actual: PSK
```

---

# 🧠 Summary

This project demonstrates a complete pipeline for modulation recognition using:

* Signal processing
* Feature engineering
* Machine learning

It achieves strong accuracy and robustness under noisy conditions, making it suitable for applications in **software-defined radio and cognitive radio systems**.

---

# ⭐ If you like this project

Give it a ⭐ on GitHub!

---
