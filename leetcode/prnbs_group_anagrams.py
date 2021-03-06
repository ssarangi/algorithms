# class Solution(object):
#     def __init__(self):
#         self.alpha_pos = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7,
#                           "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14,
#                           "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21,
#                           "v":22, "w":23, "x":24, "y":25, "z":26}
#         self.groups = {}

#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         for word in strs:
#             hash = ''.join(sorted(word))
#             if hash not in self.groups:
#                 group = [word]
#                 self.groups[hash] = group
#             else:
#                 self.groups[hash].append(word)

#         result = []
#         for key in self.groups:
#             self.groups[key].sort()
#             result.append(self.groups[key])
#         return result


# if __name__ == "__main__":
#     soln = Solution()
#     ls = ["incentive","countersink","pickaxing","explicit","unethical","seoul","gyrates","dismounting","dartboard","socialism","sissiest","radiotherapist","sprawl","hems","raggedier","conscripted","repealed","implanted","coverage","traitorous","barmaid","pointier","huntress","summers","finnish","mouthed","mamore","lemur","osteoporosis","frowziest","sop","comical","speedup","oasis","peon","testers","stances","chuckles","childes","consensuses","rastafarian","battlement","christies","urbanized","penitence","replenishment","disperse","kibosh","combatting","repealing","guise","grassiest","grafts","waddle","pigsties","moneymaking","polite","reprogramming","audaciously","gorier","blaze","yaqui","racially","inc","reupholstering","fez","lemaitre","nineties","pedal","deferred","tranquil","surveyor","narrow","hopper","solemnize","federate","trisecting","cravat","lille","biography","land","jazzing","rhomboids","nudes","mundanely","greenbacks","chattel","deceleration","devoting","itemizing","routing","jukebox","passkey","infants","prerecorded","fuzzing","gandhi","roseate","bandit","prong","bowels","bounciest","misdeeds","unseemliness","emceed","later","hailed","crotchet","steepness","jot","improves","eucharistic","natalia","exalt","performers","predictor","voyeurism","fedex","activate","crypt","magics","treats","viewed","chauffeur","ladybug","peppiest","seismic","microscopes","liners","wraps","footman","tape","daubers","aerial","sparer","politic","shamed","decal","ayrshire","ruggeder","washcloths","neurologists","singsong","kaitlin","conn","monopolizes","sunroof","zonked","overall","celsius","fins","caparison","imus","enfranchises","microns","promulgates","aspartame","fails","decamps","spiciness","impieties","starring","receded","skying","suetonius","pornographers","intellectualized","truckled","abdications","openness","principally","sellers","complaining","jeopardizing","concerto","fibula","cliffs","aorta","inhale","transgressions","copywriter","understands","coccis","disperses","fraying","strengths","macaulay","mitigation","competences","ides","linked","tawnier","hallucinate","dairymen","puffier","matchless","wheeling","drily","nephews","clandestinely","tsingtao","disarraying","headier","experts","yippee","repellent","tributary","clannish","dumpsters","genealogies","ballooned","denouements","hymned","length","sasses","uncontrollably","fortune","wastefully","overproducing","sickening","headboard","burrs","prohibits","keogh","outs","lamer","repressed","rowdyism","transgressed","euros","amenity","garfunkel","rather","noseys","lampoons","raja","impermanence","heaters","shakespeareans","judiciaries","tweaked","extrapolations","succeeded","jowls","vociferation","roadways","herb","inactivity","registrars","checks","deservedly","heehaws","apologetics","fatness","aced","promote","atriums","deidre","redound","litterbug","barehanded","scheduled","flakiest","twirler","graduated","coccus","gadfly","unforeseeable","emendation","woodsman","wiriest","tangelo","weakening","intimidating","sternness","reiteration","wicca","heresies","inches","encodes","sidebar","starking","wastelands","pepsi","emigrate","stuttgart","shindigs","pansy","chintzy","limbo","disbarred","gallivant","hallmarked","respiratory","eminences","unabated","affirms","twinned","wordiness","installing","donn","westerly","interfaces","benton","mussy","identical","sulfates","starvings","woodwork","hyphenated","catechizing","transition","dramatist","demilitarize","buber","spoonful","laconic","undervaluing","inestimably","severer","improvidence","stoneware","cholera","peru","rearm","recluses","diaz","tablespoonsful","sandals","cinderella","insubordination","sires","stern","jeremiah","snowbound","ramifies","lexicographer","skimpiest","predetermining","lapidary","dentists","upbeats","marketplace","ploughs","esteem","miserably","overreaction","unlikelihood","kinswoman","averts","remonstrating","asinine","amortize","wasps","coal","tenderfoot","subplot","coyotes","sauntering","rices","fraughts","decoded","millipedes","knocking","homework","furor","expansionists","j","emergency","sharon","provisoes","president","assuaging","curtail","indigestion","liming","cryptozoic","auguring","indenture","magisterially","groped","ensue","steaming","mutinous","incomplete","yuletide","nomenclatures","hundredth","jimmies","irk","common","wetly","volley","summary","obsequies","granola","forests","allege","informal","shapeless","earplugs","disunite","insinuations","junked","riverbeds","georgian","brushed","sequenced","bucketfuls","spiel","humors","screwed","capitulating","downturns","intimidates","refueling","mingled","arisen","dragnet","aftereffects","practised","obduracy","canon","penning","inflammatory","wisher","actuate","kari","actuating","reupholstered","successes","inborn","canvasbacks","incapacitated","aristocratic","britt","lazying","hymnals","tyroes","tamper","graduate","franc","seasons","pompom","throeing","deviate","leveling","inaccurate","impaling","trouping","restoring","deduces","perforating","artie","alleghenies","crusader","rosemary","chastest","educational","caveatting","ablest","doorstepped","strange","eccentricities","sublimity","afire","humbugging","jots","ordinary","foyer","kayak","snake","wheal","dispensations","transponders","zing","pit","meowing","improved","crowd","nonfatal","epsilon","nodding","cyclones","imbibed","rebroadcasting","quibbles","moisturizes","zippy","braille","visaing","abetters","lurked","snafus","moppet","lemon","wifeliest","stuarts","boyish","reapportion","kneecaps","stymying","villagers","obscenity","bumble","zeroing","objectionably","connolly","memorial","clanging","gallstones","dibbled","outlasting","mendez","reproaching","antagonized","sisterhoods","hunchbacks","superimposed","siphon","professionally","spermicides","lebanon","facing","pierces","philosophically","mcdowell","rotated","tic","correspondents","nonplussed","litchi","ascots","millennial","booked","immunize","prefabricate","spumoni","odyssey","fey","bunched","olen","regularizing","superconductors","aside","infirmary","allaying","saturdays","caucasian","doreen","france","speeding","wretched","slovakia","chiselled","peseta","tho","gales","loincloths","shock","readers","boarder","entryway","toning","transitively","preponderances","internships","rating","pelleting","audition","amusement","theed","cocked","toddler","rusty","kinfolk","frames","gorgonzola","overrate","lightweight","bayous","populists","insensible","bandoliers","travelogs","tactically","weatherproofs","sleigh","develops","oxygenate","relaid","mimi","wheezier","chill","salween","theatre","vitalizes","nun","olives","offings","tricycling","tipper","kindly","bellies","sixteenths","ganglia","recombining","eastward","minestrone","fairgrounds","undelivered","scapula","breadth","groupie","ophelia","adrenaline","dork","autographing","watersides","sent","socks","somnolence","systematize","signings","rachmaninoff","santa","snacks","leno","spurs","heliotropes","silenced","roundhouses","illegitimacy","hedgehog","wet","depressed","eris","pure","pouncing","obtuseness","caulk","openly","kerosene","grille","buccaneers","oar","modals","playacts","shroud","plowshares","iciness","retort","jaunt","identities","mellower","redesigning","molest","forlorner","guacamole","cohan","refocus","dossier","interrogating","cants","diligence","stomps","enjoy","awe","loggerhead","csonka","inversions","den","lunged","alkaid","palming","delivers","proprietorship","groveler","choreographs","instals","merton","cyclops","augmentation","manipulated","nasal","trousseaux","critiques","arenas","stale","suspect","behoove","propose","cellulite","purification","leah","polestar","potato","gladlier","sunders","entreat","herbalist","filthier","skinflints","asseverating","insulted","mildly","modulate","charges","libyans","weekended","rodeos","allegedly","tarawa","valedictorians","spacy","spontaneously","yore","classify","centigrade","videoing","airdropping","dejection","pierce","imagined","isabel","reiterates","blazing","stuck","deceasing","netherlands","citric","tormented","monotoning","bestowals","betrayals","adoptions","scrolls","sex","idol","whaler","telephotos","conjugation","abductions","bundestag","disruptions","nouakchott","stuffiest","goodly","dissatisfying","anglicize","flowing","identifying","depots","stoicism","thessalonian","hundred","whetstone","defroster","headwaiter","feisty","inhibited","reamed","demonstrator","accursed","hector","interchanges","erotically","sportscaster","gentlewomen","teabag","smelts","disorganization","conveniently","maugham","hatchery","regards","arguably","govern","boulevards","niches","gristlier","obtrude","catharses","throughway","stoppered","drinkers","indeterminacy","vacuums","plainest","acuff","eases","defined","splurge","severing","griddles","thermoplastics","dilution","vinegary","straights","testament","sticks","shanghai","childproofing","clobbers","taco","castro","arrests","fetter","discomposing","timbres","wondrous","pullmans","amusements","telephonic","manning","inhabiting","finery","admires","defensively","fiord","incriminate","oust","collapse","deliquescent","bulwark","consciousness","roguery","beefburger","amounted","pheasants","archdioceses","vote","gujarati","forwards","waggling","tanned","liberalization","chap","finishing","catawba","anus","farina","butterflying","folks","crumple","criticize","unswerving","snack","gentrification","enthroning","drearies","marietta","farley","recede","incise","electrodes","dirac","corn","livest","coughs","noreen","rapscallion","codeine","acidly","confiscates","dislikes","administrators","valid","prep","legated","wherewithal","subjugating","wallabies","boning","creakiest","erotica","neophytes","drowses","bushmen","basis","regattas","melancholy","clubfeet","there","generalized","rotunding","condone","hemlines","bantered","vertebral","ruby","companions","postmarked","aping","finalized","prado","mutilations","partied","isiah","desk","calcines","agreeing","bode","cygnet","downsizing","naiads","preambled","recife","randall","gillespie","convalescent","victories","obsessed","leaders","strips","parmesan","germicide","clarion","pictograph","nutshells","bungalows","hagged","colosseum","ferraro","recapitulations","labored","acrostic","dynamics","bucked","betaking","pragmatically","gobbed","glossy","congresses","rewindable","trout","renovates","mattered","davenport","stenographer","nudism","deduced","unattributed","equally","wrestled","sequoia","measurable","lamb","babe","concourses","creamer","fascination","steroids","deplaned","germinated","progressed","swashbuckling","pools","officemax","brewers","banjul","thong","periodic","grub","typescript","lemurs","excreta","seeps","clearinghouses","isolating","particularized","thallium","waistcoat","misread","extensiveness","violations","insistent","zany","newses","predominate","enunciating","ultras","burlap","dowelled","elision","person","minneapolis","edification","endued","asseverates","meeter","iceberg","mexican","end","wale","veronese","ida","earshot","tunnels","debuting"]
#     print(soln.groupAnagrams(ls))

