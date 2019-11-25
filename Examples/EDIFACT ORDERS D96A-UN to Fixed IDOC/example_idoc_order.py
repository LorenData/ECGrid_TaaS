from bots.botsconfig import *

nextmessage = ({'BOTSID':'EDI_DC40'},{'BOTSID':'E2EDK01003'})

structure = [
{ID:'EDI_DC40',MIN:1,MAX:1,
    QUERIES:{
        'frompartner':  {'BOTSID':'EDI_DC40','SNDPRN':None},
        'topartner':    {'BOTSID':'EDI_DC40','RCVPRN':None},
        'testindicator':{'BOTSID':'EDI_DC40','TEST':None},
        'reference':   {'BOTSID':'EDI_DC40','DOCNUM':None},
        },
    LEVEL:[
        {ID:'E2EDK01003',MIN:1,MAX:99999,LEVEL:[
            {ID:'ZFILE_INFO',MIN:0,MAX:9999,LEVEL:[
                {ID:'ZEKKO',MIN:0,MAX:10},
                ]},
            {ID:'E2EDK14',MIN:0,MAX:12},
            {ID:'E2EDK03',MIN:0,MAX:10},
            {ID:'E2EDK04',MIN:0,MAX:10},
            {ID:'E2EDK05',MIN:0,MAX:16},
            {ID:'E2EDKA1002',MIN:0,MAX:8},
            {ID:'E2EDK02',MIN:0,MAX:10},
            {ID:'E2EDK17',MIN:0,MAX:4},
            {ID:'E2EDK18',MIN:0,MAX:3},
            {ID:'E2EDKT1',MIN:0,MAX:99,LEVEL:[
                {ID:'E2EDKT2',MIN:0,MAX:99999999},
                ]},
            {ID:'E2EDP01003',MIN:0,MAX:999999,LEVEL:[
                {ID:'ZEKPO',MIN:0,MAX:10},
                {ID:'E2EDP02',MIN:0,MAX:10},
                {ID:'E2EDP03',MIN:0,MAX:10},
                {ID:'E2EDP04',MIN:0,MAX:10},
                {ID:'E2EDP05',MIN:0,MAX:16},
                {ID:'E2EDP20',MIN:0,MAX:9999},
                {ID:'ZEKET',MIN:0,MAX:9999},
                {ID:'E2EDPA1',MIN:0,MAX:8},
                {ID:'E2EDP19001',MIN:0,MAX:5},
                {ID:'E2EDP17',MIN:0,MAX:5},
                {ID:'E2EDP18',MIN:0,MAX:3},
                {ID:'E2EDPT1',MIN:0,MAX:9999999,LEVEL:[
                    {ID:'E2EDPT2',MIN:0,MAX:99999999},
                    ]},
                {ID:'E2EDS01',MIN:0,MAX:5},
                ]},
            ]},
        ]},
    ]

