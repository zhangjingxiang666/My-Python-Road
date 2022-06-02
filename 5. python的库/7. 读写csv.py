import csv

#写：追加
row = ['5', 'hanmeimei', '23', '81']
out = open("test.csv", "a", newline = "")
csv_writer = csv.writer(out, dialect = "excel")
csv_writer.writerow(row)