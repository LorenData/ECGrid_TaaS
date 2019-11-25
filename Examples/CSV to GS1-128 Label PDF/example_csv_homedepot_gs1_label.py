from bots.botsconfig import *

syntax = {
    'field_sep': '|',
    'quote_char': '"',
    'charset': "iso-8859-1",
    'noBOTSID': True
    }

nextmessageblock = ({'BOTSID': 'LBL', 'TONUMBER': None})

structure = [{ID:'LBL', MIN:1, MAX:10000}]

recorddefs = {
    'LBL': [
            ['BOTSID', 'C', 3, 'A'],
            ['FROMNAME', 'C', 60, 'AN'],
            ['FROMADDR', 'C', 55, 'AN'],
            ['FROMADDR2', 'C', 55, 'AN'],
            ['FROMCITY', 'C', 30, 'AN'],
            ['FROMSTATE', 'C', 2, 'AN'],
            ['FROMZIP', 'C', 15, 'AN'],
            ['TONUMBER', 'C', 30, 'AN'],
            ['TONAME', 'C', 60, 'AN'],
            ['TOADDR', 'C', 55, 'AN'],
            ['TOADDR2', 'C', 55, 'AN'],
            ['TOCITY', 'C', 30, 'AN'],
            ['TOSTATE', 'C', 2, 'AN'],
            ['TOZIP', 'C', 15, 'AN'],
            ['CARRIER', 'C', 30, 'AN'],
            ['PRONUMBER', 'C', 30, 'AN'],
            ['BOL', 'C', 30, 'AN'],
            ['STORENUMBER', 'C', 30, 'AN'],
            ['PONUMBER', 'C', 22, 'AN'],
            ['PALLETNUMBER', 'C', 5, 'AN'],
            ['TOTALPALLETS', 'C', 5, 'AN'],
            ['CARTONS', 'C', 5, 'AN'],
            ['SSCCCOMPANYPREFIX', 'C', 7, 'AN'],
            ['SSCCSERIAL', 'C', 9, 'AN'],
        ],
    }
