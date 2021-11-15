# RFM Projesi

# Data Tanımı
# InvoiceNo: Fatura numarası. Her işleme yani faturaya ait eşsiz numara. Eğer bu kod C ile başlıyorsa işlemin iptal edildiğini ifade eder.
# StockCode: Ürün kodu. Her bir ürün için eşsiz numara.
# Description: Ürün ismi
# Quantity: Ürün adedi. Faturalardaki ürünlerden kaçar tane  satıldığını ifade etmektedir.
# InvoiceDate: Fatura tarihi ve zamanı.
# UnitPrice: Ürün fiyatı (Sterlin cinsinden)
# CustomerID: Eşsiz müşteri numarası
# Country: Ülke ismi. Müşterinin yaşadığı ülke

import pandas as pd
import numpy as np
import datetime as dt

data = pd.read_excel("online_retail_II.xlsx",
                    sheet_name="Year 2010-2011",
                    parse_dates=["InvoiceDate"])
df = data.copy()

def df_summary(dataframe):
    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables {dataframe.shape[1]}")
    cat_col = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].dtypes == "O"
                   and dataframe[col].nunique() > 20]
    print(f"Categorical Variables: {len(cat_col)}, (Cat But Car Variables: {len(cat_but_car)})")
    num_col = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].dtypes != "O" and
                   dataframe[col].nunique() <= 10]
    missing_v = df.isna().sum().sum()
    print(f"Numerical Variables {len(num_col)}, (Num But Cat Variables: {len(num_but_cat)})")
    print(f"Missing Values: {missing_v}")

# Data özet çıktısı
df_summary(df)
df.dtypes

# Eşsiz ürün sayısı
df["Description"].nunique()

# Hangi urunden kac tane var ?
df["Description"].value_counts().head(10)

# En cok satılan urunler
df.groupby("Description").agg({"Quantity":"sum"}) \
.sort_values("Quantity", ascending=False).head()

# Toplam kesilen fatura
df["Invoice"].nunique()

# Eksi degerler iade edilen urunlerden kaynaklı, bu yuzden fatura kodunun basında "C"
# olan urunleri cıkartıyoruz
df = df[~df["Invoice"].str.contains("C", na=False)]

# Fatura başına ortalama kazanç ne kadar ?
# Bunun için Quantity ve Price çarpıp yeni bir değişken oluşturmalıyız
df["Total_Price"] = df["Quantity"] * df["Price"]
df.head()

# Hangi ülke ortalama ne kadar kazandırdı ?
df.groupby("Country").agg({"Total_Price":"mean"}).sort_values("Total_Price",ascending=False).head()

# Eksik gözlemlere bakalım, Veri ön işleme yapmayacağımızdan direkt siliyoruz
df.isna().sum()
df.dropna(inplace=True)


# Eksi değerlerden de kurtuldugumuzu görüyoruz
df.describe().T


# RFM Metriklerimizi hesaplamaya geçelim

# Recency = Musteri en son ne zaman alışveriş yaptı
# Bugün Tarihi - Son Satın Alma Tarihi
df["InvoiceDate"].max()

# Son tarihimizde sıfırlama olmaması için 1 ekliyoruz.
today_date = dt.datetime(2011, 12, 10)


rfm = df.groupby("Customer ID").agg({"InvoiceDate": lambda x: (today_date - x.max()).days,
                                    "Invoice": lambda x: len(x),
                                    "Total_Price": lambda x: x.sum()})
rfm.head()

# Columns name
rfm.columns = ["Recency", "Frequency", "Monetary"]
rfm.head()


# Frequency ve Monetary değerleri 0'dan büyük olmalı
rfm =  rfm[((rfm["Monetary"]) > 0 & (rfm["Frequency"] > 0))]
rfm.head()

# RFM Skorlarımızı hesaplayalım
rfm["Recency_Score"] = pd.qcut(rfm["Recency"], 5, [5,4,3,2,1])
rfm["Frequency_Score"] = pd.qcut(rfm["Frequency"], 5, [1,2,3,4,5])
rfm["Moneyary_Score"] = pd.qcut(rfm["Monetary"], 5, [1,2,3,4,5])
rfm.head()


# Skorları bir araya getiriyoruz
rfm["RFM_Score"] = (rfm["Recency_Score"].astype(str) +
                   rfm["Frequency_Score"].astype(str) +
                   rfm["Moneyary_Score"].astype(str))
rfm.head()


# RFM skorlarımızın temsil ettiği sınıfı isimlendirip segment olarak ekliyoruz
seg_map = {
    r'[1-2][1-2]': 'Hibernating',
    r'[1-2][3-4]': "At_Risk",
    r'[1-2]5': "Cant_Loose",
    r'3[1-2]': "About_to_Sleep",
    r'33': "Need_Attention",
    r'[3-4][4-5]': "Loyal_Customers",
    r'41': "Promising",
    r'51': "New_Customers",
    r'[4-5][2-3]': "Potential_Loyalists",
    r'5[4-5]': "Champions"
}

rfm["Segment"] = rfm["Recency_Score"].astype(str) + rfm["Frequency_Score"].astype(str)
rfm["Segment"] = rfm["Segment"].replace(seg_map, regex=True)
rfm.head()

# Segment raporlama
rfm[["Segment", "Recency", "Frequency", "Monetary"]].groupby("Segment").agg(["mean","count"])

new_df = pd.DataFrame()
new_df["Loyal_Customers"] = rfm[rfm["Segment"] == "Loyal_Customers"].index
new_df.to_excel("LoyalCustomers.xlsx")

pd.set_option("display.max_rows",None)
rfm[rfm["Segment"]=="Need_Attention"].groupby(["RFM_Score"]).agg({"Recency":"mean","Frequency":"mean","Monetary":"mean"})
df["Customer ID"].nunique()

rfm[rfm["Segment"]=="Cant_Loose"].groupby(["RFM_Score"]).agg({"Recency":"mean","Frequency":"mean","Monetary":"mean"})

rfm[rfm["Segment"]=="Loyal_Customers"].groupby(["RFM_Score"]).agg({"Recency":"mean","Frequency":"mean","Monetary":"mean"})
