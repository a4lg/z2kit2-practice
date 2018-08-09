#! /usr/bin/env python3
from z2kit2.elf import *
from z2kit2.elffile import *

f = open('hello1', 'rb')
e = ELFFile(f)

def section_name(e, idx):
	ndx = e.elf_header.e_shstrndx
	#  仕様:
	#  (1) ELF ヘッダの e_shstrndx が SHN_XINDEX である場合、
	#      セクションヘッダ名を格納する文字列テーブルセクションのインデックスは
	#      先頭のセクションヘッダ (section_headers[0]) の sh_link メンバーの値
	#  (2) 最終的なインデックスが 0 の場合、セクション名は定義できない
	#      (この課題では、仮に b'' を返すこと)
	if ndx == SHN_XINDEX:
		ndx = e.section_headers[0].sh_link
	if ndx == 0:
		return b''
	return e.read_string_by_offset(e.section_headers[ndx].sh_offset + e.section_headers[idx].sh_name)

for i in range(len(e.section_headers)):
	print(section_name(e, i).decode('utf-8'))
