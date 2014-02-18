import sys
import re
import itertools

from Entry import Entry
from DictionaryRetrieval2 import RetrieveEntriesFromFile

#reload(sys)
#sys.setdefaultencoding('utf-8')

a = sys.getfilesystemencoding()
#print "Filesystem encoding: " + a

gAllEntries = {}

def reverse_search_entries(search_term):
    matched_entries = []
    for english, list_of_entries in gAllEntries.items():
        for entry in list_of_entries:
            if entry.search_fields(search_term):
                matched_entries.append((entry, "place holder"))
    return matched_entries

def arabic_regex_search_1(ial):
    #print "===== arabic_regex_search_1"
    filler = "(.)?"
    #print filler
    arabic_regex_list = list(itertools.chain.from_iterable(zip(ial, [filler] * len(ial))))
    #del arabic_regex_list[-1]
    begin_word = "^"
    end_word = "$"
    arabic_regex_list.insert(0, begin_word)
    arabic_regex_list.append(end_word)
    #print arabic_regex_list
    arabic_regex = "".join(arabic_regex_list)
    #print arabic_regex
    
    arabic_matched_entries_1 = []
    arabic_matched_words = []
    compiled_regex = re.compile(arabic_regex)
    #print compiled_regex
    for english, list_of_entries in gAllEntries.items():
        if len(arabic_matched_entries_1) < 20:
            for entry in list_of_entries:
                if len(arabic_matched_entries_1) < 20:
                    arabic_word = entry.regex_search_fields(compiled_regex)
                    if entry.regex_search_fields(compiled_regex):
                        if entry.arabic in arabic_matched_words:
                            pass
                        else:
                            arabic_matched_words.append(entry.arabic)
                            arabic_matched_entries_1.append((entry, arabic_word))
    return arabic_matched_entries_1

def arabic_regex_search_2(ial):
    #print "===== arabic_regex_search_2"
    filler = "(.){0,2}"
    #print filler
    arabic_regex_list = list(itertools.chain.from_iterable(zip(ial, [filler] * len(ial))))
    del arabic_regex_list[-1]
    arabic_regex_list.append("(.?)")
    begin_word = "^"
    end_word = "$"
    arabic_regex_list.insert(0, begin_word)
    arabic_regex_list.append(end_word)
    #print arabic_regex_list
    arabic_regex = "".join(arabic_regex_list)
    #print arabic_regex
    
    arabic_matched_entries_2 = []
    arabic_matched_words = []
    compiled_regex = re.compile(arabic_regex)
    #print compiled_regex
    for english, list_of_entries in gAllEntries.items():
        if len(arabic_matched_entries_2) < 20:
            for entry in list_of_entries:
                if len(arabic_matched_entries_2) < 20:
                    arabic_word = entry.regex_search_fields(compiled_regex)
                    if entry.regex_search_fields(compiled_regex):
                        if entry.arabic in arabic_matched_words:
                            pass
                        else:
                            arabic_matched_words.append(entry.arabic)
                            arabic_matched_entries_2.append((entry, arabic_word))
    return arabic_matched_entries_2
        
def arabic_regex_search_3(ial):
    #print "===== arabic_regex_search_3"
    filler = "(.{0,2})"
    #"((\S?)|((\S?)(\S?))|((\S?)(\S?)(\S?)))"
    #"(([^ ]?)|([^ ][^ ]?))" another way
    #"((.?)|(..?))" yet another
    #print filler
    arabic_regex_list = list(itertools.chain.from_iterable(zip(ial, [filler] * len(ial))))
    del arabic_regex_list[-1]
    begin_word = "^"
    end_word = ""
    arabic_regex_list.insert(0, begin_word)
    arabic_regex_list.append(end_word)
    #print arabic_regex_list
    arabic_regex = "".join(arabic_regex_list)
    #print arabic_regex
    
    arabic_matched_entries_3 = []
    arabic_matched_words = []
    compiled_regex = re.compile(arabic_regex)
    #print compiled_regex
    for english, list_of_entries in gAllEntries.items():
        if len(arabic_matched_entries_3) < 20:
            for entry in list_of_entries:
                if len(arabic_matched_entries_3) < 20:
                    arabic_word = entry.regex_search_fields(compiled_regex)
                    if entry.regex_search_fields(compiled_regex):
                        if entry.arabic in arabic_matched_words:
                            pass
                        else:
                            arabic_matched_words.append(entry.arabic)
                            arabic_matched_entries_3.append((entry, arabic_word))
    return arabic_matched_entries_3

