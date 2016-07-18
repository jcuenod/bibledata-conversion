import json

nt_json_url = "firetranslate-5c0ca-export.json"
ot_json_url = "firetranslate_wlc.json"

output_url = "complete_bibledata.json"

with open(nt_json_url, encoding='utf-8') as data_file:
	fire_export = json.load(data_file)
	nt_json = fire_export["bibledata"]

with open(ot_json_url, encoding='utf-8') as data_file:
	ot_json = json.load(data_file)

ot_json.update(nt_json)

with open(output_url, 'w', encoding='utf-8') as outfile:
	json.dump(ot_json, outfile, separators=(',',':'), ensure_ascii=False)
