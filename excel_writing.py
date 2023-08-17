import xlsxwriter

def excel_write(matrix, offers_list, counts_available):
    workbook = xlsxwriter.Workbook('edbo.xlsx')

    worksheet = workbook.add_worksheet('Distributing')
    bold = workbook.add_format({'bold': True})
    col = 1

    # Iterate over the data and write it out row by row.
    for ind, offer_info in list(enumerate(offers_list)):
        worksheet.write(0, col, offer_info[0],  bold)
        worksheet.set_column(col, col, 20)
        worksheet.write(0, col+1, 'БО: ' + str(offer_info[1]),  bold)
        worksheet.set_column(col+1, col+1, 25)
        worksheet.write(0, col+2, 'Вільно: ' + str(counts_available[ind]),  bold)
        worksheet.set_column(col+2, col+2, 4)

        col += 9


    for ind, offer in list(enumerate(matrix)):
        row = 1
        col = ind*9
        for req in offer:
            for data in req:
                worksheet.write(row, col, str(data))
                col += 1
                print(row, col)
            col = ind*9
            row += 1
        
    workbook.close()

matrix = [ [ (1,2,3), (1,2,3)], [[2,3.87,4], [2.5,3,4]], [[3,4,5], [3,4,5]]]
offers_list = (("one", 23), ("two", 12), ("three", 17))
counts_available = [2, 0, 4]

