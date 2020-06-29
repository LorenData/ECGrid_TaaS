from bots.botsconfig import *

nextmessage = ({'BOTSID': 'ISA'}, {'BOTSID': 'GS'}, {'BOTSID': 'ST'})

structure = [
    {ID:'ISA',MIN:0,MAX:99999,    
        QUERIES: {
            'ISA01': {'BOTSID': 'ISA', 'ISA01': None},
            'ISA02': {'BOTSID': 'ISA', 'ISA02': None},
            'ISA03': {'BOTSID': 'ISA', 'ISA03': None},
            'ISA04': {'BOTSID': 'ISA', 'ISA04': None},
            'ISA05': {'BOTSID': 'ISA', 'ISA05': None},
            'frompartner':  {'BOTSID':'ISA','ISA06':None},
            'ISA07': {'BOTSID': 'ISA', 'ISA07': None},
            'topartner': {'BOTSID': 'ISA', 'ISA08': None},
            'ISA09': {'BOTSID': 'ISA', 'ISA09': None},
            'ISA10': {'BOTSID': 'ISA', 'ISA10': None},
            'ISA11': {'BOTSID': 'ISA', 'ISA11': None},
            'ISA12': {'BOTSID': 'ISA', 'ISA12': None},
            'ISA13': {'BOTSID': 'ISA', 'ISA13': None},
            'ISA14': {'BOTSID': 'ISA', 'ISA14': None},
            'ISA15': {'BOTSID': 'ISA', 'ISA15': None},
            'testindicator': {'BOTSID': 'ISA', 'ISA15': None},
            },
        LEVEL:
            [
            {ID:'TA1',MIN:0,MAX:99999},
            {ID:'GS',MIN:0,MAX:99999,
                QUERIES: {
                    'functionalgroup': {'BOTSID': 'GS', 'GS01': None},
                    'GS06':{'BOTSID':'GS','GS06':None},
                    'GS07': {'BOTSID': 'GS', 'GS07': None},
                    'GS08':{'BOTSID':'GS','GS08':None},
                    'version':{'BOTSID':'GS','GS08':None},
                    },
                LEVEL:
                    [
                    {ID:'ST',MIN:0,MAX:99999,
                        QUERIES: {
                            'ST01':   {'BOTSID':'ST','ST01':None},
                            'reference':   {'BOTSID':'ST','ST02':None},
                            },
                        SUBTRANSLATION: [
                            {'BOTSID': 'ST', 'ST01': None}
                        ] 
                        },
                    {ID:'GE',MIN:1,MAX:1},
                    ]
                },
            {ID:'IEA',MIN:1,MAX:1}
            ]
        }
    ]


recorddefs =    {
    'ISA':[
        ['BOTSID','M',3,'AN'],
        ['ISA01','M',(2,2),'AN'],
        ['ISA02','C',(10,10),'AN'],
        ['ISA03','M',(2,2),'AN'],
        ['ISA04','C',(10,10),'AN'],
        ['ISA05','M',(2,2),'AN'],
        ['ISA06','M',(15,15),'AN'],
        ['ISA07','M',(2,2),'AN'],
        ['ISA08','M',(15,15),'AN'],
        ['ISA09','M',(6,6),'DT'],
        ['ISA10','M',(4,4),'TM'],
        ['ISA11','C',(1,1),'AN'],
        ['ISA12','M',(5,5),'AN'],
        ['ISA13','M',(9,9),'N'],
        ['ISA14','M',(1,1),'AN'],
        ['ISA15','M',(1,1),'AN'],
        #~ ['ISA16','M',(1,1),'AN'],
        ['ISA16', 'C',  
            [
            ['ISA16.0001', 'C', 1, 'AN'],    
            ['ISA16.0002', 'C', 1, 'AN'],    
            ]],
        ],
    'GS':[
        ['BOTSID','M',3,'AN'],
        ['GS01','M',2,'AN'],
        ['GS02','M',15,'AN'],
        ['GS03','M',15,'AN'],
        ['GS04','M',(6,8),'DT'],
        ['GS05','M',(4,8),'TM'],
        ['GS06','M',9,'N'],
        ['GS07','M',2,'AN'],
        ['GS08','M',12,'AN'],
        ],
    'ST':[
        ['BOTSID','M',3,'AN'],
        ['ST01','M',3,'AN'],
        ['ST02','M',(4,9),'AN'],
        ['ST03','C',35,'AN'],
        ],
    'SE':[
        ['BOTSID','M',3,'AN'],
        ['SE01', 'M', 10, 'N'],    
        ['SE02', 'M', (4,9), 'AN'],    
        ],
    'GE':[
        ['BOTSID','M',3,'AN'],
        ['GE01', 'M', 6, 'N'],    
        ['GE02', 'M', 9, 'N'],    
        ],
    'IEA':[
        ['BOTSID','M',3,'AN'],
        ['IEA01', 'M', 5, 'N'],    
        ['IEA02', 'M', (9,9), 'N'],    
        ],
     'TA1': [
        ['BOTSID', 'M', 3,'AN'],
        ['TA101', 'M', (9,9),'N0'],
        ['TA102', 'M', (6,8),'DT'],
        ['TA103', 'M', (4,4),'TM'],
        ['TA104', 'M', 1,'ID'],
        ['TA105', 'M', (3,3),'ID'],
        ],
   }
