from bots.botsconfig import *
from bots.usersys.grammars.tradacoms.records_9 import recorddefs

syntax = { 
        'checkcharsetout'   :   'ignore',
        }

structure = [
{ID:'MHD',MIN:1,MAX:1,LEVEL:[
    {ID:'TYP',MIN:1,MAX:1},
    {ID:'SDT',MIN:1,MAX:1},
    {ID:'CDT',MIN:1,MAX:1},
    {ID:'DNA',MIN:0,MAX:99999},
    {ID:'FIL',MIN:1,MAX:1},
    {ID:'MTR',MIN:1,MAX:1},
    ]
}]
