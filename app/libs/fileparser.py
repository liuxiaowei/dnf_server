import xlrd
import csv
from datetime import datetime
import math
from app.libs.error import APIError
from app.libs.error_code import *
from app.libs.log import APP_LOGGER
import os


class Excel_Column_Info():
    def __init__(self, column_name):
        self.column_name = column_name
        self.column_index = 0
    def match_index(self, column, content):
        if self.column_name:
           if content == self.column_name:
                self.column_index = column
                return True
        return False


class BillInfomation():
    def __init__(self, row, name, trade_time, amount, account,serial_number='', time_fomart = '%Y-%m-%d %H:%M'):
        self.row = row
        self.name = str(name).strip()
        self.trade_time = str(trade_time).strip().replace('/','-')
        self.amount = amount
        self.account = str(account).strip()
        self.serial_number = str(serial_number).strip()
        self.trade_date = datetime.strptime(self.trade_time, time_fomart)

    def outputdebuginfo(self):
        print('row [',self.row, '] name [',self.name,'] trade time[', self.trade_time, '] account[', self.account,
              '] amount[',self.amount, '] serial number[', self.serial_number,']')


#账单分析基类
class BillParseBase():
    __abstract__ = True

    def __init__(self, name, trade_time, amount, account, serial_number='', time_fomart = '%Y-%m-%d %H:%M'):
        self.name = Excel_Column_Info(name)#"姓名"列的序号
        self.trade_time = Excel_Column_Info(trade_time) #订单创建时间的序号
        self.amount =Excel_Column_Info(amount)#金额
        self.account = Excel_Column_Info(account)#对方账号的序号
        self.serial_number =Excel_Column_Info(serial_number)#金额
        self.time_fomart = time_fomart
    def checkcolumns(self):#检查文件是否有效
        if self.amount.column_index == 0 or self.trade_time.column_index == 0 or self.account.column_index == 0:
            return False
        return True


class AlipayParse(BillParseBase):
    def __init__(self):
        self.name.column_name = '交易对方'
        self.create_time.column_name = '交易创建时间'
        self.amount_column.column_name = '金额（元)'


class SDRCUParse(BillParseBase):#山东农村信用社
    def __init__(self):
        BillParseBase.__init__(self,'对方户名', '交易日期', '存入', '对方账户','', '%Y%m%d')


class BQDParse(BillParseBase):#青岛银行
    def __init__(self):
        BillParseBase.__init__(self,'对方户名', '交易日期', '收入金额', '对方账号','','%Y-%m-%d')


class CIBParse(BillParseBase):  # 兴业银行
    def __init__(self):
        BillParseBase.__init__(self, '对方户名', '交易日期', '贷方金额', '对方账号','银行流水号','%Y-%m-%d %H:%M:%S')


def alipay_parse(bankname, filename):
    csv_reader = csv.reader(open(filename, encoding='GBK'))
    result = []
    index = 0
    for row in csv_reader:
        index += 1
        if len(row)<11:
            continue
        if str(row[11]).find('收入') != -1 and str(row[9]).find('收款') != -1 and str(row[11]).find('交易成功') != -1:
            continue
        if row[3].strip() == '':
                continue
        try:#检验金额
            amount = float(str(row[9]).replace(',', ''))
        except Exception:
            continue
            pass
        if math.isclose(amount, 0.0) == False:
            result.append(BillInfomation(index, row[7], row[3].strip(),amount, '',row[0],'%Y-%m-%d %H:%M:%S'))
    for item in result:
        item.outputdebuginfo()
    return result

