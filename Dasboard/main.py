import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi
st.title("Analisis Data Penjualan")

# Membaca file CSV
df = pd.read_csv('https://drive.google.com/uc?id=12kIQWk9E73FQWqL0WcgxR8IZ9jBCYfws')

# Menampilkan beberapa baris pertama dari DataFrame
st.write("Data Awal:")
st.write(df.head())

# Menampilkan statistik deskriptif
st.write("Statistik Deskriptif:")
st.write(df.describe())

# Menambahkan judul dan subjudul
st.title('Proyek Akhir: Analisis Data Penjualan')
st.header('Nama: Muhammad Harsyam')
st.subheader('Email: jja85120@gmail.com')
st.subheader('Id Dicoding: muhammad_harsyam')

# Menambahkan opsi "Semua Produk" ke dropdown kategori
categories = ['Semua Produk'] + list(df['product_category_name'].unique())
selected_category = st.selectbox("Pilih Kategori Produk:", categories)

# Filter berdasarkan rentang tanggal
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
start_date, end_date = st.date_input("Pilih Rentang Tanggal:", 
                                      [df['order_purchase_timestamp'].min().date(), 
                                       df['order_purchase_timestamp'].max().date()])

# Filter data berdasarkan kategori dan rentang tanggal yang dipilih
if selected_category == 'Semua Produk':
    filtered_data = df[(df['order_purchase_timestamp'].dt.date >= start_date) & 
                       (df['order_purchase_timestamp'].dt.date <= end_date)]
else:
    filtered_data = df[(df['product_category_name'] == selected_category) & 
                       (df['order_purchase_timestamp'].dt.date >= start_date) & 
                       (df['order_purchase_timestamp'].dt.date <= end_date)]

st.header('1. Top Produk Terlaris dalam Kategori Terpilih')
st.write(f'Produk terlaris dalam kategori {selected_category} dari {start_date} hingga {end_date}:')

# Total penjualan per kategori
total_penjualan_per_kategori = filtered_data.groupby('product_category_name')['order_id'].count().reset_index()

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
plt.clf()  # Membersihkan figure

st.write('''
     Kategori produk yang berkaitan dengan kebutuhan rumah tangga dan kesehatan tampaknya sangat diminati. Kategori automotivo dan ferramentas_jardim tidak berada di urutan teratas, namun produk ini masih menunjukkan potensi untuk mengalami pertumbuhan.
     ''')

# Analisis jumlah produk per kategori
product_category = filtered_data['product_category_name'].value_counts()
st.title("2. Distribusi Jumlah Produk per Kategori:")
st.bar_chart(product_category)
st.write('''
        Grafik di atas menunjukkan distribusi jumlah produk berdasarkan kategori. Dari data yang ditampilkan, terlihat bahwa kategori "casa_construção" dan "brinquedos" memiliki jumlah produk yang paling tinggi, menunjukkan popularitas dan permintaan yang signifikan dalam kategori tersebut. Sebaliknya, beberapa kategori lainnya, seperti "esporte_lazer" dan "eletrodomésticos," menunjukkan jumlah produk yang lebih rendah, yang mungkin mencerminkan tren pasar atau preferensi konsumen yang berbeda.
         ''')

# Visualisasi waktu pemesanan
monthly_orders = filtered_data.groupby(filtered_data['order_purchase_timestamp'].dt.to_period('M')).size()

st.title("3. Jumlah Pesanan per Bulan:")
plt.figure(figsize=(10, 5))
plt.plot(monthly_orders.index.astype(str), monthly_orders.values, marker='o')
plt.title('Jumlah Pesanan per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Pesanan')
plt.xticks(rotation=45)
st.pyplot(plt)
plt.clf()  # Membersihkan figure

st.write('''
        Secara keseluruhan, terdapat tren pertumbuhan yang jelas dalam jumlah pembelian dari awal 2017 hingga pertengahan 2018, meskipun ada fluktuasi bulanan. Terjadi lonjakan signifikan dalam jumlah pembelian pada bulan November 2017. Lonjakan ini mungkin terkait dengan promosi khusus, seperti Black Friday atau kampanye penjualan akhir tahun.
        ''')

# Menambahkan Caption
st.caption('Copyright © Muhammad Harsyam 2024')
