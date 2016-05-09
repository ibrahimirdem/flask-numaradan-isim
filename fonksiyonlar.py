def numarami(deger):
    deger = str(deger)
    sayilar = "0123456789"
    sonuc = 0
    if len(deger) == 10:
        for i in deger:
            if i not in sayilar:
                sonuc=sonuc+1
        if sonuc > 0:
            return False
        else:
            return True
    else:
        return False
def numara_denetim(numara):
    import re
    import mechanize
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    cookies = mechanize.CookieJar()

    browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US)     AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
    browser.open("http://m.facebook.com/")
    browser.select_form(nr=0)
    browser.form['email'] = 'irdem1'
    browser.form['pass'] = '05357007448777'
    response = browser.submit()


    kaynak = browser.open("http://m.facebook.com/privacy/touch/block/?refid=31").read()
    browser.select_form(nr=1)
    browser.form['q'] = str(numara)
    response = browser.submit()
    kaynak =  response.read()

    if 'bulunamad' in kaynak:
        return [False,"",""]
        #print("[!] Sonuc Bulunamadi"+str(numara))
        #sayi=10
    else:
        sonuclar = re.findall('<span class="bl">(.*?)</span></a>.*?<a href="/privacy/touch/block/confirm/\?bid=(.*?)">Engelle</a>',kaynak)
        for i in sonuclar:
            isim = i[0].decode('utf-8')
            id = i[1].decode('utf-8')
            return [True, isim, id]
            #print("Ad-Soyad :"+i[0]+"\nLink : http://facebook.com/profile.php?id="+i[1]+"\n"+str(numara))
            #print("-----------------------------------------------")