def read_excel(bankname, filename):
    sr = None
    try:
        if bankname == '支付宝':
            return alipay_parse(bankname, filename)
        elif bankname == '山东农村信用社':
            sr = SDRCUParse()
        elif bankname == '青岛银行':
            sr = BQDParse()
        elif bankname == '兴业银行':
            sr = CIBParse()
        if not sr:
            raise APIError(code=CommonErrorCode.UNSUPPORT_BANK.value)
        ExcelFile=xlrd.open_workbook(r'{0}'.format(filename))
        if not ExcelFile:
            raise APIError(code=CommonErrorCode.OPEN_FILE_ERROR.value)
        sheet_names = ExcelFile.sheet_names()
        if not sheet_names:
            raise APIError(code=CommonErrorCode.NO_EXCLE_SHEET.value)
        sheet = ExcelFile.sheet_by_index(0)
        row_count = sheet.nrows
        information_row = -1
        for row in range(0, row_count):
            if information_row != -1:
                break
            row_data = sheet.row_values(row)  # 获得第1行的数据列表
            for column in range(0, len(row_data)):
                if sr.name.match_index(column, row_data[column]):
                    information_row = row
                elif sr.trade_time.match_index(column, row_data[column]):
                    information_row = row
                elif sr.account.match_index(column, row_data[column]):
                    information_row = row
                elif sr.amount.match_index(column, row_data[column]):
                    information_row = row
                elif sr.serial_number.match_index(column, row_data[column]):
                    information_row = row
        if sr.checkcolumns() == False:
            raise APIError(code=CommonErrorCode.WRONG_EXCLE_FORMAT.value)
        result = []
        for row in range(information_row+1, row_count):
            row_data = sheet.row_values(row)
            if str(row_data[sr.trade_time.column_index]).strip() == '':
                continue
            try:
                amount = float(str(row_data[sr.amount.column_index]).replace(',', ''))
            except Exception:
                continue
                pass
            if math.isclose(amount, 0.0) == False:
                if sr.serial_number.column_index != 0:
                    result.append(BillInfomation( row+1,row_data[sr.name.column_index], row_data[sr.trade_time.column_index],
                           amount,row_data[sr.account.column_index],'',sr.time_fomart))
                else:
                    result.append(BillInfomation( row+1,row_data[sr.name.column_index], row_data[sr.trade_time.column_index],
                           amount, row_data[sr.account.column_index],row_data[sr.serial_number.column_index],sr.time_fomart))
        return result
    except Exception as e:
        APP_LOGGER.error('auth_work exception: {}'.format(str(e)))
        raise APIError(code=CommonErrorCode.OPEN_FILE_ERROR.value)
    finally:
        if os.path.exists(filename):
            os.remove(filename)


def read_ad_template_file(filename):
    ExcelFile = xlrd.open_workbook(r'{0}'.format(filename))
    sheet_names = ExcelFile.sheet_names()
    if not sheet_names:
        raise APIError(code=CommonErrorCode.NO_EXCLE_SHEET.value)
    sheet = ExcelFile.sheet_by_index(0)
    row_count = sheet.nrows
    if row_count<1:
        raise APIError(code=CommonErrorCode.NO_EXCLE_ROW.value)
    column_count = len(sheet.row_values(0))  # 获得第1行的数据列表
    if column_count < 1:
       raise APIError(code=CommonErrorCode.WRONG_EXCLE_FORMAT.value)
    items = []
    for row in range(1, row_count):
        content = {'password': None, 'pin': None}
        for col in range(column_count):
            ctype = sheet.cell( row, col).ctype  # 表格的数据类型
            cell = sheet.cell_value(row, col)
            if ctype == 2 and cell % 1 == 0:  # 如果是整形
                cell = int(cell)
            if col == 0:
                content['password'] = str(cell)
            if col == 1:
                content['pin'] = str(cell)
        items.append(content)
    return items


def read_ad_template(filename):
    try:
        return read_ad_template_file(filename)
    except Exception as e:
        APP_LOGGER.error('read_ad_template exception: {}'.format(str(e)))
        raise APIError(code=CommonErrorCode.OPEN_FILE_ERROR.value)
    finally:
        if os.path.exists(filename):
            os.remove(filename)


def read_account_template_file(filename):
    excel_file = xlrd.open_workbook(r'{0}'.format(filename))
    sheet_names = excel_file.sheet_names()
    if not sheet_names:
        raise APIError(code=CommonErrorCode.NO_EXCLE_SHEET.value)
    table = excel_file.sheet_by_index(0)
    row_count = table.nrows
    if row_count < 1:
        raise APIError(code=CommonErrorCode.NO_EXCLE_ROW.value)
    column_count = table.ncols
    if column_count < 1:
        raise APIError(code=CommonErrorCode.WRONG_EXCLE_FORMAT.value)
    items = []
    for i in range(1, row_count):
        row = table.row_values(i)
        content = {
        }
        # for col in range(column_count):
        #     ctype = table.cell(row, col).ctype  # 表格的数据类型
        #     cell = table.cell_value(row, col)
        #     if ctype == 2 and cell % 1 == 0:  # 如果是整形
        #         cell = int(cell)
        #     if col == 0:
        #         content['password'] = str(cell)
        items.append(content)
    return items


def read_account_template(filename):
    try:
        return read_account_template_file(filename)
    except Exception as e:
        APP_LOGGER.error('read_ad_template exception: {}'.format(str(e)))
        raise APIError(code=CommonErrorCode.OPEN_FILE_ERROR.value)
    finally:
        if os.path.exists(filename):
            os.remove(filename)
