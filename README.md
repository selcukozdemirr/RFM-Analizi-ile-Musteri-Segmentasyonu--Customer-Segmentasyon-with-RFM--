# Proje Adı: RFM-Analizi-ile-Musteri-Segmentasyonu

Açıklama: Bu proje, bir e-ticaret şirketi olan FLO'nun müşteri segmentasyonunu gerçekleştirerek, farklı müşteri gruplarına özgü pazarlama stratejileri belirlemeyi amaçlamaktadır. Müşteri davranışlarını inceleyerek, müşterileri belirli kriterlere göre gruplandırmak ve bu gruplara özel kampanyalar geliştirmek hedeflenmektedir.

#İş Problemi
FLO, müşteri davranışlarını anlayarak daha etkili bir pazarlama stratejisi oluşturmak istiyor. Bu doğrultuda aşağıdaki iş problemleri çözülmeye çalışılacaktır:

Müşteri segmentasyonu yaparak, farklı müşteri gruplarını tanımlamak.
Belirlenen müşteri segmentlerine özel pazarlama kampanyaları ve indirimler oluşturmak.
Sadık müşterileri belirlemek ve onlara özel teklifler sunmak.
Uyuyan veya kaybedilme riski taşıyan müşterileri yeniden çekmek için stratejiler geliştirmek.

#Veri Seti Hikayesi
Kullandığımız veri seti, son alışverişlerini 2020-2021 yıllarında hem online hem offline kanallardan gerçekleştiren FLO müşterilerinin geçmiş alışveriş davranışlarına ait bilgiler içermektedir. Veri setinde aşağıdaki özellikler bulunmaktadır:

master_id: Eşsiz müşteri numarası
order_channel: Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, iOS, Desktop, Mobile, Offline)
last_order_channel: En son alışverişin yapıldığı kanal
first_order_date: Müşterinin yaptığı ilk alışveriş tarihi
last_order_date: Müşterinin yaptığı son alışveriş tarihi
last_order_date_online: Müşterinin online platformda yaptığı son alışveriş tarihi
last_order_date_offline: Müşterinin offline platformda yaptığı son alışveriş tarihi
order_num_total_ever_online: Müşterinin online platformda yaptığı toplam alışveriş sayısı
order_num_total_ever_offline: Müşterinin offline'da yaptığı toplam alışveriş sayısı
customer_value_total_ever_offline: Müşterinin offline alışverişlerinde ödediği toplam ücret
customer_value_total_ever_online: Müşterinin online alışverişlerinde ödediği toplam ücret
interested_in_categories_12: Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi

#Gereksinimler
Bu projeyi çalıştırabilmek için aşağıdaki gereksinimlere ihtiyacınız vardır:

Python 3.x
Pandas
Scikit-Learn

#Nasıl Kullanılır
Projeyi kullanabilmek için aşağıdaki adımları takip edebilirsiniz:

Proje dosyalarını bilgisayarınıza indirin veya kopyalayın.
Gereksinimleri yükleyin: pip install pandas scikit-learn
Proje klasörünün içindeki ana kod dosyasını çalıştırın: python main.py

#Testler
Proje testleri aşağıdaki adımlarla çalıştırabilirsiniz:

Test veri setini hazırlayın.
Proje kodunu çalıştırarak müşteri segmentasyonunu yapın.
Oluşturulan segmentlere göre pazarlama stratejilerini belirleyin ve uygulayın.
Kampanyaların sonuçlarını izleyin ve müşteri davranışlarını inceleyerek stratejilerin etkinliğini değerlendirin.

#Kullanılan Teknolojiler
Bu proje geliştirilirken aşağıdaki teknolojiler kullanılmıştır:

Python: Veri analizi ve işleme için kullanıldı.
Pandas: Veri çerçeveleri oluşturmak ve işlemek için kullanıldı.
Scikit-Learn: Makine öğrenimi modellerini oluşturmak ve eğitmek için kullanıldı.

#Katkıda Bulunanlar
Bu projeye katkıda bulunan ekip üyeleri:
Miuul, VeriGood

Lisans
Bu proje için kullanılan lisans: MIT Lisansı 
