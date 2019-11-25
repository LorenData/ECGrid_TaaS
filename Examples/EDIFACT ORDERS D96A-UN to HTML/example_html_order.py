from bots.botsconfig import *

syntax = { 
        'charset': 'utf-8',
        'template': 'example_htmltemplate_order.html',  # template to use
        'envelope-template': 'example_htmltemplate_orders_envelope.html',  # template to use
        'merge': True,
        'contenttype': 'text/html',
       }


structure = [
    {ID: 'HEA', MIN: 1, MAX: 10000, LEVEL: [
        {ID: 'LIN', MIN: 0, MAX: 10000},
        ]},
    ]

recorddefs = {
    'HEA': [
            ['BOTSID', 'C', 3, 'A'],
            ['VERSION', 'C', 20, 'AN'],          
            ['SENDER', 'C', 13, 'AN'],         
            ['RECEIVER', 'C', 13, 'AN'],         
            ['TEST', 'C', 1, 'AN'],         
            ['ORDERNUMBER', 'C', 17, 'AN'],         
            ['ORDERDATE', 'C', 12, 'AN'],          
            ['INDICATIONRECEPTIONCONFIRMATION', 'C', 3, 'AN'],   
            ['ORDERTYPE', 'C', 3, 'AN'],          
            ['CUSTOMER', 'C', 13, 'AN'],         
            ['SUPPLIER', 'C', 13, 'AN'],         
            ['DELIVERYADDR', 'C', 13, 'AN'],         
            ['FROMADDR', 'C', 13, 'AN'],         
            ['FINALDEST', 'C', 13, 'AN'],         
            ['INVOICE', 'C', 13, 'AN'],         
            ['DELIVERYDATE', 'C', 12, 'AN'],          
            ['EARLIESTDELIVERYDATE', 'C', 12, 'AN'],          
            ['LASTDELIVERYDATE', 'C', 12, 'AN'],          
            ['IMPROVISED', 'C', 3, 'AN'],          
            ['DUTYFREE', 'C', 3, 'AN'],          
            ['ZEROORDER', 'C', 3, 'AN'],          
            ['BACKHAULING', 'C', 3, 'AN'],          
            ['URGENTORDER', 'C', 3, 'AN'],          
            ['SHOPINSTALLATION', 'C', 3, 'AN'],          
            ['WINDOWORDERNUMBER', 'C', 17, 'AN'],         
            ['ACTIONNUMBER', 'C', 17, 'AN'],         
          ],
    'LIN': [
            ['BOTSID', 'C', 3, 'A'],
            ['LINE', 'C', 6, 'N'],         
            ['ITEM', 'C', 14, 'AN'],         
            ['PROMOCODE', 'C', 17, 'AN'],        
            ['DESCRIPTION', 'C', 35, 'AN'],         
            ['QUANTITY', 'C', 16.3, 'N'],      
          ],
    }
     
