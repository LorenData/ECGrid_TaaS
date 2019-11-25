# mapping-script

def main(inn, out):
    
    # ISA,GS,ST
    sender = inn.ta_info['frompartner']
    receiver = inn.ta_info['topartner']
    testindicator = inn.ta_info['testindicator']
    version = inn.ta_info['version']
    doc = inn.get({'BOTSID': 'ST', 'ST01': None})

    # BEG
    ordertype = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG02': None})
    ordernumber = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG03': None})
    out.ta_info['reference'] = ordernumber
    out.ta_info['botskey'] = ordernumber

    orderdate = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG05': None})
    
    # DTM
    deliverydate = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'DTM', 'DTM01': '002', 'DTM02': None})
    nodeliveryafter = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'DTM', 'DTM01': '063', 'DTM02': None})
    nodeliverybefore = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'DTM', 'DTM01': '064', 'DTM02': None})
    
    # N1
    purchaser = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': 'BY', 'N104': None})
    destination = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': 'ST', 'N104': None})
    supplier = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': 'SF', 'N104': None})

    for po1 in inn.getloop({'BOTSID':'ST'},{'BOTSID':'PO1'}):
        lineout = out.putloop({'BOTSID':'HEA'})  # this is needed; it takes care of initialising a new HEA-record

        lineout.put({'BOTSID': 'HEA', 'SENDER': sender})
        lineout.put({'BOTSID': 'HEA', 'RECEIVER': receiver})
        lineout.put({'BOTSID': 'HEA', 'TEST': testindicator})
        lineout.put({'BOTSID': 'HEA', 'ORDERVERSION': doc + version})
        lineout.put({'BOTSID': 'HEA', 'ORDERNUMBER': ordernumber})
        lineout.put({'BOTSID': 'HEA', 'ORDERTYPE': ordertype})
        lineout.put({'BOTSID': 'HEA', 'ORDERDATE': orderdate})
        lineout.put({'BOTSID': 'HEA', 'DELIVERYDATE': deliverydate})
        lineout.put({'BOTSID': 'HEA', 'NODELAFTER': nodeliveryafter})
        lineout.put({'BOTSID': 'HEA', 'NODELBEFORE': nodeliverybefore})
        lineout.put({'BOTSID': 'HEA', 'PURCHASER': purchaser})
        lineout.put({'BOTSID': 'HEA', 'SUPPLIER': supplier})
        lineout.put({'BOTSID': 'HEA', 'DESTINATION': destination})
        
        linenum = po1.get({'BOTSID': 'PO1', 'PO101': None})
        itemnum = po1.get({'BOTSID': 'PO1', 'PO107': None})
        price = po1.get({'BOTSID': 'PO1', 'PO104': None})
        qunatity = po1.get({'BOTSID': 'PO1', 'PO102': None})
        description = po1.get({'BOTSID': 'PO1'}, {'BOTSID': 'PID', 'PID05': None})
        
        lineout.put({'BOTSID': 'HEA', 'LINE': linenum})
        lineout.put({'BOTSID': 'HEA', 'ITEM': itemnum})
        lineout.put({'BOTSID': 'HEA', 'QUANTITY': qunatity})
        lineout.put({'BOTSID': 'HEA', 'PRICE': price})
        lineout.put({'BOTSID': 'HEA', 'DESCRIPTION': description})
