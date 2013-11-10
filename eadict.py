import sys
import re

all_entries = {}

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

	def retrieve_english(self):
		#english_string = "\n"
		#english_string += self.english + "\n"
		english_string = self.english
		return english_string

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
		return arabic_string
	
	def __str__(self):
		entry_string = "\n"
		entry_string += self.english + "\n"
		entry_string += self.arabic + "\n"
		entry_string += self.part_of_speech + "\n"
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

def reverse_search_entries(search_term):
	matched_entries = []
	for english, list_of_entries in all_entries.items():
		for entry in list_of_entries:
			if entry.search_fields(search_term):
				matched_entries.append(entry)
	return matched_entries

def search_entries(search_term):
	if search_term in all_entries.keys():
		for entry in all_entries[search_term]:
			print "Found via english: %s" % entry.retrieve_arabic()
		return True

	matched_entries = reverse_search_entries(search_term)
	if len(matched_entries) > 0:
		for entry in matched_entries:
			print "Found via arabic: %s" % entry.retrieve_english()
		return True
	else:
		print "The word \"%s\" was not found." % search_term
		return False

def regex_search(regex):
	print "regex_search:", regex
	compiled_regex = re.compile(regex)
	'''
	someWords = ["work", "woooden puppet", "glass", "worrm", "computer", "widow"]
	for word in someWords:
		if compiled_regex.search(word):
			print word
	'''
	
	for key in all_entries.keys():
		for entry in all_entries[key]:
			if compiled_regex.search(entry.english):
				print entry.retrieve_english()
	

def read_dict(my_file_name):
	file_handler = open(my_file_name, 'r')
	
	line_counter = 0
	num_repeats = 0
	num_all_entries = 0
	for line in file_handler:
		line_counter += 1
		# create an instance of Entry and call it current_entry
		current_entry = Entry(line.strip())

		if current_entry.english not in all_entries:
			num_all_entries += 1
			all_entries[current_entry.english] = [current_entry]
		else:
			num_all_entries += 1
			num_repeats += 1
			all_entries[current_entry.english].append(current_entry)

	print "Number of lines         :", line_counter
	print "Number of unique entries:", len(all_entries)
	print "Number of repeats       :", num_repeats
	print "Number of all entries   :", num_all_entries
	file_handler.close()

def main(name_of_file, search_term):
	read_dict(name_of_file)
	#search_entries(search_term)

	regex_search('wo\wr')

	verbs = []
	for key in all_entries.keys():
		if all_entries[key][0].part_of_speech == "v":
			verbs.append(    all_entries[key][0].english   )
	#print verbs


if __name__ == "__main__":
	if(len(sys.argv) != 3):
		print "##### ERROR: Please provide a file name and a search term"
		print "***** Example: python search_dict.py indexforvocab.txt walk"
		print "Exiting..."
		sys.exit()
	file_name = sys.argv[1]
	search_term = sys.argv[2]
	main(file_name, search_term)