def arabic_regex_search_4(ial):
    #print "===== arabic_regex_search_4"
    filler = "(.{0,3})"
    #print filler
    arabic_regex_list = list(itertools.chain.from_iterable(zip(ial, [filler] * len(ial))))
    del arabic_regex_list[-1]
    arabic_regex_list.append("(.?)")
    begin_word = ""
    end_word = "$"
    #arabic_regex_list.insert(0, begin_word)
    arabic_regex_list.append(end_word)
    #print arabic_regex_list
    arabic_regex = "".join(arabic_regex_list)
    #print arabic_regex
    
    arabic_matched_entries_4 = []
    arabic_matched_words = []
    compiled_regex = re.compile(arabic_regex)
    #print compiled_regex
    for english, list_of_entries in gAllEntries.items():
        if len(arabic_matched_entries_4) < 20:
            for entry in list_of_entries:
                if len(arabic_matched_entries_4) < 20:
                    arabic_word = entry.regex_search_fields(compiled_regex)
                    if entry.regex_search_fields(compiled_regex):
                        if entry.arabic in arabic_matched_words:
                            pass
                        else:
                            arabic_matched_words.append(entry.arabic)
                            arabic_matched_entries_4.append((entry, arabic_word))
    return arabic_matched_entries_4

def arabic_regex_search_5(ial):
    #print "===== arabic_regex_search_5"
    filler = "(.{0,3})"
    #"(([\S?][\S?][\S?][\S?]))"
    #"(([^ ]?)|([^ ][^ ]?)|([^ ][^ ][^ ]?)|([^ ][^ ][^ ][^ ]?))"
    #print filler
    arabic_regex_list = list(itertools.chain.from_iterable(zip(ial, [filler] * len(ial))))
    del arabic_regex_list[-1]
    begin_word = ""
    arabic_regex_list.insert(0, begin_word)
    #print arabic_regex_list
    arabic_regex = "".join(arabic_regex_list)
    #print arabic_regex
    
    arabic_matched_entries_5 = []
    arabic_matched_words = []
    compiled_regex = re.compile(arabic_regex)
    #print compiled_regex
    for english, list_of_entries in gAllEntries.items():
        if len(arabic_matched_entries_5) < 20:
            for entry in list_of_entries:
                if len(arabic_matched_entries_5) < 20:
                    arabic_word = entry.regex_search_fields(compiled_regex)
                    if entry.regex_search_fields(compiled_regex):
                        if entry.arabic in arabic_matched_words:
                            pass
                        else:
                            arabic_matched_words.append(entry.arabic)
                            arabic_matched_entries_5.append((entry, arabic_word))
    return arabic_matched_entries_5

def incl_arab_matches(search_term):
    ial = arabic_regex_term(search_term)
    filler = r'(.{0,2})'
    #print filler
    arabic_regex_list = list(itertools.chain.from_iterable(zip(ial, [filler] * len(ial))))
    del arabic_regex_list[-1]
    arabic_regex_list.append("(.?)")
    def_article = u'\u0627\u0644'
    arabic_regex = "".join(arabic_regex_list)
    new_search_term = '^' + r'\b' + '(' + def_article + ')' + '?' + arabic_regex + r'\b'
    compiled_regex = re.compile(new_search_term, re.U)
    #print new_search_term
    #print compiled_regex
    
    more_matches = []
    #arabic_matched_words = []
    #compiled_regex = re.compile(arabic_regex)
    #print compiled_regex
    for english, list_of_entries in gAllEntries.items():
        if len(more_matches) < 20:
            for entry in list_of_entries:
                if len(more_matches) < 20:
                    arabic_word = entry.regex_search_fields(compiled_regex)
                    if entry.regex_search_fields(compiled_regex):
                        #arabic_matched_words.append(entry.arabic)
                        more_matches.append((entry, arabic_word))

    new_search_term_2 = r'\b' + '(' + def_article + ')' + '?' + arabic_regex + r'\b'
    compiled_regex_2 = re.compile(new_search_term_2, re.U)
    #print new_search_term_2
    #print compiled_regex_2
    for english, list_of_entries in gAllEntries.items():
        if len(more_matches) < 20:
            for entry in list_of_entries:
                if len(more_matches) < 20:
                    arabic_word = entry.regex_search_fields(compiled_regex_2)
                    if entry.regex_search_fields(compiled_regex_2):
                        #arabic_matched_words.append(entry.arabic)
                        more_matches.append((entry, arabic_word))
    return more_matches

