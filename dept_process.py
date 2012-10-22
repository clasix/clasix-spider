# encoding: UTF-8
import re
import codecs

import sys 
reload(sys) 
sys.setdefaultencoding('utf8')

#输入文件
f = codecs.open('D:\DepartmentList.txt', 'r', 'utf8') 
#输出文件
fw = open(r'D:\DepartmentList.sql','w')
# 地区
area = re.compile(r"\[\".+\"\]")
#院系
dept = re.compile(r"\".+\"")
#按行读出所有文本
lines = f.readlines()
num = -1
area_str = ""
univ_str = ""
dept_str = ""
for line in lines:
	if line[-2:] == '\r\n':
		line = line[0: -2]
	if line[-1:] == '\n':
		line = line[0: -1]
	if line[-2:] == '"]':
		area_str = area.search(line).group()[2:-2]
	elif line[-2:] == '")':
		univ_str = area.search(line).group()[2:-2]
	elif line[-1:] == '"':
		dept_str = dept.search(line).group()[1:-1]
		#写入文件
		fw.write(area_str + "\t" + univ_str + "\t" + dept_str + '\n')
#关闭文件句柄
f.close()
fw.close()


# 将正则表达式编译成Pattern对象
#pattern = re.compile(r"\[\".+\"\]")
 
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
#match = pattern.search('1, - ["中国_北京"]')
 
#if match:
    # 使用Match获得分组信息
#    print match.group()
	
#print "end"
 
### 输出 ###
# hello
# \[\"\w+\"\]

