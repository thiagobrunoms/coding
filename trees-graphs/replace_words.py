# In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

# Return the sentence after the replacement.

 

# Example 1:

# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
# Example 2:

# Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# Output: "a a b c"
 

# Constraints:

# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 100
# dictionary[i] consists of only lower-case letters.
# 1 <= sentence.length <= 106
# sentence consists of only lower-case letters and spaces.
# The number of words in sentence is in the range [1, 1000]
# The length of each word in sentence is in the range [1, 1000]
# Every two consecutive words in sentence will be separated by exactly one space.
# sentence does not have leading or trailing spaces.

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {} #key: char, #value: reference to another TrieNode

    def __str__(self):
        return "char = " + self.char + ", is_ending = " + str(self.is_end) + ", children = " + self.children.__str__()

class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert_word(self, word: str):
        current = self.root

        for letter in word:
            # print('processando letra', letter)
            if letter not in current.children:
                current.children[letter] = TrieNode(letter)
            
            current = current.children[letter]

        current.is_end = True

    def replace(self, word: str, dictionary: list) -> str:
        current = self.root
        replaced = ""
        for letter in word:
            # print(current.children)
            if letter in current.children:
                replaced += letter
                if replaced in dictionary:
                    return replaced

                current = current.children[letter]

        return replaced

    def replaceWord(self, dictionary: list, sentence: str) -> str:
        words = sentence.split(" ")
        for each_word in words:
            self.insert_word(each_word)

        final_sentence = ""
        for each_word in words:
            replaced = self.replace(each_word, dictionary)
            if len(replaced) > 0:
                final_sentence += replaced + " "
            else:
                final_sentence += each_word + ""

        return final_sentence.strip()


