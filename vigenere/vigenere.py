while(True):
    filename = input("\nLütfen çevirmek istediğiniz dosyanın ismini giriniz : ")
    try:
        text = open("C:/Users/YUSUF/Desktop/" + filename, "r")
        break
    except FileNotFoundError:
        print("\nDosya bulunamadı tekrar deneyiniz...")
text,key = str(text.read()),input("Lütfen şifreleme için anahtar sözcük giriniz : ")
alfabe,çeviri,tekrar = "abcçdefgğhıijklmnoöprsştuüvyzabcçdefgğhıijklmnoöprsştuüvyz","",0
for c in text:
    if c in alfabe:
        çeviri += alfabe[alfabe.index(c) + alfabe.index(key[tekrar] )+ 1]
    else:
        çeviri += c
    tekrar += 1
    if tekrar == len(key):
        tekrar = 0
print(çeviri)