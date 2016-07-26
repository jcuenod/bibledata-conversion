from os import listdir
from os.path import isfile, join
import betacode as betacode
import re
import pprint

mypath = "../lxxproject/files/"
lxxfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

def get_unicode_word(wordInBetacode):
	encoded_word = str.encode(betacode.transliterate(wordInBetacode))
	return encoded_word.decode('utf-8')

def convertArrayOfLinesFromBetaToUnicode(line_array):
	ret = []
	for line in line_array:
		first_bit = re.search('^[^\s]+', line).group(0)
		first_bit = get_unicode_word(first_bit).ljust(25)

		last_bits = re.split("\s(?:[^\s|\n])", line[36:])

		for i, b in enumerate(last_bits):
			last_bits[i] = get_unicode_word(b).ljust(len(b))

		ret.append(first_bit + line[25:36] + ''.join(last_bits).strip())
	return ret

sequences_to_match = {
	# This search was for finding similar constructions to the title formula in Zech 1:1
	"article_genArticle_anything_uios": [
		r'.{25}RA',
		r'.{25}RA  G',
		r'.*',
		r'.{36}UI\(O/S',
	],
	# same as above but search for proper noun (it will be capitalised) and no uios (but show next line)
	"article_genArticle_properNoun": [
		r'.{25}RA',
		r'.{25}RA  G',
		r'\*.*',
		r'.*',
		r'.*',
	]
}

sequence_match = sequences_to_match["article_genArticle_properNoun"]
matches = []
ref = ""

for lxxfile in lxxfiles:
	tmpMatch = []
	sequence_counter = 0
	lines = [line.rstrip('\n') for line in open(mypath + lxxfile)]
	for line in lines:
		if re.match(".+ .+:.+", line) or re.match(".+ [1-9]+", line):
			ref = line
		elif re.match(".+", line):
			if re.match(sequence_match[sequence_counter], line):
				sequence_counter += 1
				tmpMatch.append(line)
			else:
				sequence_counter = 0
				tmpMatch = []

			if sequence_counter == len(sequence_match):
				matches.append({ref: convertArrayOfLinesFromBetaToUnicode(tmpMatch)})
				tmpMatch = []
				sequence_counter = 0

pp = pprint.PrettyPrinter()
pp.pprint(matches)
