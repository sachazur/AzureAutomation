import xlrd
def open_file(path):
    """"
    open and read file
    """
    book = xlrd.open_workbook(path)
    print (book.nsheets)
    print (book.sheet_names())
    first_sheet = book.sheet_by_index(0)
    print (first_sheet.row_values(0))
    cell = first_sheet.cell(0,0)
    print (cell.value)
if __name__ == "__main__":
    path = "example.xls"
    open_file(path)
