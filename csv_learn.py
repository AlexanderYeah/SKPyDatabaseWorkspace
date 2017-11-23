#coding=utf-8;

import csv

"""
    CSV comma-seperated Values 逗号分隔值
    列与列之间以逗号分隔
    行与行之间以空格分隔
"""
# 1 创建一个csv 文件,当前路径 不存在 进行创建 存在就会覆盖
csvFile = open('test.csv','w+');
try:
    # 写入操作
    writer = csv.writer(csvFile);
    # 写入行
    writer.writerow(('number','number plus 2','number times 2'));
    for i in  range(0,10):
        writer.writerow((i,i+2,i * 2));
finally:
    csvFile.close();
