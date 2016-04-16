# Given a list of unique words. Find all pairs of distinct indices (i, j) in the
# given list, so that the concatenation of the two words, i.e. words[i] + words[j]
# is a palindrome.

# Example 1:
# Given words = ["bat", "tab", "cat"]
# Return [[0, 1], [1, 0]]
# The palindromes are ["battab", "tabbat"]

# Example 2:
# Given words = ["abcd", "dcba", "lls", "s", "sssll"]
# Return [[0, 1], [1, 0], [3, 2], [2, 4]]
# The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]


# Naive Solution
class SolutionNaive(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def is_palindrome(word, length):
            p1 = 0
            p2 = length - 1
            while p1 < p2:
                if word[p1] != word[p2]:
                    return False
                else:
                    p1 += 1
                    p2 -= 1
                    
            return True
        
        results = []
        lengths = {}
        for i in range(0, len(words)):
            for j in range(i + 1, len(words)):
                w1 = words[i]
                w2 = words[j]
                lengths[w1] = len(w1)
                lengths[w2] = len(w2)
                s1 = w1 + w2
                s2 = w2 + w1
                
                if is_palindrome(s1, lengths[w1] + lengths[w2]):
                    results.append([i, j])
                
                if is_palindrome(s2, lengths[w1] + lengths[w2]):
                    results.append([j, i])
                    
        return results
        
    def check_correctness(self, input_list, result):
        for res in result:
            print(input_list[res[0]] + input_list[res[1]])
    
# Slightly optimized
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        word_dict = dict([(w[::-1], i) for i, w in enumerate(words)])
        
        results = []
        for i, w in enumerate(words):
            for j in range(0, len(w) + 1):
                prefix, postfix = w[:j], w[j:]
                
                if prefix in word_dict and i != word_dict[prefix] and postfix == postfix[::-1]:
                    results.append([i, word_dict[prefix]])
                    
                if j > 0 and postfix in word_dict and i != word_dict[postfix] and prefix == prefix[::-1]:
                    results.append([word_dict[postfix], i])
                    
        return results

words = ["bat", "tab", "cat"]
words = ["abcd", "dcba", "lls", "s", "sssll"]
# words = ["cgagehehhjej","ddgdahhifhafccgfif","ifbc","dhcdcfbdicgghcf","hjcafdecffad","fh","bc","biibbibfcajfiecg","ggafjiij","idbfceadbfebggdhi","baibbdahccecdjgd","jfebajeah","dgbdbifd","gh","ihbchehgeh","fajiaaddgeehfhef","bbgahiedfaeffgedigj","bacbbichdfhfjea","bjdj","fhebjfhb","iihafdieh","bji","gfcf","bddhafaaddihaaeidacj","ggdjifjbhff","c","acfgfhihcjfd","fhjjjiagcbhedeb","eiief","hi","dihiejai","ieicbgdfjegefha","efedajfjdbhif","jggfbecfheh","adg","cceeaiccdiiee","fifcbbic","gabhjj","ebcggffgijgejfhcc","ehhdhbeeggbajhfiadg","jhbj","babdadccbciebc","bcbaehgfcfeajb","igfjdbhfhggjjd","agfjbdgfhbi","ifchfefbgga","dhbgf","jifdfdheajfehaija","f","jcjhje","ejhicbh","hfdad","eaebaggcdabbebd","gdceiacjjccdhdcdh","facc","hhbfafaddihecbgaj","dghgaaeabjgah","fbfghdeaefeacchb","ibfgebabch","cfbdcgbgijfda","ffjaicfiddjajhhg","hfcdi","aigbgfdjhddhdcbceg","hfdhi","adhejjcbifj","feegbec","agfjhgeihbbfiieifgce","jfgaffaciidjeeffbfi","befcdghadhfeaf","aecgcihjjgdedddac","fjcgheejhdfagbib","aedhifeai","ac","cgde","cfahgge","hhdajbj","fjaejjdahfed","ceiceedg","gdbggfd","dehhaafjdbbb","fgicbgfjeaajf","gjefcd","bdjgagabadacjdbbhid","dfbfdicjbcbehaccdg","fhdcdhajjdbjg","fgaihbhicjdf","gjacdbbdde","jieejjd","icdhb","bfjj","fd","jachafjdgieaahb","cjgidgdfdah","hhgjifhcdachgc","hij","hhgfgejfha","cfdebh","gfjgjbhjdeafabgchhgg","jfadgdbiedeehhbcedae","fadcicjgegabejdcfi","hhiehaadd","fgjbdigchcj","igiggbggbhiaf","acajbacbggjf","cehgfhfgibedcfdb","cfdfcbcg","ebibidiieeja","bigadehjcae","jhjechai","aiefdggjfed","gicejfjchbhfcb","ch","jdffc","giideibbadahhhg","gjbejcdi","cgdca","gdcgjie","dgifaecieegbfjhjbde","hhcchg","ccaffjihh","bhigcibechccbdajg","bhbjgcih","bhgfbdf","ceibiedfjighfiaa","hbcfdfgdjj","jcfgeccjaacca","gdh","iahdgaheiidacabdb","bdfhc","cichdgacfjcdfadfgfjf","j","jgghhbjjia","fi","bdahga","ecegieegef","ehbaech","djibgcg","hadjgjcgaji","jeieicagjfhiaddidfb","eehahbffacajad","cgceejeaeafbiha","hifccbigjc","hibchjdeeaghbd","jgbjdacdb","fjcbddeideahjd","iicgggaebhjdjgdgga","agfhhfjijhda","cdibejghfcabfedb","iiidfhf","jdedaieghdfhifc","gbccd","fecgbagaf","hfddbdff","fhghadjighahbgeaigic","fahgdfjiccbhbd","caiccjcibdgdahegcgh","hcfbicahfg","jccjejbb","jbafffeigi","jijdacgejc","jehdbhaabcggfedje","afcdhed","ejfdiebibhh","ihaddcgbcb","iddaehffddiiadea","cedadfhhfa","agicbjea","ijhj","jaefeijhaffiihhiahhf","aacefcdfgb","dghe","jdjbcegjedjfij","fhidbjjcfg","aeggebje","cidhhciaae","afbdj","echii","dibhgfeahdbebc","fagieaiiebbbfch","ibjidebcgeggbcbhhj","aiadajgie","fhjdfdii","dcbbecaeahbeib","acb","ccfdabefchdcjgfedg","fddbjjjeeh","gdbfbje","fdgjjdgcjdicdffcihi","fibghhgi","idahdgdghbicfc","efdfcciiibdg","jibjbcch","gdafgibjgjfi","jfhegdffj","daif","hf","eddgai","hfdghdgicbbfbgcj","dabcgiibbhca","iadcceedefibicchhgb","fjieciejjghdcj","biae","eb","jgjggghid","aedbhd","fbbfbbfdjcieghaeci","adhj","gdaaccafeba","abiefadhdae","edhdiich","cebagdagijhj","bejefcbahacde","fiacefhebecjifecehca","hjgii","cdccfcehbc","abhgbacicdg","bhiffhfhbdeafegd","ijdchceidi","gjfc","bgedieidhfa","iiijicjhbgaeccfgbfg","chbhiaideffhd","gahcjd","cgcbidecadb","bij","ijcccjdhgdd","fjcdib","iggejiicdgjbcdfeiegb","baigabgjcge","hdjibgdffgdhfaci","gjddabihagad","ifbh","chhdbajhgiabcb","gjhadagahfabjehbjb","abbhdefhdca","geihficghde","fgcigfbciafgfcche","eadcgbhgabhd","bhfihfaeafdd","beaadciibc","geg","ebaehcbcdhiaaad","ihgh","afbjadehdaeajg","hfggfjbadcjgfjfadiab","ebhcfdbhjif","efahg","cebiiidfaieeegjcccbg","daegaidefjehbifdbg","jiaifa","ibgc","gacabiidagdaaga","fieiggjhfcjbf","cdghdifgefija","gcfecdceffceej","fhcehhcei","a","bdgehagcbedeiije","jdgic","hj","ahddiec","baiicieecgfcadha","didgjchgg","eggdcgee","dajggfhcdbed","dhbhcfadedhaajcidjgg","fgibcehceicgahcfd","cjejaadjgdjihfec","gfbefggghd","cieagdih","ihaeijgeadghiba","aijjeb","iheifhchedfji","digfabcbgihcfjjig","ae","fbhagfigcdhcjcfgfii","gab","igfb","jjhfddifjcbjjeehcbg","gefheajaifieiegaeci","bgdeieaifhfajjafge","gebgjbddi","e","beiiaghiegaghdbdfb","jcfjcjhafj","dfaijf","jhadhj","giejaeafgedgfad","dfej","dff","gcagchdeejdegaabcia","hgbieh","iiejdcebgb","hdcccgfagef","acajedaejg","cebggi","cfcgeeaebegbhfeh","b","edchgdgdjijdeca","di","cgddahccae","ehachgidjgbabjajjg","egihjcidfafcccbhefbe","hgi","egbacjfebbdbha","dicja","aefghcjiebij","habgafbhgfccac","ijbdadhifiibab","eii","fbagfd","ghddcbgg","bdajheifjfhddaif","igab","hgfffiiiahhgjddf","gcjachdibifebg","dhhdeba","dgegig","je","fdfdhe","gedhcdedfaeddejca","g","hah","digifhahbe","ghhfjccdhh","ahbbafhabhaijd","hhjdagidcbjdfjg","aeacbafabej","aaghddaafaef","bjagiedajidccihiicib","fbidjjfaigci","idieghaehjgigbjfaeba","hedjd","accjbgdegg","cgebicidddef","egjcadiabjhbjbi","jbbdcigdf","jjfhc","ifbfeihbbiiif","affig","gcjiahaifddbg","dcidhf","ddgebhfjbihjge","hdgcdecgc","bihjbbbaabdaeg","egigfgcbdb","ijajfied","agifeefhajfcgeh","fefgfeebffiddcihe","gjghejbjfeehhjciij","eabehdbceac","jcfgeiddi","jbgcbabebbi","bjeicedfhihgjc","hhihijii","h","dbgidgcafgidbjhhb","heifhecief","fefhiagcieiijfdbjf","ahjbcedfdh","ccieibcjjbdgiafeicg","jcefbighebeghheeg","bjghidhfjhahgjgjhijg","fgij","gccjbfhdbhfijhje","bhcdahifbbf","gie","icjafb","hihieajgieibj","chi","dhajff","aifdibgdbi","caijhfajbhcgdc","hha","higdabcbjbeidbhdbhb","dagghghdd","hdddiaaidgdgcbdgg","bjheibdgjcjahee","bbafchbhcbadjibjj","egfh","dgcehjdjchgbgfjcafc","cjaehhdchagcfe","fgabcbgfcfbfedg","dfggedegchjafcfedff","fbdebegdacgdiaib","hdbicghdjgh","dgif","ibhjjghhidfhi","bbaeaeefbge","ihahjicjdhag","dghhbfjbbaihhiiidh","chbfa","jhbjbe","fbdaebbibfccejcab","djffefbhdegebe","iedafejdcdjbhe","jde","ghdcaijdjaddcbhhe","bj","gfbcjgfdbdeg","ijgh","gfdibdjiecghcbig","eh","egjjefad","aahejbdjeiefcd","ajb","fbhhjicfcijbajgj","ceaeaahbdeibjad","ddiaecabeifjhcc","accdbcfaabd","hbe","hchdgchg","bdibh","fgecbfjibifaj","jhcaafjbgdfgjdb","haiagcacbgbafaceffib","cddhfdfigfabhheaeei","bgjdbiejgafhaeegajee","igjfddaadbgajaebf","behcac","ghaggffaijhbfcbbh","cjjichbi","djgcgbfiaadgbehdaia","eajgijcdgdcbcgjg","hjebbc","hbfhheecbejcabdaijg","ibjiafafgffca","gbhecjfcfhhiaafeghfg","adgjigfagidhbah","jgehigfbb"]
soln = Solution()
print(soln.palindromePairs(words))