def remove_dup(ordered_list):
    seen = set()
    seen_add = seen.add
    return [ x for x in ordered_list if x not in seen and not seen_add(x)]

def search_entries(search_term):
    if search_term in gAllEntries.keys():
        entries_found = []
        for entry in gAllEntries[search_term]:
            #print "Found via english: %s" % entry.retrieve_arabic()
            word = entry.arabic
            #print list(word)
            #print gAllEntries.values[1]
            #unicode_word = unicode(word, encoding='utf-8')
            #print list(unicode_word)
            entries_found.append((entry, 0))
        additional_matches = contained_matches(search_term)
        for entry in additional_matches:
            entries_found.append((entry, 0))
        unique_entries = remove_dup(entries_found)
        return unique_entries

    #print "NOT FOUND VIA ENGLISH"
    matched_entries = reverse_search_entries(search_term)
    if len(matched_entries) > 0:
        entries_found = []
        for match in matched_entries:
            #print "Found via arabic: %s" % entry.retrieve_english()
            entries_found.append((match, 2))
        more_matches = incl_arab_matches(search_term)
        for match in more_matches:
            entries_found.append((match, 2))
        unique_entries = remove_dup(entries_found)
        return unique_entries

    regex_results = all_regex_searches(search_term)
    if len(regex_results) > 0:
        return regex_results

    else:
        #print "The word \"%s\" was not found." % search_term
        return [(None, 4)]

def all_regex_searches(search_term):
    search_term_2 = remove_punct(search_term)
    matched_regex_entries_1 = regex_search_1(search_term_2)
    matched_regex_entries_2 = regex_search_2(search_term_2)
    matched_regex_entries_3 = regex_search_3(search_term_2)
    matched_regex_entries_4 = regex_search_4(search_term_2)
    #matched_regex_entries_5 = regex_search_5(search_term_2)
    all_matched_regex_entries = matched_regex_entries_1 + matched_regex_entries_2 + \
    matched_regex_entries_3 + matched_regex_entries_4# + matched_regex_entries_5
    unique_matched_regex_entries = remove_dup(all_matched_regex_entries)
    if len(unique_matched_regex_entries) > 0:
        entries_found = []
        for entry in unique_matched_regex_entries:
            #print "Did you mean: %s" % entry.retrieve_english()
            entries_found.append((entry, 1))
        return entries_found

    important_arabic_letters = arabic_regex_term(search_term_2)
    arabic_matched_entries_1 = arabic_regex_search_1(important_arabic_letters)
    arabic_matched_entries_2 = arabic_regex_search_2(important_arabic_letters)
    arabic_matched_entries_3 = arabic_regex_search_3(important_arabic_letters)
    arabic_matched_entries_4 = arabic_regex_search_4(important_arabic_letters)
    arabic_matched_entries_5 = arabic_regex_search_5(important_arabic_letters)
    #These are now all tuples!  The entry AND the matching arabic word from within that entry.
    all_arabic_matched_entries = arabic_matched_entries_1 + arabic_matched_entries_2 + \
    arabic_matched_entries_3 + arabic_matched_entries_4 + arabic_matched_entries_5
    unique_arabic_matched_entries = remove_dup(all_arabic_matched_entries)
    if len(unique_arabic_matched_entries) > 0:
        entries_found = []
        for entry, word in unique_arabic_matched_entries:
            #print "Did you mean: %s" % word#entry.regex_search_fields()
            entries_found.append(((entry, word), 3))
            #print word
        return entries_found

    else:
        return []

