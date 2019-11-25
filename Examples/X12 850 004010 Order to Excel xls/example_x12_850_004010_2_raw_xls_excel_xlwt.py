# mapping-script
import xlwt
import io


def main(inn, out):

    excelData = io.BytesIO()
    out.ta_info['frompartner'] = ""
    out.ta_info['topartner'] = ""
    out.ta_info['testindicator'] = "P"
    inn.ta_info['testindicator'] = "P"
    inn.ta_info['botskey'] = "HDGS1-128"
    out.ta_info['botskey'] = "HDGS1-128"

    # Create a workbook
    workbook = xlwt.Workbook()

    # Create a worksheet
    worksheet1 = workbook.add_sheet("Sheet1")

    # Select row to write data
    row_object = worksheet1.row(0)

    reference = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG03': None})
    orderdate = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG05': None})
    purpose_code = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG01': None})
    SCAC = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'TD5', 'TD502': '2', 'TD503': None})
    CarrierName = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'TD5', 'TD505': None})

    # index,value
    row_object.write(0, reference)
    row_object.write(1, orderdate)
    row_object.write(2, purpose_code)
    row_object.write(3, SCAC)
    row_object.write(4, CarrierName)

    # Save the workbook
    workbook.save(excelData)

    # Write to Output.
    out.root = excelData.getvalue()

    excelData.close()
