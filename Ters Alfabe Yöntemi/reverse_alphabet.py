text = input("\nÇevirilecek Metin : ")
alphabet = "abcçdefgğhıijklmnoöprsştuüvyz "
ttext = ''
for c in text:
    if c in alphabet:
        ttext += alphabet[28 - alphabet.index(c)]
print("\nÇevrilmiş Metin : " + ttext)