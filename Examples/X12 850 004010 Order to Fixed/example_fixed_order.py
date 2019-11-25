from bots.botsconfig import *

nextmessage = ({'BOTSID': 'HEA'},)

syntax = { 
        'charset'     : 'iso-8859-1',
        'checkfixedrecordtooshort': True,
        }

structure=    [
    {ID:'HEA',MIN:1,MAX:10000,
        QUERIES:{
            'frompartner':  {'BOTSID':'HEA','SENDER':None},
            'topartner':    {'BOTSID':'HEA','RECEIVER':None},
            'reference':    {'BOTSID':'HEA','ORDERNUMBER':None},
            'testindicator':{'BOTSID':'HEA','TEST':None}},
        LEVEL:[
            {ID:'LIN',MIN:0,MAX:10000},
            ]},
    ]

recorddefs = {
    'HEA':[
            ['BOTSID','C',3,'A'],    #pos 1
            ['ORDERVERSION', 'C', 20, 'A'],    #pos 4
            ['SENDER', 'C', 13, 'AN'],    #pos 24
            ['RECEIVER', 'C', 13, 'AN'],    #pos 37
            ['TEST', 'C', 1, 'AN'],    #pos 50
            ['ORDERNUMBER', 'C', 17, 'AN'],    #pos 51
            ['ORDERDATE', 'C', 8, 'AN'],    #pos 68
            ['ORDERTYPE', 'C', 2, 'AN'],    #pos 83
            ['PURCHASER', 'C', 13, 'AN'],    #pos 86
            ['SUPPLIER', 'C', 13, 'AN'],    #pos 99
            ['DESTINATION', 'C', 13, 'AN'],    #pos 138
            ['INVOICE', 'C', 13, 'AN'],    #pos 151
            ['DELIVERYDATE', 'C', 8, 'AN'],    #pos 164
            ['NODELAFTER', 'C', 8, 'AN'],    #pos 172
			['NODELBEFORE', 'C', 8, 'AN'],    #pos 180
          ],
    'LIN':[
            ['BOTSID','C',3,'A'],    #pos 1
            ['LINE', 'C', 6, 'N'],    #pos 4
            ['ITEM', 'C', 14, 'AN'],    #pos 10
            ['COUNT', 'C', 16.3, 'N'],    #pos 76
            ['DESCRIPTION', 'C', 80, 'AN'],    #pos 92-172
          ],
    }
