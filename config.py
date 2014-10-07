'''
Created on 17-03-2014

@author: esanchez
'''

#http://bato.to

#http://submanga.com/claymore/completa
#http://esmangaonline.com/alive/
from model.bean import Manga
CONST_PATH_SRC = '/home/esanchez/lenguajes/python/wget'
CONST_PATH='/media/Shampoo/Manga/'
CONST_FILE_LOG = 'logs.csv'
CONST_EXCLUSIONS_FILE = "exclusions.txt"
CONST_INFO_FILE = "info.txt"

volumenurl = "manga.animea.net"
infourl = "https://www.mangaupdates.com/series.html?id=%s"

esmangaonline = "esmangaonline.com"
eshentaionline = "eshentaionline.com"
submanga = "submanga.com"
esmangahere = "es.mangahere.co"
mangaCovers="http://manga.joentjuh.nl/series/%s/"
mangas = {
    "gantz"             : Manga("gantz", submanga, (mangaCovers%"208"), "gantz.html", (infourl%"208")),
    "dragon_head"       : Manga("dragon_head", esmangahere, (mangaCovers%"384"), "dragon-head.html", (infourl%"384")),
    "dragon_head2"      : Manga("dragon_head", esmangaonline, (mangaCovers%"384"), "dragon-head.html", (infourl%"384")),
    "dragon_head3"      : Manga("dragon_head", submanga, (mangaCovers%"384"), "dragon-head.html", (infourl%"384")),
    "ant"               : Manga("apocalypse_no_toride", esmangahere, (mangaCovers%"68982"), "apocalypse-no-toride.html", (infourl%"68982")),
    "ant2"              : Manga("apocalypse_no_toride", submanga, (mangaCovers%"68982"), "apocalypse-no-toride.html", (infourl%"68982")),
    "btooom"            : Manga("btooom", esmangahere), 
    "zetman2"           : Manga("zetman", submanga, (mangaCovers%"42"), "zetman.html"),
    "zetman"            : Manga("zetman", esmangaonline, (mangaCovers%"42"), "zetman.html"),
    "i_am_a_hero"       : Manga("i_am_a_hero", submanga, (mangaCovers%"43241"), "i-am-a-hero.html"),
    "i_am_a_hero2"      : Manga("i_am_a_hero", esmangahere, (mangaCovers%"43241"), "i-am-a-hero.html"),
    "i_am_a_hero3"      : Manga("i_am_a_hero", esmangaonline, (mangaCovers%"43241"), "i-am-a-hero.html"),
    "liar_game"         : Manga("liar_game", submanga, (mangaCovers%"3296"), "liar-game.html"),
    "liar_game2"        : Manga("liar_game", esmangahere, (mangaCovers%"3296", "liar-game.html")),
    "dorohedoro"        : Manga("dorohedoro", esmangaonline, (mangaCovers%"209")),
    "dorohedoro2"       : Manga("dorohedoro", submanga, (mangaCovers%"209")),
    "Doubt"             : Manga("Doubt", submanga),
    "shingeki_no_kyojin": Manga("shingeki_no_kyojin", esmangaonline, (mangaCovers%"47446")),
    "noblesse"          : Manga("noblesse", esmangaonline),
    "noblesse2"         : Manga("noblesse", submanga),
    "majutsu"           : Manga("to_aru_majutsu_no_index", esmangaonline),
    "holy_knight"       : Manga("holy_knight", esmangahere, None, "holy-knight.html", (infourl%"68740")),
    "pandora"           : Manga("pandora-hearts", esmangaonline, (mangaCovers%"9709")),
    "claymore"          : Manga("claymore", esmangaonline),
    "claymore2"         : Manga("claymore", submanga),
    "allumage"          : Manga("allumage", esmangaonline),    
    "dance"             : Manga("dance_in_the_vampire_bund", esmangaonline),
    "berserk"           : Manga("berserk", esmangaonline, (mangaCovers%"88")),
    "berserk2"          : Manga("berserk", submanga),
    "gasuki"            : Manga("Me+gustas+Onii-chan!", eshentaionline),
    "slam-dunk"         : Manga("slam-dunk", esmangaonline, (mangaCovers%"90"), "slam-dunk.html"),
    "alive"             : Manga("alive", esmangaonline),
    "uzumaki"           : Manga("uzumaki", esmangaonline),
    "uzumaki2"          : Manga("uzumaki", submanga),
    "parasyte"          : Manga("parasyte", esmangaonline),
    "priest"            : Manga("priest", esmangaonline),
    "yahari"            : Manga("Yahari_Ore_no_Seishun_Love_Come_wa_Machigatteiru", submanga),
    "parasyte2"         : Manga("parasyte", submanga),
    "is"                : Manga("is", esmangaonline, (mangaCovers%"3599")),
    "is"                : Manga("is", esmangaonline, (mangaCovers%"3599")),
    "terraFormars"      : Manga("TERRA_FORMARS", submanga),
    
    #"allKill"           : Manga("All_you_need_is_Kill", submanga, None, "all-you-need-is-kill-2.html"),    
    #wolf_guy"          : Manga("wolf_guy", submanga, (mangaCovers%"40128"), "wolf-guy-ookami-no-monshou.html", (infourl%"40128")),
    #"wolf_guy2"         : Manga("wolf_guy", esmangahere, (mangaCovers%"40128"), "wolf-guy-ookami-no-monshou.html", (infourl%"40128")),

}

letras = map(chr, range(97, 101))