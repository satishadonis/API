import requests
import xlrd

path = "Usernames.xlsx"

inputWorkbook = xlrd.open_workbook(path)

#sheet = inputWorkbook.sheet_by_name("users")
sheet = inputWorkbook.sheet_by_index(0)
print(sheet.cell_value(1,0))

def test_case1():
    userName = 'lprincipe'
    URL= "http://10.10.220.99:91/api/v1/Member/User/{0}".format(userName)
    print(URL)
    response = requests.get(URL)
    print(response.json(),response.status_code,"-->",response.reason)