def filter_main_diacritics(search_term):
    fatha = u'\u064e'
    damma = u'\u064f'
    kasra = u'\u0650'
    shadda = u'\u0651'
    sukun = u'\u0652'
    maddah = u'\u0653'
    hamza_above = u'\u0654'
    hamza_below = u'\u0655'
    #special_letters = [fatha, damma, kasra, shadda, sukun, maddah, hamza_above, hamza_below]

    unicode_letters = list(search_term)
    #print unicode_letters
    fatha_filtered = list(filter((fatha).__ne__, unicode_letters))
    damma_filtered = list(filter((damma).__ne__, fatha_filtered))
    kasra_filtered = list(filter((kasra).__ne__, damma_filtered))
    shadda_filtered = list(filter((shadda).__ne__, kasra_filtered))
    sukun_filtered = list(filter((sukun).__ne__, shadda_filtered))
    maddah_filtered = list(filter((maddah).__ne__, sukun_filtered))
    hamza_above_filtered = list(filter((hamza_above).__ne__, maddah_filtered))
    hamza_below_filtered = list(filter((hamza_below).__ne__, hamza_above_filtered))
    filtered_term = "".join(hamza_below_filtered)
    return filtered_term

def arabic_regex_term(search_term):
    filtered_term = filter_main_diacritics(search_term)

    alif_maddah = u'\u0622'
    alif_hamza_above = u'\u0623'
    alif_hamza_below = u'\u0625'
    alif = u'\u0627'

    #alifs_list = [alif_maddah, alif_hamza_above, alif_hamza_below, alif]
    #unc_alifs = "".join(alifs_list)

    #reg_alifs = re.compile(ur'[\u0622\u0623\u0625\u0627]{1}', re.U)
    #subbed_alif_term = reg_alifs.sub(ur'[\u0622\u0623\u0625\u0627]', search_term)

    hamza_on_alif_maksura = u'\u0626'
    yah = u'\u064a'
    waw = u'\u0648'
    meem = u'\u0645'
    bah = u'\u0628'
    tah = u'\u062a'
    tah_marbuuta = u'\u0629'
    noon = u'\u0646'
    hah = u'\u0647'
    kaaf = u'\u0643'
    hah_heavy = u'\u062d'
    seen = u'\u0633'
    lam = u'\u0644'
    fah = u'\u0641'
    ein = u'\u0639'
    saad = u'\u0635'
    daal = u'\u062f'
    rah = u'\u0631'

    alif_maksura = u'\u0649'
    tah_heavy = u'\u0637'
    hamza = u'\u0621'
    waw_with_hamza = u'\u0624'
    
    #utf8_letters = [hamza_on_alif_maksura, yah, waw, meem, bah, tah_marbuuta, tah, noon,\
    #hah, kaaf, hah_heavy, seen, lam, fah, ein, saad, daal, rah]
    '''
    utf8_letters = [waw_with_hamza]
    
    unc_spec_lett = []
    for char in utf8_letters:
        unc_char = unicode(char, encoding='utf-8')
        unc_spec_lett.append(unc_char)
    print "unicode alifs: "
    print unc_spec_lett
    '''
    
    unicode_letters = list(filtered_term)
    
    alif_madda_replaced_list = [ur'[\u0622\u0623\u0625\u0627]' if x==alif_maddah else x for x in unicode_letters]
    alif_hamza_above_replaced_list = [ur'[\u0622\u0623\u0625\u0627]' if x==alif_hamza_above else x for x in alif_madda_replaced_list]
    alif_hamza_below_replaced_list = [ur'[\u0622\u0623\u0625\u0627]' if x==alif_hamza_below else x for x in alif_hamza_above_replaced_list]
    alif_replaced_list = [ur'[\u0622\u0623\u0625\u0627]' if x==alif else x for x in alif_hamza_below_replaced_list]
    
    #alif_maksura_replaced_list = ["[\xd9\x89\xd9\x8a]{1}" if x=="\xd9\x89" else x for x in alif_replaced_list]
    #yah_replaced_list = ["[\xd9\x89\xd9\x8a]{1}" if x=="\xd9\x8a" else x for x in alif_maksura_replaced_list]
    asterisk_replaced_list = ["(.)" if x=="*" else x for x in alif_replaced_list]
    important_arabic_letters = asterisk_replaced_list
    #print important_arabic_letters
    return important_arabic_letters


