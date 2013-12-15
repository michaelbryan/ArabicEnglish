import sys
import re
import itertools

from Entry import Entry
from DictionaryRetrieval import RetrieveEntriesFromFile

#reload(sys)
#sys.setdefaultencoding('utf-8')

gAllEntries = {}

def reverse_search_entries(search_term):
    matched_entries = []
    for english, list_of_entries in gAllEntries.items():
        for entry in list_of_entries:
            if entry.search_fields(search_term):
                matched_entries.append(entry)
    return matched_entries

def arabic_regex_search_1(ial):
    print "===== arabic_regex_search_1"
    filler = ""
    #filler.encode('utf-8')
    print filler
    arabic_regex_list = list(itertools.chain.from_iterable(zip(ial, [filler] * len(ial))))
    del arabic_regex_list[-1]
    begin_word = "^"
    end_word = "$"
    arabic_regex_list.insert(0, begin_word)
    arabic_regex_list.append(end_word)
    print arabic_regex_list
    arabic_regex = "".join(arabic_regex_list)
    print arabic_regex
    
    arabic_matched_entries_1 = []
    compiled_regex = re.compile(arabic_regex)
    print compiled_regex
    for english, list_of_entries in gAllEntries.items():
        for entry in list_of_entries:
            if entry.regex_search_fields(compiled_regex, arabic_regex):
                arabic_matched_entries_1.append(entry)
    return arabic_matched_entries_1

def arabic_regex_search_2(ial):
    print "===== arabic_regex_search_2"
    filler = "(\S?)"
    #filler.encode('utf-8')
    print filler
    arabic_regex_list = list(itertools.chain.from_iterable(zip(ial, [filler] * len(ial))))
    #del arabic_regex_list[-1]
    begin_word = "^"
    end_word = "$"
    arabic_regex_list.insert(0, begin_word)
    arabic_regex_list.append(end_word)
    print arabic_regex_list
    arabic_regex = "".join(arabic_regex_list)
    print arabic_regex
    
    arabic_matched_entries_2 = []
    compiled_regex = re.compile(arabic_regex)
    print compiled_regex
    for english, list_of_entries in gAllEntries.items():
        for entry in list_of_entries:
            if entry.regex_search_fields(compiled_regex, arabic_regex):
                arabic_matched_entries_2.append(entry)
    return arabic_matched_entries_2
        
def arabic_regex_search_3(ial):
    print "===== arabic_regex_search_3"
    filler = "(\S{0,3})"
    #"((\S?)|((\S?)(\S?))|((\S?)(\S?)(\S?)))"
    #"(([^ ]?)|([^ ][^ ]?))" another way
    #"((.?)|(..?))" yet another
    #filler.encode('utf-8')
    print filler
    arabic_regex_list = list(itertools.chain.from_iterable(zip(ial, [filler] * len(ial))))
    del arabic_regex_list[-1]
    begin_word = "^"
    end_word = ""
    arabic_regex_list.insert(0, begin_word)
    arabic_regex_list.append(end_word)
    print arabic_regex_list
    arabic_regex = "".join(arabic_regex_list)
    print arabic_regex
    
    arabic_matched_entries_3 = []
    compiled_regex = re.compile(arabic_regex)
    print compiled_regex
    for english, list_of_entries in gAllEntries.items():
        for entry in list_of_entries:
            if entry.regex_search_fields(compiled_regex, arabic_regex):
                arabic_matched_entries_3.append(entry)
    return arabic_matched_entries_3

def arabic_regex_search_4(ial):
    print "===== arabic_regex_search_4"
    filler = "(\w{0,3})"
    #filler.encode('utf-8')
    print filler
    arabic_regex_list = list(itertools.chain.from_iterable(zip(ial, [filler] * len(ial))))
    del arabic_regex_list[-1]
    begin_word = ""
    end_word = "$"
    #arabic_regex_list.insert(0, begin_word)
    arabic_regex_list.append(end_word)
    print arabic_regex_list
    arabic_regex = "".join(arabic_regex_list)
    print arabic_regex
    
    arabic_matched_entries_4 = []
    compiled_regex = re.compile(arabic_regex)
    print compiled_regex
    for english, list_of_entries in gAllEntries.items():
        for entry in list_of_entries:
            if entry.regex_search_fields(compiled_regex, arabic_regex):
                arabic_matched_entries_4.append(entry)
    return arabic_matched_entries_4

