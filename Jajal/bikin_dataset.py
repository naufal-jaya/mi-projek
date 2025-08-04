import pandas as pd
import random 
from datetime import datetime, timedelta

rute_list = ['A', 'B', 'C']
tanggal_list = pd.date_range(start="2025-08-01", end="2025-08-31")
jam_list = list(range(5,22))
is_weekend = None
is_libur = None
df = pd.read_csv("Daftar Hari Libur Nasional Tahun 2025.csv")
list_libur = pd.to_datetime(df["Tanggal Libur"], format = "%d/%m/%Y")

data = []

for tanggal in tanggal_list:
    hari = tanggal.strftime("%A")
    is_weekend = hari in ["Saturday", "Sunday"]
    is_libur = tanggal.date() in list_libur.dt.date.values 
    # awalnya: is_libur = tanggal in list_libur
    
    for jam in jam_list:
        for rute in rute_list:
            if is_weekend or is_libur:
                if jam in range (6,9) or jam in range (16,19):
                    base = 60 if rute == 'A' else 40 if rute == 'B' else 20 #if rute == 'C' #else 
                elif jam in range (10,15):
                    base = 20 if rute =='A' else 10 if rute == 'B' else 5
                else: 
                    base = 10 if rute == 'A' else 5 if rute == 'B' else 3

            else:
                if jam in range (6,9) or jam in range (16,19):
                    base = 100 if rute =='A'else 60 if rute == 'B' else 40
                elif jam in range (10,15):
                    base = 40 if rute =='A' else 25 if rute == 'B' else 20 #if rute == 'C' else 60 if rute == 'D' else 40 if rute 'E' else 30
                else:
                    base = 20 if rute == 'A' else 15 if rute =='B' else 10 #if rute == 'C' else 60 if rute == 'D' else 40 if rute 'E' else 30

            noise = int(random.gauss(0, base * 0.1))
            #print("noise", noise, "base ", base)
            penumpang = max(0, base + noise)
            #print(penumpang)
            
            data.append([
            tanggal.strftime("%Y-%m-%d"),
            hari,
            is_libur,
            is_weekend,
            rute,
            jam,
            penumpang
            ])

            # df = pd.DataFrame(data, columns=["Tanggal", "Hari", "Libur", "Akhir Pekan", "*base penumpang"])
            # data.append([
            #     tanggal.strftime("%Y-%m-%d"),
            #     hari,
            #     is_weekend,
            #     jam,
            #     rute,
            #     penumpang
            # ]) 

pd.set_option('display.max_rows', None)
df = pd.DataFrame(data, columns=["Tanggal", "Hari", "LiburNasional", "AkhirPekan", "Rute", "Jam", "JumlahPenumpang"])
df.to_csv("data_sintetis_jumlah_penumpang.csv", index=False)
print(df)

#print(df)