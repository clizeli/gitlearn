#excel数据自动读写

from openpyxl import workbook
from openpyxl.reader.excel import load_workbook
import os
import time

#定义写入文件路径，创建保存文件名
def fullname():
	excelPath = os.path.join(os.getcwd(), 'ExcelData')
	print("******")
	print("Excel数据将保存路径为:%s"%excelPath)
    # 定义文件名称
    #  invalid mode ('wb') or filename: 'Excel2017-09-21_20:15:57.xlsx'   这种方式明明文件，会提示保存失败，无效的文件名。
    # nameTime = time.strftime('%Y-%m-%d_%H:%M:%S')
	nameTime = time.strftime('%Y-%m-%d_%H-%M-%S')
	excelName = 'Excel' + nameTime + '.xlsx' 
	ExcelFullName= os.path.join(excelPath,excelName)
	print("Excel的文件名为：%s"%ExcelFullName)





#写数据

#读文件


if __name__ == '__main__':
	fullname()
#    ExcelFullName = writeExcel()
#    readExcel(ExcelFullName)






