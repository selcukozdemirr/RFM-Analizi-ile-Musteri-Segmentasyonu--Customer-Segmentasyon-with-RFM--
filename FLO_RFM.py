
###############################################################
# RFM ile Müşteri Segmentasyonu (Customer Segmentation with RFM)
###############################################################

###############################################################
# İş Problemi (Business Problem)
###############################################################
# FLO müşterilerini segmentlere ayırıp bu segmentlere göre pazarlama stratejileri belirlemek istiyor.
# Buna yönelik olarak müşterilerin davranışları tanımlanacak ve bu davranış öbeklenmelerine göre gruplar oluşturulacak..

###############################################################
# Veri Seti Hikayesi
###############################################################

# Veri seti son alışverişlerini 2020 - 2021 yıllarında OmniChannel(hem online hem offline alışveriş yapan) olarak yapan müşterilerin geçmiş alışveriş davranışlarından
# elde edilen bilgilerden oluşmaktadır.

# master_id: Eşsiz müşteri numarası
# order_channel : Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, ios, Desktop, Mobile, Offline)
# last_order_channel : En son alışverişin yapıldığı kanal
# first_order_date : Müşterinin yaptığı ilk alışveriş tarihi
# last_order_date : Müşterinin yaptığı son alışveriş tarihi
# last_order_date_online : Muşterinin online platformda yaptığı son alışveriş tarihi
# last_order_date_offline : Muşterinin offline platformda yaptığı son alışveriş tarihi
# order_num_total_ever_online : Müşterinin online platformda yaptığı toplam alışveriş sayısı
# order_num_total_ever_offline : Müşterinin offline'da yaptığı toplam alışveriş sayısı
# customer_value_total_ever_offline : Müşterinin offline alışverişlerinde ödediği toplam ücret
# customer_value_total_ever_online : Müşterinin online alışverişlerinde ödediği toplam ücret
# interested_in_categories_12 : Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi

###############################################################
# GÖREVLER
###############################################################

# GÖREV 1: Veriyi Anlama (Data Understanding) ve Hazırlama
           # 1. flo_data_20K.csv verisini okuyunuz.
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
df_ = pd.read_csv('C:/Users/rocksever/Desktop/Miuul Veri Bilimi Dokümanları/06-11 Temmuz/FLOMusteriSegmentasyonu-221114-233246/FLOMusteriSegmentasyonu/flo_data_20k.csv')
df = df_.copy()

           # 2. Veri setinde
                     # a. İlk 10 gözlem,
df.head(10)
                     # b. Değişken isimleri,
df.columns

                     # c. Betimsel istatistik,
df.describe().T
                     # d. Boş değer,
df.isnull().sum()
                     # e. Değişken tipleri, incelemesi yapınız.
df.dtypes

           # 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir. Herbir müşterinin toplam
           # alışveriş sayısı ve harcaması için yeni değişkenler oluşturun.

df['order_num_total_All'] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
df['customer_value_total_All'] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]


           # 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
for column in df.columns:
    if 'date' in column.lower():
        df[column] = pd.to_datetime(df[column])
##kesin çözüm

import numpy as np

def is_date(string):
    try:
        pd.to_datetime(string)
        return True
    except ValueError:
        return False

for column in df.columns:
    if df[column].dtype != 'object':
        continue

    if df[column].apply(lambda x: is_date(x)):
        df[column] = pd.to_datetime(df[column])

print(df)

           # 5. Alışveriş kanallarındaki müşteri sayısının, ortalama alınan ürün sayısının ve ortalama harcamaların dağılımına bakınız.

customer_counts = df.groupby('order_channel')['master_id'].count()

##pilot yapmayı unuttum

           # 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.

df.groupby("master_id").agg({"customer_value_total_All": sum}).sort_values(by="customer_value_total_All", ascending=False).head(10)

           # 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.

df.groupby("master_id").agg({"order_num_total_All": sum}).sort_values(by="order_num_total_All", ascending=False).head(10)

           # 8. Veri ön hazırlık sürecini fonksiyonlaştırınız.
def pre_processing (dataframe):
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
df_ = pd.read_csv(
        'C:/Users/rocksever/Desktop/Miuul Veri Bilimi Dokümanları/06-11 Temmuz/FLOMusteriSegmentasyonu-221114-233246/FLOMusteriSegmentasyonu/flo_data_20k.csv')
df = df_.copy()
df.head(10)
df.columns
df.describe().T
df.isnull().sum()
df.dtypes
df['order_num_total_All'] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
df['customer_value_total_All'] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]
for column in df.columns:
    if 'date' in column.lower():
        df[column] = pd.to_datetime(df[column])
customer_counts = df.groupby('order_channel')['master_id'].count()
df.groupby("master_id").agg({"customer_value_total_All": sum}).sort_values(by="customer_value_total_All", ascending=False).head(10)
df.groupby("master_id").agg({"order_num_total_All": sum}).sort_values(by="order_num_total_All", ascending=False).head(10)

