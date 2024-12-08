import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi
st.title("Analisis Data Penjualan")

# Memuat data
data_file = st.file_uploader("Unggah file CSV", type=["csv"])
if data_file is not None:
    df = pd.read_csv(data_file)
    st.write("Data berhasil dimuat:")
    st.dataframe(df)

    # Menampilkan statistik deskriptif
    st.write("Statistik Deskriptif:")
    st.write(df.describe())

 # Menambahkan judul dan subjudul
st.title('Proyek Akhir: Analisis Data Penjualan:')
st.header('Nama: Muhammad Harsyam')
st.subheader('Email: jja85120@gmail.com')
st.subheader('Id Dicoding: muhammad_harsyam')

st.header('Proyek Akhir: Analisis Data penjualan:')
st.subheader('1.Top Produk Terlaris')
st.write('''
    Berdasarkan grafik di bawah ini dapat dilihat bahwa cama_mesa_banho merupakan produk terlaris.
''')

# Total penjualan per kategori
total_penjualan_per_kategori = df.groupby('product_category_name')['order_id'].count().reset_index()

# Mengurutkan dan mengambil 10 kategori teratas
top_10_kategori = total_penjualan_per_kategori.sort_values(by='order_id', ascending=False).head(10)

# Visualisasi
plt.figure(figsize=(12, 6))
sns.barplot(data=top_10_kategori, x='product_category_name', y='order_id', palette='viridis')
plt.title('Top 10 Kategori Produk Terlaris')
plt.xlabel('Kategori Produk')
plt.ylabel('Total Penjualan')
plt.xticks(rotation=45)
st.pyplot(plt)
st.write('''
         Kategori produk yang berkaitan dengan kebutuhan rumah tangga dan kesehatan tampaknya sangat diminati. kategori automotivo dan ferramentas_jardim tidak berada di urutan teratas namun, produk ini masih menunjukkan potensi untuk mengalami pertumbuhan.
         ''')

# Analisis jumlah produk per kategori
product_category = df['product_category_name'].value_counts()
st.title("2.Distribusi Jumlah Produk per Kategori:")
st.bar_chart(product_category)
st.write('''
         Grafik di atas menunjukkan distribusi jumlah produk berdasarkan kategori. Dari data yang ditampilkan, terlihat bahwa kategori "casa_construção" dan "brinquedos" memiliki jumlah produk yang paling tinggi, menunjukkan popularitas dan permintaan yang signifikan dalam kategori tersebut.

Sebaliknya, beberapa kategori lainnya, seperti "esporte_lazer" dan "eletrodomésticos," menunjukkan jumlah produk yang lebih rendah, yang mungkin mencerminkan tren pasar atau preferensi konsumen yang berbeda.
         ''')

# Visualisasi waktu pemesanan
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['order_purchase_month'] = df['order_purchase_timestamp'].dt.to_period('M')
monthly_orders = df.groupby('order_purchase_month').size()
    
st.title("3.Jumlah Pesanan per Bulan:")
plt.figure(figsize=(10, 5))
plt.plot(monthly_orders.index.astype(str), monthly_orders.values)
plt.title('Jumlah Pesanan per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Pesanan')
plt.xticks(rotation=45)
st.pyplot(plt)
st.write(''''
         Secara keseluruhan, terdapat tren pertumbuhan yang jelas dalam jumlah pembelian dari awal 2017 hingga pertengahan 2018, meskipun ada fluktuasi bulanan serta Terjadi lonjakan signifikan dalam jumlah pembelian pada bulan November 2017. Lonjakan ini mungkin terkait dengan promosi khusus, seperti Black Friday atau kampanye penjualan akhir tahun.
         ''')

# Menambahkan Caption
st.caption('Copyright © Muhammad Harsyam 2024')