def get_regex_term(search_term):
    eng_letters_list = list(search_term)
    asterisk_replaced_list = replace_asterisk_in_english_list(eng_letters_list)
    filler = ".*"
    #filler.encode('utf-8')
    #print filler
    with_filler_list = list(itertools.chain.from_iterable(zip(asterisk_replaced_list, [filler] * len(asterisk_replaced_list))))
    del with_filler_list[-1]
    #print with_filler_list
    new_search_term = "".join(with_filler_list)
    #print new_search_term
    return new_search_term

def regex_search_5(search_term):
    #print "regex_search_5:", search_term
    new_endings = replace_endings(search_term)
    new_search_term = replace_asterisk_in_english_string(new_endings)
    new_search_term_2 = "^" + new_search_term + "?"
    #print new_search_term_2
    compiled_regex = re.compile(new_search_term, re.I)
    matched_regex_entries_5 = []
    matched_regex_english = []

    for key in gAllEntries.keys():
        if len(matched_regex_entries_5) < 20:
            for entry in gAllEntries[key]:
                if len(matched_regex_entries_5) < 20:
                    if compiled_regex.search(entry.english):
                        if entry.english in matched_regex_english:
                            pass
                        else:
                            matched_regex_english.append(entry.english)
                            matched_regex_entries_5.append(entry)
    ##print matched_regex_entries_5
    return matched_regex_entries_5

def regex_search_4(search_term):
    #print "regex_search_4:", search_term
    new_endings = replace_endings(search_term)
    new_search_term = replace_asterisk_in_english_string(new_endings)
    #print new_search_term
    compiled_regex = re.compile(new_search_term, re.I)
    matched_regex_entries_4 = []
    matched_regex_english = []

    for key in gAllEntries.keys():
        if len(matched_regex_entries_4) < 20:
            for entry in gAllEntries[key]:
                if len(matched_regex_entries_4) < 20:
                    if compiled_regex.search(entry.english):
                        if entry.english in matched_regex_english:
                            pass
                        else:
                            matched_regex_english.append(entry.english)
                            matched_regex_entries_4.append(entry)
    #print matched_regex_entries_4
    return matched_regex_entries_4

def regex_search_3(search_term):
    #print "regex_search_3:", search_term
    new_endings = replace_endings(search_term)
    new_search_term = replace_asterisk_in_english_string(new_endings)
    new_search_term_2 = new_search_term + "$"
    #print new_search_term_2
    compiled_regex = re.compile(new_search_term_2, re.I)
    matched_regex_entries_3 = []
    matched_regex_english = []

    for key in gAllEntries.keys():
        if len(matched_regex_entries_3) < 20:
            for entry in gAllEntries[key]:
                if len(matched_regex_entries_3) < 20:
                    if compiled_regex.search(entry.english):
                        if entry.english in matched_regex_english:
                            pass
                        else:
                            matched_regex_english.append(entry.english)
                            matched_regex_entries_3.append(entry)
    #print matched_regex_entries_3
    return matched_regex_entries_3

def regex_search_2(search_term):
    #print "regex_search_2:", search_term
    new_endings = replace_endings(search_term)
    new_search_term = replace_asterisk_in_english_string(new_endings)
    new_search_term_2 = "^" + new_search_term
    #print new_search_term_2
    compiled_regex = re.compile(new_search_term_2, re.I)
    matched_regex_entries_2 = []
    matched_regex_english = []

    for key in gAllEntries.keys():
        if len(matched_regex_entries_2) < 20:
            for entry in gAllEntries[key]:
                if len(matched_regex_entries_2) < 20:
                    if compiled_regex.search(entry.english):
                        if entry.english in matched_regex_english:
                            pass
                        else:
                            matched_regex_english.append(entry.english)
                            matched_regex_entries_2.append(entry)
    #print matched_regex_entries_2
    return matched_regex_entries_2

