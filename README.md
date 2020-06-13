# Yaz-muh-guncel-konular-proje
Yazılım Mühendisliği Güncel Konular Dersi Proje Takibi için oluşturulmuştur.

1-) Kocaeli ili için Çevre ve Şehircilik Bakanlığının yayınlamış olduğu veriler ile veriseti oluşturuldu. 
Veri setinde oldukça fazla eksik veri bulunduğundan eksik verileri gidermek için pandas kütüphanesinde bulunan ve zaman serilerinde kullanılan "interpolate" yöntemi ile veri setindeki eksik veriler giderildi.

2-) Veri setinde kirletici hava parametreleri ;
     NO2
     SO2
     PM10
     PM25
     CO 
     
![aylaragore](https://user-images.githubusercontent.com/62748526/84568679-ba8aba00-ad89-11ea-85c0-345729ff0e24.PNG)

![aylaragore1](https://user-images.githubusercontent.com/62748526/84568781-6a602780-ad8a-11ea-9be9-5ad24d3b5062.PNG)
 
Yukarıdaki  resimde her bir parametrenin yıllara ve aylara göre dağılımı bulunmaktadır.

Dağılımlara göre parametreler yorumlandığında PM10 değerinin 5. ayda en düşük seviyete düştüğünü en yüksek seviyelerde bulunduğu zaman ise OCAK - ŞUBAT aylarında yani kış mevsimlerinde bu oranın daha yüksek olduğu görülmektedir. 

Yıllara göre dağılımda SO2 parametresi ise 2011-2012 yılları arasında yükselmeye geçerken 2012-2013 arasında azalarak tekrar normal seyrine döndüğü söylenebilir.

3-) Veri setinde bulunan değerlerin ortalama - mod - medyan değerleri hesaplanmıştır.

![ortalama](https://user-images.githubusercontent.com/62748526/84568956-a34ccc00-ad8b-11ea-9390-4e3253de09f6.PNG)

![mod](https://user-images.githubusercontent.com/62748526/84568963-bf506d80-ad8b-11ea-90da-5e053a117b1d.PNG)

![median](https://user-images.githubusercontent.com/62748526/84568967-c7a8a880-ad8b-11ea-82ef-b55963bc5ea1.PNG)


4- ) Ulusal Hava Kalite İndeksi Kesme Noktaları ile Havaya olumsuz etki eden parametrelerin skalası mevcuttur. 
 
![ulusalhki](https://user-images.githubusercontent.com/62748526/84569061-68976380-ad8c-11ea-8518-946e89f6e547.PNG)

5-) Modelleme aşamasında Zaman Serilerinde kullanılan ARIMA ve SARIMA modelleri kullanıldı. Kullanılan Modellerden çıkan tahmin sonuçları aşağıdaki şekildedir. 

![Sarıma](https://user-images.githubusercontent.com/62748526/84569172-215da280-ad8d-11ea-9e15-81f345371627.PNG)

![Arıma](https://user-images.githubusercontent.com/62748526/84569174-24589300-ad8d-11ea-9542-b2c614d8f0e1.PNG)

6-) Modelin Değerlendirilmesi
 
 Arıma ve Sarıma modellerini değerlendirmek için MAE, MASE, MSE, RMSE ölçütleri kullanıldı.
 
Arıma Modeli için Çıktılar  

RMSE: 7.149942
MAE: 4.547
MASE: 2.132
MSE: 51.122
  
Sarıma Modeli için Çıktılar :

RMSE: 7.237
MAE: 3.876
MASE: 1.969
MSE: 52.368

7- ) Örneğin Sarıma Modelinde 



