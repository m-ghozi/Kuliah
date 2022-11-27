import re 

listKota = [
    'Padang', 'Payakumbuh', 'Riau','Pekanbaru'
]

listHurufVokal = [
    'a', 'i', 'u', 'e', 'o'
]

for kota in listKota:
    print('[' + kota + ']')

    for vokal in listHurufVokal: 
     print('-->', re.sub('[aiueo]', vokal, kota))