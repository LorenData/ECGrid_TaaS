from bots.botsconfig import *

syntax = {
        'field_sep': ',',
        'quote_char':	'"',
        'charset':  "iso-8859-1",
        'noBOTSID': True,   # use this if there is no 'record identification' this is only possible it all records are the same kind of records.
        }

nextmessageblock = ({'BOTSID': 'HEA', 'ORDERNUMBER': None})

structure = [{ID: 'HEA', MIN: 1, MAX: 10000}]


recorddefs = {
    'HEA':[
            ['BOTSID','C',3,'A'],
            ['ORDERVERSION', 'C', 20, 'AN'],
            ['SENDER', 'C', 13, 'AN'],
            ['RECEIVER', 'C', 13, 'AN'],
            ['TEST', 'C', 1, 'AN'],
            ['ORDERNUMBER', 'C', 17, 'AN'],
            ['ORDERDATE', 'C', 12, 'AN'],
            ['ORDERTYPE', 'C', 3, 'AN'],
            ['PURCHASER', 'C', 13, 'AN'],
            ['SUPPLIER', 'C', 13, 'AN'],
            ['DESTINATION', 'C', 13, 'AN'],
            ['INVOICE', 'C', 13, 'AN'],
            ['DELIVERYDATE', 'C', 12, 'AN'],
            ['NODELAFTER', 'C', 12, 'AN'],
            ['NODELBEFORE', 'C', 12, 'AN'],
            ['LINE', 'C', 6, 'N'],
            ['ITEM', 'C', 14, 'AN'],
            ['QUANTITY', 'C', 16, 'R'],
            ['PRICE', 'C', 15.3, 'N'],
            ['DESCRIPTION', 'C', 80, 'AN'],
          ],
    }
