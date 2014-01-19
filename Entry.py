# -*- coding: utf-8 -*-

import verbchart1a #import VerbChart1a
from verbchart1b import VerbChart1b
from verbchart1c import VerbChart1c
from verbchart1d import VerbChart1d
from verbchart1e import VerbChart1e
from verbchart1f import VerbChart1f
from verbchart1g import VerbChart1g
from verbchart1h import VerbChart1h
from verbchart1i import VerbChart1i
from verbchart1j import VerbChart1j
from verbchart1k import VerbChart1k
from verbchart1l import VerbChart1l
from verbchart1m import VerbChart1m
from verbchart1n import VerbChart1n
from verbchart1o import VerbChart1o
from verbchart1p import VerbChart1p
from verbchart1q import VerbChart1q
from verbchart1r import VerbChart1r
from verbchart1s import VerbChart1s
from verbchart1t import VerbChart1t
from verbchart1u import VerbChart1u
from verbchart2a import VerbChart2a
from verbchart2b import VerbChart2b
from verbchart2c import VerbChart2c
from verbchart2d import VerbChart2d
from verbchart2e import VerbChart2e
from verbchart3a import VerbChart3a
from verbchart3b import VerbChart3b
from verbchart3c import VerbChart3c
from verbchart4a import VerbChart4a
from verbchart4b import VerbChart4b
from verbchart4c import VerbChart4c
from verbchart4d import VerbChart4d
from verbchart4e import VerbChart4e
from verbchart4f import VerbChart4f
from verbchart5a import VerbChart5a
from verbchart5b import VerbChart5b
from verbchart5c import VerbChart5c
from verbchart6a import VerbChart6a
from verbchart6b import VerbChart6b
from verbchart7a import VerbChart7a
from verbchart7b import VerbChart7b
from verbchart7c import VerbChart7c
from verbchart7d import VerbChart7d
from verbchart8a import VerbChart8a
from verbchart8b import VerbChart8b
from verbchart8c import VerbChart8c
from verbchart8d import VerbChart8d
from verbchart8e import VerbChart8e
from verbchart8f import VerbChart8f
from verbchart8g import VerbChart8g
from verbchart8h import VerbChart8h
from verbchart8i import VerbChart8i
from verbchart8j import VerbChart8j
from verbchart9a import VerbChart9a
from verbchart10a import VerbChart10a
from verbchart10b import VerbChart10b
from verbchart10c import VerbChart10c
from verbchart10d import VerbChart10d
from verbchart10e import VerbChart10e
from verbchart10f import VerbChart10f

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
            return verbchart1a.get_chart(self.arabic)
        elif self.verb_type == "1b":
            return VerbChart1b(self.arabic)
        elif self.verb_type == "1c":
            return VerbChart1c(self.arabic)
        elif self.verb_type == "1d":
            return VerbChart1d(self.arabic)
        elif self.verb_type == "1e":
            return VerbChart1e(self.arabic)
        elif self.verb_type == "1f":
            return VerbChart1f(self.arabic)
        elif self.verb_type == "1g":
            return VerbChart1g(self.arabic)
        elif self.verb_type == "1h":
            return VerbChart1h(self.arabic)
        elif self.verb_type == "1i":
            return VerbChart1i(self.arabic)
        elif self.verb_type == "1j":
            return VerbChart1j(self.arabic)
        elif self.verb_type == "1k":
            return VerbChart1k(self.arabic)
        elif self.verb_type == "1l":
            return VerbChart1l(self.arabic)
        elif self.verb_type == "1m":
            return VerbChart1m(self.arabic)
        elif self.verb_type == "1n":
            return VerbChart1n(self.arabic)
        elif self.verb_type == "1o":
            return VerbChart1o(self.arabic)
        elif self.verb_type == "1p":
            return VerbChart1p(self.arabic)
        elif self.verb_type == "1q":
            return VerbChart1q(self.arabic)
        elif self.verb_type == "1r":
            return VerbChart1r(self.arabic)
        elif self.verb_type == "1s":
            return VerbChart1s(self.arabic)
        elif self.verb_type == "1t":
            return VerbChart1t(self.arabic)
        elif self.verb_type == "1u":
            return VerbChart1u(self.arabic)
        elif self.verb_type == "2a":
            return VerbChart2a(self.arabic)
        elif self.verb_type == "2b":
            return VerbChart2b(self.arabic)
        elif self.verb_type == "2c":
            return VerbChart2c(self.arabic)
        elif self.verb_type == "2d":
            return VerbChart2d(self.arabic)
        elif self.verb_type == "2e":
            return VerbChart2e(self.arabic)
        elif self.verb_type == "3a":
            return VerbChart3a(self.arabic)
        elif self.verb_type == "3b":
            return VerbChart3b(self.arabic)
        elif self.verb_type == "3c":
            return VerbChart3c(self.arabic)
        elif self.verb_type == "4a":
            return VerbChart4a(self.arabic)
        elif self.verb_type == "4b":
            return VerbChart4b(self.arabic)
        elif self.verb_type == "4c":
            return VerbChart4c(self.arabic)
        elif self.verb_type == "4d":
            return VerbChart4d(self.arabic)
        elif self.verb_type == "4e":
            return VerbChart4e(self.arabic)
        elif self.verb_type == "4f":
            return VerbChart4f(self.arabic)
        elif self.verb_type == "5a":
            return VerbChart5a(self.arabic)
        elif self.verb_type == "5b":
            return VerbChart5b(self.arabic)
        elif self.verb_type == "5c":
            return VerbChart5c(self.arabic)
        elif self.verb_type == "6a":
            return VerbChart6a(self.arabic)
        elif self.verb_type == "6b":
            return VerbChart6b(self.arabic)
        elif self.verb_type == "7a":
            return VerbChart7a(self.arabic)
        elif self.verb_type == "7b":
            return VerbChart7b(self.arabic)
        elif self.verb_type == "7c":
            return VerbChart7c(self.arabic)
        elif self.verb_type == "7d":
            return VerbChart7d(self.arabic)
        elif self.verb_type == "8a":
            return VerbChart8a(self.arabic)
        elif self.verb_type == "8b":
            return VerbChart8b(self.arabic)
        elif self.verb_type == "8c":
            return VerbChart8c(self.arabic)
        elif self.verb_type == "8d":
            return VerbChart8d(self.arabic)
        elif self.verb_type == "8e":
            return VerbChart8e(self.arabic)
        elif self.verb_type == "8f":
            return VerbChart8f(self.arabic)
        elif self.verb_type == "8g":
            return VerbChart8g(self.arabic)
        elif self.verb_type == "8h":
            return VerbChart8h(self.arabic)
        elif self.verb_type == "8i":
            return VerbChart8i(self.arabic)
        elif self.verb_type == "8j":
            return VerbChart8j(self.arabic)
        elif self.verb_type == "9a":
            return VerbChart9a(self.arabic)
        elif self.verb_type == "10a":
            return VerbChart10a(self.arabic)
        elif self.verb_type == "10b":
            return VerbChart10b(self.arabic)
        elif self.verb_type == "10c":
            return VerbChart10c(self.arabic)
        elif self.verb_type == "10d":
            return VerbChart10d(self.arabic)
        elif self.verb_type == "10e":
            return VerbChart10e(self.arabic)
        elif self.verb_type == "10f":
            return VerbChart10f(self.arabic)
        else:
            print "##### ERROR: Unexpected input to some_verb_chart or verb type not assigned"
            return "No verb chart assigned"

    def retrieve_english(self):
        #english_string = "\n"
        #english_string += self.english + "\n"
        english_string = " "
        english_string += self.part_of_speech + ": "
        english_string += self.english
        return english_string

    def retrieve_just_arabic(self):
        arabic_string = " "
        arabic_string += self.part_of_speech + ": "
        arabic_string += self.arabic
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
        #if self.part_of_speech == "v":
            # converting your list back to a string...
            #arabic_string += "".join(self.some_verb_chart())
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
        if search_term == self.arabic or search_term == self.plural or \
            search_term == self.alt_plural or search_term == self.fem_sing or \
            search_term == self.fem_plural:
            return True
        else:
            return False

    def regex_search_fields(self, compiled_regex, arabic_regex):
        if compiled_regex.search(self.arabic):
            return self.arabic
        if compiled_regex.search(self.plural):
            return self.plural
        if compiled_regex.search(self.alt_plural):
            return self.alt_plural
        if compiled_regex.search(self.fem_sing):
            return self.fem_sing
        if compiled_regex.search(self.fem_plural):
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
        '''