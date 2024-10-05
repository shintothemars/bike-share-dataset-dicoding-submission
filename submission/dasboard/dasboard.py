import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Muat data
day_df = pd.read_csv("day_clean.csv")
hour_df = pd.read_csv("hour_clean.csv")

# Buat judul dasbor
st.title("Dasbor Penyewaan Sepeda")

# Buat tab untuk menampilkan data
tab1, tab2 = st.tabs(["Penyewaan Sepeda Berdasarkan Jam", "Penyewaan Sepeda Berdasarkan Musim"])

# Tab 1: Penyewaan Sepeda Berdasarkan Jam
with tab1:
    st.header("Penyewaan Sepeda Berdasarkan Jam")
    st.write("Grafik berikut menampilkan jumlah penyewaan sepeda berdasarkan jam:")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x="hours", y="count_cr", data=hour_df.groupby("hours").count_cr.sum().reset_index())
    ax.set_title("Penyewaan Sepeda Berdasarkan Jam")
    ax.set_xlabel("Jam")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)

# Tab 2: Penyewaan Sepeda Berdasarkan Musim
with tab2:
    st.header("Penyewaan Sepeda Berdasarkan Musim")
    st.write("Grafik berikut menampilkan jumlah penyewaan sepeda berdasarkan musim:")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x="season", y="count_cr", data=day_df.groupby("season").count_cr.sum().reset_index())
    ax.set_title("Penyewaan Sepeda Berdasarkan Musim")
    ax.set_xlabel("Musim")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)

# Tambahkan informasi tambahan
st.write("Informasi tambahan:")
st.write("Penyewaan sepeda paling banyak pada jam 17:00 dengan total penyewaan 336860.")
st.write("Penyewaan sepeda paling sedikit pada jam 04:00 dengan total penyewaan 4428.")
st.write("Musim fall menjadi musim paling banyak penyewaan dengan total penyewaan 1061129.")