import random

def generate_strings(length, total_num_of_strings):
    chars = [chr(i + 97) for i in range(0, 27)]

    all_strings = [0] * total_num_of_strings

    for i in range(0, total_num_of_strings):
        s = ""
        for j in range(0, length):
            s += chars[random.randint(0, 26)]

        all_strings[i] = s

    return all_strings

######################################################### PRNBS ##############################################################################################
class Solution(object):
    def __init__(self):
        self.alpha_pos = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7,
                          "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14,
                          "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21,
                          "v":22, "w":23, "x":24, "y":25, "z":26}
        self.groups = {}

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        for word in strs:
            hash = ''.join(sorted(word))
            if hash not in self.groups:
                group = [word]
                self.groups[hash] = group
            else:
                self.groups[hash].append(word)

        result = []
        for key in self.groups:
            self.groups[key].sort()
            result.append(self.groups[key])
        return result


if __name__ == "__main__":
    soln = Solution()
    all_strs = generate_strings(10000000, 10000)
    print(soln.groupAnagrams(all_strs))
#######################################################################################################################################################

    
# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         def get_char_count(s):
#             char_count = {}
#             for c in s:
#                 if c in char_count:
#                     char_count[c] += 1
#                 else:
#                     char_count[c] = 1

#             return char_count

