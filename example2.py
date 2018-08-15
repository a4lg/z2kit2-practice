#! /usr/bin/env python3
import os
import os.path
import sys
from z2kit2.decisions import *
from z2kit2.elf import *
from z2kit2.elffile import *
from z2kit2.features import *
from z2kit2.filedata import *

filedatas = []
for malware_filename in sorted(os.listdir('malware-samples/elf')):
	malware_filepath = 'malware-samples/elf/' + malware_filename
	if not os.path.isfile(malware_filepath):
		continue
	filedata = FileData(malware_filepath)
	filedata.filename = malware_filename  # 動的型付け特有の緩い代入
	# BEGIN: 必要ならここに、キャッシュすべき何かを事前計算するコードを追加する
	# END
	filedatas.append(filedata)

feature = LstrfuzzyFeature()
for filedata in filedatas:
	data = feature.get_feature(filedata)
	if data:
		print(filedata.filename + ' has lstrfuzzy feature of ' + data)
