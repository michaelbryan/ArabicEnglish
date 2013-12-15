class Entry:
    def __init__(self, line):
        fields = line.split("|")

        self.english = fields[0]
        self.page = fields[1]
        self.plural_type = fields[2]
        self.arabic = fields[3]
        self.plural = fields[4]
        self.alt_plural = fields[5]
        self.fem_sing = fields[6]
        self.fem_plural = fields[7]
        self.part_of_speech = fields[8]
        self.verb_type = fields[9]

    def verb_chart_1a(self):
        broken_unicode = list(self.arabic)
        print broken_unicode
        arabic_letters = [i+j for i,j in zip(broken_unicode[::2],broken_unicode[1::2])]
        print arabic_letters
        fatha = "\xd9\x8e"
        damma = "\xd9\x8f"
        kasra = "\xd9\x90"
        shadda = "\xd9\x91"
        sukun = "\xd9\x92"
        maddah = "\xd9\x93"
        hamza_above = "\xd9\x94"
        hamza_below = "\xd9\x95"
        yah = "\xd9\x8a"
        waw = "\xd9\x88"
        alif = "\xd8\xa7"
        alif_hamza_above = "\xd8\xa3"
        alif_hamza_below = "\xd8\xa5"
        meem = "\xd9\x85"
        bah = "\xd8\xa8"
        tah = "\xd8\xaa"
        tah_marbuuta = "\xd8\xa9"
        noon = "\xd9\x86"
        hah = "\xd9\x87"
        kaaf = "\xd9\x83"
        hah_heavy = "\xd8\xad"
        #these arabic letters are commonly used in conjugations
        fatha_filtered = list(filter((fatha).__ne__, arabic_letters))
        damma_filtered = list(filter((damma).__ne__, fatha_filtered))
        kasra_filtered = list(filter((kasra).__ne__, damma_filtered))
        shadda_filtered = list(filter((shadda).__ne__, kasra_filtered))
        sukun_filtered = list(filter((sukun).__ne__, shadda_filtered))
        maddah_filtered = list(filter((maddah).__ne__, sukun_filtered))
        hamza_above_filtered = list(filter((hamza_above).__ne__, maddah_filtered))
        hamza_below_filtered = list(filter((hamza_below).__ne__, hamza_above_filtered))
        #meem_filtered = list(filter((meem).__ne__, hamza_below_filtered))
        #if "\xd9\x8e" in arabic_letters: arabic_letters.remove("\xd9\x8e")
        #if "\xd9\x8f" in arabic_letters: arabic_letters.remove("\xd9\x8f")
        #if "\xd9\x90" in arabic_letters: arabic_letters.remove("\xd9\x90")
        #if "\xd9\x91" in arabic_letters: arabic_letters.remove("\xd9\x91")
        #if "\xd9\x92" in arabic_letters: arabic_letters.remove("\xd9\x92")
        #if "\xd9\x93" in arabic_letters: arabic_letters.remove("\xd9\x93")
        #if "\xd9\x94" in arabic_letters: arabic_letters.remove("\xd9\x94")
        #if "\xd9\x95" in arabic_letters: arabic_letters.remove("\xd9\x95")
        arabic_root = hamza_below_filtered
        first_root_letter = arabic_root[0]
        second_root_letter = arabic_root[1]
        third_root_letter = arabic_root[2]
        print first_root_letter
        print second_root_letter
        print third_root_letter
        print arabic_root
        he_past_broken = [first_root_letter, fatha, second_root_letter, fatha, third_root_letter]
        he_past_string = "".join(he_past_broken)
        verb_columns_list = [he_past_string, "Past", "Present", "Command", "Following a Verb", "With Pronoun"]
        print he_past_string
        print verb_columns_list
        i_arabic_broken = [alif_hamza_above, fatha, noon, alif]
        i_arabic_string = "".join(i_arabic_broken)
        i_past_broken = [first_root_letter, fatha, second_root_letter, fatha, third_root_letter, sukun, tah]
        i_past_string = "".join(i_past_broken)
        i_present_b_broken = [bah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        i_present_b_string = "".join(i_present_b_broken)
        i_command_string = ""
        i_present_broken = [alif_hamza_above, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        i_present_string = "".join(i_present_broken)
        i_present_with_pronoun_broken = [alif_hamza_above, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, sukun, hah, damma, meem]
        i_present_with_pronoun_string = "".join(i_present_with_pronoun_broken)
        i_conjugations_list = [i_arabic_string, i_past_string, i_present_b_string, i_command_string, i_present_string, i_present_with_pronoun_string]
        print i_arabic_string + "\n"
        print i_past_string + "\n"
        print i_present_b_string + "\n"
        print i_command_string + "\n"
        print i_present_string + "\n"
        print i_present_with_pronoun_string + "\n"
        print i_conjugations_list
        you_m_arabic_broken = [alif_hamza_below, noon, sukun, tah, fatha]
        you_m_arabic_string = "".join(you_m_arabic_broken)
        you_m_past_broken = [first_root_letter, fatha, second_root_letter, fatha, third_root_letter, sukun, tah]
        you_m_past_string = "".join(you_m_past_broken)
        you_m_present_b_broken = [bah, sukun, tah, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        you_m_present_b_string = "".join(you_m_present_b_broken)
        you_m_command_broken = [alif_hamza_below, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        you_m_command_string = "".join(you_m_command_broken)
        you_m_present_broken = [tah, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        you_m_present_string = "".join(you_m_present_broken)
        you_m_present_with_pronoun_broken = [tah, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, damma, hah]
        you_m_present_with_pronoun_string = "".join(you_m_present_with_pronoun_broken)
        you_m_conjugations_list = [you_m_arabic_string, you_m_past_string, you_m_present_b_string, you_m_command_string, you_m_present_string, you_m_present_with_pronoun_string]
        print you_m_arabic_string + "\n"
        print you_m_past_string + "\n"
        print you_m_present_b_string + "\n"
        print you_m_command_string + "\n"
        print you_m_present_string + "\n"
        print you_m_present_with_pronoun_string + "\n"
        print you_m_conjugations_list
        you_f_arabic_broken = [alif_hamza_below, noon, sukun, tah, kasra, yah]
        you_f_arabic_string = "".join(you_f_arabic_broken)
        you_f_past_broken = [first_root_letter, fatha, second_root_letter, fatha, third_root_letter, sukun, tah, kasra, yah]
        you_f_past_string = "".join(you_f_past_broken)
        you_f_present_b_broken = [bah, sukun, tah, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, kasra, yah]
        you_f_present_b_string = "".join(you_f_present_b_broken)
        you_f_command_broken = [alif_hamza_below, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, kasra, yah]
        you_f_command_string = "".join(you_f_command_broken)
        you_f_present_broken = [tah, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, kasra, yah]
        you_f_present_string = "".join(you_f_present_broken)
        you_f_present_with_pronoun_broken = [tah, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, kasra, yah, hah, alif]
        you_f_present_with_pronoun_string = "".join(you_f_present_with_pronoun_broken)
        you_f_conjugations_list = [you_f_arabic_string, you_f_past_string, you_f_present_b_string, you_f_command_string, you_f_present_string, you_f_present_with_pronoun_string]
        print you_f_arabic_string + "\n"
        print you_f_past_string + "\n"
        print you_f_present_b_string + "\n"
        print you_f_command_string + "\n"
        print you_f_present_string + "\n"
        print you_f_present_with_pronoun_string + "\n"
        print you_f_conjugations_list
        he_arabic_broken = [hah, damma, waw, shadda, fatha]
        he_arabic_string = "".join(he_arabic_broken)
        he_past_broken = [first_root_letter, fatha, second_root_letter, fatha, third_root_letter]
        he_past_string = "".join(he_past_broken)
        he_present_b_broken = [bah, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        he_present_b_string = "".join(he_present_b_broken)
        he_command_string = ""
        he_present_broken = [yah, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        he_present_string = "".join(he_present_broken)
        he_present_with_pronoun_broken = [yah, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, fatha, kaaf]
        he_present_with_pronoun_string = "".join(he_present_with_pronoun_broken)
        he_conjugations_list = [he_arabic_string, he_past_string, he_present_b_string, he_command_string, he_present_string, he_present_with_pronoun_string]
        print he_arabic_string + "\n"
        print he_past_string + "\n"
        print he_present_b_string + "\n"
        print he_command_string + "\n"
        print he_present_string + "\n"
        print he_present_with_pronoun_string + "\n"
        print he_conjugations_list
        she_arabic_broken = [hah, kasra, yah, shadda, fatha]
        she_arabic_string = "".join(she_arabic_broken)
        she_past_broken = [first_root_letter, fatha, second_root_letter, fatha, third_root_letter, fatha, tah]
        she_past_string = "".join(she_past_broken)
        she_present_b_broken = [bah, sukun, tah, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        she_present_b_string = "".join(she_present_b_broken)
        she_command_string = ""
        she_present_broken = [tah, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        she_present_string = "".join(she_present_broken)
        she_present_with_pronoun_broken = [tah, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, kasra, kaaf]
        she_present_with_pronoun_string = "".join(she_present_with_pronoun_broken)
        she_conjugations_list = [she_arabic_string, she_past_string, she_present_b_string, she_command_string, she_present_string, she_present_with_pronoun_string]
        print she_arabic_string + "\n"
        print she_past_string + "\n"
        print she_present_b_string + "\n"
        print she_command_string + "\n"
        print she_present_string + "\n"
        print she_present_with_pronoun_string + "\n"
        print she_conjugations_list
        we_arabic_broken = [alif_hamza_below, kasra, hah_heavy, sukun, noon, alif]
        we_arabic_string = "".join(we_arabic_broken)
        we_past_broken = [first_root_letter, fatha, second_root_letter, fatha, third_root_letter, sukun, noon, alif]
        we_past_string = "".join(we_past_broken)
        we_present_b_broken = [meem, sukun, noon, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        we_present_b_string = "".join(we_present_b_broken)
        we_command_string = ""
        we_present_broken = [noon, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        we_present_string = "".join(we_present_broken)
        we_present_with_pronoun_broken = [noon, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, sukun, kaaf, damma, meem]
        we_present_with_pronoun_string = "".join(we_present_with_pronoun_broken)
        we_conjugations_list = [we_arabic_string, we_past_string, we_present_b_string, we_command_string, we_present_string, we_present_with_pronoun_string]
        print we_arabic_string + "\n"
        print we_past_string + "\n"
        print we_present_b_string + "\n"
        print we_command_string + "\n"
        print we_present_string + "\n"
        print we_present_with_pronoun_string + "\n"
        print we_conjugations_list
        you_all_arabic_broken = [alif_hamza_below, noon, sukun, tah, damma, waw, alif]
        you_all_arabic_string = "".join(you_all_arabic_broken)
        you_all_past_broken = [first_root_letter, fatha, second_root_letter, fatha, third_root_letter, sukun, tah, damma, waw, alif]
        you_all_past_string = "".join(you_all_past_broken)
        you_all_present_b_broken = [bah, sukun, tah, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, damma, waw, alif]
        you_all_present_b_string = "".join(you_all_present_b_broken)
        you_all_command_broken = [alif_hamza_below, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, damma, waw, alif]
        you_all_command_string = "".join(you_all_command_broken)
        you_all_present_broken = [tah, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, damma, waw, alif]
        you_all_present_string = "".join(you_all_present_broken)
        you_all_present_with_pronoun_broken = [tah, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, damma, waw, noon, alif]
        you_all_present_with_pronoun_string = "".join(you_all_present_with_pronoun_broken)
        you_all_conjugations_list = [you_all_arabic_string, you_all_past_string, you_all_present_b_string, you_all_command_string, you_all_present_string, you_all_present_with_pronoun_string]
        print you_all_arabic_string + "\n"
        print you_all_past_string + "\n"
        print you_all_present_b_string + "\n"
        print you_all_command_string + "\n"
        print you_all_present_string + "\n"
        print you_all_present_with_pronoun_string + "\n"
        print you_all_conjugations_list
        they_arabic_broken = [hah, damma, meem, shadda, fatha]
        they_arabic_string = "".join(they_arabic_broken)
        they_past_broken = [first_root_letter, fatha, second_root_letter, fatha, third_root_letter, damma, waw, alif]
        they_past_string = "".join(they_past_broken)
        they_present_b_broken = [bah, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, damma, waw, alif]
        they_present_b_string = "".join(they_present_b_broken)
        they_command_string = ""
        they_present_broken = [yah, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, damma, waw, alif]
        they_present_string = "".join(they_present_broken)
        they_present_with_pronoun_broken = [yah, kasra, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, damma, waw, noon, kasra, yah]
        they_present_with_pronoun_string = "".join(they_present_with_pronoun_broken)
        they_conjugations_list = [they_arabic_string, they_past_string, they_present_b_string, they_command_string, they_present_string, they_present_with_pronoun_string]
        print they_arabic_string + "\n"
        print they_past_string + "\n"
        print they_present_b_string + "\n"
        print they_command_string + "\n"
        print they_present_string + "\n"
        print they_present_with_pronoun_string + "\n"
        print they_conjugations_list
        #other arabic letters for naming parts of speech
        seen = "\xd8\xb3"
        lam = "\xd9\x84"
        fah = "\xd9\x81"
        ein = "\xd8\xb9"
        saad = "\xd8\xb5"
        daal = "\xd8\xaf"
        rah = "\xd8\xb1"
        word_active_participle_broken = [alif, seen, sukun, meem, " ", alif, lam, fah, alif, ein, kasra, lam]
        word_active_participle_string = "".join(word_active_participle_broken)
        word_direct_object_broken = [alif, seen, sukun, meem, " ", alif, lam, meem, fatha, fah, sukun, ein, damma, waw, lam]
        word_direct_object_string = "".join(word_direct_object_broken)
        word_verbal_noun_broken = [alif, lam, meem, fatha, saad, sukun, daal, fatha, rah]
        word_verbal_noun_string = "".join(word_verbal_noun_broken)
        active_participle_broken = [first_root_letter, alif, second_root_letter, kasra, third_root_letter]
        active_participle_string = "".join(active_participle_broken)
        direct_object_broken = [meem, fatha, first_root_letter, sukun, second_root_letter, damma, waw, third_root_letter]
        direct_object_string = "".join(direct_object_broken)
        verbal_noun_broken = [first_root_letter, fatha, second_root_letter, kasra, third_root_letter]
        verbal_noun_string = "".join(verbal_noun_broken)
        print word_active_participle_string + ": " + active_participle_string + "\n"
        print word_direct_object_string + ": " + direct_object_string + "\n"
        print word_verbal_noun_string + ": " + verbal_noun_string + "\n"
        # youre now returning a list...
        return arabic_root

    def verb_chart_1b(self):
        arabic_root = list(self.arabic)
        print "".join(arabic_root[3:4])
        # youre now returning a list...
        return arabic_root

    def some_verb_chart(self):
        if self.verb_type == "1a":
            return self.verb_chart_1a()
        elif self.verb_type == "1b":
            return self.verb_chart_1b()
        else:
            print "##### ERROR: Unexpected input to some_verb_chart or verb type not assigned"
            return "CRAP"

    def retrieve_english(self):
        #english_string = "\n"
        #english_string += self.english + "\n"
        english_string = self.english
        return english_string

    def retrieve_just_arabic(self):
        arabic_string = " "
        arabic_string += self.arabic + " "
        arabic_string += self.part_of_speech + " "
        return arabic_string

    def retrieve_arabic(self):
        arabic_string = "\n"
        arabic_string += self.arabic + "\n"
        arabic_string += self.part_of_speech + "\n"
        if self.plural:
            arabic_string += "Plural: " + self.plural + "\n"
        if self.alt_plural:
            arabic_string += "Alt. Plural: " + self.alt_plural + "\n"
        if self.fem_sing:
            arabic_string += "Fem. Sing.: " + self.fem_sing + "\n"
        if self.fem_plural:
            arabic_string += "Fem. Plural: " + self.fem_plural + "\n"
        if self.part_of_speech == "v":
            # converting your list back to a string...
            arabic_string += "".join(self.some_verb_chart())
        return arabic_string
    
    def __str__(self):
        entry_string = "\n"
        entry_string += self.english + "\n"
        entry_string += self.arabic + "\n"
        entry_string += "".join(self.part_of_speech) + "\n"
        if self.plural:
            entry_string += "Plural: " + self.plural + "\n"
        if self.alt_plural:
            entry_string += "Alt. Plural: " + self.alt_plural + "\n"
        if self.fem_sing:
            entry_string += "Fem. Sing.: " + self.fem_sing + "\n"
        if self.fem_plural:
            entry_string += "Fem. Plural: " + self.fem_plural + "\n"
        return entry_string

    def search_fields(self, search_term):
        if search_term == self.page or search_term == self.plural_type or search_term == self.arabic or \
            search_term == self.plural or search_term == self.alt_plural or search_term == self.fem_sing or \
            search_term == self.fem_plural or search_term == self.part_of_speech:
            return True
        else:
            return False

    def regex_search_fields(self, compiled_regex, arabic_regex):
        '''
        if compiled_regex.search(self.arabic):
            return self.arabic
        elif compiled_regex.search(self.plural):
            return self.plural
        elif compiled_regex.search(self.alt_plural):
            return self.alt_plural
        elif compiled_regex.search(self.fem_sing):
            return self.fem_sing
        elif compiled_regex.search(self.fem_plural):
            return self.fem_plural
        else:
            return False
        '''
        if compiled_regex.search(self.arabic) or compiled_regex.search(self.plural) or \
            compiled_regex.search(self.alt_plural) or compiled_regex.search(self.fem_sing) or \
            compiled_regex.search(self.fem_plural):
            print "WOOOOOOOOOOOOOOOOOOOOOOOAH"
            return True
        else:
            return False