# mapping-script
# use out.data to add attributes.
# out.data is passed to the template.


def main(inn, out):

    if 'testindicator' not in inn.ta_info:
        inn.ta_info['testindicator'] = 0

    out.data.header = {}
    out.data.header['VERSION'] = 'D96A'
    out.data.header['SENDER'] = inn.ta_info['frompartner']
    out.data.header['RECEIVER'] = inn.ta_info['topartner']
    out.data.header['TEST'] = inn.ta_info['testindicator']
    out.data.header['ORDERNUMBER'] = inn.get({'BOTSID': 'UNH'}, {'BOTSID': 'BGM', '1004': None})
    out.data.header['ORDERTYPE'] = inn.get({'BOTSID': 'UNH'}, {'BOTSID': 'BGM', 'C002.1001': None})
    out.data.header['CUSTOMER'] = inn.get({'BOTSID': 'UNH'}, {'BOTSID': 'NAD', '3035': 'BY', 'C082.3039': None})
    out.data.header['SUPPLIER'] = inn.get({'BOTSID': 'UNH'}, {'BOTSID': 'NAD', '3035': 'SU', 'C082.3039': None})
    out.data.header['DELIVERYADDR'] = inn.get({'BOTSID': 'UNH'}, {'BOTSID': 'NAD', '3035': 'DP', 'C082.3039': None})
    out.data.header['FROMADDR'] = inn.get({'BOTSID': 'UNH'}, {'BOTSID': 'NAD', '3035': 'SF', 'C082.3039': None})
    out.data.header['FINALDEST'] = inn.get({'BOTSID': 'UNH'}, {'BOTSID': 'NAD', '3035': 'UC', 'C082.3039': None})
    out.data.header['ORDERDATE'] = inn.get({'BOTSID': 'UNH'}, {'BOTSID': 'DTM', 'C507.2005': '137', 'C507.2380': None})
    out.data.header['DELIVERYDATE'] = inn.get({'BOTSID': 'UNH'}, {'BOTSID': 'DTM', 'C507.2005': '2', 'C507.2380': None})
    out.data.header['EARLIESTDELIVERYDATE'] = inn.get({'BOTSID': 'UNH'}, {'BOTSID': 'DTM', 'C507.2005': '64', 'C507.2380': None})
    out.data.header['LASTDELIVERYDATE'] = inn.get({'BOTSID': 'UNH'}, {'BOTSID': 'DTM', 'C507.2005': '63', 'C507.2380': None})
    out.data.header['DUTYFREE'] = 'Duty Free' if inn.get({'BOTSID': 'UNH'}, {'BOTSID': 'TAX', '5283': '7', 'C241.5153': 'ACT', '5305': 'E'}) else None
    out.data.header['IMPROVISED'] = 'Improvised' if inn.get({'BOTSID': 'UNH'}, {'BOTSID': 'BGM', '1225': '46'}) else None
    out.data.header['INDICATIONRECEPTIONCONFIRMATION'] = 'Confirmation Requested' if inn.get({'BOTSID': 'UNH'}, {'BOTSID': 'BGM', '4343': 'AB'}) else None
    out.data.header['BACKHAULING'] = 'Order is being met' if inn.get({'BOTSID': 'UNH'}, {'BOTSID': 'TOD', '4055': '4'}) else None
    out.data.header['URGENTORDER'] = 'Rush order' if inn.get({'BOTSID': 'UNH'}, {'BOTSID': 'TOD', '4055': '3', 'C100.4053': '02E'}) else None
    out.data.header['SHOPINSTALLATION'] = 'Store installation' if inn.get({'BOTSID': 'UNH'}, {'BOTSID': 'ALI', '4183#1': '77E'}) else None
    out.data.header['WINDOWORDERNUMBER'] = inn.get({'BOTSID': 'UNH'}, {'BOTSID': 'RFF', 'C506.1153': 'BO', 'C506.1154': None})
    out.data.header['ACTIONNUMBER'] = inn.get({'BOTSID': 'UNH'}, {'BOTSID': 'RFF', 'C506.1153': 'PD', 'C506.1154': None})

    out.data.lines = []
    for lin in inn.getloop({'BOTSID': 'UNH'}, {'BOTSID': 'LIN'}):
        out.data.lines.append({})
        out.data.lines[-1]['LINE'] = lin.get({'BOTSID': 'LIN', '1082': None})
        out.data.lines[-1]['ITEM'] = lin.get({'BOTSID': 'LIN', 'C212.7140': None})
        out.data.lines[-1]['QUANTITY'] = lin.get({'BOTSID': 'LIN'}, {'BOTSID': 'QTY', 'C186.6063': '21', 'C186.6060': None})
        out.data.lines[-1]['PROMOCODE'] = lin.get({'BOTSID': 'LIN'}, {'BOTSID': 'RFF', 'C506.1153': 'PD', 'C506.1154': None})
        out.data.lines[-1]['DESCRIPTION'] = lin.get({'BOTSID': 'LIN'}, {'BOTSID': 'IMD', 'C273.7008#1': None})
