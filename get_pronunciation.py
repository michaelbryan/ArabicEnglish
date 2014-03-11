# -*- coding: utf-8 -*-

def get_fatha_transl(arabic):
	#re.sub(pattern, repl, string, count=0, flags=0)
	# This match includes waw, hah, kaaf, daal, lam, sheen, seen, dhal
	#for m in re.finditer((?<=[u'\u0648\u0647\u0643\u062f\u0644\u0634\u0633\u0630'])u'\u064e'(?=[u'\u0648\u0647\u0643\u062f\u0644\u0634\u0633\u0630']), \
		#arabic):
		#print '%02d-%02d: %s' % (m.start(), m.end(), m.group(0))


	'''>>> text = "He was carefully disguised but captured quickly by police."
	>>> for m in re.finditer(r"\w+ly", text):
	...     print '%02d-%02d: %s' % (m.start(), m.end(), m.group(0))
	07-16: carefully
	40-47: quickly'''

def get_eng_phonetics(arabic):
	ara_letters = list(arabic)
	x = len(ara_letters)
	transliteration = [None] * x
	fatha = u'\u064e'
	#if fatha in arabic:
		#get_fatha_transl(arabic)
	arabic = arabic.replace(fatha, "a")
	damma = u'\u064f'
	arabic = arabic.replace(damma, "u")
	kasra = u'\u0650'
	arabic = arabic.replace(kasra, "i")

	shadda = u'\u0651'
	arabic = arabic.replace(shadda, "")
	sukun = u'\u0652'
	arabic = arabic.replace(sukun, "-")
	maddah = u'\u0653'
	hamza_above = u'\u0654'
	hamza_below = u'\u0655'

	alif_maddah = u'\u0622'
	arabic = arabic.replace(alif_maddah, "aa")
	alif_hamza_above = u'\u0623'
	arabic = arabic.replace(alif_hamza_above, "'")
	alif_hamza_below = u'\u0625'
	arabic = arabic.replace(alif_hamza_below, "'")
	alif = u'\u0627'
	arabic = arabic.replace(alif, "A")

	hamza_on_alif_maksura = u'\u0626'
	arabic = arabic.replace(hamza_on_alif_maksura, "'")
	yah = u'\u064a'
	arabic = arabic.replace(yah, "y")
	waw = u'\u0648'
	arabic = arabic.replace(waw, "oo")
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

	ara_letters.append('foo')
	phonetics = ''.join(ara_letters)
	return arabic