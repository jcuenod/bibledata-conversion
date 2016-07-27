from os import listdir
from os.path import isfile, join
import betacode as betacode
import re
import pprint

class color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

mypath = "../lxxproject/files/"
lxxfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

def get_unicode_word(wordInBetacode):
	encoded_word = str.encode(betacode.transliterate(wordInBetacode))
	return encoded_word.decode('utf-8')

# def convertArrayOfLinesFromBetaToUnicode(line_array):
# 	ret = []
# 	for line in line_array:
# 		first_bit = re.search('^[^\s]+', line).group(0)
# 		first_bit = get_unicode_word(first_bit).ljust(25)
#
# 		last_bits = re.split("\s(?:[^\s|\n])", line[36:])
#
# 		for i, b in enumerate(last_bits):
# 			last_bits[i] = get_unicode_word(b).ljust(len(b))
#
# 		ret.append(first_bit + line[25:36] + ''.join(last_bits).strip())
# 	return ret

sequences_to_match = {
	# This search was for finding similar constructions to the title formula in Zech 1:1
	"article_genArticle_anything_uios": [
		r'.{25}RA',			# Article
		r'.{25}RA  G',		# Genitive Article
		r'.*',				# Anything
		r'.{36}UI\(O/S',	# Any form of uios
	],
	# same as above but search for proper noun (it will be capitalised) and no uios (but show next line)
	"article_genArticle_properNoun": [
		r'.{25}RA',			# Article
		r'.{25}RA  G',		# Genitive Article
		r'\*.*',			# Capitalised Word in Text
	]
}

sequence_match = sequences_to_match["article_genArticle_properNoun"]
matches = []
ref = ""
do_print = ""

for lxxfile in lxxfiles:
	tmpMatch = []
	sequence_counter = 0
	lines = [line.rstrip('\n') for line in open(mypath + lxxfile)]
	for line in lines:
		if re.match(".+ .+:.+", line) or re.match(".+ [1-9]+", line):
			if do_print != "":
				match_line = v.strip()
				match_line_highlight = match_line[:match_line.index(do_print)] + color.GREEN + do_print + color.END + match_line[match_line.index(do_print) + len(do_print):]
				print (color.BOLD + ref + color.END)
				print (match_line_highlight + "\n")
				do_print = ""
			ref = line
			v = "";
		elif re.match(".+", line):
			first_bit = re.search('^[^\s]+', line).group(0)
			unicode_first_bit = get_unicode_word(first_bit)
			v += " " + unicode_first_bit
			if re.match(sequence_match[sequence_counter], line):
				sequence_counter += 1
				tmpMatch.append(line)
				match_string += " " + unicode_first_bit
			else:
				sequence_counter = 0
				tmpMatch = []
				match_string = ""

			if sequence_counter == len(sequence_match):
				# matches.append({ref: convertArrayOfLinesFromBetaToUnicode(tmpMatch)})
				tmpMatch = []
				sequence_counter = 0
				do_print = match_string

# pp = pprint.PrettyPrinter()
# pp.pprint(matches)
