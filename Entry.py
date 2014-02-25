# -*- coding: utf-8 -*-

#from bidi.algorithm import get_display
#import arabic_reshaper

import sys
sys.path.append('verbcharts/')
import verbchart1a 
import verbchart1b
import verbchart1c
import verbchart1d
import verbchart1e
import verbchart1f
import verbchart1g
import verbchart1h
import verbchart1i
import verbchart1j
import verbchart1k
import verbchart1l
import verbchart1m
import verbchart1n
import verbchart1o
import verbchart1p
import verbchart1q
import verbchart1r
import verbchart1s
import verbchart1t
import verbchart1u
import verbchart1v
import verbchart2a
import verbchart2b
import verbchart2c
import verbchart2d
import verbchart2e
import verbchart3a
import verbchart3b
import verbchart3c
import verbchart4a
import verbchart4b
import verbchart4c
import verbchart4d
import verbchart4e
import verbchart4f
import verbchart5a
import verbchart5b
import verbchart5c
import verbchart6a
import verbchart6b
import verbchart6c
import verbchart7a
import verbchart7b
import verbchart7c
import verbchart7d
import verbchart8a
import verbchart8b
import verbchart8c
import verbchart8d
import verbchart8e
import verbchart8f
import verbchart8g
import verbchart8h
import verbchart8i
import verbchart8j
import verbchart8k
import verbchart9a
import verbchart10a
import verbchart10b
import verbchart10c
import verbchart10d
import verbchart10e
import verbchart10f

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
            return verbchart1b.get_chart(self.arabic)
        elif self.verb_type == "1c":
            return verbchart1c.get_chart(self.arabic)
        elif self.verb_type == "1d":
            return verbchart1d.get_chart(self.arabic)
        elif self.verb_type == "1e":
            return verbchart1e.get_chart(self.arabic)
        elif self.verb_type == "1f":
            return verbchart1f.get_chart(self.arabic)
        elif self.verb_type == "1g":
            return verbchart1g.get_chart(self.arabic)
        elif self.verb_type == "1h":
            return verbchart1h.get_chart(self.arabic)
        elif self.verb_type == "1i":
            return verbchart1i.get_chart(self.arabic)
        elif self.verb_type == "1j":
            return verbchart1j.get_chart(self.arabic)
        elif self.verb_type == "1k":
            return verbchart1k.get_chart(self.arabic)
        elif self.verb_type == "1l":
            return verbchart1l.get_chart(self.arabic)
        elif self.verb_type == "1m":
            return verbchart1m.get_chart(self.arabic)
        elif self.verb_type == "1n":
            return verbchart1n.get_chart(self.arabic)
        elif self.verb_type == "1o":
            return verbchart1o.get_chart(self.arabic)
        elif self.verb_type == "1p":
            return verbchart1p.get_chart(self.arabic)
        elif self.verb_type == "1q":
            return verbchart1q.get_chart(self.arabic)
        elif self.verb_type == "1r":
            return verbchart1r.get_chart(self.arabic)
        elif self.verb_type == "1s":
            return verbchart1s.get_chart(self.arabic)
        elif self.verb_type == "1t":
            return verbchart1t.get_chart(self.arabic)
        elif self.verb_type == "1u":
            return verbchart1u.get_chart(self.arabic)
        elif self.verb_type == "1v":
            return verbchart1v.get_chart(self.arabic)
        elif self.verb_type == "2a":
            return verbchart2a.get_chart(self.arabic)
        elif self.verb_type == "2b":
            return verbchart2b.get_chart(self.arabic)
        elif self.verb_type == "2c":
            return verbchart2c.get_chart(self.arabic)
        elif self.verb_type == "2d":
            return verbchart2d.get_chart(self.arabic)
        elif self.verb_type == "2e":
            return verbchart2e.get_chart(self.arabic)
        elif self.verb_type == "3a":
            return verbchart3a.get_chart(self.arabic)
        elif self.verb_type == "3b":
            return verbchart3b.get_chart(self.arabic)
        elif self.verb_type == "3c":
            return verbchart3c.get_chart(self.arabic)
        elif self.verb_type == "4a":
            return verbchart4a.get_chart(self.arabic)
        elif self.verb_type == "4b":
            return verbchart4b.get_chart(self.arabic)
        elif self.verb_type == "4c":
            return verbchart4c.get_chart(self.arabic)
        elif self.verb_type == "4d":
            return verbchart4d.get_chart(self.arabic)
        elif self.verb_type == "4e":
            return verbchart4e.get_chart(self.arabic)
        elif self.verb_type == "4f":
            return verbchart4f.get_chart(self.arabic)
        elif self.verb_type == "5a":
            return verbchart5a.get_chart(self.arabic)
        elif self.verb_type == "5b":
            return verbchart5b.get_chart(self.arabic)
        elif self.verb_type == "5c":
            return verbchart5c.get_chart(self.arabic)
        elif self.verb_type == "6a":
            return verbchart6a.get_chart(self.arabic)
        elif self.verb_type == "6b":
            return verbchart6b.get_chart(self.arabic)
        elif self.verb_type == "6c":
            return verbchart6c.get_chart(self.arabic)
        elif self.verb_type == "7a":
            return verbchart7a.get_chart(self.arabic)
        elif self.verb_type == "7b":
            return verbchart7b.get_chart(self.arabic)
        elif self.verb_type == "7c":
            return verbchart7c.get_chart(self.arabic)
        elif self.verb_type == "7d":
            return verbchart7d.get_chart(self.arabic)
        elif self.verb_type == "8a":
            return verbchart8a.get_chart(self.arabic)
        elif self.verb_type == "8b":
            return verbchart8b.get_chart(self.arabic)
        elif self.verb_type == "8c":
            return verbchart8c.get_chart(self.arabic)
        elif self.verb_type == "8d":
            return verbchart8d.get_chart(self.arabic)
        elif self.verb_type == "8e":
            return verbchart8e.get_chart(self.arabic)
        elif self.verb_type == "8f":
            return verbchart8f.get_chart(self.arabic)
        elif self.verb_type == "8g":
            return verbchart8g.get_chart(self.arabic)
        elif self.verb_type == "8h":
            return verbchart8h.get_chart(self.arabic)
        elif self.verb_type == "8i":
            return verbchart8i.get_chart(self.arabic)
        elif self.verb_type == "8j":
            return verbchart8j.get_chart(self.arabic)
        elif self.verb_type == "8k":
            return verbchart8k.get_chart(self.arabic)
        elif self.verb_type == "9a":
            return verbchart9a.get_chart(self.arabic)
        elif self.verb_type == "10a":
            return verbchart10a.get_chart(self.arabic)
        elif self.verb_type == "10b":
            return verbchart10b.get_chart(self.arabic)
        elif self.verb_type == "10c":
            return verbchart10c.get_chart(self.arabic)
        elif self.verb_type == "10d":
            return verbchart10d.get_chart(self.arabic)
        elif self.verb_type == "10e":
            return verbchart10e.get_chart(self.arabic)
        elif self.verb_type == "10f":
            return verbchart10f.get_chart(self.arabic)
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
        if search_term == self.arabic:
            return self.arabic
        if search_term == self.plural:
            return self.plural
        if search_term == self.alt_plural:
            return self.alt_plural
        if search_term == self.fem_sing:
            return self.fem_sing
        if search_term == self.fem_plural:
            return self.fem_plural
        else:
            return False

    def regex_search_fields(self, compiled_regex):
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