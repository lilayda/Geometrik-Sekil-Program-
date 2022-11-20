print('''Geometrik Şekil Hesaplama''')
print('Hesaplamak istediğiniz şekli seçiniz.')
print('Seçenekler:Dörtgen\n           Üçgen')
k = input('Seçiminiz:')

if k == 'Dörtgen':
    print('4 kenar giriniz.')
    a = int(input('1.kenar:'))
    b = int(input('2.kenar:'))
    c = int(input('3.kenar:'))
    d = int(input('4.kenar:'))
    if (a==b and c==d and a==c):
        print('Belirlediğiniz şekil bir kare.')
    else:
        print('Belirlediğiniz şekil sıradan bir dörtgen.')
elif (k=='Üçgen'):
    print('3 kenar giriniz.')
    x = int(input('1.kenar:'))
    y = int(input('2.kenar:'))
    z = int(input('3.kenar:'))
    if (x==y and x==z and y==z):
        print('Belirlediğiniz şekil bir eşkenar üçgen.')
    elif (x==y and not(y==z)):
        print('Belirlediğiniz şekil bir ikizkenar üçgen.')
    elif (x==y and not(x==z)):
        print('Belirlediğiniz şekil bir ikizkenar üçgen.')
    elif (x==z and not(x==y)):
        print('Belirlediğiniz şekil bir ikizkenar üçgen.')
    elif (x+y<z or x+z<y or y+z<x):
        print('Bu bir üçgen belirtmiyor.')
    elif (abs(x-y)>z or abs(x-z)>y or abs(y-z)>x):
        print('Bu bir üçgen belirtmiyor.')