def regex_search_1(search_term):
    #print "regex_search_1:", search_term
    new_endings = replace_endings(search_term)
    new_search_term = replace_asterisk_in_english_string(new_endings)
    new_search_term_2 = "^" + new_search_term + "$"
    #print new_search_term_2
    compiled_regex = re.compile(new_search_term_2, re.I)
    matched_regex_entries_1 = []
    matched_regex_english = []
    
    for key in gAllEntries.keys():
        if len(matched_regex_entries_1) < 20:
            for entry in gAllEntries[key]:
                if len(matched_regex_entries_1) < 20:
                    if compiled_regex.search(entry.english):
                        if entry.english in matched_regex_english:
                            pass
                        else:
                            matched_regex_english.append(entry.english)
                            matched_regex_entries_1.append(entry)
                            #print entry
    #print matched_regex_entries_1
    return matched_regex_entries_1

def contained_matches(search_term):
    new_search_term = replace_asterisk_in_english_string(search_term)
    new_search_term_2 = replace_endings(new_search_term)
    new_search_term_3 = '^' + r'\b' + new_search_term_2 + '[(s)(es)]?' + '(ing)?' + r'\b'
    compiled_regex = re.compile(new_search_term_3, re.I)
    #print new_search_term_3
    #print compiled_regex
    additional_matches = []
    #matched_regex_english = []
    
    for key in gAllEntries.keys():
        if len(additional_matches) < 20:
            for entry in gAllEntries[key]:
                if len(additional_matches) < 20:
                    if compiled_regex.search(entry.english):
                        #matched_regex_english.append(entry.english)
                        additional_matches.append(entry)
                        #print entry

    new_search_term_4 = r'\b' + new_search_term_2 + '[(s)(es)]?' + '(ing)?' + r'\b'
    compiled_regex_2 = re.compile(new_search_term_4, re.I)
    #print new_search_term_4
    #print compiled_regex_2

    for key in gAllEntries.keys():
        if len(additional_matches) < 20:
            for entry in gAllEntries[key]:
                if len(additional_matches) < 20:
                    if compiled_regex_2.search(entry.english):
                        #matched_regex_english.append(entry.english)
                        additional_matches.append(entry)
                        #print entry

    #print additional_matches
    return additional_matches

def replace_endings(search_term):
    letters = list(search_term)
    if len(letters) >= 3:
        if (letters[-3] + letters[-2] + letters[-1]) == 'ing':
            del letters[-3]
            del letters[-2]
            del letters[-1]
            letters.append('[(e)(ing)]?')
    if len(letters) >= 2:
        if (letters[-2] + letters[-1]) == 'es':
            del letters[-2]
            del letters[-1]
            letters.append('[(e)(es)]?')
    if len(letters) >= 1:
        if letters[-1] == 's':
            del letters[-1]
            letters.append('(s)?')
    new_term = "".join(letters)
    return new_term

def remove_punct(search_term):
    half_removed = search_term.replace("(", ".?")
    paren_removed = half_removed.replace(")", ".?")
    comma_removed = paren_removed.replace(",", ".?")
    semic_removed = comma_removed.replace(";", ".?")
    colon_removed = semic_removed.replace(":", ".?")
    apostr_removed = colon_removed.replace("'", ".?")
    quote_removed = apostr_removed.replace("\"", ".?")
    hyphen_removed = quote_removed.replace("-", ".?")
    #space_removed = hyphen_removed.replace(" ", ".?")
    exclam_removed = hyphen_removed.replace("!", ".?")
    questi_removed = exclam_removed.replace("?", ".?")
    new_search_term = questi_removed
    return new_search_term

def replace_asterisk_in_english_list(list_with_asterisk):
    asterisk_replaced_list = ["(.)" if x=="*" else x for x in list_with_asterisk]
    #print asterisk_replaced_list
    return asterisk_replaced_list

def replace_asterisk_in_english_string(search_term):
    new_search_term = search_term.replace("*", "(.)")
    #print new_search_term
    return new_search_term

def PopulateDB(name_of_file):
    RetrieveEntriesFromFile(name_of_file, gAllEntries)

def main(name_of_file, search_term):
    PopulateDB(name_of_file)
    search_entries(search_term)

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print "##### ERROR: Please provide a file name and a search term"
        print "***** Example: python search_dict.py indexforvocab.txt walk"
        print "Exiting..."
        sys.exit()
    file_name = sys.argv[1]
    search_term = sys.argv[2]
    main(file_name, search_term)
