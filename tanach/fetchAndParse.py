import urllib.request, re

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
	"Habbakuk",
	"Zephaniah",
	"Haggai",
	"Zechariah",
	"Malachi"
]


i = 0
for book in books:
	fileData = []
	if i > 0:
		continue
	i += 1
	response = urllib.request.urlopen("http://tanach.us/TextServer?" + book + "*&content=Accents")
	html = response.readlines()
	lineNumber = 0
	for line in html:
		if line[0:7] != b'\xe2\x80\xaaxxxx':
			# if lineNumber > 10:
			# 	continue
			lineNumber += 1
			line = line.decode('utf-8')
			ref = line[0:10].split("׃")
			if len(line) <= 20:
				print (line)
			else:
				text = re.sub(r"[\u202b\u202a\u202c]", r"", line[10:])
				text = re.sub(r"\[\d\]", r"", text).strip()
				fileData.append({
					"chapter": re.sub(r"[\u202b\u202a\u202c]", r"", ref[1]).strip(),
					"verse": re.sub(r"[\u202b\u202a\u202c]", r"", ref[0]).strip(),
					"text": text
				})
	print(repr(fileData))