suggestions = Trie()
final_sentence = suggestions.replaceWord(["cat","bat","rat"], "the cattle was rattled by the battery")
print(final_sentence)
final_sentence = suggestions.replaceWord(["a","b","c"], "aadsfasf absbs bbab cadsfafs")
print(final_sentence)
final_sentence = suggestions.replaceWord(["nakthwkd","aqmkofeam","ltj","asycsolo","ghozdacynn","zgrvm","usvxalln","sjnmhgyakn","lumzeoo","qqsuqtcgho","cojtgdzjb","ejcto","qylqnjcdic","djyaou","haurjcz","gfeenyoi","fakt","ufjj","plqxdfw","apdgvq","tddrrpmcsi","rcknpzke","vwd","azsq","jppbduzsxa","xetscjr","fdtbr","keadoe","xxgt","wzm","qclg","zyotynth","keyzk","djehwemoyi","znrc","dfg","uwatuetj","xtg","epxjpfivwh","rnpu","cqtatgvvz","ujqo","vyxwrlmfk","ijmwqnwk","enom","rtcb","pdiwgp","fmn","bxafyjyqv","zfcn","tzgacwm","dbryeomj","csnzkioo","dbmw","akentvtw","dypugd","vnik","risklf","cxnqluell","biiu","vhxlace","beitgcjpd","anczigum","lxd","iqoq","qju","jkan","ixqze","umgwhlhvio","xhpswcr","ywn","ewesuhwr","ujimq","rmnaumsof","ccu","peubi","zssmnjnbel","vpm","ekpk","jpzxugm","emj","mdfmpblxz","uiazkmw","gvmuob","xojenhpl","arhjhlbkr","ojqt","wtqyb","wwxeim","dfnxqvypud","ppzkdev","axzl","cyt","hegj","xyzajij","veksjk","hbjstwir","ptqiyc","xcv","ggga"], "lrmahrqeflrqigcyvshcqdvxgpmqenootweaezodnnizyokszagizhxqrtohpzedvhgcexllnddaobfbkqlvpndsgzihpfw jreayzqagsoaupufwjvwbwnevfpzolfpzvzdlfzxtmqbrxhbahaqcafzhrdgmnrqmsidsgadcdrfqifqsnggchprzk zpegkenqfrzycnjjnmnojrphflwlbdaubvwebnfsqqtfdguftoqxhbcteqtrupprijtvcfsyglsqsusbneltwvquubt gvrxdfusgkleajiajrwdwcnfqcbsvjnwnfsxfgkkxjwyahgsotqmvphulufullajjwlfasbessvitetgv wgxxcrebenzngns sybgspcszeoaqnchefnvwmfoscupldjsdleouhgbdkkborpecmenquuudtsnbumwayhzzkbxcwbtaxrradduyc fslbmlqevqzezjakadasoweuuveimgnevgiuahssmamocxohoqkflgzkqhgsyeveeuyzkoolrljpubeil vnyevqtzjbfpnwqkojrliticraxddsqakmqzpvpcpbubjjebfunxwmsbyzdfejoeywsisncozafanipewhzrhqvzftjfhaf bkrggqjcxelemxx jiexqrigoeppghetojajgkmgqmzbqejswvzrrplaobxtzl fkczckbgxexgdpypdpxhltziyhjmdq icbvbulxqjxvvsxyszmlpeplkbohucrqmdusmzu nycoedwengprbloifmgkwgoshrfyggmelljbgeuopiohpedncmnedwrskoyztkpgytqdtypcpbtirkqb dgoafuiszr fzlupxxboewaiqpyfremgrqtbtocrm dagzciqnnarskjpbzvepgpzbtghjgbdnrtcukorkkfozhywsnxzopfnxh bknwasqstivj wkuvkohbklvnyndwnzmjccwqtjwlxvzjraadjtgqsbquhgajgowecqqkddpeimiluupbetbjyejk dczssrvavuqoroneqpqopjjyacqlewmdntdsi szpnlwahbzcksteulmkzlftcqkgkwtmpltydmll eivsbmkgbzxybxsoriwpcojqebguwurjdjloibwyzbnshbpacggmjlpzexoojioxgforpqwqfhjsltfzeotzh qoevyooaryjlaybsagxjgtt ehhppoourfqqulpqlmwssyrsdqnymwncbl acqvxhrmpzieqlodekhik ryjoozpaiqhqfgmbpe bzemlecljjipgnvjdcqgakquyrpkt edrhzvmtqdsvpbzwrubejkzrqjjmcenyrophrzp bpmobtcsgwdhtryymuiptcgerwecsdlfpgcbjliyevlbeqrkxsbztwgepxegefvngzyhpugihbcgwujlgyttlyfzytyvuk cdkpxnntidxdgkj fxszzvvrli dzjzghpafsxmuarzbjjmduywgbdzhyicdstgiamwevemgqtxsothjzastmvvekkcooqfrakpwjtueevhtqahvxmpduo eyqzrwdq vpbcyvazvqmnirlwljvysrpt oxfcmjnwmdsbkrfxgaimmdkcgwvcyhbdlcqhmygfmvqfuuzjramxkbfakhpmuywpjsvowrzebfffocthteqzgtsfow xccuyrzwzvaekwencflfcbsorfsqqdyirjyqbgjxvjoenjncfhdwecfscgvlzcrscwjawohwmizdjniiocrou fauqmruzvnyjpyhgtyemvectxegpiacyxcpmwjfpvnzzajclszchbwpjbloxurkxabntqkqbfiehqohnvi bmtkzfahjrbfvmigclnarnhxjwrgxztxoqrjawkjvjvkkyfrbjvzbpkuoknsyhuzcvenwg fjtthdyezsgrweknstwfujuxdvururqjoehocodruqarodhdr wzdivsgpgplqrftczbdmbpryiokfks yhhaxmfuzjouckjktqobfjvvwynnhcljsjmhch ftzyzygrkquhsekrcbaczmsjdksxfuloedyfjohkbkeceehdanlsmkbfqjbuqlgnpduauaotczngmwnfholio odsfggordipikxbepzofnrmubbzkivztydspnyddfxzlkohsjmvclvhobrajbacuservqnrihedisltphvkiksu rhoguncbsqnpcwwvlfqfaebljonuqkkhykdvxcpstslosgwbhcaofgnudmelwjgjhkaopwuyssdwhhsmg wwcnxompnkyegzjygolfugpkghhardlgwcqjgfoijjewhuhkofctnpvhwlrxwewizpwxuyznexdgbzjggcfjahzizch hifwhgkfutixvbtzvaqivasywbvbvmsaxjqywyqcwutykeqgcduhwudmngumuavdfcwtvwomaougtpjxz nbozqxzdihg qhnlkbrutsbajhoncuvdaelsclaxoccavqgyzqtvvzknvlhced pvpyvtsqjzqvfgkmhpdbsqwmfojyxuhwvnmwawpjcspluruywvtwwggvgmoqokhvbpqioigfw nuuwvlenhwqoswaemrcocexcfckzratxnfwwfwidixnyvwanvounlqszhwzcbjhaejgqf ijnhzjzotihlvdhaxadffjsiadvgvqqmbikdygrybeahthkdjbhnirplxai pvazvqtuvqrxhoysberbdyki cksdfryztvgwvzoggimzcaugjvoudoxfxojvxdjzmogdtlmvcmbtvwsbgoscrgwtggwsipmuevwxtrc nqwxcrigkwqvcyxinximsdrwafjmssnkshofgdazrxfvfnvmgeyidnggvzuvddktow yxuvmttnmphvnkpirddobaxjsqmrkzhfhixnbspjdorxezsqqstjxftkrxuzenlrpzxsqwxxutkbjtluueydzyhdpgxvns uzcahfshwnypmpsywuipbkjimwgqilkrxccapyycgjwfvcdkuymdbgwfisjeexziopehvtqanknrpunjwmiuxfjfxfgpudturnm kzhefpihmgrsjlbtozgdwcasostsjsmbrkeorjjuhbvkuwhfudqxutvvzacnwapdwjsmafquuyonfwxskiru fcwaovesdgvfppkzdccntmavtwzwlsdwzyczggenhkyeiwutjnhrpgyvkqgkegvtdmtwxjqrxggxetgjneiyofcrklzgwff owyhnperxajjtlljiubycqxrvhrtlvuybbkwbkcwycp geredmlqskrqzrerjogcsfdjssqxfmkigfrsr uynqwclcnwknrekebqeyrccerzxoxoupvrzpikabfyvnspzr qhslrcnexiofkblnqweyeq bzzdqgsxqnjapramtsxiefoahivjlrtvdwivltmzqb ddqzgkfcypiahqcxxmbfngdjdrnrsqxwkmbtfxqcvyeiumthxxgclfdrgizs hjqcmvoxeboozlgihaxpmyheuhllmzllzsnkavcldhwgpduzstevairyqqxbaeatgtqjvebekxmqsieyrllsbojjnunpdmdmvk dpmmixjszxhxefxjgshvrshtshpveitkwiuciarmsdfsgyjalfrfopgqbdlvepaphreghgssuuotyrajljkg mijpumhtdxwsccqnelitolspqloxueurfshzqrxxwogdlypcmospogqoqebwzmqgudvgdo oqzqvngul vjvyqasibtmohfinwihjozzcneylgafwfbwhpqrkczfnaewmluohnazerdhzjvuunapwfaacepvnmjwkykftfimxuzkikjbs znuyyzobucqsiyvclginjouxzopgorhlyvwyovugiriwjomwlamevcenemevuoqhsbtyiexabsqchde wakwxdanzimbdzxykgpthcpuznrtnypigexdhhntcdqfoahftvvnufnibzmfvopdtto dwljilpkbtyrwgqjvmgc qsgayondipikyombjjrxjliripfcwmtdrsxmdfqhjkhnvbyqbfnhfembbedbrkawpjhj quqwwscmdguvlwpofoubtlcocvowxvglyg qzncqtogmfiahgzimoqkzkxag qmnugbzcuhhjphjpunjpkyyubeczufiinjoynuxowhpgljibnfhxpdmrxxkqavjhhrqxqcijajh gnsrsezbrewebjnvlrnywpdfeysrjjkpauvmjblphmrd xldnnoukbyfgvmhojacfooqgifdppikctloizeshrtbtpcofqcdclvvhddsxwtouzdxerrgdf utnoxuqlwdymjhagxyrraxcikgccmaxlbfzdwpxrjve btzfvbcgqleh blpraciczcmmebirqwqjvehyymwnesyqzezbhyetgkhifagxob jekwpefqhbtbpqqgyktbadengstovukwqtlwraisaesfkonzhuarnpciqaokwwvxrbrhwjdggzpstujfkvguyojsygm synpvylhxtfhfihmwthlggspzrfsiikrhcvsjkfol llbecwobcgzqqsklqgjrgyvmvqpazxmmbuwaqryctxlsnicbyfzqtjptm xopeojjmgxaehqyroxkkyvlabkorm aamnnsrwxvwjnhjuvce ddsydgtrrikcigqelsictfcoefqpjvsosxicllxr tjoinewtilolhnntqvvgaltvxrmtepskxahziuevdsgqlwritxxcoseqnay pzmvuvaaesdymwrnyieeqqyrghtszqgmllqzjbvaasztpeqaunikgtnaorevxvn npuwsprb icgjwoqeaqfihsfenngucrschtrggpuhmnu mjfsdwgobqfuo upsgsdumhlfpewhjgxbcxoabqysrrjxhzcmuobqil dgqksvrlqeygbzpzgunkfdhibynxxtpixmonubqbnvdoppryhoexjeawspcocpinmytnsjoguysuwhqdohnkwntvdoyovg hqldkusjtulrkgnfmbakvpxrdxecoosonkbqrvhdjqvmqlykktfasldtxnefctg gkziknfzkhmckpfkvopnprjxieiwhhsdbnkuypazvsqbtdfambsnabpvrlvfoecwobtdycvdpfodspgzhozhqfmln mzrlfnyqfdniejdehdhavxcrxxyvmnjvnolxrqeoyuzzwnzauztrwguqaymmlpjmwtxuwdtzqzcwvgva ijjqeoklvmrjhguepcwuqobxuogjjylmpxbosiicvichzkbmxtqmgnnecwhqayfjovcjunrtfrgrawn xouwdblnifqiyeysqmmuezjzfktsfeyjyplhdkolhrgvvvzgxizqxqmbbwrggucmpijnixxbqpnlxharisnkhrlnszzrd tkksshlhpvnrcmmfgvxtziqvstjdfydbxufsbgoknwgkdromhvjydfddxahxitxuudae iachhkqzgnwssoqbswxhfppbbgkqurtrcemchsudkykwnriqbd")
print(final_sentence)