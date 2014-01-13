# -*- coding: utf-8 -*-

from bidi.algorithm import get_display

#import arabic_reshaper

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

    def some_verb_chart(self):
        if self.verb_type == "1a":
            return self.verb_chart_1a()
        elif self.verb_type == "1b":
            return self.verb_chart_1b()
        elif self.verb_type == "1c":
            return self.verb_chart_1c()
        elif self.verb_type == "1d":
            return self.verb_chart_1d()
        elif self.verb_type == "1e":
            return self.verb_chart_1e()
        elif self.verb_type == "1f":
            return self.verb_chart_1f()
        elif self.verb_type == "1g":
            return self.verb_chart_1g()
        elif self.verb_type == "1h":
            return self.verb_chart_1h()
        elif self.verb_type == "1i":
            return self.verb_chart_1i()
        elif self.verb_type == "1j":
            return self.verb_chart_1j()
        elif self.verb_type == "1k":
            return self.verb_chart_1k()
        elif self.verb_type == "1l":
            return self.verb_chart_1l()
        elif self.verb_type == "1m":
            return self.verb_chart_1m()
        elif self.verb_type == "1n":
            return self.verb_chart_1n()
        elif self.verb_type == "1o":
            return self.verb_chart_1o()
        elif self.verb_type == "1p":
            return self.verb_chart_1p()
        elif self.verb_type == "1q":
            return self.verb_chart_1q()
        elif self.verb_type == "1r":
            return self.verb_chart_1r()
        elif self.verb_type == "1s":
            return self.verb_chart_1s()
        elif self.verb_type == "1t":
            return self.verb_chart_1t()
        elif self.verb_type == "1u":
            return self.verb_chart_1u()
        elif self.verb_type == "2a":
            return self.verb_chart_2a()
        elif self.verb_type == "2b":
            return self.verb_chart_2b()
        elif self.verb_type == "2c":
            return self.verb_chart_2c()
        elif self.verb_type == "2d":
            return self.verb_chart_2d()
        elif self.verb_type == "2e":
            return self.verb_chart_2e()
        elif self.verb_type == "3a":
            return self.verb_chart_3a()
        elif self.verb_type == "3b":
            return self.verb_chart_3b()
        elif self.verb_type == "3c":
            return self.verb_chart_3c()
        elif self.verb_type == "4a":
            return self.verb_chart_4a()
        elif self.verb_type == "4b":
            return self.verb_chart_4b()
        elif self.verb_type == "4c":
            return self.verb_chart_4c()
        elif self.verb_type == "4d":
            return self.verb_chart_4d()
        elif self.verb_type == "4e":
            return self.verb_chart_4e()
        elif self.verb_type == "4f":
            return self.verb_chart_4f()
        elif self.verb_type == "5a":
            return self.verb_chart_5a()
        elif self.verb_type == "5b":
            return self.verb_chart_5b()
        elif self.verb_type == "5c":
            return self.verb_chart_5c()
        elif self.verb_type == "6a":
            return self.verb_chart_6a()
        elif self.verb_type == "6b":
            return self.verb_chart_6b()
        elif self.verb_type == "7a":
            return self.verb_chart_7a()
        elif self.verb_type == "7b":
            return self.verb_chart_7b()
        elif self.verb_type == "7c":
            return self.verb_chart_7c()
        elif self.verb_type == "7d":
            return self.verb_chart_7d()
        elif self.verb_type == "8a":
            return self.verb_chart_8a()
        elif self.verb_type == "8b":
            return self.verb_chart_8b()
        elif self.verb_type == "8c":
            return self.verb_chart_8c()
        elif self.verb_type == "8d":
            return self.verb_chart_8d()
        elif self.verb_type == "8e":
            return self.verb_chart_8e()
        elif self.verb_type == "8f":
            return self.verb_chart_8f()
        elif self.verb_type == "8g":
            return self.verb_chart_8g()
        elif self.verb_type == "8h":
            return self.verb_chart_8h()
        elif self.verb_type == "8i":
            return self.verb_chart_8i()
        elif self.verb_type == "8j":
            return self.verb_chart_8j()
        elif self.verb_type == "9a":
            return self.verb_chart_9a()
        elif self.verb_type == "10a":
            return self.verb_chart_10a()
        elif self.verb_type == "10b":
            return self.verb_chart_10b()
        elif self.verb_type == "10c":
            return self.verb_chart_10c()
        elif self.verb_type == "10d":
            return self.verb_chart_10d()
        elif self.verb_type == "10e":
            return self.verb_chart_10e()
        elif self.verb_type == "10f":
            return self.verb_chart_10f()
        else:
            print "##### ERROR: Unexpected input to some_verb_chart or verb type not assigned"
            return "No verb chart assigned"

    def retrieve_english(self):
        #english_string = "\n"
        #english_string += self.english + "\n"
        english_string = " "
        english_string += self.part_of_speech + " "
        english_string += self.english
        return english_string

    def retrieve_just_arabic(self):
        arabic_string = " "
        arabic_string += self.part_of_speech + " "
        arabic_string += self.arabic + " "
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

        #arabic_text = get_display(arabic_reshaper.reshape(u'العربية Hello World')).encode('utf-8')
        #myArabic = get_display(arabic_reshaper.reshape(self.arabic)).encode('utf-8')
        #z = unicode(self.arabic, 'utf-8')
        #myArabic = get_display(arabic_reshaper.reshape(z)).decode('utf-8')
        #print "*********************************** ", myArabic
        #return get_display(arabic_reshaper.reshape(self.arabic))#.decode('utf-8')
        
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
            return True
        else:
            return False