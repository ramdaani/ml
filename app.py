import streamlit as st
import pickle
import numpy as np

# Load model
with open('model_tb.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Diagnosis Tuberkulosis (TB)")

st.write("Masukkan gejala yang dialami pasien untuk memprediksi kemungkinan TB.")

# Contoh input gejala biner (1 = Ya, 0 = Tidak)
cough = st.selectbox("Batuk terus menerus?", ["Tidak", "Ya"])
fever = st.selectbox("Demam berkepanjangan?", ["Tidak", "Ya"])
weight_loss = st.selectbox("Penurunan berat badan?", ["Tidak", "Ya"])
chest_pain = st.selectbox("Nyeri dada?", ["Tidak", "Ya"])

if st.button("Prediksi"):
    # Ubah input ke format numerik
    input_data = np.array([[int(cough == "Ya"),
                            int(fever == "Ya"),
                            int(weight_loss == "Ya"),
                            int(chest_pain == "Ya")]])

    # Prediksi
    prediction = model.predict(input_data)

    # Tampilkan hasil
    if prediction[0] == 1:
        st.error("Hasil Prediksi: Kemungkinan terkena TB.")
    else:
        st.success("Hasil Prediksi: Kemungkinan **tidak** terkena TB.")
