# mapping-script
import bots.transform as transform
import decimal


def main(inn, out):
    # process the lines in a loop
    headerwritten = False
    for line in inn.getloop({'BOTSID': 'HEA'}):
        if not headerwritten:
            out.ta_info['frompartner'] = line.get({'BOTSID': 'HEA', 'SENDER': None})
            out.ta_info['topartner'] = line.get({'BOTSID': 'HEA', 'RECEIVER': None})
            out.ta_info['testindicator'] = line.get({'BOTSID': 'HEA', 'TEST': None})
            inn.ta_info['testindicator'] = line.get({'BOTSID': 'HEA', 'TEST': None})

            # ST Segment
            out.put({'BOTSID': 'ST', 'ST01': '850'})
            out.put({'BOTSID': 'ST', 'ST02': out.ta_info['reference'].zfill(4)})

            # BEG
            purpose_code = '00'
            ordertype_code = line.get({'BOTSID':'HEA','ORDERTYPE':None})

            order_number = line.get({'BOTSID':'HEA','ORDERNUMBER':None})
            inn.ta_info['botskey'] = order_number
            out.ta_info['botskey'] = order_number

            order_date = transform.datemask(line.get({'BOTSID':'HEA','ORDERDATE':None}), 'YYYY-mm-DDT', 'YYYYmmDD')

            out.put({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG01': purpose_code})
            out.put({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG02': ordertype_code})
            out.put({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG03': order_number})
            out.put({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG05': order_date})

            # DTM
            deldate = transform.datemask(line.get({'BOTSID': 'HEA', 'DELIVERYDATE': None}), 'YYYY-mm-DDT', 'YYYYmmDD')
            notbeforedate = transform.datemask(line.get({'BOTSID': 'HEA', 'NODELBEFORE': None}), 'YYYY-mm-DDT', 'YYYYmmDD')
            notafterdate = transform.datemask(line.get({'BOTSID': 'HEA', 'NODELAFTER': None}), 'YYYY-mm-DDT', 'YYYYmmDD')

            out.put({'BOTSID':'ST'},{'BOTSID':'DTM','DTM01':'002','DTM02': deldate})
            out.put({'BOTSID':'ST'},{'BOTSID':'DTM','DTM01':'064','DTM02': notafterdate})
            out.put({'BOTSID': 'ST'}, {'BOTSID': 'DTM', 'DTM01': '063', 'DTM02': notbeforedate})

            # N1
            puchaser = line.get({'BOTSID': 'HEA', 'PURCHASER': None})
            out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': 'BY', 'N103': '92', 'N104': puchaser})

            supplier = line.get({'BOTSID': 'HEA', 'SUPPLIER': None})
            out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': 'SE', 'N103': '92', 'N104': supplier})

            delivery = line.get({'BOTSID': 'HEA', 'DESTINATION': None})
            out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': 'ST', 'N103': '92', 'N104': delivery})

            headerwritten = True

        # process the line items
        lineout = out.putloop({'BOTSID': 'ST'}, {'BOTSID': 'PO1'})

        linenum = int(float(line.get({'BOTSID': 'HEA', 'LINE': None})))

        itemnum = line.get({'BOTSID':'HEA','ITEM':None})
        quantity = int(float(line.get({'BOTSID': 'HEA', 'QUANTITY': None})))

        price = line.get({'BOTSID': 'HEA', 'PRICE': None})

        DECIMALPLACES = decimal.Decimal(10) ** -2
        price = decimal.Decimal(price).quantize(DECIMALPLACES)

        description = line.get({'BOTSID':'HEA','DESCRIPTION':None})

        lineout.put({'BOTSID': 'PO1', 'PO101': linenum})
        lineout.put({'BOTSID': 'PO1', 'PO102': int(quantity), 'PO103': 'EA'})
        lineout.put({'BOTSID': 'PO1', 'PO104': price})
        lineout.put({'BOTSID': 'PO1', 'PO106': 'UP', 'PO107': itemnum})
        lineout.put({'BOTSID': 'PO1'}, {'BOTSID': 'PID', 'PID01': 'F', 'PID02': '08', 'PID05': description})

    # bots counts line items
    out.put({'BOTSID': 'ST'}, {'BOTSID': 'CTT', 'CTT01': out.getcountoccurrences({'BOTSID': 'ST'}, {'BOTSID': 'PO1'})})

    # SE01: bots counts the segments produced in the X12 message.
    out.put({'BOTSID': 'ST'}, {'BOTSID': 'SE', 'SE01': out.getcount() + 1, 'SE02': out.ta_info['reference'].zfill(4)})
