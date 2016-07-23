import json

nt_json_url = "sblgnt/firetranslate_sbl.json"
ot_json_url = "tanach/firetranslate_wlc.json"

output_url = "firetranslate_bibledata.json"

with open(nt_json_url, encoding='utf-8') as data_file:
	nt_json = json.load(data_file)

with open(ot_json_url, encoding='utf-8') as data_file:
	ot_json = json.load(data_file)

ot_json.update(nt_json)

with open(output_url, 'w', encoding='utf-8') as outfile:
	json.dump(ot_json, outfile, separators=(',',':'), ensure_ascii=False)
