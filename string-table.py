#! /usr/bin/env python3
from z2kit2.elf import *
from z2kit2.elffile import *
import sys

f = open('hello1', 'rb')
e = ELFFile(f)

if DT_STRTAB not in e.dynamic_headers:
	sys.exit(1)
if DT_STRSZ not in e.dynamic_headers:
	sys.exit(1)

# ここにコードを追加 (適宜表示するコードを付けると良いかもしれない)
