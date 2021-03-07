from urllib.request import urlopen
import time #dastur ishlash vaqtini tekshirish uchun

#ranglar va boshqa belgilarning kodlari
oq = '\033[1;97m'
yashil = '\033[1;32m'
osmonrang_uzur_boshqacha_nomlay_olmadim = '\033[1;31m'
sariq = '\033[1;33m'
end = '\033[1;m'  #nimagaligini bilmayman, lekin shu belgisiz dastur ishlamaydi;)
info = '\033[1;33m[!]\033[1;m'
savol =  '\033[1;34m[?]\033[1;m'
minus = '\033[1;31m[-]\033[1;m'
plyus = '\033[1;32m[+]\033[1;m'


print('''%s
\    /  __    __    |__|    __    __
 \/\/  |__|  |__|   |  |   |__|  |__|%s\n'''% (sariq,end)) #dasturning reklama afishasi va uning qanday rangda ko`rinishi
print("____________________________________")

'''Xohlasangiz 20-satrda yozilgan kodning o`zini aktivlashtirib, 22 va 23-satrlarni o`chirib tashlang
yoki # belgisi bilan kommentariya sifatida belgilab qo`ying. 
Ikkala holatda ham dastur bir xil ishlaydi'''
#url = "https://google.com" 

url1 = str(input(print("html kodini olmoqchi bo`lgan saytning nomini kiriting (masalan, google.com, aytgancha None so`ziga e'tibor bermang;) ):")))
url = 'https://' + url1 #foydalanuvchilarga qulay bo`lishi uchun shunday qilishga to`g`ri keldi. Shunchaki ular 'https://website.com' deb kiritib yurmasliklari uchun
time1 = time.time()
page = urlopen(url) #manzili kiritilgan saytni ochish

html = page.read().decode("utf-8")  #sayt kodini terminalda ochish mumkin bo`lishi uchun 
print(html)
time2 = time.time()
print("Dastur ushbu saytni ochishga hamda qayta ishlashga ", time2-time1, "s vaqt sarfladi!")