def arabic_regex_search_5(ial):
    print "===== arabic_regex_search_5"
    filler = "(\S)*"
    #"(([\S?][\S?][\S?][\S?]))"
    #"(([^ ]?)|([^ ][^ ]?)|([^ ][^ ][^ ]?)|([^ ][^ ][^ ][^ ]?))"
    #filler.encode('utf-8')
    print filler
    arabic_regex_list = list(itertools.chain.from_iterable(zip(ial, [filler] * len(ial))))
    del arabic_regex_list[-1]
    begin_word = ""
    arabic_regex_list.insert(0, begin_word)
    print arabic_regex_list
    arabic_regex = "".join(arabic_regex_list)
    print arabic_regex
    
    matched_regex_entries_5 = []
    compiled_regex = re.compile(arabic_regex)
    print compiled_regex
    for english, list_of_entries in gAllEntries.items():
        for entry in list_of_entries:
            if entry.regex_search_fields(compiled_regex, arabic_regex):
                matched_regex_entries_5.append(entry)
    return matched_regex_entries_5

def remove_dup(ordered_list):
    seen = set()
    seen_add = seen.add
    return [ x for x in ordered_list if x not in seen and not seen_add(x)]

def search_entries(search_term):
    if search_term in gAllEntries.keys():
        for entry in gAllEntries[search_term]:
            print "Found via english: %s" % entry.retrieve_arabic()
        return True

    matched_regex_entries_1 = regex_search_1(search_term)
    matched_regex_entries_2 = regex_search_2(search_term)
    matched_regex_entries_3 = regex_search_3(search_term)
    matched_regex_entries_4 = regex_search_4(search_term)
    all_matched_regex_entries = matched_regex_entries_1 + matched_regex_entries_2 + matched_regex_entries_3 + matched_regex_entries_4
    unique_matched_regex_entries = remove_dup(all_matched_regex_entries)
    if len(unique_matched_regex_entries) > 0:
        for entry in unique_matched_regex_entries:
            print "Did you mean: %s" % entry.retrieve_english()
        return True

    print "NOT FOUND VIA ENGLISH"
    matched_entries = reverse_search_entries(search_term)
    if len(matched_entries) > 0:
        for entry in matched_entries:
            print "Found via arabic: %s" % entry.retrieve_english()
        return True

    print "NOT FOUND VIA ARABIC"
    important_arabic_letters = arabic_regex_term(search_term)
    arabic_matched_entries_1 = arabic_regex_search_1(important_arabic_letters)
    arabic_matched_entries_2 = arabic_regex_search_2(important_arabic_letters)
    arabic_matched_entries_3 = arabic_regex_search_3(important_arabic_letters)
    arabic_matched_entries_4 = arabic_regex_search_4(important_arabic_letters)
    arabic_matched_entries_5 = arabic_regex_search_5(important_arabic_letters)
    all_arabic_matched_entries = arabic_matched_entries_1 + arabic_matched_entries_2 + arabic_matched_entries_3 + arabic_matched_entries_4 + arabic_matched_entries_5
    unique_arabic_matched_entries = remove_dup(all_arabic_matched_entries)
    if len(unique_arabic_matched_entries) > 0:
        for entry in unique_arabic_matched_entries:
            print "Did you mean: %s" % entry#.retrieve_just_arabic()
        return True

    else:
        print "The word \"%s\" was not found." % search_term
        return False

