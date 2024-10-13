import wget
import os
from zipfile import ZipFile
import requests
from lxml.html import fromstring
link = 'https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip'
if not os.path.isdir('steam'):
    os.mkdir('steam')
    wget.download(link, 'steam')
    with ZipFile('steam\\steamcmd.zip') as arquivo:
        arquivo.extractall('steam')
    os.remove('steam\\steamcmd.zip')
    print()
link_colecao = 'https://steamcommunity.com/sharedfiles/filedetails/?id='
colecao = str(input('Digite o id da coleção de mods: '))
link_colecao += colecao
page = fromstring(requests.get(link_colecao).content)
mods = page.find_class('collectionChildren')[0].find_class('collectionItem')
game_id = mods[0].find_class('collectionItemDetails')[0].find_class('workshopItemAuthor')[0].find_class('workshopItemAuthorName')[0]
game_id = game_id.find('a').get('href').split('=')[1]
steam = ['login anonymous\n']
for mod in mods:
    steam.append(f'workshop_download_item {game_id} '+mod.get('id').split('_')[1]+'\n')
steam.append('quit')
with open('modzin.txt', 'w') as arquivo:
    arquivo.writelines(steam)
os.system('steam\\steamcmd.exe +runscript ..\\modzin.txt')
os.remove('modzin.txt')
os.startfile(f'steam\\steamapps\\workshop\\content\\{game_id}')