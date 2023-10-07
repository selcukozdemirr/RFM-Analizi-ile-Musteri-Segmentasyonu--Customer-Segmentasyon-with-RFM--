Aşağıdaki yazıyı revize etmenize yardımcı olmaktan memnuniyet duyarım. Öncelikle, projenizin adını ve açıklamasını daha dikkat çekici hale getirmek için başlık olarak kullanabilirsiniz. Ayrıca, projenizin amacını ve iş problemlerini daha kısa ve net bir şekilde ifade edebilirsiniz. İşte revize edilmiş yazı:

# RFM Analizi ile Müşteri Segmentasyonu

Bu proje, FLO adlı bir e-ticaret şirketinin müşterilerini RFM (Recency, Frequency, Monetary) analizi ile segmentlere ayırarak, her segmente uygun pazarlama stratejileri geliştirmeyi amaçlamaktadır.

## İş Problemi

FLO, müşterilerinin alışveriş davranışlarını anlayarak daha etkili bir pazarlama stratejisi oluşturmak istiyor. Bu doğrultuda aşağıdaki sorulara cevap aranmaktadır:

- Müşterileri hangi kriterlere göre segmentlere ayırabiliriz?
- Her segment için hangi pazarlama kampanyaları ve indirimler uygulanabilir?
- Sadık müşterileri nasıl belirleyebilir ve onlara özel teklifler sunabiliriz?
- Uyuyan veya kaybedilme riski taşıyan müşterileri nasıl yeniden kazanabiliriz?

## Veri Seti

Kullandığımız veri seti, son alışverişlerini 2020-2021 yıllarında hem online hem offline kanallardan gerçekleştiren FLO müşterilerinin geçmiş alışveriş davranışlarına ait bilgiler içermektedir. Veri setinde aşağıdaki özellikler bulunmaktadır:

- master_id: Eşsiz müşteri numarası
- order_channel: Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, iOS, Desktop, Mobile, Offline)
- last_order_channel: En son alışverişin yapıldığı kanal
- first_order_date: Müşterinin yaptığı ilk alışveriş tarihi
- last_order_date: Müşterinin yaptığı son alışveriş tarihi
- last_order_date_online: Müşterinin online platformda yaptığı son alışveriş tarihi
- last_order_date_offline: Müşterinin offline platformda yaptığı son alışveriş tarihi
- order_num_total_ever_online: Müşterinin online platformda yaptığı toplam alışveriş sayısı
- order_num_total_ever_offline: Müşterinin offline'da yaptığı toplam alışveriş sayısı
- customer_value_total_ever_offline: Müşterinin offline alışverişlerinde ödediği toplam ücret
- customer_value_total_ever_online: Müşterinin online alışverişlerinde ödediği toplam ücret
- interested_in_categories_12: Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi
  ![image](https://github.com/selcukozdemirr/RFM-Analizi-ile-Musteri-Segmentasyonu--Customer-Segmentasyon-with-RFM--/assets/139502981/b01c0c9c-abf9-444c-826c-d29d56001aa3)


## Gereksinimler

Bu projeyi çalıştırabilmek için aşağıdaki gereksinimlere ihtiyacınız vardır:

- Python 3.x
- Pandas
- Scikit-Learn

## Nasıl Kullanılır

Projeyi kullanabilmek için aşağıdaki adımları takip edebilirsiniz:

1. Proje dosyalarını bilgisayarınıza indirin veya kopyalayın.
2. Gereksinimleri yükleyin: `pip install pandas scikit-learn`
3. Proje klasörünün içindeki ana kod dosyasını çalıştırın: `python main.py`

## Testler

Proje testleri aşağıdaki adımlarla çalıştırabilirsiniz:

1. Test veri setini hazırlayın.
2. Proje kodunu çalıştırarak müşteri segmentasyonunu yapın.
3. Oluşturulan segmentlere göre pazarlama stratejilerini belirleyin ve uygulayın.
4. Kampanyaların sonuçlarını izleyin ve müşteri davranışlarını inceleyerek stratejilerin etkinliğini değerlendirin.

## Kullanılan Teknolojiler

Bu proje geliştirilirken aşağıdaki teknolojiler kullanılmıştır:

- Python: Veri analizi ve işleme için kullanıldı.
- Pandas: Veri çerçeveleri oluşturmak ve işlemek için kullanıldı.
- Scikit-Learn: Makine öğrenimi modellerini oluşturmak ve eğitmek için kullanıldı.

## Katkıda Bulunanlar

Bu projeye katkıda bulunan ekip üyeleri: Miuul, VeriGood

## Lisans

Bu proje için kullanılan lisans: MIT Lisansı
