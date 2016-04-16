import yaml
import json

lexeme_file = "lexemes"
# lexeme_file = "lexshort"

yml = open(lexeme_file + ".yaml", 'r').read()
# yml = open('lexshort.yaml', 'r').read()

data = yaml.load(yml)

# filter out everything but the gloss
for lexeme in data:
	for key in list(data[lexeme]):
		if key != "gloss":
			del data[lexeme][key]

# ensure_ascii=False gives unicode output
with open(lexeme_file + ".json", 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, separators=(',',':'), ensure_ascii=False)