def arabic_regex_term(search_term):
    fatha = "\xd9\x8e"
    damma = "\xd9\x8f"
    kasra = "\xd9\x90"
    shadda = "\xd9\x91"
    sukun = "\xd9\x92"
    maddah = "\xd9\x93"
    hamza_above = "\xd9\x94"
    hamza_below = "\xd9\x95"
    new_search_term = search_term.replace("*", "**")
    #This is just to maintain an even number of elements in the list of split utf-8 encodings.
    broken_unicode = list(new_search_term)
    print broken_unicode
    arabic_letters = [i+j for i,j in zip(broken_unicode[::2],broken_unicode[1::2])]
    print arabic_letters
    fatha_filtered = list(filter((fatha).__ne__, arabic_letters))
    damma_filtered = list(filter((damma).__ne__, fatha_filtered))
    kasra_filtered = list(filter((kasra).__ne__, damma_filtered))
    shadda_filtered = list(filter((shadda).__ne__, kasra_filtered))
    sukun_filtered = list(filter((sukun).__ne__, shadda_filtered))
    maddah_filtered = list(filter((maddah).__ne__, sukun_filtered))
    hamza_above_filtered = list(filter((hamza_above).__ne__, maddah_filtered))
    hamza_below_filtered = list(filter((hamza_below).__ne__, hamza_above_filtered))
    alif_madda_replaced_list = ["[\xd8\xa2\xd8\xa3\xd8\xa5\xd8\xa7]{1}" if x=="\xd8\xa2" else x for x in hamza_below_filtered]
    alif_hamza_above_replaced_list = ["[\xd8\xa2\xd8\xa3\xd8\xa5\xd8\xa7]{1}" if x=="\xd8\xa3" else x for x in alif_madda_replaced_list]
    alif_hamza_below_replaced_list = ["[\xd8\xa2\xd8\xa3\xd8\xa5\xd8\xa7]{1}" if x=="\xd8\xa5" else x for x in alif_hamza_above_replaced_list]
    alif_replaced_list = ["[\xd8\xa2\xd8\xa3\xd8\xa5\xd8\xa7]{1}" if x=="\xd8\xa7" else x for x in alif_hamza_below_replaced_list]
    #alif_maksura_replaced_list = ["[\xd9\x89\xd9\x8a]{1}" if x=="\xd9\x89" else x for x in alif_replaced_list]
    #yah_replaced_list = ["[\xd9\x89\xd9\x8a]{1}" if x=="\xd9\x8a" else x for x in alif_maksura_replaced_list]
    asterisk_replaced_list = ["(\S{1,2})" if x=="**" else x for x in alif_replaced_list]
    important_arabic_letters = asterisk_replaced_list
    print important_arabic_letters
    return important_arabic_letters
    #uni_arabic_regex = unicode(arabic_regex, 'utf-8')
    #print uni_arabic_regex
    #return uni_arabic_regex
    #unicode(string[, encoding, errors])
    #.encode([encoding], [errors='strict'])
    #cell = str(cell)

def get_regex_term(search_term):
    eng_letters_list = list(search_term)
    asterisk_replaced_list = replace_asterisk_in_english_list(eng_letters_list)
    filler = ".*"
    #filler.encode('utf-8')
    print filler
    with_filler_list = list(itertools.chain.from_iterable(zip(asterisk_replaced_list, [filler] * len(asterisk_replaced_list))))
    del with_filler_list[-1]
    print with_filler_list
    new_search_term = "".join(with_filler_list)
    print new_search_term
    return new_search_term

def regex_search_4(search_term):
    print "regex_search_4:", search_term
    new_search_term = get_regex_term(search_term)
    compiled_regex = re.compile(new_search_term, re.I)
    matched_regex_entries_4 = []

    for key in gAllEntries.keys():
        for entry in gAllEntries[key]:
            if compiled_regex.search(entry.english):
                matched_regex_entries_4.append(entry)
    return matched_regex_entries_4

def regex_search_3(search_term):
    print "regex_search_3:", search_term
    new_search_term = replace_asterisk_in_english_string(search_term)
    compiled_regex = re.compile(new_search_term, re.I)
    matched_regex_entries_3 = []

    for key in gAllEntries.keys():
        for entry in gAllEntries[key]:
            if compiled_regex.search(entry.english):
                matched_regex_entries_3.append(entry)
    return matched_regex_entries_3

def regex_search_2(search_term):
    print "regex_search_2:", search_term
    new_search_term = replace_asterisk_in_english_string(search_term)
    new_search_term_2 = "^" + new_search_term
    print new_search_term_2
    compiled_regex = re.compile(new_search_term_2, re.I)
    matched_regex_entries_2 = []

    for key in gAllEntries.keys():
        for entry in gAllEntries[key]:
            if compiled_regex.search(entry.english):
                matched_regex_entries_2.append(entry)
    return matched_regex_entries_2

def regex_search_1(search_term):
    print "regex_search_1:", search_term
    new_search_term = replace_asterisk_in_english_string(search_term)
    new_search_term_2 = "^" + new_search_term + "$"
    print new_search_term_2
    compiled_regex = re.compile(new_search_term_2, re.I)
    matched_regex_entries_1 = []
    
    for key in gAllEntries.keys():
        for entry in gAllEntries[key]:
            if compiled_regex.search(entry.english):
                matched_regex_entries_1.append(entry)
    return matched_regex_entries_1

def replace_asterisk_in_english_list(list_with_asterisk):
    asterisk_replaced_list = ["(.)" if x=="*" else x for x in list_with_asterisk]
    print asterisk_replaced_list
    return asterisk_replaced_list

def replace_asterisk_in_english_string(search_term):
    new_search_term = search_term.replace("*", "(.)")
    print new_search_term
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
