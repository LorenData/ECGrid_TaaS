# mapping-script
import time


def main(inn,out):
    
    # Set Out TA info
    out.ta_info['frompartner'] = inn.ta_info['frompartner']
    out.ta_info['topartner'] = inn.ta_info['topartner']

    if 'testindicator' not in inn.ta_info:
        inn.ta_info['testindicator'] = 'P'
        out.ta_info['testindicator'] = 'P'

    # ST Segment
    out.put({'BOTSID': 'ST', 'ST01': '850'})
    out.put({'BOTSID': 'ST', 'ST02': out.ta_info['reference'].zfill(4)})

    # BEG
    purpose_code = '00'
    ordertype_code = 'NE'

    order_number = inn.get({'BOTSID':'HEA','ORDERNUMBER':None})
    inn.ta_info['botskey'] = order_number
    out.ta_info['botskey'] = order_number

    order_date = inn.get({'BOTSID':'HEA','ORDERDATE':None})
    
    out.put({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG01': purpose_code})
    out.put({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG02': ordertype_code})
    out.put({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG03': order_number})
    out.put({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG05': order_date})

    deldate = inn.get({'BOTSID': 'HEA', 'DELIVERYDATE': None})
    notbeforedate = inn.get({'BOTSID': 'HEA', 'NODELBEFORE': None})
    notafterdate = inn.get({'BOTSID': 'HEA', 'NODELAFTER': None})

    out.put({'BOTSID':'ST'},{'BOTSID':'DTM','DTM01':'002','DTM02':deldate})
    out.put({'BOTSID':'ST'},{'BOTSID':'DTM','DTM01':'064','DTM02':notafterdate})
    out.put({'BOTSID':'ST'},{'BOTSID':'DTM','DTM01':'063','DTM02':notbeforedate})

    # N1
    puchaser = inn.get({'BOTSID': 'HEA', 'PURCHASER': None})
    out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': 'BY', 'N103': '92', 'N104': puchaser})
    
    supplier = inn.get({'BOTSID': 'HEA', 'SUPPLIER': None})
    out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': 'SE', 'N103': '92', 'N104': supplier})
    
    delivery = inn.get({'BOTSID': 'HEA', 'DESTINATION': None})
    out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': 'ST', 'N103': '92', 'N104': delivery})
    

    for item in inn.getloop({'BOTSID':'HEA'},{'BOTSID':'LIN'}):
        lineout = out.putloop({'BOTSID':'ST'},{'BOTSID':'PO1'})
        
        linenum = item.get({'BOTSID':'LIN','LINE':None})
        itemnum = item.get({'BOTSID':'LIN','ITEM':None})
        count = item.get({'BOTSID':'LIN','COUNT':None})
        description = item.get({'BOTSID':'LIN','DESCRIPTION':None})

        lineout.put({'BOTSID': 'PO1', 'PO101': linenum})
        lineout.put({'BOTSID': 'PO1', 'PO106': 'UP', 'PO107': itemnum})
        lineout.put({'BOTSID': 'PO1', 'PO102': count, 'PO103': 'EA', 'PO104': '0.00'})
        lineout.put({'BOTSID':'PO1'},{'BOTSID':'PID','PID01':'F', 'PID02':'08', 'PID05':description})
        
    # bots counts line items
    out.put({'BOTSID': 'ST'}, {'BOTSID': 'CTT', 'CTT01': out.getcountoccurrences({'BOTSID': 'ST'}, {'BOTSID': 'PO1'})})
    
    #SE01: bots counts the segments produced in the X12 message.
    out.put({'BOTSID':'ST'},{'BOTSID':'SE','SE01':out.getcount()+1,'SE02':out.ta_info['reference'].zfill(4)})  
