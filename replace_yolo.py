import re

with open('blog-yolo11.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the <section id="blog"> block with the new article content
content = re.sub(r'<section id="blog".*?</section>', '''  <section id="article" aria-labelledby="article-title" style="padding: 7rem 0;">
    <div class="container" style="max-width: 800px;">
      
      <!-- Back Link -->
      <a href="blog.html" style="color: var(--text-muted); text-decoration: none; display: inline-flex; align-items: center; gap: 8px; margin-bottom: 2rem; font-weight: 600; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='var(--text-muted)'">
        &larr; <span data-tr="Blog'a Dön" data-en="Back to Blog">Blog'a Dön</span>
      </a>

      <!-- Header Image -->
      <img src="images/yolo.png" alt="YOLO11" style="width: 100%; border-radius: var(--radius-lg); margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">

      <!-- Title -->
      <h1 id="article-title" style="font-family: var(--font-head); font-size: clamp(2rem, 5vw, 2.5rem); line-height: 1.2; margin-bottom: 1.5rem;" data-tr="Gökyüzündeki Gözümüz: YOLO11 ile Nesne Algılama" data-en="Our Eye in the Sky: Object Detection with YOLO11">Gökyüzündeki Gözümüz: YOLO11 ile Nesne Algılama</h1>
      
      <div class="article-content" style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.8;">
        
        <h3 style="color: var(--text); font-family: var(--font-head); margin-top: 2rem; margin-bottom: 1rem; font-size: 1.5rem;" data-tr="Giriş: Sıfırdan Kendi Zekamızı İnşa Etmek" data-en="Introduction: Building Our Own Intelligence From Scratch">Giriş: Sıfırdan Kendi Zekamızı İnşa Etmek</h3>
        
        <p data-tr="SUAS ve benzeri otonom görevlerde nesne ve insan tespiti, operasyonun başarısını belirleyen en kritik aşamadır. TULPAR-FF olarak, görev bilgisayarımızda (Edge Device) yüksek FPS ile çalışacak, kendi eğittiğimiz YOLO tabanlı iki ana yapay zeka modülü geliştirdik: InfernoGuard (Yangın/Duman) ve SAR (Arama-Kurtarma). Basitçe hazır bir açık kaynak kod alıp kullanmak yerine, kendi verisetlerimizi cerrahi bir hassasiyetle temizledik, optimize ettik ve eğittik." data-en="In SUAS and similar autonomous missions, object and human detection is the most critical stage determining the success of the operation. As TULPAR-FF, we developed two main custom-trained YOLO-based artificial intelligence modules to run at high FPS on our Edge Device: InfernoGuard (Fire/Smoke) and SAR (Search-Rescue). Instead of simply using open-source code, we cleaned, optimized, and trained our own datasets with surgical precision.">SUAS ve benzeri otonom görevlerde nesne ve insan tespiti, operasyonun başarısını belirleyen en kritik aşamadır. TULPAR-FF olarak, görev bilgisayarımızda (Edge Device) yüksek FPS ile çalışacak, kendi eğittiğimiz YOLO tabanlı iki ana yapay zeka modülü geliştirdik: InfernoGuard (Yangın/Duman) ve SAR (Arama-Kurtarma). Basitçe hazır bir açık kaynak kod alıp kullanmak yerine, kendi verisetlerimizi cerrahi bir hassasiyetle temizledik, optimize ettik ve eğittik.</p>

        <h3 style="color: var(--text); font-family: var(--font-head); margin-top: 2.5rem; margin-bottom: 1rem; font-size: 1.5rem;" data-tr="1. InfernoGuard: Sıfır Yanlış Alarm (False Positive) Hedefi" data-en="1. InfernoGuard: Zero False Positive Goal">1. InfernoGuard: Sıfır Yanlış Alarm (False Positive) Hedefi</h3>
        <p data-tr="Havadan yangın tespitindeki en büyük problem, otopilotun bulutları, sis tabakasını veya beyaz kayaları duman sanarak yanlış alarm vermesidir. Bunu çözmek için verisetimizde özel bir strateji izledik." data-en="The biggest problem in airborne fire detection is the autopilot giving false alarms by mistaking clouds, fog, or white rocks for smoke. To solve this, we followed a special strategy in our dataset.">Havadan yangın tespitindeki en büyük problem, otopilotun bulutları, sis tabakasını veya beyaz kayaları duman sanarak yanlış alarm vermesidir. Bunu çözmek için verisetimizde özel bir strateji izledik.</p>
        
        <ul style="margin-left: 1.5rem; margin-bottom: 1.5rem; margin-top: 1rem; display: flex; flex-direction: column; gap: 0.8rem;">
          <li data-tr="<strong>Veri Optimizasyonu:</strong> FASDD_UAV verisetini kullanarak 25.000'den fazla drone perspektifi fotoğrafını sistemimize entegre ettik."><strong>Veri Optimizasyonu:</strong> FASDD_UAV verisetini kullanarak 25.000'den fazla drone perspektifi fotoğrafını sistemimize entegre ettik.</li>
          <li data-tr="<strong>Kör Nokta Eğitimi:</strong> Sistemin kafasının karışmasını önlemek için verisetinin içine tam 11.986 adet negatif veri (arkaplan ve bulut fotoğrafı) dahil ettik."><strong>Kör Nokta Eğitimi:</strong> Sistemin kafasının karışmasını önlemek için verisetinin içine tam 11.986 adet negatif veri (arkaplan ve bulut fotoğrafı) dahil ettik.</li>
          <li data-tr="<strong>Donanım ve Eğitim:</strong> Yerel bilgisayarlarımızın donanım sınırlarını aşmak ve eğitim süresini kısaltmak için Kaggle'ın çift NVIDIA Tesla T4 GPU bulut sunucularını kullandık. Uçuş bilgisayarımızda (Raspberry Pi vb.) sorunsuz çalışması için mimari olarak <span style='color: var(--accent); font-weight: 700;'>YOLO11s (Small)</span> modelini tercih ettik."><strong>Donanım ve Eğitim:</strong> Yerel bilgisayarlarımızın donanım sınırlarını aşmak ve eğitim süresini kısaltmak için Kaggle'ın çift NVIDIA Tesla T4 GPU bulut sunucularını kullandık. Uçuş bilgisayarımızda (Raspberry Pi vb.) sorunsuz çalışması için mimari olarak <span style="color: var(--accent); font-weight: 700;">YOLO11s (Small)</span> modelini tercih ettik.</li>
          <li data-tr="<strong>Eğitim Sonuçları:</strong> Sisteme kurduğumuz Early Stopping (Erken Durdurma) mekanizması sayesinde modelimiz 200 turu beklemeden 50. Turda (Epoch) maksimum zekasına ulaşarak en stabil ağırlık dosyasını (fassd.pt) üretti."><strong>Eğitim Sonuçları:</strong> Sisteme kurduğumuz Early Stopping (Erken Durdurma) mekanizması sayesinde modelimiz 200 turu beklemeden 50. Turda (Epoch) maksimum zekasına ulaşarak en stabil ağırlık dosyasını (fassd.pt) üretti.</li>
        </ul>

        <!-- METRICS GRID -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; margin: 2.5rem 0;">
          <div style="background: var(--surface2); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 2rem 1.5rem; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.03); transition: transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
            <div style="font-family: var(--font-head); font-size: 2.5rem; font-weight: 800; color: var(--accent); margin-bottom: 0.5rem;">%93.7</div>
            <div style="font-weight: 700; color: var(--text); font-size: 1.1rem; margin-bottom: 0.5rem;">mAP50 Skoru</div>
            <div style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.4;" data-tr="Ateş ve dumanı doğru tespit etme oranı">Ateş ve dumanı doğru tespit etme oranı</div>
          </div>
          <div style="background: var(--surface2); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 2rem 1.5rem; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.03); transition: transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
            <div style="font-family: var(--font-head); font-size: 2.5rem; font-weight: 800; color: var(--accent); margin-bottom: 0.5rem;">%90.4</div>
            <div style="font-weight: 700; color: var(--text); font-size: 1.1rem; margin-bottom: 0.5rem;">Precision (Kesinlik)</div>
            <div style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.4;" data-tr='Hedefe "Yangın" dediğinde doğruluk ihtimali'>Hedefe "Yangın" dediğinde doğruluk ihtimali</div>
          </div>
          <div style="background: var(--surface2); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 2rem 1.5rem; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.03); transition: transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
            <div style="font-family: var(--font-head); font-size: 2.5rem; font-weight: 800; color: var(--accent); margin-bottom: 0.5rem;">%89.1</div>
            <div style="font-weight: 700; color: var(--text); font-size: 1.1rem; margin-bottom: 0.5rem;">Recall (Duyarlılık)</div>
            <div style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.4;" data-tr="Sahadaki gerçek yangınları gözden kaçırmama oranı">Sahadaki gerçek yangınları gözden kaçırmama oranı</div>
          </div>
        </div>

        <h3 style="color: var(--text); font-family: var(--font-head); margin-top: 2.5rem; margin-bottom: 1rem; font-size: 1.5rem;" data-tr="Eğitim Eğrisi" data-en="Training Curve">Eğitim Eğrisi</h3>
        <div style="width: 100%; height: 350px; background: rgba(255, 255, 255, 0.2); border: 2px dashed var(--border); border-radius: var(--radius-lg); display: flex; align-items: center; justify-content: center; margin-bottom: 2rem; color: var(--text-muted); font-weight: 600; letter-spacing: 0.05em;" data-tr="[Kaggle Eğitim Grafiği Buraya Gelecek]" data-en="[Kaggle Training Graph Placeholder]">[Kaggle Eğitim Grafiği Buraya Gelecek]</div>

        <h3 style="color: var(--text); font-family: var(--font-head); margin-top: 3rem; margin-bottom: 1rem; font-size: 1.5rem;" data-tr="2. Otonom İnsan Tespiti (SAR Modülü)" data-en="2. Autonomous Human Detection (SAR Module)">2. Otonom İnsan Tespiti (SAR Modülü)</h3>
        <p data-tr="Arama kurtarma (SAR) görevlerinde hedeflerimiz çok daha küçük; yüksek irtifadan bakıldığında insan bedenleri sadece birkaç pikselden ibaret olabiliyor. Üstelik ormanlık veya enkazlık alanlar tespiti daha da zorlaştırıyor.">Arama kurtarma (SAR) görevlerinde hedeflerimiz çok daha küçük; yüksek irtifadan bakıldığında insan bedenleri sadece birkaç pikselden ibaret olabiliyor. Üstelik ormanlık veya enkazlık alanlar tespiti daha da zorlaştırıyor.</p>
        
        <ul style="margin-left: 1.5rem; margin-bottom: 2rem; margin-top: 1rem; display: flex; flex-direction: column; gap: 0.8rem;">
          <li data-tr="<strong>Hız ve Mimari Seçimi:</strong> İnsan tespitinde saniyedeki kare hızının (FPS) kritik olması sebebiyle, bu görevde en hafif mimari olan <span style='color: var(--accent); font-weight: 700;'>YOLO11n (Nano)</span> versiyonunu seçtik. Edge cihazlarda maksimum hız ve minimum güç tüketimi hedefledik."><strong>Hız ve Mimari Seçimi:</strong> İnsan tespitinde saniyedeki kare hızının (FPS) kritik olması sebebiyle, bu görevde en hafif mimari olan <span style="color: var(--accent); font-weight: 700;">YOLO11n (Nano)</span> versiyonunu seçtik. Edge cihazlarda maksimum hız ve minimum güç tüketimi hedefledik.</li>
          <li data-tr="<strong>Performans Karnesi:</strong> 58.000'den fazla doğru hedef tahmini (instance) üzerinden eğitilen sistemimiz, <span style='color: var(--accent); font-weight: 700;'>%83.0</span> gibi yüksek irtifa için oldukça iddialı bir mAP50 skoruyla sahada (deploy) kullanıma hazır hale geldi."><strong>Performans Karnesi:</strong> 58.000'den fazla doğru hedef tahmini (instance) üzerinden eğitilen sistemimiz, <span style="color: var(--accent); font-weight: 700;">%83.0</span> gibi yüksek irtifa için oldukça iddialı bir mAP50 skoruyla sahada (deploy) kullanıma hazır hale geldi.</li>
        </ul>

        <h3 style="color: var(--text); font-family: var(--font-head); margin-top: 2.5rem; margin-bottom: 1rem; font-size: 1.5rem;" data-tr="Gelecek Adımı (Termal Doğrulama)" data-en="Next Step (Thermal Verification)">Gelecek Adımı (Termal Doğrulama)</h3>
        <p data-tr="RGB kamera üzerinden yaptığımız bu görsel tespiti %100'e yaklaştırmak için FLIR Lepton 3.5 termal sensör verilerini kullanmayı planlıyoruz. Böylece yapay zekanın &quot;insan&quot; dediği hedefleri, 25°C-40°C arası ısı imzalarıyla eşleştirerek kesin &quot;canlı&quot; onayı alabileceğiz.">RGB kamera üzerinden yaptığımız bu görsel tespiti %100'e yaklaştırmak için FLIR Lepton 3.5 termal sensör verilerini kullanmayı planlıyoruz. Böylece yapay zekanın "insan" dediği hedefleri, 25°C-40°C arası ısı imzalarıyla eşleştirerek kesin "canlı" onayı alabileceğiz.</p>

        <div style="background: rgba(174, 226, 255, 0.2); border-left: 4px solid var(--accent); padding: 1.5rem 2rem; border-radius: 0 var(--radius) var(--radius) 0; margin-top: 2.5rem;">
          <p style="margin: 0; font-size: 1.1rem;" data-tr="<strong>Özetle:</strong> TULPAR-FF görüntü işleme birimi, donanım kaynaklarını en verimli şekilde kullanacak, yanlış alarm oranını sıfıra indirecek ve görev alanına girdiği an hedefini şaşmadan bulacak olgun bir otonom tespit mimarisine sahiptir."><strong>Özetle:</strong> TULPAR-FF görüntü işleme birimi, donanım kaynaklarını en verimli şekilde kullanacak, yanlış alarm oranını sıfıra indirecek ve görev alanına girdiği an hedefini şaşmadan bulacak olgun bir otonom tespit mimarisine sahiptir.</p>
        </div>

      </div>
    </div>
  </section>''', content, flags=re.DOTALL)

with open('blog-yolo11.html', 'w', encoding='utf-8') as f:
    f.write(content)
