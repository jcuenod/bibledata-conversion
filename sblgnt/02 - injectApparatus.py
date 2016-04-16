# -*- coding: utf_8 -*-
import json

fileMap = [
    { "jsonFile": "rawjson/1corinthians.json", "jsonApparatus": "injectedFiles/1corinthians.json", "apparatusFile": "apparatusFiles/1Co-APP.txt" },
    { "jsonFile": "rawjson/1john.json", "jsonApparatus": "injectedFiles/1john.json", "apparatusFile": "apparatusFiles/1Jn-APP.txt" },
    { "jsonFile": "rawjson/1peter.json", "jsonApparatus": "injectedFiles/1peter.json", "apparatusFile": "apparatusFiles/1Pe-APP.txt" },
    { "jsonFile": "rawjson/1thessalonians.json", "jsonApparatus": "injectedFiles/1thessalonians.json", "apparatusFile": "apparatusFiles/1Th-APP.txt" },
    { "jsonFile": "rawjson/1timothy.json", "jsonApparatus": "injectedFiles/1timothy.json", "apparatusFile": "apparatusFiles/1Ti-APP.txt" },
    { "jsonFile": "rawjson/2corinthians.json", "jsonApparatus": "injectedFiles/2corinthians.json", "apparatusFile": "apparatusFiles/2Co-APP.txt" },
    { "jsonFile": "rawjson/2john.json", "jsonApparatus": "injectedFiles/2john.json", "apparatusFile": "apparatusFiles/2Jn-APP.txt" },
    { "jsonFile": "rawjson/2peter.json", "jsonApparatus": "injectedFiles/2peter.json", "apparatusFile": "apparatusFiles/2Pe-APP.txt" },
    { "jsonFile": "rawjson/2thessalonians.json", "jsonApparatus": "injectedFiles/2thessalonians.json", "apparatusFile": "apparatusFiles/2Th-APP.txt" },
    { "jsonFile": "rawjson/2timothy.json", "jsonApparatus": "injectedFiles/2timothy.json", "apparatusFile": "apparatusFiles/2Ti-APP.txt" },
    { "jsonFile": "rawjson/3john.json", "jsonApparatus": "injectedFiles/3john.json", "apparatusFile": "apparatusFiles/3Jn-APP.txt" },
    { "jsonFile": "rawjson/acts.json", "jsonApparatus": "injectedFiles/acts.json", "apparatusFile": "apparatusFiles/Ac-APP.txt" },
    { "jsonFile": "rawjson/colossians.json", "jsonApparatus": "injectedFiles/colossians.json", "apparatusFile": "apparatusFiles/Col-APP.txt" },
    { "jsonFile": "rawjson/ephesians.json", "jsonApparatus": "injectedFiles/ephesians.json", "apparatusFile": "apparatusFiles/Eph-APP.txt" },
    { "jsonFile": "rawjson/galatians.json", "jsonApparatus": "injectedFiles/galatians.json", "apparatusFile": "apparatusFiles/Ga-APP.txt" },
    { "jsonFile": "rawjson/hebrews.json", "jsonApparatus": "injectedFiles/hebrews.json", "apparatusFile": "apparatusFiles/Heb-APP.txt" },
    { "jsonFile": "rawjson/james.json", "jsonApparatus": "injectedFiles/james.json", "apparatusFile": "apparatusFiles/Jas-APP.txt" },
    { "jsonFile": "rawjson/john.json", "jsonApparatus": "injectedFiles/john.json", "apparatusFile": "apparatusFiles/Jn-APP.txt" },
    { "jsonFile": "rawjson/jude.json", "jsonApparatus": "injectedFiles/jude.json", "apparatusFile": "apparatusFiles/Jud-APP.txt" },
    { "jsonFile": "rawjson/luke.json", "jsonApparatus": "injectedFiles/luke.json", "apparatusFile": "apparatusFiles/Lk-APP.txt" },
    { "jsonFile": "rawjson/mark.json", "jsonApparatus": "injectedFiles/mark.json", "apparatusFile": "apparatusFiles/Mk-APP.txt" },
    { "jsonFile": "rawjson/matthew.json", "jsonApparatus": "injectedFiles/matthew.json", "apparatusFile": "apparatusFiles/Mt-APP.txt" },
    { "jsonFile": "rawjson/philemon.json", "jsonApparatus": "injectedFiles/philemon.json", "apparatusFile": "apparatusFiles/Phm-APP.txt" },
    { "jsonFile": "rawjson/philippians.json", "jsonApparatus": "injectedFiles/philippians.json", "apparatusFile": "apparatusFiles/Php-APP.txt" },
    { "jsonFile": "rawjson/revelation.json", "jsonApparatus": "injectedFiles/revelation.json", "apparatusFile": "apparatusFiles/Re-APP.txt" },
    { "jsonFile": "rawjson/romans.json", "jsonApparatus": "injectedFiles/romans.json", "apparatusFile": "apparatusFiles/Ro-APP.txt" },
    { "jsonFile": "rawjson/titus.json", "jsonApparatus": "injectedFiles/titus.json", "apparatusFile": "apparatusFiles/Tit-APP.txt" },
]


def index_by_key(list, key, value):
    # note that sometimes key is "22"
    #        but sometimes it is "22-23"
    usableValue = value.rsplit('–')[0]
    for i, item in enumerate(list):
        if int(item[key]) == int(usableValue):
            return i
    raise (ValueError, "%s not in list" % value)

def injectApparatus(filesToInject):
    with open(filesToInject["jsonFile"], encoding='utf-8') as data_file:
        data = json.load(data_file)

    apparatusFile = open(filesToInject["apparatusFile"], "r", encoding='utf-8')

    lineCounter = 0

    for line in apparatusFile:
        lineCounter += 1
        strippedLine = line.strip()
        if lineCounter <= 4 or strippedLine == "":
            continue

        halves = strippedLine.split("\t")

        tcNotes = halves[1].split(" • ")

        verseRef = halves[0].split()

        verseRef[0]
        splitVerseRef = verseRef[1].split(":")

        indexOfChapter = index_by_key(data["chapters"], "chapter", splitVerseRef[0])
        indexOfVerse = index_by_key(data["chapters"][indexOfChapter]["verses"], "verse", splitVerseRef[1])

        if len(tcNotes) > 0:
            data["chapters"][indexOfChapter]["verses"][indexOfVerse]["textCrit"] = []

        for i, note in enumerate(tcNotes):
            data["chapters"][indexOfChapter]["verses"][indexOfVerse]["textCrit"].append(note)

    with open(filesToInject["jsonApparatus"], 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, separators=(',',':'), ensure_ascii=False)

for fnObject in fileMap:
    injectApparatus(fnObject)

# injectApparatus({ "jsonFile": "rawjson/titus.json", "jsonApparatus": "injectedFiles/titus.json", "apparatusFile": "apparatusFiles/Tit-APP.txt" })
