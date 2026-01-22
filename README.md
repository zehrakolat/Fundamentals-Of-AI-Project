# AI-Powered Drug Recommendation Chatbot Prototype

Bu proje, kullanıcıların sağlık durumlarına göre **bilinçli ve güvenli kararlar almalarına yardımcı olmak** amacıyla geliştirilmiş **yapay zeka destekli bir chatbot prototipidir**.  
Sistem; **ilaç kullanımı**, **ilaç–ilaç etkileşimleri** ve **yaşa uygunluk** gibi kritik konularda **hızlı ve kişiselleştirilmiş bilgi** sağlamayı hedefler.

> ⚠️ Bu chatbot **tanı veya tedavi amaçlı değildir**. Sağlanan bilgiler bilgilendirme amaçlıdır.

---

## 📋 Proje Özeti

Chatbot iki ana kullanım senaryosu üzerine kurgulanmıştır:

### 1. İlaç Bazlı Sorgulama
Kullanıcı, belirli bir ilaç hakkında aşağıdaki bilgileri talep edebilir:
- Yan etkiler
- İlaç–ilaç etkileşimleri
- Gıda etkileşimleri
- Yaş uygunluğu

### 2. Durum Bazlı Tavsiye
Kullanıcı yaşadığı bir **hastalık** veya **belirtiyi** girerek:
- Uygun ilaç önerileri
- Yaşına uygunluk kontrolü
- Olası riskler hakkında bilgilendirme alır.

---

## 🛠 Kullanılan Teknolojiler

Proje, yapılandırılmış verilerle çalışan **kural tabanlı ve veri odaklı** bir yaklaşım benimser:

- **Python**  
  Chatbot’un ana geliştirme dili.

- **Pandas**  
  CSV formatındaki veri setinin yüklenmesi, filtrelenmesi ve işlenmesi.

- **Düzenli İfadeler (re)**  
  Kullanıcı girdilerinden sayısal yaş bilgilerinin ayıklanması.

- **Komut Satırı Arayüzü (CLI)**  
  Terminal tabanlı kullanıcı etkileşimi.


---

## 🔄 Çalışma Metodolojisi ve Akış

Sistem aşağıdaki adımları izleyerek çalışır:

1. **Giriş ve Yaş Kontrolü**  
   Kullanıcıdan yaş bilgisi alınır ve ilaçların yaş uygunluğu denetlenir.

2. **Eşleştirme (Matching)**  
   Girilen ilaç adı veya tıbbi duruma göre veri seti filtrelenir.

3. **Etkileşim Analizi**  
   Kullanıcı birden fazla ilaç kullandığını belirtirse, olası riskli etkileşimler kontrol edilir.

4. **Bildirim ve Geri Bildirim**  
   - Yaş uyumsuzluğu
   - Gıda etkileşimleri
   - Olası yan etkiler  
   
   kullanıcıya **özet ve anlaşılır** bir yanıt olarak sunulur.

---

## 🎯 Projenin Amacı

- Sağlıkla ilgili **bilgiye hızlı erişim** sağlamak
- İlaç kullanımında **farkındalık oluşturmak**
- Yapay zekânın sağlık alanındaki **destekleyici rolünü** göstermek



Bu proje **akademik ve prototip amaçlıdır**.  
Gerçek klinik kararlar için mutlaka bir **sağlık uzmanına danışılmalıdır**.
