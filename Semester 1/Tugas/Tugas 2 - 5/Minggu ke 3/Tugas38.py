listhero = [
    'layla', 'kagura', 'hayabusa', 'lancelot', 'tigreal',
    'odette', 'karrie', 'jawhead'
]
HeroYangDicari = input('Ketik nama hero yang kamu cari: ')
for i, hero in enumerate(listhero):
# kita ubah katanya ke lowercase agar
# menjadi case insensitive
    if hero.lower() == HeroYangDicari.lower():
        print('Hero yang anda cari berada pada indeks', i)
        break
else:
    print('Maaf, Hero yang anda cari tidak ada')