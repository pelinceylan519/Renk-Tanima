from PIL import Image

img = Image.open('C:\\Users\\HP\\Desktop\\Yazılım\\Kırmızı Renk Tanıma\\Resimler\\Resim2.jpg')
renk = img.convert('RGB')
kirmizi_varmi = False

for yatay in range (img.width):
    for dikey in range (img.height):
        krmizi, yesil, mavi = renk.getpixel((yatay, dikey))
        if krmizi > 150 and yesil < 100 and mavi < 100:
            kirmizi_varmi = True
            break

if kirmizi_varmi:
    print("Resimde kirmizi renk var.") 

else:
    print("Resimde kirmizi renk yok.")
