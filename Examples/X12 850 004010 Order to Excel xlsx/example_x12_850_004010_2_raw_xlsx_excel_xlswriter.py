# mapping-script
import xlsxwriter
import io
import bots.transform as transform


def main(inn, out):

    out.ta_info['frompartner'] = ""
    out.ta_info['topartner'] = ""
    out.ta_info['testindicator'] = "P"
    inn.ta_info['testindicator'] = "P"
    inn.ta_info['botskey'] = "123456"
    out.ta_info['botskey'] = "123456"

    reference = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG03': None})
    orderdate = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG05': None})
    purpose_code = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG01': None})
    SCAC = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'TD5', 'TD502': '2', 'TD503': None})
    CarrierName = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'TD5', 'TD505': None})

    # Create a workbook and add a worksheet.
    excelData = io.BytesIO()
    workbook = xlsxwriter.Workbook(excelData)
    worksheet = workbook.add_worksheet()

    # Some data we want to write to the worksheet.
    expenses = (
        ['Rent', 1000],
        ['Gas',   100],
        ['Food',  300],
        ['Gym',    50],
    )

    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0

    # Iterate over the data and write it out row by row.
    for item, cost in (expenses):
        worksheet.write(row, col,     item)
        worksheet.write(row, col + 1, cost)
        row += 1

    # Write a total using a formula.
    worksheet.write(row, 0, 'Total')
    worksheet.write(row, 1, '=SUM(B1:B4)')
    worksheet.write(7, 0, reference)
    worksheet.write(7, 1, orderdate)
    worksheet.write(7, 2, purpose_code)
    worksheet.write(7, 3, SCAC)
    worksheet.write(7, 4, CarrierName)

    workbook.close()

    # Write to Output.
    out.root = excelData.getvalue()

    excelData.close()
