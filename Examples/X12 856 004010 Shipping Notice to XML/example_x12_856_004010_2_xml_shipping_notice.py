# mapping-script
import bots.transform as transform
from datetime import datetime


def main(inn, out):
    
    # ISA,GS,ST
    sender = inn.ta_info['frompartner']
    receiver = inn.ta_info['topartner']
    testindicator = inn.ta_info['testindicator']

    out.put({'BOTSID': 'message', 'sender': sender})
    out.put({'BOTSID': 'message', 'receiver': receiver})
    out.put({'BOTSID': 'message', 'testindicator': testindicator})

    # BSN

    shipmentnum = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'BSN', 'BSN02': None})
    out.ta_info['botskey'] = shipmentnum
    asndate = transform.datemask(inn.get({'BOTSID': 'ST'}, {'BOTSID': 'BSN', 'BSN03': None}), 'CCYYMMDD', 'CCYY-MM-DD')
    asntime = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'BSN', 'BSN04': None})

    out.put({'BOTSID': 'message', 'docnum': shipmentnum})
    out.put({'BOTSID': 'message', 'docdtm': asndate})
    out.put({'BOTSID': 'message', 'doctime': asntime})

    # shipment level/loop
    shipmentLoop = inn.getloop({'BOTSID':'ST'},{'BOTSID':'HL','HL01':'1','HL03':'S'})

    for shipment in shipmentLoop: 

        #TD5
        scac = shipment.get({'BOTSID': 'HL'}, {'BOTSID': 'TD5', 'TD501': 'O', 'TD502': '2', 'TD503': None})
        out.put({'BOTSID': 'message', 'scac': scac})
        
        # REF
        bol = shipment.get({'BOTSID': 'HL'}, {'BOTSID': 'REF', 'REF01': 'BM', 'REF02': None})
        carrierref = shipment.get({'BOTSID': 'HL'}, {'BOTSID': 'REF', 'REF01': 'CN', 'REF02': None})
        
        out.put({'BOTSID': 'message', 'bol': bol})
        out.put({'BOTSID': 'message', 'carrierreferencenumber': carrierref})
        
        # DTM
        shipdate = transform.datemask(shipment.get({'BOTSID': 'HL'}, {'BOTSID': 'DTM', 'DTM01': '011', 'DTM02': None}), 'CCYYMMDD', 'CCYY-MM-DD')
        deliverydate = transform.datemask(shipment.get({'BOTSID': 'HL'}, {'BOTSID': 'DTM', 'DTM01': '017', 'DTM02': None}), 'CCYYMMDD', 'CCYY-MM-DD')

        out.put({'BOTSID': 'message', 'shipdtm': shipdate})
        out.put({'BOTSID': 'message', 'deldtm': deliverydate})

        # N1 loop on shipment level
        partysLoop = shipment.getloop({'BOTSID': 'HL'}, {'BOTSID': 'N1'})

        for party in partysLoop:
            partyout = out.putloop({'BOTSID': 'message'}, {'BOTSID': 'partys'}, {'BOTSID': 'party'})
            
            # N1
            partyQual = party.get({'BOTSID': 'N1', 'N101': None})
            # get DUNS number. 2 qualifiers are used; helper function transform.useoneof checks both
            duns = transform.useoneof(party.get({'BOTSID': 'N1', 'N103': '1', 'N104': None}), party.get({'BOTSID': 'N1', 'N103': '9', 'N104': None}))
            externalID = party.get({'BOTSID': 'N1', 'N103': '92', 'N104': None})
            internalID = party.get({'BOTSID': 'N1', 'N103': '91', 'N104': None})
            name1 = party.get({'BOTSID':'N1','N102':None})
            
            partyout.put({'BOTSID': 'party', 'qual': partyQual})
            partyout.put({'BOTSID': 'party', 'DUNS': duns})
            partyout.put({'BOTSID': 'party', 'externalID': externalID})
            partyout.put({'BOTSID': 'party', 'internalID': internalID})
            partyout.put({'BOTSID': 'party', 'name1': name1})
            
            # N2
            name2 = party.get({'BOTSID': 'N1'}, {'BOTSID': 'N2', 'N201': None})

            partyout.put({'BOTSID': 'party', 'name2': name2})
            
            # N3
            address1 = party.get({'BOTSID': 'N1'}, {'BOTSID': 'N3', 'N301': None})
            address2 = party.get({'BOTSID': 'N1'}, {'BOTSID': 'N3', 'N302': None})

            partyout.put({'BOTSID': 'party', 'address1': address1})
            partyout.put({'BOTSID': 'party', 'address2': address2})
            
            # N4
            city = party.get({'BOTSID': 'N1'}, {'BOTSID': 'N4', 'N401': None})
            region = party.get({'BOTSID': 'N1'}, {'BOTSID': 'N4', 'N402': None})
            zipcode = party.get({'BOTSID': 'N1'}, {'BOTSID': 'N4', 'N403': None})
            country = party.get({'BOTSID': 'N1'}, {'BOTSID': 'N4', 'N404': None})

            partyout.put({'BOTSID': 'party', 'city': city})
            partyout.put({'BOTSID': 'party', 'state': region})
            partyout.put({'BOTSID': 'party', 'pcode': zipcode})
            partyout.put({'BOTSID': 'party', 'country': country})
            
    # order level/loop
    orderLoop = inn.getloop({'BOTSID':'ST'},{'BOTSID':'HL','HL03':'O'})
    for in_order in orderLoop:
        out_order = out.putloop({'BOTSID': 'message'}, {'BOTSID': 'orders'}, {'BOTSID': 'order'})
        current_order = in_order.get({'BOTSID': 'HL', 'HL01': None})
        
        # PRF
        order_number = in_order.get({'BOTSID': 'HL'}, {'BOTSID': 'PRF', 'PRF01': None})
        orderdate = transform.datemask(in_order.get({'BOTSID': 'HL'}, {'BOTSID': 'PRF', 'PRF04': None}), 'CCYYMMDD', 'CCYY-MM-DD')
        
        out_order.put({'BOTSID': 'order', 'ordernumber': order_number})
        out_order.put({'BOTSID': 'order', 'orderdtm': orderdate})
        
        # pack/sscc level/loop
        packs = inn.getloop({'BOTSID':'ST'},{'BOTSID':'HL','HL02':current_order,'HL03':'P'})
        for in_pack in packs:
            current_sscc = in_pack.get({'BOTSID': 'HL', 'HL01': None})
            sscc = in_pack.get({'BOTSID': 'HL'}, {'BOTSID': 'MAN', 'MAN01': 'GM', 'MAN02': None})
            
            # linelevel/loop
            # loop over all lines that have this sscc
            linesinpack = inn.getloop({'BOTSID':'ST'},{'BOTSID':'HL','HL02':current_sscc,'HL03':'I'})
            for line in linesinpack:
                lineout = out_order.putloop({'BOTSID': 'order'}, {'BOTSID': 'lines'}, {'BOTSID': 'line'})
                
                # LIN
                linenum = line.get({'BOTSID': 'HL'}, {'BOTSID': 'LIN', 'LIN01': None})
                gtin = line.get({'BOTSID': 'HL'}, {'BOTSID': 'LIN', 'LIN02': 'UP', 'LIN03': None})
                
                lineout.put({'BOTSID': 'line', 'linenum': linenum})
                lineout.put({'BOTSID': 'line', 'gtin': gtin})

                # SN1
                deliveryquantity = line.get({'BOTSID': 'HL'}, {'BOTSID': 'SN1', 'SN103': 'EA', 'SN102': None})
                orderquantity = line.get({'BOTSID': 'HL'}, {'BOTSID': 'SN1', 'SN106': 'EA', 'SN105': None})

                lineout.put({'BOTSID': 'line', 'delqua': deliveryquantity})
                lineout.put({'BOTSID': 'line', 'ordqua': orderquantity})

                # PID
                descritpion = line.get({'BOTSID': 'HL'}, {'BOTSID': 'PID', 'PID01': 'F', 'PID02': '08', 'PID05': None})

                lineout.put({'BOTSID': 'line', 'desc': descritpion})
                lineout.put({'BOTSID': 'line', 'sscc': sscc})
