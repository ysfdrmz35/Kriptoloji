text = input("\nÇevirilecek Metin : ")
alphabet = "abcçdefgğhıijklmnoöprsştuüvyz "
ttext = ''
for c in text:
    if c in alphabet:
        ttext += alphabet[alphabet.index(c) + 3]
print("\nÇevrilmiş Metin : " + ttext)