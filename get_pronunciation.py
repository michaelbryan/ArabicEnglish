# -*- coding: utf-8 -*-

import re

def get_eng_phonetics(arabic):
	#ara_letters = list(arabic)
	#x = len(ara_letters)
	#transliteration = [None] * x
	arabic = arabic.replace(u'\u064e\u0648\u0652', "ow")
	arabic = arabic.replace(u'\u0629\u064b', "tuhn")
	arabic = arabic.replace(u'\u0627\u064b', "uhn")
	arabic = arabic.replace(u'\u0627\u0648\u0652', "ou")
	arabic = arabic.replace(u'\u064f\u0648\u0652', "oo")
	arabic = arabic.replace(u'\u0650\u064a\u0652', "ee")
	arabic = arabic.replace(u'\u064e\u064a\u0652', "ay")
	arabic = arabic.replace(u'\u064e\u064a', "ay")
	arabic = arabic.replace(u'\u0627\u064a\u0652', "ay")
	arabic = arabic.replace(u'\u0627\u064a', "ay")

	arabic = re.sub(ur'(^)\u0627\u0644', "'il-", \
		arabic, count=0, flags=0)
	arabic = re.sub(ur'(\s)\u0627\u0644', " 'il-", arabic)
	arabic = re.sub(ur'^[\u0627\u0625]\u0650?', "'i", arabic)
	arabic = re.sub(ur'\s[\u0627\u0625]\u0650?', " 'i", arabic)
	arabic = re.sub(ur'^[\u0623]\u064f', "'oo", arabic, re.U)
	arabic = re.sub(ur'\s[\u0623]\u064f', " 'oo", arabic, re.U)
	arabic = re.sub(ur'^[\u0623]\u064e?', "'a", arabic, re.U)
	arabic = re.sub(ur'\s[\u0623]\u064e?', " 'a", arabic, re.U)
	arabic = re.sub(ur'\b\u0641\u064a\b', "fee", arabic)
	# (?=...) This is a lookahead assertion.
	# (?!...) This is a negative lookahead assertion.
	# (?<=...) This is a positive lookbehind assertion.
	# (?<!...) This is a negative lookbehind assertion.

	#arabic = re.sub(ur'\u064f\u0648(?=...)', " 'i", arabic)
	arabic = re.sub(ur'\u064f\u0648(?![\u064e\u064f\u0650\u0651])', "oo", arabic)
	arabic = re.sub(ur'\u0650\u064a(?![\u064e\u064f\u0650\u0651])', "ee", arabic)
	#arabic = re.sub(ur'\u064e\u064a(?![\u064e\u064f\u0650\u0651])', "ay", arabic)
	#arabic = re.sub(ur'\u0627\u064a(?![\u064e\u064f\u0650\u0651])', "ay", arabic)

	fatha = u'\u064e'
	#if fatha in arabic:
		#get_fatha_transl(arabic)
	arabic = arabic.replace(fatha, "a")
	damma = u'\u064f'
	arabic = arabic.replace(damma, "u")
	kasra = u'\u0650'
	arabic = arabic.replace(kasra, "i")

	# m = re.match(r"(..)+", "a1b2c3")  # Matches 3 times.
	# m.group(1)
	shadda = u'\u0651'
	#arabic = re.sub(ur'(?<=(?P<double>\w))\u0651', '\g<double>', arabic)
	m1 = re.search(ur"\w(?=\u0651)", arabic, re.U)
	if m1 != None:
		#if m1.group(0):
		try:
			foo = 3#print "0: " + m1.group(0)
			x = m1.group(0) + shadda
			foo = 3#print x
			arabic = re.sub(x, m1.group(0)*2, arabic, re.U)
			foo = 3#print arabic
		except IndexError:
			pass
		#if m1.group(1):
		try:
			foo = 3#print "1: " + m1.group(1)
		except IndexError:
			pass
		#if m1.group(2):
		try:
			foo = 3#print "2: " + m1.group(2)
		except IndexError:
			pass
	
	m2 = re.search(ur"\w(?=\u0651)", arabic, re.U)
	if m2 != None:
		#if m2.group(0):
		try:
			foo = 3#print "0: " + m2.group(0)
			x = m2.group(0) + shadda
			foo = 3#print x
			arabic = re.sub(x, m2.group(0)*2, arabic, re.U)
			foo = 3#print arabic
		except IndexError:
			pass
	m3 = re.search(ur"\w(?=\u0651)", arabic, re.U)
	if m3 != None:
		#if m3.group(0):
		try:
			foo = 3#print "0: " + m3.group(0)
			x = m3.group(0) + shadda
			foo = 3#print x
			arabic = re.sub(x, m3.group(0)*2, arabic, re.U)
			foo = 3#print arabic
		except IndexError:
			pass
	m4 = re.search(ur"\w(?=\u0651)", arabic, re.U)
	if m4 != None:
		#if m4.group(0):
		try:
			foo = 3#print "0: " + m4.group(0)
			x = m4.group(0) + shadda
			foo = 3#print x
			arabic = re.sub(x, m4.group(0)*2, arabic, re.U)
			foo = 3#print arabic
		except IndexError:
			pass
		
	#arabic = arabic.replace(shadda, "")
	#arabic = re.sub(ur'\u0650\u064a(?![\u064e\u064f\u0650\u0651])', "ee", arabic)

	sukun = u'\u0652'
	arabic = arabic.replace(sukun, "")
	maddah = u'\u0653'
	hamza_above = u'\u0654'
	hamza_below = u'\u0655'

	alif_maddah = u'\u0622'
	arabic = arabic.replace(alif_maddah, "'aa")
	alif_hamza_above = u'\u0623'
	arabic = arabic.replace(alif_hamza_above, "'")
	alif_hamza_below = u'\u0625'
	arabic = arabic.replace(alif_hamza_below, "'")
	alif = u'\u0627'
	arabic = arabic.replace(alif, "aa")

	hamza_on_alif_maksura = u'\u0626'
	arabic = arabic.replace(hamza_on_alif_maksura, "'")
	yah = u'\u064a'
	arabic = arabic.replace(yah, "y")
	waw = u'\u0648'
	arabic = arabic.replace(waw, "w")
	meem = u'\u0645'
	arabic = arabic.replace(meem, "m")
	bah = u'\u0628'
	arabic = arabic.replace(bah, "b")
	tah = u'\u062a'
	arabic = arabic.replace(tah, "t")
	tah_marbuuta = u'\u0629'
	arabic = arabic.replace(tah_marbuuta, "eh")
	noon = u'\u0646'
	arabic = arabic.replace(noon, "n")
	hah = u'\u0647'
	arabic = arabic.replace(hah, "h")
	kaaf = u'\u0643'
	arabic = arabic.replace(kaaf, "k")
	hah_heavy = u'\u062d'
	arabic = arabic.replace(hah_heavy, "H")
	alif_maksura = u'\u0649'
	arabic = arabic.replace(alif_maksura, "uh")
	tah_heavy = u'\u0637'
	arabic = arabic.replace(tah_heavy, "T")
	hamza = u'\u0621'
	arabic = arabic.replace(hamza, "'")

	seen = u'\u0633'
	arabic = arabic.replace(seen, "s")
	lam = u'\u0644'
	arabic = arabic.replace(lam, "l")
	fah = u'\u0641'
	arabic = arabic.replace(fah, "f")
	ein = u'\u0639'
	arabic = arabic.replace(ein, "3")
	saad = u'\u0635'
	arabic = arabic.replace(saad, "S")
	daal = u'\u062f'
	arabic = arabic.replace(daal, "d")
	rah = u'\u0631'
	arabic = arabic.replace(rah, "r")
	fathatan = u'\u064b'
	arabic = arabic.replace(fathatan, "un")

	waw_with_hamza = u'\u0624'
	arabic = arabic.replace(waw_with_hamza, "'")

	ar_quest_mrk = u'\u061F'
	arabic = arabic.replace(ar_quest_mrk, "?")
	thah = u'\u062B'
	arabic = arabic.replace(thah, "th")
	jeem = u'\u062C'
	arabic = arabic.replace(jeem, "j")
	khah = u'\u062E'
	arabic = arabic.replace(khah, "kh")
	dhal = u'\u0630'
	arabic = arabic.replace(dhal, "dh")
	zay = u'\u0632'
	arabic = arabic.replace(zay, "z")
	sheen = u'\u0634'
	arabic = arabic.replace(sheen, "sh")
	Dha = u'\u0638'
	arabic = arabic.replace(Dha, "DH")
	ghain = u'\u063A'
	arabic = arabic.replace(ghain, "gh")
	qaaf = u'\u0642'
	arabic = arabic.replace(qaaf, "q")
	Daa = u'\u0636'
	arabic = arabic.replace(Daa, "D")

	#ara_letters.append('foo')
	#phonetics = ''.join(ara_letters)
	return arabic