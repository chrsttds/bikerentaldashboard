import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

day_df = pd.read_csv("day.csv")
categorycols = ['season','yr','mnth','holiday','weekday','workingday','weathersit']

day_df[categorycols] = day_df[categorycols].astype('category')

day_df['weekday'] = day_df['weekday'].cat.rename_categories({
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday'
})

weekday_average_count = day_df.groupby('weekday')['cnt'].mean()

st.title('Proyek Akhir Data analysis menggunakan python : Bike Sharing')
st.write("""Nama : Christ Thaddeus   
         Email : christ.535220196@stu.untar.ac.id   
         Dicoding ID : mc325d5y0790   
         """)

st.header('Dashboard analisis penyewaan sepeda')
st.subheader('1. Bagaimana suhu mempengaruhi jumlah penyewaan sepeda')

fig, ax = plt.subplots(figsize=(10,5))
sns.scatterplot(x='temp', y='cnt', data=day_df)
ax.set_title('Distribusi antara temperatur dan jumlah user')
ax.set_xlabel('temperatur')
ax.set_ylabel('jumlah user')
st.pyplot(fig)

st.write('Diatas adalah hasil scatter plot dari distribusi temperatur dan jumlah user')

st.subheader('2. Variasi penyewaan sepeda setiap harinya')
fig1,ax1 = plt.subplots(figsize=(10,5))
weekday_average_count.plot(kind='line',marker='o')
ax1.set_title('Rata-Rata jumlah user per hari')
ax1.set_xlabel('Hari')
ax1.set_ylabel('rata-rata jumlah user')
st.pyplot(fig1)

st.write('Diatas adalah grafik yang menunjukkan rata-rata jumlah user setiap harinya')
