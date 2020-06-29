from bots.botsconfig import *

syntax = { 
        'envelope'   :  'edifact',	#for outgoing edifact-messages: this is the envelope to use in merge()
        'charset'   :  'UNOA',	#for outgoing edifact-messages: this is the envelope to use in merge()
        'version'    :  '3',    #for outgong: value to use in UNB
        }

structure=    [
{ID:'UNH',MIN:1,MAX:1,LEVEL:[
{ID:'UCI',MIN:1,MAX:1},
{ID:'UCM',MIN:0,MAX:99999,LEVEL:[
    {ID:'UCS',MIN:0,MAX:999,LEVEL:[
        {ID:'UCD',MIN:0,MAX:99},
        ]},
    ]},            
{ID:'UNT',MIN:1,MAX:1},
]
}
]

recorddefs = {
'UCD': [
    ['BOTSID', 'M', 3, 'AN'],
    ['0085', 'M', 3, 'AN'],
    ['S011', 'M',
        [
        ['S011.0098', 'M', 3, 'N'],
        ['S011.0104', 'C', 3, 'N'],
        ]],
],
'UCI':[
    ['BOTSID','M',3,'A'],
    ['0020', 'M', 14, 'AN'],
    ['S002', 'M',
        [
        ['S002.0004', 'M', 35, 'AN'],
        ['S002.0007', 'C', 4, 'AN'],
        ['S002.0008', 'C', 35, 'AN'],
        ['S002.0042', 'C', 35, 'AN'],
        ]],
    ['S003', 'M',
        [
        ['S003.0010', 'M', 35, 'AN'],
        ['S003.0007', 'C', 4, 'AN'],
        ['S003.0014', 'C', 35, 'AN'],
        ['S003.0046', 'C', 35, 'AN'],
        ]],
    ['0083', 'M', 3, 'AN'],
    ['0085', 'C', 3, 'AN'],
    ['0013', 'C', 3, 'AN'],
    ['S011', 'C',
        [
        ['S011.0098', 'M', 3, 'N'],
        ['S011.0104', 'C', 3, 'N'],
        ]],
    ],
'UCM': [
    ['BOTSID', 'M', 3, 'AN'],
    ['0062', 'M', 14, 'AN'],
    ['S009', 'C', [
        ['S009.0065', 'M', 6, 'AN'],
        ['S009.0052', 'M', 3, 'AN'],
        ['S009.0054', 'M', 3, 'AN'],
        ['S009.0051', 'M', 2, 'AN'],
        ['S009.0057', 'C', 6, 'AN'],
    ]],
    ['0083', 'M', 3, 'AN'],
    ['0085', 'C', 3, 'AN'],
    ['0013', 'C', 3, 'AN'],
    ['S011', 'C',
        [
        ['S011.0098', 'M', 3, 'N'],
        ['S011.0104', 'C', 3, 'N'],
        ]],
],
'UCS': [
    ['BOTSID', 'M', 3, 'AN'],
    ['0096', 'M', 6, 'N'],
    ['0085', 'C', 3, 'AN'],
],
'UNH': [
    ['BOTSID', 'M', 3, 'AN'],
    ['0062', 'M', 14, 'AN'],
    ['S009', 'C', [
        ['S009.0065', 'M', 6, 'AN'],
        ['S009.0052', 'M', 3, 'AN'],
        ['S009.0054', 'M', 3, 'AN'],
        ['S009.0051', 'M', 2, 'AN'],
        ['S009.0057', 'C', 6, 'AN'],
    ]],
    ['0068', 'C', 35, 'AN'],
    ['S010', 'C', [
        ['S010.0070', 'M', 2, 'N'],
        ['S010.0073', 'C', 1, 'A'],
    ]],
],
'UNT': [
    ['BOTSID', 'M', 3, 'AN'],
    ['0074', 'M', 6, 'N'],
    ['0062', 'M', 14, 'AN'],
],
}
