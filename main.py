import json
import glob # ファイルリストを取得

keep_dir = './Keep'
# keep_file_path = './keep.json'
sb_file_path = './scrapbox.json'

# keep.json を読み込む
json_files = glob.glob(keep_dir+'/*.json')
# print(json_files) # debug

# for debug
cnt = {'trushed':0, 'archived':0, 'textContents':0, 'selected':0}

# タイトルが無いと Scrapbox のインポートでエラー吐く気がするので、No titleはオートインクリメントする。
AutoIncrement = 0

# keep.json から scrapbox.json に変換する
sb:json = dict()
sb['pages'] = list()

for keep_file_path in json_files:
    # print(keep_file_path) # debug
    f_keep = open(keep_file_path, 'r')
    keep:json = json.load(f_keep)
    if keep['isTrashed']:
        cnt['trushed'] += 1 # debug
        continue
    if keep['isArchived']:
        cnt['archived'] += 1 # debug
    if not 'textContent' in keep:
        continue
    cnt['textContents'] += 1
    flag = False

    # select content for debug
    for label in keep.get('labels', []):
        if label['name'] == '#10思考':
            flag = True
    if not flag:
        continue
    cnt['selected'] += 1

    sb['pages'].append(dict())
    sb_page_json = sb['pages'][-1]
    sb_page_json['title'] = keep['title']
    if sb_page_json['title'] == '':
        sb_page_json['title'] = 'AutoIncrement_' + str(AutoIncrement)
        AutoIncrement += 1
    sb_page_json['created'] = keep['createdTimestampUsec'] // 1000 // 1000
    sb_page_json['updated'] = keep['userEditedTimestampUsec'] // 1000 // 1000
    sb_page_json['lines'] = list()
    sb_page_json['lines'].append(sb_page_json['title'])
    sb_page_json['lines'] += keep['textContent'].split('\n')

    # taglist:str = str()
    # taglist += '#' + keep['color'] # colorは要らんかなあ…
    # for label in keep.get('labels', []):
    #     taglist += ' #' + label['name']
    # sb_page_json['lines'].append(taglist)

    state_tag_list:str = str()
    if keep['isTrashed']:
        state_tag_list += '#trashed '
    if keep['isPinned']:
        state_tag_list += '#pinned '
    if keep['isArchived']:
        state_tag_list += '#archived '
    sb_page_json['lines'].append(state_tag_list)

    f_keep.close()
    

# scrapbox.json を書き出す
f_sb = open(sb_file_path, 'w')
json.dump(sb, f_sb, indent=1, ensure_ascii=False)
# endure_ascii=True だと全角文字などがエスケープシーケンスで書かれてしまう。
# indent=2 にすると改行・インデントして出力される。なしだと1行。

# for debug
print(json_files.__len__(), 'files')
for key in cnt.keys():
    print(cnt[key], key)