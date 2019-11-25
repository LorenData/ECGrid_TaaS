# mapping-script


def main(inn,out):
    
    # ISA,GS,ST
    sender = inn.ta_info['frompartner']
    receiver = inn.ta_info['topartner']
    testindicator = inn.ta_info['testindicator']

    out.put({'BOTSID':'HEA','SENDER':sender})
    out.put({'BOTSID':'HEA','RECEIVER':receiver})
    out.put({'BOTSID':'HEA','TEST':testindicator})

    # BEG
    reference = inn.get({'BOTSID':'ST'},{'BOTSID':'BEG','BEG03':None})
    out.put({'BOTSID': 'HEA', 'ORDERNUMBER': reference})
    out.ta_info['botskey'] = reference
    out.ta_info['reference'] = reference

    orderdate = inn.get({'BOTSID':'ST'},{'BOTSID':'BEG','BEG05':None})
    out.put({'BOTSID':'HEA','ORDERDATE':orderdate})
    
    # DTM
    deldate = inn.get({'BOTSID':'ST'},{'BOTSID':'DTM','DTM01':'002','DTM02':None})
    out.put({'BOTSID': 'HEA', 'DELIVERYDATE': deldate})
    
    delAfterdate = inn.get({'BOTSID':'ST'},{'BOTSID':'DTM','DTM01':'063','DTM02':None})
    out.put({'BOTSID': 'HEA', 'NODELAFTER': delAfterdate})
    
    delBeforedate = inn.get({'BOTSID':'ST'},{'BOTSID':'DTM','DTM01':'064','DTM02':None})
    out.put({'BOTSID':'HEA','NODELBEFORE':delBeforedate})

    # N1
    purchaserNum = inn.get({'BOTSID':'ST'},{'BOTSID':'N1','N101':'BY','N104':None})
    out.put({'BOTSID':'HEA','PURCHASER':purchaserNum})

    destination = inn.get({'BOTSID':'ST'},{'BOTSID':'N1','N101':'ST','N104':None})
    out.put({'BOTSID':'HEA','DESTINATION':destination})
    
    supplier = inn.get({'BOTSID':'ST'},{'BOTSID':'N1','N101':'SF','N104':None})
    out.put({'BOTSID':'HEA','SUPPLIER':supplier})

    # PO1 and PID
    for po1 in inn.getloop({'BOTSID':'ST'},{'BOTSID':'PO1'}):
        lineout = out.putloop({'BOTSID':'HEA'},{'BOTSID':'LIN'})
        
        linenum = po1.get({'BOTSID':'PO1','PO101':None})
        itemnum = po1.get({'BOTSID':'PO1','PO107':None})
        count = po1.get({'BOTSID':'PO1','PO102':None})
        description = po1.get({'BOTSID':'PO1'},{'BOTSID':'PID','PID05':None})

        lineout.put({'BOTSID':'LIN','LINE': linenum})
        lineout.put({'BOTSID':'LIN','ITEM': itemnum})
        lineout.put({'BOTSID':'LIN','COUNT': count})
        lineout.put({'BOTSID':'LIN','DESCRIPTION': description})
