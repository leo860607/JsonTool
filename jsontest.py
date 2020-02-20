import sys
import os
import json
import operator
import pprint


filename1 = input('請輸入你的檔名：')
filename2 = input('請輸入你的檔名2：')
#load json from file
with open(filename1+".json",'r',encoding='utf-8') as load_f:
    b_str = load_f.read()
    load_dicf = json.loads(b_str)
    a =json.dumps(load_dicf,sort_keys = True)
    #print(a)
#load json from file
with open(filename2+".json",'r',encoding='utf-8') as load_f2:
    b_str2 = load_f2.read()
    load_dicf2 = json.loads(b_str2)
    a2 =json.dumps(load_dicf2,sort_keys = True)
    #print(a2)


#with open(r"C:\Users\leo86\Desktop\1_output.json",'w',encoding='utf-8') as f:
#   f.write(a)


def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o : (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
    same = set(o for o in intersect_keys if d1[o] == d2[o])
    return added, removed, modified, same


added, removed, modified, same = dict_compare(load_dicf, load_dicf2)
print("modified >>"+repr(modified))
pprint.pprint(modified)
print("same >>"+repr(same))

with open(r"Jsoncompare_output.json",'w',encoding='utf-8') as f:
   f.write("不同 >>> \n"+pprint.pformat(modified)+"\n\n")
   f.write("相同 >>> \n"+pprint.pformat(same))


