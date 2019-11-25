# mapping-script


def main(inn, out):

    sender = inn.ta_info['frompartner']
    out.ta_info['frompartner'] = sender

    receiver = inn.ta_info['topartner']
    out.ta_info['topartner'] = receiver

    if 'testindicator' not in inn.ta_info:
        inn.ta_info['testindicator'] = '0'
        out.ta_info['testindicator'] = '0'

    out.put({'BOTSID': 'UNH', '0062': out.ta_info['reference'], 'S009.0065': 'ORDERS', 'S009.0052': 'D', 'S009.0054': '96A', 'S009.0051': 'UN', 'S009.0057': 'EAN008'})
    out.put({'BOTSID': 'UNH'}, {'BOTSID': 'UNS', '0081': 'S'})

    docnr = inn.get({'BOTSID': 'E2EDK01003', 'BELNR': None})
    out.put({'BOTSID': 'UNH'}, {'BOTSID': 'BGM', '1004': docnr})
    inn.ta_info['botskey'] = docnr
    out.ta_info['botskey'] = docnr

    idocsortorder = inn.get({'BOTSID': 'E2EDK01003'}, {'BOTSID': 'E2EDKA1002', 'PARVW': 'AG', 'IHREZ': None})
    if idocsortorder is None:  # not there, or empty string
        sortorder = '220'
    elif idocsortorder.isdigit():
        sortorder = '352'
        out.put({'BOTSID': 'UNH'}, {'BOTSID': 'FTX', '4451': 'ZZZ', 'C107.3055': '92', 'C107.4441': idocsortorder})
    elif idocsortorder == 'A':
        sortorder = '220'
        out.put({'BOTSID': 'UNH'}, {'BOTSID': 'RFF', 'C506.1153': 'PD', 'C506.1154': '99'})
    elif idocsortorder == 'AC':
        sortorder = '230'
    else:
        raise Exception('Geen valide code in IHREZ waar PARVW = "AG".')

    out.put({'BOTSID': 'UNH'}, {'BOTSID': 'BGM', 'C002.1001': sortorder})
    out.put({'BOTSID': 'UNH'}, {'BOTSID': 'RFF', 'C506.1153': 'AAK', 'C506.1154': inn.get({'BOTSID': 'E2EDK01003'}, {'BOTSID': 'E2EDK02', 'BELNR': None, 'QUALF': '007'})})
    out.put({'BOTSID': 'UNH'}, {'BOTSID': 'NAD', '3035': 'BY', 'C082.3055': '9', 'C082.3039': inn.get({'BOTSID': 'E2EDK01003'}, {'BOTSID': 'E2EDKA1002', 'PARVW': 'AG', 'PARTN': None})})
    out.put({'BOTSID': 'UNH'}, {'BOTSID': 'NAD', '3035': 'SU', 'C082.3055': '9', 'C082.3039': inn.get({'BOTSID': 'E2EDK01003'}, {'BOTSID': 'E2EDKA1002', 'PARVW': 'LF', 'ILNNR': None})})
    out.put({'BOTSID': 'UNH'}, {'BOTSID': 'NAD', '3035': 'DP', 'C082.3055': '9', 'C082.3039': inn.get({'BOTSID': 'E2EDK01003'}, {'BOTSID': 'E2EDKA1002', 'PARVW': 'WE', 'LIFNR': None})})
    out.put({'BOTSID': 'UNH'}, {'BOTSID': 'DTM', 'C507.2005': '137', 'C507.2379': '102', 'C507.2380': inn.get({'BOTSID': 'E2EDK01003'}, {'BOTSID': 'E2EDK03', 'DATUM': None, 'IDDAT': '012'})})

    DELIVERYDATE = inn.get({'BOTSID': 'E2EDK01003'}, {'BOTSID': 'E2EDP01003'}, {'BOTSID': 'E2EDP20', 'EDATU': None})
    if DELIVERYDATE:
        if len(DELIVERYDATE) == 8:
            FDELIVERYDATE = '102'
        else:
            FDELIVERYDATE = '203'
        out.put({'BOTSID': 'UNH'}, {'BOTSID': 'DTM', 'C507.2005': '2', 'C507.2380': DELIVERYDATE, 'C507.2379': FDELIVERYDATE})
        LDELIVERYDATE = inn.get({'BOTSID': 'E2EDK01003'}, {'BOTSID': 'E2EDK02', 'DATUM': None, 'QUALF': '020'})

    if LDELIVERYDATE:
        if len(LDELIVERYDATE) == 8:
            FDELIVERYDATE = '102'
        else:
            FDELIVERYDATE = '203'
        out.put({'BOTSID': 'UNH'}, {'BOTSID': 'DTM', 'C507.2005': '63', 'C507.2380': LDELIVERYDATE, 'C507.2379': FDELIVERYDATE})

    for line in inn.getloop({'BOTSID': 'E2EDK01003'}, {'BOTSID': 'E2EDP01003'}):
        lou = out.putloop({'BOTSID': 'UNH'}, {'BOTSID': 'LIN'})
        lou.put({'BOTSID': 'LIN', '1082': line.get({'BOTSID': 'E2EDP01003', 'POSEX': None})})
        lou.put({'BOTSID': 'LIN', 'C212.7143': 'IN', 'C212.7140': line.get({'BOTSID': 'E2EDP01003'}, {'BOTSID': 'E2EDP19001', 'QUALF': '001', 'IDTNR': None})})
        lou.put({'BOTSID': 'LIN'}, {'BOTSID': 'QTY', 'C186.6063': '21', 'C186.6060': line.get({'BOTSID': 'E2EDP01003', 'MENGE': None})})

    # last line (counts the segments produced in out-message, add 1 for UNT itself)
    out.put({'BOTSID': 'UNH'}, {'BOTSID': 'UNT', '0074': out.getcount() + 1, '0062': out.ta_info['reference']})
