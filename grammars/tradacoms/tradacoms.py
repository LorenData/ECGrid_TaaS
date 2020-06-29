from bots.botsconfig import *

syntax = { 
        'checkcharsetout'   :   'ignore',
        }

nextmessage = ({'BOTSID':'STX'},)

structure = [
    {ID:'STX',MIN:0,MAX:99999,
        QUERIES:{
            'frompartner':  {'BOTSID':'STX','FROM.01':None},
            'topartner':    {'BOTSID':'STX','UNTO.01':None},
            },
        LEVEL:
            [
            {ID:'MHD',MIN:0,MAX:99999,
                SUBTRANSLATION:[
                    {'BOTSID':'MHD','TYPE.01':None},
                    {'BOTSID':'MHD','TYPE.02':None},
                    ]},
            {ID:'END',MIN:1,MAX:1}
            ]
        }
    ]

recorddefs = {
#envelope segments
'STX':  [
	['BOTSID','M',3,'X'],
	['STDS', 'M',
		[
		['STDS1', 'M', 4, 'X'],
		['STDS2', 'M', 1, '9'],
		]],
	['FROM', 'M',
		[
		['FROM.01', 'C', 14, 'X'],
		['FROM.02', 'C', 35, 'X'],
		]],
	['UNTO', 'M',
		[
		['UNTO.01', 'C', 14, 'X'],
		['UNTO.02', 'C', 35, 'X'],
		]],
	['TRDT', 'M',
		[
		['TRDT.01', 'M', (6,6), 'X'],
		['TRDT.02', 'C', (6,6), 'X'],
		]],
	['SNRF', 'M', 14, 'X'],
	['RCRF', 'C', 14, 'X'],
	['APRF', 'C', 14, 'X'],
	['PRCD', 'C', 1, 'X'],
	],
'MHD':  [
	['BOTSID','M',3,'X'],
	['MSRF', 'M', 12, 'X'],
	['TYPE', 'M',
		[
		['TYPE.01', 'M', 6, 'X'],
		['TYPE.02', 'M', 1, 'X'],
		]],
	],
'MTR':  [
	['BOTSID','M',3,'X'],
	['NOSG', 'M', 10, '9'],
	],
'END':  [
	['BOTSID','M',3,'X'],
	['NMST', 'M', 5, '9'],
	],
}
