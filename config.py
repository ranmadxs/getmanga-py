'''
Created on 17-03-2014

@author: esanchez
'''

#http://submanga.com/claymore/completa
#http://esmangaonline.com/alive/
from model.bean import Manga
CONST_PATH='/media/Shampoo/Manga/'
CONST_FILE_LOG = 'logs.csv'
esmangaonline = "esmangaonline.com"
eshentaionline = "eshentaionline.com"
submanga = "submanga.com"
mangaCovers="http://manga.joentjuh.nl/series/%s/"
mangas = {
    "zetman2"           : Manga("zetman", submanga),
    "zetman"            : Manga("zetman", esmangaonline, (mangaCovers%"42")),
    "liar_game"         : Manga("liar_game", submanga, (mangaCovers%"3296")),
    "wolf_guy"          : Manga("wolf_guy", submanga, (mangaCovers%"40128")),
    "dorohedoro"        : Manga("dorohedoro", esmangaonline, (mangaCovers%"209")),
    "dorohedoro2"       : Manga("dorohedoro", submanga, (mangaCovers%"209")),
    "Doubt"             : Manga("Doubt", submanga),
    "shingeki_no_kyojin": Manga("shingeki_no_kyojin", esmangaonline, (mangaCovers%"47446")),
    "noblesse"          : Manga("noblesse", esmangaonline),
    "noblesse2"         : Manga("noblesse", submanga),
    "majutsu"           : Manga("to_aru_majutsu_no_index", esmangaonline),
    "holy_knight"       : Manga("holy_knight", esmangaonline),
    "pandora"           : Manga("pandora-hearts", esmangaonline, (mangaCovers%"9709")),
    "claymore"          : Manga("claymore", esmangaonline),
    "claymore2"         : Manga("claymore", submanga),
    "allumage"          : Manga("allumage", esmangaonline),
    "allKill"           : Manga("All_you_need_is_Kill", submanga),
    "dance"             : Manga("dance_in_the_vampire_bund", esmangaonline),
    "berserk"           : Manga("berserk", esmangaonline, (mangaCovers%"88")),
    "berserk2"          : Manga("berserk", submanga),
    "gasuki"            : Manga("Me+gustas+Onii-chan!", eshentaionline),
    "slam-dunk"         : Manga("slam-dunk", esmangaonline, (mangaCovers%"90")),
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
}

letras = map(chr, range(97, 101))
