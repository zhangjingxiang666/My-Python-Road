import xlrd
import xlwt
from xlutils.copy import copy
import os

def create_excel(path, sheet_name):
    workbook = xlwt.Workbook()  # 新建一个工作簿
    workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    workbook.save(path)  # 保存工作簿

def read_data(FileName):
    # 1.打开文件
    open_file = xlrd.open_workbook(FileName)

    # 2.读取第二列的内容（表中第一列索引值为0）
    st = open_file.sheet_by_index(0)
    data = [st.cell_value(i,1) for i in range(1, st.nrows)]
    # 3.将表名追加到列表作为第一个元素
    title = open_file.sheet_names()
    data = title + data

    return data

def write_data(path, data):
    index = len(data) # 获取索引写入的行数
    workbook = xlrd.open_workbook(path) # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    cols_old = worksheet.ncols  # 获取表格中已存在的数据的列数

    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
            new_worksheet.write( i, cols_old + 1, data[i])  # 追加写入数据
    new_workbook.save(path)  # 保存工作簿

def get_file_name(file_dir):
    tmp_lst = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            tmp_lst.append(os.path.join(root, file))
    return tmp_lst

def main():
    DIR_NAME = r'D:\test\\'
    create_excel(DIR_NAME + '合并.xls','汇总数据')
    print(DIR_NAME + '合并.xls')
    tmp_list = get_file_name(DIR_NAME + 'data\\')
    for dir in tmp_list:
        data = read_data(dir)
        write_data(DIR_NAME + '\合并.xls', data)
        print('------------'+ dir.split("\\")[-1] + '数据写入成功！-----------' )

if __name__ == '__main__':
    main()