# GÖREV 2: RFM Metriklerinin Hesaplanması
orderdate=df["last_order_date"].max()
import datetime as dt
today_date = dt.datetime(2021,6,1)
rfm = df.groupby('master_id').agg({'last_order_date': lambda last_order_date: (today_date - last_order_date.max()).days,
                                   'order_num_total_All': lambda total_of_purchases: total_of_purchases.sum(),
                                   'customer_value_total_All': lambda total_of_pspending: total_of_pspending.sum()})
rfm.head()

rfm.columns = ["recency","frequency","monetary"]

rfm.describe().T


# GÖREV 3: RF ve RFM Skorlarının Hesaplanması
rfm["recency_score"] = pd.qcut(rfm["recency"], 5, labels=[5,4,3,2,1])
rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[5,4,3,2,1])
rfm["monetary_score"] = pd.qcut(rfm["monetary"], 5, labels=[5,4,3,2,1])
rfm["RFM_SCORE"]=(rfm["recency_score"].astype(str)+rfm["frequency_score"].astype(str)+rfm["monetary_score"].astype(str))
rfm["RF_SCORE"]=(rfm["recency_score"].astype(str)+rfm["frequency_score"].astype(str))
rfm.head()
# GÖREV 4: RF Skorlarının Segment Olarak Tanımlanması
seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}

rfm["segment"] = rfm["RFM_SCORE"].replace(seg_map,regex=True)
rfm= rfm[["recency", 'frequency',"monetary","segment"]]


# GÖREV 5: Aksiyon zamanı!
           # 1. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.

rfm[["segment","recency","frequency","monetary"]].groupby("segment").agg(["mean","count"])

           # 2. RFM analizi yardımı ile 2 case için ilgili profildeki müşterileri bulun ve müşteri id'lerini csv ye kaydediniz.
                   # a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
                   # tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Sadık müşterilerinden(champions,loyal_customers),
                   # ortalama 250 TL üzeri ve kadın kategorisinden alışveriş yapan kişiler özel olarak iletişim kuralacak müşteriler. Bu müşterilerin id numaralarını csv dosyasına
                   # yeni_marka_hedef_müşteri_id.cvs olarak kaydediniz.

# RFM analizi sonucu oluşturulan DataFrame'deki segmentlere göre filtreleme



filtered_customers_1 = rfm[(rfm['segment'].str.contains('champions|loyal_customers', case=False)) &
                         (rfm['monetary'] >= 250)]
filtered_df = df[df['interested_in_categories_12'].str.contains("KADIN", case=False)]

intersected_df = pd.merge(filtered_customers_1, filtered_df, on='master_id')
intersected_master_ids = intersected_df['master_id']

# Müşteri ID'lerini CSV dosyasına kaydetme
intersected_master_ids.to_csv('C:/Users/rocksever/Desktop/Miuul Veri Bilimi Dokümanları/06-11 Temmuz/FLOMusteriSegmentasyonu-221114-233246/FLOMusteriSegmentasyonu/yeni_marka_hedef_musteri_id.csv', index=False)

                   # b. Erkek ve Çoçuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte iyi müşteri olan ama uzun süredir
                   # alışveriş yapmayan kaybedilmemesi gereken müşteriler, uykuda olanlar ve yeni gelen müşteriler özel olarak hedef alınmak isteniliyor. Uygun profildeki müşterilerin id'lerini csv dosyasına indirim_hedef_müşteri_ids.csv
                   # olarak kaydediniz.
#İlk aşama, filtreler...
filtered_customers_2 = rfm[(rfm["segment"]=="cant_loose1") | (rfm["segment"]=="about_to_sleep1") | (rfm["segment"]=="new_customers1")]
filtered_df_2= df[(df["interested_in_categories_12"]).str.contains("ERKEK|COCUK")]

#Son aşama filtrelerin kesişimini almak ve maste idleri csv yapmak.
intersected_df2 = pd.merge(filtered_customers_2,filtered_df_2[["interested_in_categories_12","master_id"]],on=["master_id"])
intersected_df2.to_csv("C:/Users/rocksever/Desktop/Miuul Veri Bilimi Dokümanları/06-11 Temmuz/FLOMusteriSegmentasyonu-221114-233246/FLOMusteriSegmentasyonu/indirim_hedef_müşteri_ids.csv")


####tek bir excel formatında sheet sheet çıkarmak istersek bu şekilde yazabiliriz
import pandas as pd

with pd.ExcelWriter("C:/Users/rocksever/Desktop/Miuul Veri Bilimi Dokümanları/06-11 Temmuz/FLOMusteriSegmentasyonu-221114-233246/FLOMusteriSegmentasyonu/Müşteri Listesi.xlsx") as writer:
    intersected_master_ids.to_excel(writer, sheet_name="Kadın Müşteri Listesi", index=False)
    intersected_df2.to_excel(writer, sheet_name="Erkek Müşteri Listesi", index=False)


# GÖREV 6: Tüm süreci fonksiyonlaştırınız.
