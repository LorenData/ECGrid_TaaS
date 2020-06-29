from bots.botsconfig import *
from bots.usersys.grammars.tradacoms.records_9 import recorddefs

syntax = { 
        'checkcharsetout'   :   'ignore',
        }

structure = [
{ID:'MHD',MIN:1,MAX:1,LEVEL:[
    {ID:'OFT',MIN:1,MAX:1},
    {ID:'MTR',MIN:1,MAX:1},
    ]
}]