recorddefs =    {
    'EDI_DC40':[
        ['BOTSID','M',10,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['DOCREL','C',4,'AN'],
        ['STATUS','C',2,'AN'],
        ['DIRECT','C',1,'AN'],
        ['OUTMOD','C',1,'AN'],
        ['EXPRSS','C',1,'AN'],
        ['TEST','C',1,'AN'],
        ['IDOCTYP','C',30,'AN'],
        ['CIMTYP','C',30,'AN'],
        ['MESTYP','C',30,'AN'],
        ['MESCOD','C',3,'AN'],
        ['MESFCT','C',3,'AN'],
        ['STD','C',1,'AN'],
        ['STDVRS','C',6,'AN'],
        ['STDMES','C',6,'AN'],
        ['SNDPOR','C',10,'AN'],
        ['SNDPRT','C',2,'AN'],
        ['SNDPFC','C',2,'AN'],
        ['SNDPRN','C',10,'AN'],
        ['SNDSAD','C',21,'AN'],
        ['SNDLAD','C',70,'AN'],
        ['RCVPOR','C',10,'AN'],
        ['RCVPRT','C',2,'AN'],
        ['RCVPFC','C',2,'AN'],
        ['RCVPRN','C',10,'AN'],
        ['RCVSAD','C',21,'AN'],
        ['RCVLAD','C',70,'AN'],
        ['CREDAT','C',8,'AN'],
        ['CRETIM','C',6,'AN'],
        ['REFINT','C',14,'AN'],
        ['REFGRP','C',14,'AN'],
        ['REFMES','C',14,'AN'],
        ['ARCKEY','C',70,'AN'],
        ['SERIAL','C',20,'AN'],
        ],
    'E2EDK01003':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['ACTION','C',3,'AN'],
        ['KZABS','C',1,'AN'],
        ['CURCY','C',3,'AN'],
        ['HWAER','C',3,'AN'],
        ['WKURS','C',12,'AN'],
        ['ZTERM','C',17,'AN'],
        ['KUNDEUINR','C',20,'AN'],
        ['EIGENUINR','C',20,'AN'],
        ['BSART','C',4,'AN'],
        ['BELNR','C',35,'AN'],
        ['NTGETW','C',18,'AN'],
        ['BRGEW','C',18,'AN'],
        ['GEWEI','C',3,'AN'],
        ['FKART_RL','C',4,'AN'],
        ['ABLAD','C',25,'AN'],
        ['BSTZD','C',4,'AN'],
        ['VSART','C',2,'AN'],
        ['VSART_BEZ','C',20,'AN'],
        ],
    'ZFILE_INFO':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['ZIFF_FILE_ID','C',21,'AN'],
        ['ORDER_SEQNO','C',4,'AN'],
        ],
    'ZEKKO':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['INCOTERMS1','C',3,'AN'],
        ['INCOTERMS2','C',28,'AN'],
        ],
    'E2EDK14':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['QUALF','C',3,'AN'],
        ['ORGID','C',35,'AN'],
        ],
    'E2EDK03':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['IDDAT','C',3,'AN'],
        ['DATUM','C',8,'AN'],
        ['UZEIT','C',6,'AN'],
        ],
    'E2EDK04':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['MWSKZ','C',7,'AN'],
        ['MSATZ','C',17,'AN'],
        ['MWSBT','C',18,'AN'],
        ['TXJCD','C',15,'AN'],
        ],
    'E2EDK05':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['ALCKZ','C',3,'AN'],
        ['KSCHL','C',4,'AN'],
        ['KOTXT','C',80,'AN'],
        ['BETRG','C',18,'AN'],
        ['KPERC','C',8,'AN'],
        ['KRATE','C',15,'AN'],
        ['UPRBS','C',9,'AN'],
        ['MEAUN','C',3,'AN'],
        ['KOBTR','C',18,'AN'],
        ['MWSKZ','C',7,'AN'],
        ['MSATZ','C',17,'AN'],
        ],
    'E2EDKA1002':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['PARVW','C',3,'AN'],
        ['PARTN','C',17,'AN'],
        ['LIFNR','C',17,'AN'],
        ['NAME1','C',35,'AN'],
        ['NAME2','C',35,'AN'],
        ['NAME3','C',35,'AN'],
        ['NAME4','C',35,'AN'],
        ['STRAS','C',35,'AN'],
        ['STRS2','C',35,'AN'],
        ['PFACH','C',35,'AN'],
        ['ORT01','C',35,'AN'],
        ['COUNC','C',9,'AN'],
        ['PSTLZ','C',9,'AN'],
        ['PSTL2','C',9,'AN'],
        ['LAND1','C',3,'AN'],
        ['ABLAD','C',35,'AN'],
        ['PERNR','C',30,'AN'],
        ['PARNR','C',30,'AN'],
        ['TELF1','C',25,'AN'],
        ['TELF2','C',25,'AN'],
        ['TELBX','C',25,'AN'],
        ['TELFX','C',25,'AN'],
        ['TELTX','C',25,'AN'],
        ['TELX1','C',25,'AN'],
        ['SPRAS','C',1,'AN'],
        ['ANRED','C',15,'AN'],
        ['ORT02','C',35,'AN'],
        ['HAUSN','C',6,'AN'],
        ['STOCK','C',6,'AN'],
        ['REGIO','C',3,'AN'],
        ['PARGE','C',1,'AN'],
        ['ISOAL','C',2,'AN'],
        ['ISONU','C',2,'AN'],
        ['FCODE','C',20,'AN'],
        ['IHREZ','C',30,'AN'],
        ['BNAME','C',35,'AN'],
        ['PAORG','C',30,'AN'],
        ['ORGTX','C',35,'AN'],
        ['PAGRU','C',30,'AN'],
        ['KNREF','C',30,'AN'],
        ['ILNNR','C',70,'AN'],
        ['PFORT','C',35,'AN'],
        ['SPRA','C',2,'AN'],
        ['FILLER_1','C',63,'AN'],
        ['FILLER_2','C',200,'AN'],
        ['FILLER_3','C',200,'AN'],
        ],
    'E2EDK02':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['QUALF','C',3,'AN'],
        ['BELNR','C',35,'AN'],
        ['POSNR','C',6,'AN'],
        ['DATUM','C',8,'AN'],
        ['UZEIT','C',6,'AN'],
        ],
    'E2EDK17':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['QUALF','C',3,'AN'],
        ['LKOND','C',3,'AN'],
        ['LKTEXT','C',70,'AN'],
        ],
    'E2EDK18':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['QUALF','C',3,'AN'],
        ['TAGE','C',8,'AN'],
        ['PRZNT','C',8,'AN'],
        ['ZTERM_TXT','C',70,'AN'],
        ],
    'E2EDKT1':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['TDID','C',4,'AN'],
        ['TSSPRAS','C',3,'AN'],
        ],
    'E2EDKT2':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['TDLINE','C',70,'AN'],
        ],
    'E2EDP01003':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['POSEX','C',6,'AN'],
        ['ACTION','C',3,'AN'],
        ['PSTYP','C',1,'AN'],
        ['KZABS','C',1,'AN'],
        ['MENGE','C',15,'AN'],
        ['MENEE','C',3,'AN'],
        ['BMNG2','C',15,'AN'],
        ['PMENE','C',3,'AN'],
        ['ABFTZ','C',7,'AN'],
        ['VPREI','C',15,'AN'],
        ['PEINH','C',9,'AN'],
        ['NETWR','C',18,'AN'],
        ['ANETW','C',18,'AN'],
        ['SKFBP','C',18,'AN'],
        ['NTGEW','C',18,'AN'],
        ['GEWEI','C',3,'AN'],
        ['EINKZ','C',1,'AN'],
        ['CURCY','C',3,'AN'],
        ['PREIS','C',18,'AN'],
        ['MATKL','C',9,'AN'],
        ['UEPOS','C',6,'AN'],
        ['GRKOR','C',3,'AN'],
        ['EVERS','C',7,'AN'],
        ['BPUMN','C',6,'AN'],
        ['BPUMZ','C',6,'AN'],
        ],
    'ZEKPO':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['SEIZOENIND','C',4,'AN'],
        ['SEIZOENJAAR','C',4,'AN'],
        ['ORDERREDEN','C',3,'AN'],
        ['ALLOCATIE','C',10,'AN'],
        ['LAATSTEGR','C',8,'AN'],
        ['REMSHELF','C',6,'AN'],
        ['VERWIJDER','C',1,'AN'],
        ['RETURN','C',1,'AN'],
        ['TRACKING','C',10,'AN'],
        ['UNDERDELTOL','C',5,'AN'],
        ['OVERDELTOL','C',5,'AN'],
        ['UNLIMOVER','C',1,'AN'],
        ['QUALITY','C',1,'AN'],
        ['DELCOMP','C',1,'AN'],
        ['STOR_LOCATION','C',4,'AN'],
        ['PROM_NR','C',10,'AN'],
        ['INCO1','C',3,'AN'],
        ['INCO2','C',28,'AN'],
        ['ALL_AANTAL','C',5,'AN'],
        ],
    'E2EDP02':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['QUALF','C',3,'AN'],
        ['BELNR','C',35,'AN'],
        ['ZEILE','C',6,'AN'],
        ['DATUM','C',8,'AN'],
        ['UZEIT','C',6,'AN'],
        ],
    'E2EDP03':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['IDDAT','C',3,'AN'],
        ['DATUM','C',8,'AN'],
        ['UZEIT','C',6,'AN'],
        ],
    'E2EDP04':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['MWSKZ','C',7,'AN'],
        ['MSATZ','C',17,'AN'],
        ['MWSBT','C',18,'AN'],
        ['TXJCD','C',15,'AN'],
        ],
    'E2EDP05':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['ALCKZ','C',3,'AN'],
        ['KSCHL','C',4,'AN'],
        ['KOTXT','C',80,'AN'],
        ['BETRG','C',18,'AN'],
        ['KPERC','C',8,'AN'],
        ['KRATE','C',15,'AN'],
        ['UPRBS','C',9,'AN'],
        ['MEAUN','C',3,'AN'],
        ['KOBTR','C',18,'AN'],
        ['MENGE','C',15,'AN'],
        ['PREIS','C',15,'AN'],
        ['MWSKZ','C',7,'AN'],
        ['MSATZ','C',17,'AN'],
        ],
    'E2EDP20':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['WMENG','C',15,'AN'],
        ['AMENG','C',15,'AN'],
        ['EDATU','C',8,'AN'],
        ['EZEIT','C',6,'AN'],
        ['EDATU_OLD','C',8,'AN'],
        ['EZEIT_OLD','C',6,'AN'],
        ],
    'ZEKET':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['DEELLEVNR','C',4,'AN'],
        ['SAMPLE','C',15,'AN'],
        ['STATDEDATE','C',8,'AN'],
        ],
    'E2EDPA1':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['PARVW','C',3,'AN'],
        ['PARTN','C',17,'AN'],
        ['LIFNR','C',17,'AN'],
        ['NAME1','C',35,'AN'],
        ['NAME2','C',35,'AN'],
        ['NAME3','C',35,'AN'],
        ['NAME4','C',35,'AN'],
        ['STRAS','C',35,'AN'],
        ['STRS2','C',35,'AN'],
        ['PFACH','C',35,'AN'],
        ['ORT01','C',35,'AN'],
        ['COUNC','C',9,'AN'],
        ['PSTLZ','C',9,'AN'],
        ['PSTL2','C',9,'AN'],
        ['LAND1','C',3,'AN'],
        ['ABLAD','C',35,'AN'],
        ['PERNR','C',30,'AN'],
        ['PARNR','C',30,'AN'],
        ['TELF1','C',25,'AN'],
        ['TELF2','C',25,'AN'],
        ['TELBX','C',25,'AN'],
        ['TELFX','C',25,'AN'],
        ['TELTX','C',25,'AN'],
        ['TELX1','C',25,'AN'],
        ['SPRAS','C',1,'AN'],
        ['ANRED','C',15,'AN'],
        ['ORT02','C',35,'AN'],
        ['HAUSN','C',6,'AN'],
        ['STOCK','C',6,'AN'],
        ['REGIO','C',3,'AN'],
        ['PARGE','C',1,'AN'],
        ['ISOAL','C',2,'AN'],
        ['ISONU','C',2,'AN'],
        ['FCODE','C',20,'AN'],
        ['IHREZ','C',30,'AN'],
        ['BNAME','C',35,'AN'],
        ['PAORG','C',30,'AN'],
        ['ORGTX','C',35,'AN'],
        ['PAGRU','C',30,'AN'],
        ],
    'E2EDP19001':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['QUALF','C',3,'AN'],
        ['IDTNR','C',35,'AN'],
        ['KTEXT','C',70,'AN'],
        ],
    'E2EDP17':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['QUALF','C',3,'AN'],
        ['LKOND','C',3,'AN'],
        ['LKTEXT','C',70,'AN'],
        ],
    'E2EDP18':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['QUALF','C',3,'AN'],
        ['TAGE','C',8,'AN'],
        ['PRZNT','C',8,'AN'],
        ],
    'E2EDPT1':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['TDID','C',4,'AN'],
        ['TSSPRAS','C',3,'AN'],
        ],
    'E2EDPT2':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['TDLINE','C',70,'AN'],
        ],
    'E2EDS01':[
        ['BOTSID','M',10,'AN'],
        ['WHATEVER','C',20,'AN'],
        ['MANDT','C',3,'N'],
        ['DOCNUM','C',16,'N'],
        ['SEGNUM','C',6,'N'],
        ['PSGNUM','C',6,'N'],
        ['HLEVEL','C',2,'N'],
        ['SUMID','C',3,'AN'],
        ['SUMME','C',18,'AN'],
        ],
    }
