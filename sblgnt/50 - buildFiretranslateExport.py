import json
from functools import reduce

outputFile = "firetranslate_sbl.json"

books = {
	"Matthew",
	"Mark",
	"Luke",
	"John",
	"Acts",
	"Romans",
	"1 Corinthians",
	"2 Corinthians",
	"Galatians",
	"Ephesians",
	"Philippians",
	"Colossians",
	"1 Thessalonians",
	"2 Thessalonians",
	"1 Timothy",
	"2 Timothy",
	"Titus",
	"Philemon",
	"Hebrews",
	"James",
	"1 Peter",
	"2 Peter",
	"1 John",
	"2 John",
	"3 John",
	"Jude",
	"Revelation",
}
# books = {
# 	"1 John"
# }


def generate_book_name(book):
	return book.lower().replace(" ", "")

def generate_chapter_name(book, chapter):
	return generate_book_name(book) + "_" + '{0:03d}'.format(int(chapter))


def get_word(carry, word_object):
	return carry + " " + word_object["wordInText"]

def collect_words_of_verse_into_verse(verse):
	return {
		"verse": verse["verse"],
		"sbl": reduce(get_word, verse["words"], "").strip(),
	}

def collect_verses(verses):
	return list(map(collect_words_of_verse_into_verse, verses))


complete_data = {}
for book in books:
	with open("rawjson/" + generate_book_name(book) + ".json", encoding='utf-8') as data_file:
		data = json.load(data_file)

	for k, v in enumerate(data["chapters"]):
		complete_data[generate_chapter_name(book, k)] = {
			"verses": collect_verses(v["verses"])
		}


with open(outputFile, 'w', encoding='utf-8') as outfile:
	json.dump(complete_data, outfile, separators=(',',':'), ensure_ascii=False)
