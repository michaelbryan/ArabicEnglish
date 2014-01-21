# -*- coding: utf-8 -*-

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
import verbchart9a
import verbchart10a
import verbchart10b
import verbchart10c
import verbchart10d
import verbchart10e
import verbchart10f

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
            return VerbChart1b.get_chart(self.arabic)
        elif self.verb_type == "1c":
            return VerbChart1c.get_chart(self.arabic)
        elif self.verb_type == "1d":
            return VerbChart1d.get_chart(self.arabic)
        elif self.verb_type == "1e":
            return VerbChart1e.get_chart(self.arabic)
        elif self.verb_type == "1f":
            return VerbChart1f.get_chart(self.arabic)
        elif self.verb_type == "1g":
            return VerbChart1g.get_chart(self.arabic)
        elif self.verb_type == "1h":
            return VerbChart1h.get_chart(self.arabic)
        elif self.verb_type == "1i":
            return VerbChart1i.get_chart(self.arabic)
        elif self.verb_type == "1j":
            return VerbChart1j.get_chart(self.arabic)
        elif self.verb_type == "1k":
            return VerbChart1k.get_chart(self.arabic)
        elif self.verb_type == "1l":
            return VerbChart1l.get_chart(self.arabic)
        elif self.verb_type == "1m":
            return VerbChart1m.get_chart(self.arabic)
        elif self.verb_type == "1n":
            return VerbChart1n.get_chart(self.arabic)
        elif self.verb_type == "1o":
            return VerbChart1o.get_chart(self.arabic)
        elif self.verb_type == "1p":
            return VerbChart1p.get_chart(self.arabic)
        elif self.verb_type == "1q":
            return VerbChart1q.get_chart(self.arabic)
        elif self.verb_type == "1r":
            return VerbChart1r.get_chart(self.arabic)
        elif self.verb_type == "1s":
            return VerbChart1s.get_chart(self.arabic)
        elif self.verb_type == "1t":
            return VerbChart1t.get_chart(self.arabic)
        elif self.verb_type == "1u":
            return VerbChart1u.get_chart(self.arabic)
        elif self.verb_type == "2a":
            return VerbChart2a.get_chart(self.arabic)
        elif self.verb_type == "2b":
            return VerbChart2b.get_chart(self.arabic)
        elif self.verb_type == "2c":
            return VerbChart2c.get_chart(self.arabic)
        elif self.verb_type == "2d":
            return VerbChart2d.get_chart(self.arabic)
        elif self.verb_type == "2e":
            return VerbChart2e.get_chart(self.arabic)
        elif self.verb_type == "3a":
            return VerbChart3a.get_chart(self.arabic)
        elif self.verb_type == "3b":
            return VerbChart3b.get_chart(self.arabic)
        elif self.verb_type == "3c":
            return VerbChart3c.get_chart(self.arabic)
        elif self.verb_type == "4a":
            return VerbChart4a.get_chart(self.arabic)
        elif self.verb_type == "4b":
            return VerbChart4b.get_chart(self.arabic)
        elif self.verb_type == "4c":
            return VerbChart4c.get_chart(self.arabic)
        elif self.verb_type == "4d":
            return VerbChart4d.get_chart(self.arabic)
        elif self.verb_type == "4e":
            return VerbChart4e.get_chart(self.arabic)
        elif self.verb_type == "4f":
            return VerbChart4f.get_chart(self.arabic)
        elif self.verb_type == "5a":
            return VerbChart5a.get_chart(self.arabic)
        elif self.verb_type == "5b":
            return VerbChart5b.get_chart(self.arabic)
        elif self.verb_type == "5c":
            return VerbChart5c.get_chart(self.arabic)
        elif self.verb_type == "6a":
            return VerbChart6a.get_chart(self.arabic)
        elif self.verb_type == "6b":
            return VerbChart6b.get_chart(self.arabic)
        elif self.verb_type == "7a":
            return VerbChart7a.get_chart(self.arabic)
        elif self.verb_type == "7b":
            return VerbChart7b.get_chart(self.arabic)
        elif self.verb_type == "7c":
            return VerbChart7c.get_chart(self.arabic)
        elif self.verb_type == "7d":
            return VerbChart7d.get_chart(self.arabic)
        elif self.verb_type == "8a":
            return VerbChart8a.get_chart(self.arabic)
        elif self.verb_type == "8b":
            return VerbChart8b.get_chart(self.arabic)
        elif self.verb_type == "8c":
            return VerbChart8c.get_chart(self.arabic)
        elif self.verb_type == "8d":
            return VerbChart8d.get_chart(self.arabic)
        elif self.verb_type == "8e":
            return VerbChart8e.get_chart(self.arabic)
        elif self.verb_type == "8f":
            return VerbChart8f.get_chart(self.arabic)
        elif self.verb_type == "8g":
            return VerbChart8g.get_chart(self.arabic)
        elif self.verb_type == "8h":
            return VerbChart8h.get_chart(self.arabic)
        elif self.verb_type == "8i":
            return VerbChart8i.get_chart(self.arabic)
        elif self.verb_type == "8j":
            return VerbChart8j.get_chart(self.arabic)
        elif self.verb_type == "9a":
            return VerbChart9a.get_chart(self.arabic)
        elif self.verb_type == "10a":
            return VerbChart10a.get_chart(self.arabic)
        elif self.verb_type == "10b":
            return VerbChart10b.get_chart(self.arabic)
        elif self.verb_type == "10c":
            return VerbChart10c.get_chart(self.arabic)
        elif self.verb_type == "10d":
            return VerbChart10d.get_chart(self.arabic)
        elif self.verb_type == "10e":
            return VerbChart10e.get_chart(self.arabic)
        elif self.verb_type == "10f":
            return VerbChart10f.get_chart(self.arabic)
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