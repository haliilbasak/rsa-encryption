from Crypto.Util.number import getPrime, inverse

# RSA Anahtar Üretimi
def generate_rsa_keys(bits=1024):
    # Rastgele iki büyük asal sayı oluşturma
    p = getPrime(bits)
    q = getPrime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Genel anahtar (e) ve özel anahtar (d) hesaplama
    e = 65537  # Sık kullanılan genel anahtar değeri
    d = inverse(e, phi)
    return (e, n), (d, n)

# RSA Şifreleme Fonksiyonu
def rsa_encrypt(message, public_key):
    e, n = public_key
    # Mesajı şifrelenmiş bir listeye dönüştür
    return [pow(ord(char), e, n) for char in message]

# RSA Çözme Fonksiyonu
def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    # Şifrelenmiş listeyi tekrar metne dönüştür
    return ''.join(chr(pow(char, d, n)) for char in ciphertext)

# Örnek Kullanım
if __name__ == "__main__":
    # Anahtar çiftlerini oluştur
    public_key, private_key = generate_rsa_keys(1024)

    # Şifrelenecek mesaj
    message = "Merhaba, RSA!"

    # Mesajı şifrele
    ciphertext = rsa_encrypt(message, public_key)
    print("Şifreli Mesaj:", ciphertext)

    # Mesajı çöz
    decrypted_message = rsa_decrypt(ciphertext, private_key)
    print("Çözülen Mesaj:", decrypted_message)
