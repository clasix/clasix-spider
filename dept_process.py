# encoding: UTF-8
import re
import codecs

import sys 
reload(sys) 
sys.setdefaultencoding('utf8')

#�����ļ�
f = codecs.open('D:\DepartmentList.txt', 'r', 'utf8') 
#����ļ�
fw = open(r'D:\DepartmentList.sql','w')
# ����
area = re.compile(r"\[\".+\"\]")
#Ժϵ
dept = re.compile(r"\".+\"")
#���ж��������ı�
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
		#д���ļ�
		fw.write(area_str + "\t" + univ_str + "\t" + dept_str + '\n')
#�ر��ļ����
f.close()
fw.close()


# ��������ʽ�����Pattern����
#pattern = re.compile(r"\[\".+\"\]")
 
# ʹ��Patternƥ���ı������ƥ�������޷�ƥ��ʱ������None
#match = pattern.search('1, - ["�й�_����"]')
 
#if match:
    # ʹ��Match��÷�����Ϣ
#    print match.group()
	
#print "end"
 
### ��� ###
# hello
# \[\"\w+\"\]

