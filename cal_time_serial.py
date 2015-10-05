# -*- coding=utf8 -*- 
# desc: 原始外汇数据生成各个时间轴数据
# author: dongshaohui

import datetime
import sys

#把字符串转成datetime
def string_toDatetime(string):  
    return datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")  

def cal_serial(filename,delta):
	f = open(filename)
	rc = f.readlines()
	rc = map(lambda x: x.strip(), rc)
	title = rc[0]
	print title
	
	pre_time = None
	cur_time = None
	print_tup = None

	
	for i in range(1,len(rc)):
		line =  rc[i]
		tup = line.split(',')
		# print tup
		time_serial_str = tup[1][0:4] + '-' + tup[1][4:6] + '-' + tup[1][6:8] + ' ' + tup[2][0:2] + ':' + tup[2][2:4] + ':' + tup[2][4:6]
		time_serial = string_toDatetime(time_serial_str)
		cur_time = time_serial
		if pre_time == None:
			print_tup = tup
			pre_time = time_serial
		elif (cur_time - pre_time).seconds >= delta * 60:
			print ','.join(print_tup)
			pre_time = time_serial
			print_tup = tup
		else:
			if (float)(tup[4]) > (float)(print_tup[4]): # high
				print_tup[4] = tup[4]
			if (float)(tup[5]) < (float)(print_tup[5]): # low
				print_tup[5] = tup[5]
			print_tup[6] = tup[6]
			# 更新tup
			continue

if __name__ =='__main__':
	cal_serial(sys.argv[1],(int)(sys.argv[2]))