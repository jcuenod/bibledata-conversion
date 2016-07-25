from os import listdir
from os.path import isfile, join
import re
import pprint

mypath = "../lxxproject/files/"
lxxfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

sequences_to_match = {
	# This search was for finding similar constructions to the title formula in Zech 1:1
	"article_genArticle_anything_uios": [
		r'.{25}RA',
		r'.{25}RA  G',
		r'.*',
		r'.{36}UI\(O/S',
	]
}

sequence_match = sequences_to_match["article_genArticle_anything_uios"]
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
				matches.append({ref: tmpMatch})
				tmpMatch = []
				sequence_counter = 0

pp = pprint.PrettyPrinter()
pp.pprint(matches)
