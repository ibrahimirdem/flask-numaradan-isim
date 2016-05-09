# -*- coding: utf-8 -*-
from flask import Flask, render_template,request,url_for,redirect,session
import fonksiyonlar

app = Flask(__name__)

 #Anasayfayı açtığımızda karşımıza çıkacak kısımla ilgili olan kısımdır.
 #arama.html düzenleyip ekrana getirmesini söyledik.
@app.route('/')
def home():
    return render_template('arama.html')

#İşlem yapılan kısım burası olacak.
@app.route('/sonuc', methods=["GET","POST"])
def sonuc():
    if request.method == "POST":
        #numara isimli inputtan gelen tel. numarası alınıyor.
        gelen = request.form["numara"]
        #fonksiyonlar dosyasındaki numarami fonksiyonu ile gelen numaranın uygun olup olmadığına bakılıyor.
        if fonksiyonlar.numarami(gelen)== True:
            #Alınan numara numara_denetim() fonksiyonu içinde denetleniyor ve bize sonuçları sonuc değişkenine aktarılıyor.
            sonuc = fonksiyonlar.numara_denetim(gelen)
            #Sonuc değişkeni bize [dogruluk=True-False ,isim,facebook-id] şeklinde bir sonuc veriyor.
            #Doğruluk:Numarayla eşleşen bir hesap varsa True yoksa False sonucu veriyor.
            return render_template('sonuc.html', dogruluk=sonuc[0], isim=sonuc[1], id=sonuc[2])
            #return "Doğru Numara"
        else:
            #Eğer fonksiyonlar.numarami() ile kontrol edilen numara istenilen şekilde girilmediyse home fonksiyonuna yani anasayfaya yönlendiriliyor.
            return redirect(url_for('home'))
    else:
        #Eğer post verisi gelmediyse anasayfaya yönlendir.
        #Bu sayade kişi localhost:500/sonuc olarak direkt sayfaya girmeye çalışırsa anasayfaya yönlendirilir.
        return redirect(url_for('home'))

if __name__== "__main__":
    app.run(debug=True) #true debug açık halde tutar. hatalarımızı görmemizi sağlar. development ortamınd
