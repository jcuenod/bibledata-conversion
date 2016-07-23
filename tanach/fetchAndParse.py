import urllib.request, re, json

books = [
	"Genesis",
	"Exodus",
	"Leviticus",
	"Numbers",
	"Deuteronomy",
	"Joshua",
	"Judges",
	"Ruth",
	"1 Samuel",
	"2 Samuel",
	"1 Kings",
	"2 Kings",
	"1 Chronicles",
	"2 Chronicles",
	"Ezra",
	"Nehemiah",
	"Esther",
	"Job",
	"Psalms",
	"Proverbs",
	"Ecclesiastes",
	"Song of Songs",
	"Isaiah",
	"Jeremiah",
	"Lamentations",
	"Ezekiel",
	"Daniel",
	"Hosea",
	"Joel",
	"Amos",
	"Obadiah",
	"Jonah",
	"Micah",
	"Nahum",
	"Habakkuk",
	"Zephaniah",
	"Haggai",
	"Zechariah",
	"Malachi"
]

fileData = {}

def generate_chapter_name(book, chapter):
	return book.lower().replace(" ", "") + "_" + '{0:03d}'.format(int(chapter))

for counter, book in enumerate(books):
	# if book != "1 Samuel":
	# 	continue
	url = "http://tanach.us/TextServer?" + re.sub(r"\ ", r"%20", book) + "*&content=Accents"
	response = urllib.request.urlopen(url)
	html = response.readlines()
	chapter = 0
	verse = 0
	chapterData = []
	verseData = []
	for line in html:
		if line[0:7] != b'\xe2\x80\xaaxxxx':
			line = line.decode('utf-8')
			ref = line[0:10].split("׃")

			oldChapter = chapter
			oldVerse = verse
			chapter = re.sub(r"[\u202b\u202a\u202c]", r"", ref[1]).strip()
			verse = re.sub(r"[\u202b\u202a\u202c]", r"", ref[0]).strip()
			if int(oldChapter) != int(chapter) and int(oldChapter) != 0:
				chapter_name = generate_chapter_name(book, oldChapter)
				fileData[chapter_name] = {
					"verses": verseData
				}
				verseData = []

			text = re.sub(r"[\u202b\u202a\u202c]", r"", line[10:])
			text = re.sub(r"\[\d\]", r"", text).strip()
			verseData.append({
				"verse": re.sub(r"[\u202b\u202a\u202c]", r"", ref[0]).strip(),
				"wlc": text
			})
	chapter_name = generate_chapter_name(book, chapter)
	fileData[chapter_name] = {
		"verses": verseData
	}
	print(book)

with open("firetranslate_wlc.json", 'w', encoding='utf-8') as outfile:
	json.dump(fileData, outfile, separators=(',',':'), ensure_ascii=False)
