# import pandas as pd

# df_input = pd.read_csv("data_sintetis_jumlah_penumpang.csv")

# df_input["data_sintetis_jumlah_penumpang.csv"], rute_labels = df_input["Rute"].factorize()

# print("Mapping Rute ke angka:")
# for i, label in enumerate(rute_labels):
#     print(f"{label} -> {i}")

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from datetime import datetime, timedelta

# --- 1. Load data penumpang dan hari libur ---
df = pd.read_csv("data_sintetis_jumlah_penumpang.csv")
df_libur = pd.read_csv("Daftar Hari Libur Nasional Tahun 2025.csv")

# Pastikan format tanggal konsisten
df["Tanggal"] = pd.to_datetime(df["Tanggal"])
df_libur["Tanggal"] = pd.to_datetime(df_libur["Tanggal Libur"], format = "%d/%m/%Y")

# --- 2. Encode kategori Rute ---
df["Rute"], rute_kategori = df["Rute"].factorize()

# --- 3. Siapkan fitur dan target ---
X = df[["LiburNasional", "AkhirPekan", "Rute", "Jam"]]
y = df["JumlahPenumpang"]

# --- 4. Train model ---
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# --- 5. Siapkan data prediksi untuk hari berikutnya ---
tanggal_terakhir = df["Tanggal"].max()
tanggal_besok = tanggal_terakhir + timedelta(days=1)
hari_besok = tanggal_besok.strftime("%A")
is_weekend = hari_besok in ["Saturday", "Sunday"]
#is_libur = tanggal_besok in df_libur["Tanggal Libur"].values  # <-- otomatis cek libur
is_libur = True 

# --- 6. Buat data prediksi ---
rute_list = list(rute_kategori)
prediksi_data = []

for rute in rute_list:
    rute_encoded = rute_kategori.get_loc(rute)
    for jam in range(5, 23):  # Jam 5 s/d 22
        fitur = [is_weekend, is_libur, rute_encoded, jam]
        jumlah_prediksi = int(model.predict([fitur])[0])
        prediksi_data.append({
            "Tanggal": tanggal_besok.strftime("%Y-%m-%d"),
            "Rute": rute,
            "Jam": jam,
            "IsWeekend": is_weekend,
            "IsLibur": is_libur,
            "PrediksiPenumpang": jumlah_prediksi
        })

# --- 7. Hasil akhir ---
df_prediksi = pd.DataFrame(prediksi_data)
print(df_prediksi)

# Simpan ke CSV (opsional)
df_prediksi.to_csv("prediksi_penumpang_besok.csv", index=False)
