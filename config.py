'''
Created on 17-03-2014

@author: esanchez
'''
#TODO: Debo arreglar el programa que baja las caraatulas por que el josting murio y ahora hay uno nuevo

#http://es.mangahere.co/manga/freezing/
#http://bato.to

#http://submanga.com/claymore/completa
#http://esmangaonline.com/alive/
from model.bean import Manga
CONST_PATH_SRC = '/home/esanchez/lenguajes/python/wget'
CONST_PATH='/media/Shampoo/Manga/'
CONST_FILE_LOG = 'logs.csv'
CONST_EXCLUSIONS_FILE = "exclusions.txt"
CONST_INFO_FILE = "info.txt"
CONST_MANGA_CFT_FILE = "/home/esanchez/lenguajes/python/wget/list_manga.cfg"

volumenurl = "manga.animea.net"
#infourl = "https://www.mangaupdates.com/series.html?id=%s"

# MANGA SERVERS

esmangaonline = "esmangaonline.com"
eshentaionline = "eshentaionline.com"
submanga = "submanga.com"
esmangahere = "es.mangahere.co"
esmanga = "esmanga.com"

## Nuevo servidor -> http://esmanga.com

MANGA_DEFAULT_SERVER = esmangahere

#mangaCovers="http://manga.joentjuh.nl/series/%s/" -> ya no sirve
#mangaCovers=http://mcd.iosphe.re/ -> esta es la nueva y mantiene los mismos ids parece
#http://mcd.iosphe.re/manga/42898/   tiene api json XDDD     =>   http://mcd.iosphe.re/api/v1/series/%s/

# por ejemplo http://mcd.iosphe.re/manga/1037/
mangas = {    
    "Doubt"             : Manga("Doubt", submanga),
    "shingeki_no_kyojin": Manga("shingeki_no_kyojin", esmangaonline, "47446"),    
    "gasuki"            : Manga("Me+gustas+Onii-chan!", eshentaionline),
    "pandora"           : Manga("pandora-hearts", esmangaonline, "9709"),
    "alive"             : Manga("alive", esmangaonline),
    "uzumaki"           : Manga("uzumaki", esmangaonline),
    "uzumaki2"          : Manga("uzumaki", submanga),
    "priest"            : Manga("priest", esmangaonline),
    "yahari"            : Manga("Yahari_Ore_no_Seishun_Love_Come_wa_Machigatteiru", submanga),
    "is"                : Manga("is", esmangaonline, "3599", "is.html"),
    "terraFormars"      : Manga("TERRA_FORMARS", submanga),    
    "alita"             : Manga("battle-angel-alita", esmangaonline, "2157", "battle-angel-alita.html"),
    "dance"             : Manga("dance_in_the_vampire_bund", esmangaonline),
    "allumage"          : Manga("allumage", esmangaonline),    
    "berserk"           : Manga("berserk", esmangaonline, "88"),
    "berserk2"          : Manga("berserk", submanga),    
    "nausica"           : Manga("nausica", submanga, "4565", "nausicaa-of-the-valley-of-the-wind.html"),
    "torre_de_dios"     : Manga("torre_de_dios", esmangahere),
        
    "sun_ken_rock2"      : Manga("Sun-Ken_Rock", submanga, 8996, "sun-ken-rock.html"),    
    "sun_ken_rock3"      : Manga("Sun-Ken+Rock", esmangaonline, 8996, "sun-ken-rock.html"),
    
    
    #"ant"               : Manga("apocalypse_no_toride", esmangahere, "68982", "apocalypse-no-toride.html"),
    #"ant2"              : Manga("apocalypse_no_toride", submanga, "68982", "apocalypse-no-toride.html"),
    #"btooom"            : Manga("btooom", esmangahere, "45009", "btooom-.html"), 
    #"zetman2"           : Manga("zetman", submanga, "42", "zetman.html"),
    #"zetman"            : Manga("zetman", esmangaonline, "42", "zetman.html"),
    #"i_am_a_hero"       : Manga("i_am_a_hero", submanga, "43241", "i-am-a-hero.html"),
    #"i_am_a_hero2"      : Manga("i_am_a_hero", esmangahere,"43241", "i-am-a-hero.html"),
    #"i_am_a_hero3"      : Manga("i_am_a_hero", esmangaonline, "43241", "i-am-a-hero.html"),
    #"liar_game"         : Manga("liar_game", submanga, "3296", "liar-game.html"),
    #"liar_game2"        : Manga("liar_game", esmangahere, "3296", "liar-game.html"),
    #"dorohedoro"        : Manga("dorohedoro", esmangaonline, "209", "dorohedoro.html"),
    #"dorohedoro2"       : Manga("dorohedoro", submanga, "209", "dorohedoro.html"),    
    #"noblesse"          : Manga("noblesse", esmangaonline, 49160, "noblesse.html"),
    #"noblesse2"         : Manga("noblesse", submanga, 49160, "noblesse.html"),        
    #"claymore"          : Manga("claymore", esmangaonline, "1037", "claymore.html"),
    #"claymore2"         : Manga("claymore", submanga, "1037", "claymore.html"),
    #"claymore3"         : Manga("claymore", esmangahere, "1037", "claymore.html"),    
    #"sun_ken_rock"      : Manga("sun_ken_rock", esmangahere, 8996, "sun-ken-rock.html"),
    #"holy_knight"       : Manga("holy_knight", esmangahere, "68740", "holy-knight.html"),
    #"mushishi"          : Manga("mushishi", esmangahere, 452, "mushishi.html"),
    #"slam_dunk"         : Manga("slam_dunk", esmangahere, 90, "slam-dunk.html"), 

}

def readFile(archivo):
    lines = []
    try:
        lines = [line.strip() for line in open(archivo)]
    except IOError:
        None
    return lines

listMangaFile = readFile(CONST_MANGA_CFT_FILE)
#print listMangaFile
for mangaFileList in listMangaFile:
    mangaArray = []    
    mangaFileArray = mangaFileList.split("\t")
    for mangaField in mangaFileArray:
        if mangaField.strip() != "":
            mangaArray.append(mangaField)  
    if mangaArray.__len__() < 3:        
        mangaArray[mangaArray.__len__():3] = [None] * (3 - mangaArray.__len__())
    mangaCode = mangaArray[0].strip()
    mangaObj = Manga(mangaCode, MANGA_DEFAULT_SERVER, mangaArray[1], mangaArray[2])
    #print mangaObj
    mangas[mangaCode] = mangaObj

letras = map(chr, range(97, 101))