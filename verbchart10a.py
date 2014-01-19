# -*- coding: utf-8 -*-

from bidi.algorithm import get_display

import arabic_reshaper

class VerbChart10a:
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

        arabic_letters = list(self.arabic)
        #print arabic_letters
        #these arabic letters are commonly used in conjugations
        fatha = u'\u064e'
        damma = u'\u064f'
        kasra = u'\u0650'
        shadda = u'\u0651'
        sukun = u'\u0652'
        maddah = u'\u0653'
        hamza_above = u'\u0654'
        hamza_below = u'\u0655'

        alif_maddah = u'\u0622'
        alif_hamza_above = u'\u0623'
        alif_hamza_below = u'\u0625'
        alif = u'\u0627'

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
        alif_maksura = u'\u0649'
        tah_heavy = u'\u0637'
        hamza = u'\u0621'
        #other arabic letters for naming parts of speech
        seen = u'\u0633'
        lam = u'\u0644'
        fah = u'\u0641'
        ein = u'\u0639'
        saad = u'\u0635'
        daal = u'\u062f'
        rah = u'\u0631'
        
        fatha_filtered = list(filter((fatha).__ne__, arabic_letters))
        damma_filtered = list(filter((damma).__ne__, fatha_filtered))
        kasra_filtered = list(filter((kasra).__ne__, damma_filtered))
        shadda_filtered = list(filter((shadda).__ne__, kasra_filtered))
        sukun_filtered = list(filter((sukun).__ne__, shadda_filtered))
        maddah_filtered = list(filter((maddah).__ne__, sukun_filtered))
        hamza_above_filtered = list(filter((hamza_above).__ne__, maddah_filtered))
        hamza_below_filtered = list(filter((hamza_below).__ne__, hamza_above_filtered))
        
        arabic_root = hamza_below_filtered
        first_root_letter = arabic_root[3]
        second_root_letter = arabic_root[4]
        third_root_letter = arabic_root[5]
        print first_root_letter
        print second_root_letter
        print third_root_letter
        print arabic_root
        he_past_broken = [alif, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, fatha, third_root_letter]
        he_past_string = "".join(he_past_broken)
        verb_columns_list = [he_past_string, "Past", "Present", "Command", "Following a Verb", "With Pronoun"]
        print he_past_string
        print verb_columns_list
        i_arabic_broken = [alif_hamza_above, fatha, noon, alif]
        i_arabic_string = "".join(i_arabic_broken)
        i_past_broken = [alif, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, fatha, third_root_letter, sukun, tah]
        i_past_string = "".join(i_past_broken)
        i_present_b_broken = [bah, fatha, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        i_present_b_string = "".join(i_present_b_broken)
        i_command_string = ""
        i_present_broken = [alif_hamza_above, fatha, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        i_present_string = "".join(i_present_broken)
        i_present_with_pronoun_broken = [alif_hamza_above, fatha, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, sukun, hah, damma, meem]
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
        you_m_past_broken = [alif, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, fatha, third_root_letter, sukun, tah]
        you_m_past_string = "".join(you_m_past_broken)
        you_m_present_b_broken = [bah, sukun, tah, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        you_m_present_b_string = "".join(you_m_present_b_broken)
        you_m_command_broken = [alif, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        you_m_command_string = "".join(you_m_command_broken)
        you_m_present_broken = [tah, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        you_m_present_string = "".join(you_m_present_broken)
        you_m_present_with_pronoun_broken = [tah, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, damma, hah]
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
        you_f_past_broken = [alif, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, fatha, third_root_letter, sukun, tah, kasra, yah]
        you_f_past_string = "".join(you_f_past_broken)
        you_f_present_b_broken = [bah, sukun, tah, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, kasra, yah]
        you_f_present_b_string = "".join(you_f_present_b_broken)
        you_f_command_broken = [alif, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, kasra, yah]
        you_f_command_string = "".join(you_f_command_broken)
        you_f_present_broken = [tah, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, kasra, yah]
        you_f_present_string = "".join(you_f_present_broken)
        you_f_present_with_pronoun_broken = [tah, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, kasra, yah, hah, alif]
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
        he_past_broken = [alif, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, fatha, third_root_letter]
        he_past_string = "".join(he_past_broken)
        he_present_b_broken = [bah, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        he_present_b_string = "".join(he_present_b_broken)
        he_command_string = ""
        he_present_broken = [yah, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        he_present_string = "".join(he_present_broken)
        he_present_with_pronoun_broken = [yah, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, fatha, kaaf]
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
        she_past_broken = [alif, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, fatha, tah]
        she_past_string = "".join(she_past_broken)
        she_present_b_broken = [bah, sukun, tah, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        she_present_b_string = "".join(she_present_b_broken)
        she_command_string = ""
        she_present_broken = [tah, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        she_present_string = "".join(she_present_broken)
        she_present_with_pronoun_broken = [tah, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, kasra, kaaf]
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
        we_past_broken = [alif, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, fatha, third_root_letter, sukun, noon, alif]
        we_past_string = "".join(we_past_broken)
        we_present_b_broken = [meem, sukun, noon, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        we_present_b_string = "".join(we_present_b_broken)
        we_command_string = ""
        we_present_broken = [noon, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        we_present_string = "".join(we_present_broken)
        we_present_with_pronoun_broken = [noon, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, sukun, kaaf, damma, meem]
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
        you_all_past_broken = [alif, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, fatha, third_root_letter, sukun, tah, damma, waw, alif]
        you_all_past_string = "".join(you_all_past_broken)
        you_all_present_b_broken = [bah, sukun, tah, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, damma, waw, alif]
        you_all_present_b_string = "".join(you_all_present_b_broken)
        you_all_command_broken = [alif, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, damma, waw, alif]
        you_all_command_string = "".join(you_all_command_broken)
        you_all_present_broken = [tah, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, damma, waw, alif]
        you_all_present_string = "".join(you_all_present_broken)
        you_all_present_with_pronoun_broken = [tah, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, damma, waw, noon, alif]
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
        they_past_broken = [alif, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, fatha, third_root_letter, damma, waw, alif]
        they_past_string = "".join(they_past_broken)
        they_present_b_broken = [bah, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, damma, waw, alif]
        they_present_b_string = "".join(they_present_b_broken)
        they_command_string = ""
        they_present_broken = [yah, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, damma, waw, alif]
        they_present_string = "".join(they_present_broken)
        they_present_with_pronoun_broken = [yah, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter, damma, waw, noon, kasra, yah]
        they_present_with_pronoun_string = "".join(they_present_with_pronoun_broken)
        they_conjugations_list = [they_arabic_string, they_past_string, they_present_b_string, they_command_string, they_present_string, they_present_with_pronoun_string]
        print they_arabic_string + "\n"
        print they_past_string + "\n"
        print they_present_b_string + "\n"
        print they_command_string + "\n"
        print they_present_string + "\n"
        print they_present_with_pronoun_string + "\n"
        print they_conjugations_list
        
        word_active_participle_broken = [alif, seen, sukun, meem, " ", alif, lam, fah, alif, ein, kasra, lam]
        word_active_participle_string = "".join(word_active_participle_broken)
        word_direct_object_broken = [alif, seen, sukun, meem, " ", alif, lam, meem, fatha, fah, sukun, ein, damma, waw, lam]
        word_direct_object_string = "".join(word_direct_object_broken)
        word_verbal_noun_broken = [alif, lam, meem, fatha, saad, sukun, daal, fatha, rah]
        word_verbal_noun_string = "".join(word_verbal_noun_broken)
        active_participle_broken = [meem, kasra, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, kasra, third_root_letter]
        active_participle_string = "".join(active_participle_broken)
        direct_object_broken = [meem, damma, seen, sukun, tah, fatha, first_root_letter, sukun, second_root_letter, fatha, third_root_letter]
        direct_object_string = "".join(direct_object_broken)
        verbal_noun_broken = [alif, seen, sukun, tah, kasra, first_root_letter, sukun, second_root_letter, alif, third_root_letter]
        verbal_noun_string = "".join(verbal_noun_broken)
        
        act_part = word_active_participle_string + ": " + active_participle_string
        dir_object = word_direct_object_string + ": " + direct_object_string
        verbal_noun = word_verbal_noun_string + ": " + verbal_noun_string

        chart_extras = (act_part, dir_object, verbal_noun)
        # other important verb info

        column_titles = verb_columns_list[::-1]
        row_2 = i_conjugations_list[::-1]
        row_3 = you_m_conjugations_list[::-1]
        row_4 = you_f_conjugations_list[::-1]
        row_5 = he_conjugations_list[::-1]
        row_6 = she_conjugations_list[::-1]
        row_7 = we_conjugations_list[::-1]
        row_8 = you_all_conjugations_list[::-1]
        row_9 = they_conjugations_list[::-1]

        all_conj = column_titles + row_2 + row_3 + row_4 + row_5 + row_6 + row_7 + row_8 + row_9
        # all 54 cells for the chart of 6 by 9

        chart_stuff_tuple = (all_conj, chart_extras)
        # youre now returning a tuple of two lists...
        return chart_stuff_tuple