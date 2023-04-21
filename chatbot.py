import random
import time

def greet():
    print("Merhaba, benim adım Chat Bot. Size nasıl yardımcı olabilirim?")
    print("Yazmayı bırakmak isterseniz 'çıkış' yazabilirsiniz.")
    print("-" * 50)

def get_date():
    t = time.localtime()
    return time.strftime("%d/%m/%Y", t)

def get_time():
    t = time.localtime()
    return time.strftime("%H:%M:%S", t)

def say_bye():
    print("Görüşmek üzere, iyi günler!")
    exit()

def chat():
    name = input("Adınız nedir? ")
    print(f"Hoş geldiniz, {name}!")
    print(f"Bugün {get_date()} tarihi, saat {get_time()}. Nasıl yardımcı olabilirim?")

    while True:
        message = input("> ")
        message = message.lower()
        if message in ["merhaba", "selam", "hey"]:
            print("Merhaba, nasıl yardımcı olabilirim?")
        elif "hava" in message:
            print("Hava durumu hakkında hangi şehirde bilgi almak istersiniz?")
        elif "ankara" in message:
            print("Ankara'da bugün hava açık ve sıcaklık 30 derece.")
        elif "istanbul" in message:
            print("İstanbul'da bugün hava kapalı ve sıcaklık 25 derece.")
        elif "izmir" in message:
            print("İzmir'de bugün hava parçalı bulutlu ve sıcaklık 27 derece.")
        elif "nasılsın" in message:
            print("İyiyim, teşekkür ederim. Ya siz?")
        elif "iyiyim" in message:
            print("Ne güzel, bir şeye ihtiyacınız var mı?")
        elif "teşekkür ederim" in message:
            print("Rica ederim, nasıl yardımcı olabilirim?")
        elif message in ["şaka yap", "espri yap"]:
            jokes = ["Neden tavşanlar havuç yer? Çünkü tavşanların gözü patatesli salatada!", 
                     "Ben arkadaşıma bir güvercin verdim, o da bana bir kızıl ördek. İkinci adımda büyük bir hata yaptığımı anladım.", 
                     "Bir adam içeri girer ve 'Bira verin' der. Diğer adam da 'Aynen, bana da getir.' der.",
                    "İki balık yüzüyormuş. Birincisi 'Su sıcak bugün, değil mi?' diye sormuş diğeri de 'Aaa! Kıyafetin!' demiş.",
                    "Bir atom bir bara girer ve bardaki diğer atomlara sorar: 'Benim elektron kaybettiğimi gördünüz mü?' Diğer atomlar cevap verir: 'Evet, sen artık pozitif bir atom oldun.' Atom ise yanıt verir: 'Kötü bir günüm var, negatif kalmak istiyordum.'",
"Bir programcı bar karşısına geçtiğinde, 'git commit' demek yerine 'gin tonic' diyor."  ]
            joke = random.choice(jokes)
            print(joke)
        elif "çıkış" in message:
            say_bye()
        else:
            print("Ne demek istediğinizi tam olarak anlamadım. Başka bir şeyler söyleyebilir misiniz?")

greet()
chat()