#         def is_anagram(char_count, reference):
#             for c, v in char_count.items():
#                 if c not in reference or char_count[c] != reference[c]:
#                     return False

#             return True

#         considered = {}
#         all_char_counts = {}

#         for s in strs:
#             all_char_counts[s] = get_char_count(s)

#         all_anagrams = []
#         for i, s in enumerate(strs):
#             if s in considered:
#                 continue
                
#             current_anagram = [s]
#             char_count = get_char_count(s)
#             for j in range(i + 1, len(strs)):
#                 if strs[j] not in considered:
#                     if is_anagram(all_char_counts[strs[j]], char_count):
#                         current_anagram.append(strs[j])
#                         considered[strs[j]] = True

#             all_anagrams.append(current_anagram)

#         return all_anagrams

# soln = Solution()
# # ls = ["eat", "tea", "tan", "ate", "nat", "bat"]
# # ls = ["incentive","countersink","pickaxing","explicit","unethical","seoul","gyrates","dismounting","dartboard","socialism","sissiest","radiotherapist","sprawl","hems","raggedier","conscripted","repealed","implanted","coverage","traitorous","barmaid","pointier","huntress","summers","finnish","mouthed","mamore","lemur","osteoporosis","frowziest","sop","comical","speedup","oasis","peon","testers","stances","chuckles","childes","consensuses","rastafarian","battlement","christies","urbanized","penitence","replenishment","disperse","kibosh","combatting","repealing","guise","grassiest","grafts","waddle","pigsties","moneymaking","polite","reprogramming","audaciously","gorier","blaze","yaqui","racially","inc","reupholstering","fez","lemaitre","nineties","pedal","deferred","tranquil","surveyor","narrow","hopper","solemnize","federate","trisecting","cravat","lille","biography","land","jazzing","rhomboids","nudes","mundanely","greenbacks","chattel","deceleration","devoting","itemizing","routing","jukebox","passkey","infants","prerecorded","fuzzing","gandhi","roseate","bandit","prong","bowels","bounciest","misdeeds","unseemliness","emceed","later","hailed","crotchet","steepness","jot","improves","eucharistic","natalia","exalt","performers","predictor","voyeurism","fedex","activate","crypt","magics","treats","viewed","chauffeur","ladybug","peppiest","seismic","microscopes","liners","wraps","footman","tape","daubers","aerial","sparer","politic","shamed","decal","ayrshire","ruggeder","washcloths","neurologists","singsong","kaitlin","conn","monopolizes","sunroof","zonked","overall","celsius","fins","caparison","imus","enfranchises","microns","promulgates","aspartame","fails","decamps","spiciness","impieties","starring","receded","skying","suetonius","pornographers","intellectualized","truckled","abdications","openness","principally","sellers","complaining","jeopardizing","concerto","fibula","cliffs","aorta","inhale","transgressions","copywriter","understands","coccis","disperses","fraying","strengths","macaulay","mitigation","competences","ides","linked","tawnier","hallucinate","dairymen","puffier","matchless","wheeling","drily","nephews","clandestinely","tsingtao","disarraying","headier","experts","yippee","repellent","tributary","clannish","dumpsters","genealogies","ballooned","denouements","hymned","length","sasses","uncontrollably","fortune","wastefully","overproducing","sickening","headboard","burrs","prohibits","keogh","outs","lamer","repressed","rowdyism","transgressed","euros","amenity","garfunkel","rather","noseys","lampoons","raja","impermanence","heaters","shakespeareans","judiciaries","tweaked","extrapolations","succeeded","jowls","vociferation","roadways","herb","inactivity","registrars","checks","deservedly","heehaws","apologetics","fatness","aced","promote","atriums","deidre","redound","litterbug","barehanded","scheduled","flakiest","twirler","graduated","coccus","gadfly","unforeseeable","emendation","woodsman","wiriest","tangelo","weakening","intimidating","sternness","reiteration","wicca","heresies","inches","encodes","sidebar","starking","wastelands","pepsi","emigrate","stuttgart","shindigs","pansy","chintzy","limbo","disbarred","gallivant","hallmarked","respiratory","eminences","unabated","affirms","twinned","wordiness","installing","donn","westerly","interfaces","benton","mussy","identical","sulfates","starvings","woodwork","hyphenated","catechizing","transition","dramatist","demilitarize","buber","spoonful","laconic","undervaluing","inestimably","severer","improvidence","stoneware","cholera","peru","rearm","recluses","diaz","tablespoonsful","sandals","cinderella","insubordination","sires","stern","jeremiah","snowbound","ramifies","lexicographer","skimpiest","predetermining","lapidary","dentists","upbeats","marketplace","ploughs","esteem","miserably","overreaction","unlikelihood","kinswoman","averts","remonstrating","asinine","amortize","wasps","coal","tenderfoot","subplot","coyotes","sauntering","rices","fraughts","decoded","millipedes","knocking","homework","furor","expansionists","j","emergency","sharon","provisoes","president","assuaging","curtail","indigestion","liming","cryptozoic","auguring","indenture","magisterially","groped","ensue","steaming","mutinous","incomplete","yuletide","nomenclatures","hundredth","jimmies","irk","common","wetly","volley","summary","obsequies","granola","forests","allege","informal","shapeless","earplugs","disunite","insinuations","junked","riverbeds","georgian","brushed","sequenced","bucketfuls","spiel","humors","screwed","capitulating","downturns","intimidates","refueling","mingled","arisen","dragnet","aftereffects","practised","obduracy","canon","penning","inflammatory","wisher","actuate","kari","actuating","reupholstered","successes","inborn","canvasbacks","incapacitated","aristocratic","britt","lazying","hymnals","tyroes","tamper","graduate","franc","seasons","pompom","throeing","deviate","leveling","inaccurate","impaling","trouping","restoring","deduces","perforating","artie","alleghenies","crusader","rosemary","chastest","educational","caveatting","ablest","doorstepped","strange","eccentricities","sublimity","afire","humbugging","jots","ordinary","foyer","kayak","snake","wheal","dispensations","transponders","zing","pit","meowing","improved","crowd","nonfatal","epsilon","nodding","cyclones","imbibed","rebroadcasting","quibbles","moisturizes","zippy","braille","visaing","abetters","lurked","snafus","moppet","lemon","wifeliest","stuarts","boyish","reapportion","kneecaps","stymying","villagers","obscenity","bumble","zeroing","objectionably","connolly","memorial","clanging","gallstones","dibbled","outlasting","mendez","reproaching","antagonized","sisterhoods","hunchbacks","superimposed","siphon","professionally","spermicides","lebanon","facing","pierces","philosophically","mcdowell","rotated","tic","correspondents","nonplussed","litchi","ascots","millennial","booked","immunize","prefabricate","spumoni","odyssey","fey","bunched","olen","regularizing","superconductors","aside","infirmary","allaying","saturdays","caucasian","doreen","france","speeding","wretched","slovakia","chiselled","peseta","tho","gales","loincloths","shock","readers","boarder","entryway","toning","transitively","preponderances","internships","rating","pelleting","audition","amusement","theed","cocked","toddler","rusty","kinfolk","frames","gorgonzola","overrate","lightweight","bayous","populists","insensible","bandoliers","travelogs","tactically","weatherproofs","sleigh","develops","oxygenate","relaid","mimi","wheezier","chill","salween","theatre","vitalizes","nun","olives","offings","tricycling","tipper","kindly","bellies","sixteenths","ganglia","recombining","eastward","minestrone","fairgrounds","undelivered","scapula","breadth","groupie","ophelia","adrenaline","dork","autographing","watersides","sent","socks","somnolence","systematize","signings","rachmaninoff","santa","snacks","leno","spurs","heliotropes","silenced","roundhouses","illegitimacy","hedgehog","wet","depressed","eris","pure","pouncing","obtuseness","caulk","openly","kerosene","grille","buccaneers","oar","modals","playacts","shroud","plowshares","iciness","retort","jaunt","identities","mellower","redesigning","molest","forlorner","guacamole","cohan","refocus","dossier","interrogating","cants","diligence","stomps","enjoy","awe","loggerhead","csonka","inversions","den","lunged","alkaid","palming","delivers","proprietorship","groveler","choreographs","instals","merton","cyclops","augmentation","manipulated","nasal","trousseaux","critiques","arenas","stale","suspect","behoove","propose","cellulite","purification","leah","polestar","potato","gladlier","sunders","entreat","herbalist","filthier","skinflints","asseverating","insulted","mildly","modulate","charges","libyans","weekended","rodeos","allegedly","tarawa","valedictorians","spacy","spontaneously","yore","classify","centigrade","videoing","airdropping","dejection","pierce","imagined","isabel","reiterates","blazing","stuck","deceasing","netherlands","citric","tormented","monotoning","bestowals","betrayals","adoptions","scrolls","sex","idol","whaler","telephotos","conjugation","abductions","bundestag","disruptions","nouakchott","stuffiest","goodly","dissatisfying","anglicize","flowing","identifying","depots","stoicism","thessalonian","hundred","whetstone","defroster","headwaiter","feisty","inhibited","reamed","demonstrator","accursed","hector","interchanges","erotically","sportscaster","gentlewomen","teabag","smelts","disorganization","conveniently","maugham","hatchery","regards","arguably","govern","boulevards","niches","gristlier","obtrude","catharses","throughway","stoppered","drinkers","indeterminacy","vacuums","plainest","acuff","eases","defined","splurge","severing","griddles","thermoplastics","dilution","vinegary","straights","testament","sticks","shanghai","childproofing","clobbers","taco","castro","arrests","fetter","discomposing","timbres","wondrous","pullmans","amusements","telephonic","manning","inhabiting","finery","admires","defensively","fiord","incriminate","oust","collapse","deliquescent","bulwark","consciousness","roguery","beefburger","amounted","pheasants","archdioceses","vote","gujarati","forwards","waggling","tanned","liberalization","chap","finishing","catawba","anus","farina","butterflying","folks","crumple","criticize","unswerving","snack","gentrification","enthroning","drearies","marietta","farley","recede","incise","electrodes","dirac","corn","livest","coughs","noreen","rapscallion","codeine","acidly","confiscates","dislikes","administrators","valid","prep","legated","wherewithal","subjugating","wallabies","boning","creakiest","erotica","neophytes","drowses","bushmen","basis","regattas","melancholy","clubfeet","there","generalized","rotunding","condone","hemlines","bantered","vertebral","ruby","companions","postmarked","aping","finalized","prado","mutilations","partied","isiah","desk","calcines","agreeing","bode","cygnet","downsizing","naiads","preambled","recife","randall","gillespie","convalescent","victories","obsessed","leaders","strips","parmesan","germicide","clarion","pictograph","nutshells","bungalows","hagged","colosseum","ferraro","recapitulations","labored","acrostic","dynamics","bucked","betaking","pragmatically","gobbed","glossy","congresses","rewindable","trout","renovates","mattered","davenport","stenographer","nudism","deduced","unattributed","equally","wrestled","sequoia","measurable","lamb","babe","concourses","creamer","fascination","steroids","deplaned","germinated","progressed","swashbuckling","pools","officemax","brewers","banjul","thong","periodic","grub","typescript","lemurs","excreta","seeps","clearinghouses","isolating","particularized","thallium","waistcoat","misread","extensiveness","violations","insistent","zany","newses","predominate","enunciating","ultras","burlap","dowelled","elision","person","minneapolis","edification","endued","asseverates","meeter","iceberg","mexican","end","wale","veronese","ida","earshot","tunnels","debuting"]
# ls = generate_strings(10000000, 10000)
# print(soln.groupAnagrams(ls))