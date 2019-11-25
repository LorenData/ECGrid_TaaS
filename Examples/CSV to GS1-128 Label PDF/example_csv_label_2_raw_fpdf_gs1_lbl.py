# mapping-script
import os
import io
import uuid
import bots.transform as transform
import bots.botsglobal as botsglobal
from fpdf import FPDF
import barcode
from barcode.writer import ImageWriter


def main(inn, out):

    # initialize Home Depot FPDF sub class
    pdf = HOMEDEPOTPDF(orientation='P', unit='mm', format=(101.6, 152.4))
    pdf.set_title('Home Depot GS1-128 Label')
    pdf.set_margins(0, 0, 0)

    pdf.set_font(family='courier', style='', size=8)
    pdf.set_auto_page_break(True, 1)

    out.ta_info['frompartner'] = ""
    out.ta_info['topartner'] = ""
    out.ta_info['testindicator'] = "P"
    inn.ta_info['testindicator'] = "P"
    inn.ta_info['botskey'] = "HDGS1-128"
    out.ta_info['botskey'] = "HDGS1-128"

    # process the lines
    for line in inn.getloop({'BOTSID': 'LBL'}):

        # Add New Page
        pdf.add_page()

        # Label Lines
        pdf.addLBL_Lines()

        out.ta_info['frompartner'] = ""
        out.ta_info['topartner'] = ""
        out.ta_info['testindicator'] = "P"
        inn.ta_info['testindicator'] = "P"
        inn.ta_info['botskey'] = "HDGS1-128"
        out.ta_info['botskey'] = "HDGS1-128"

        # From address
        from_name = line.get({'BOTSID': 'LBL', 'FROMNAME': None})
        from_addr = line.get({'BOTSID': 'LBL', 'FROMADDR': None})
        from_addr2 = line.get({'BOTSID': 'LBL', 'FROMADDR2': None})
        from_city = line.get({'BOTSID': 'LBL', 'FROMCITY': None})
        from_state = line.get({'BOTSID': 'LBL', 'FROMSTATE': None})
        from_zip = line.get({'BOTSID': 'LBL', 'FROMZIP': None})

        if from_addr2 is not None:
            pdf.addLBL_From('FROM:', from_name + '\n' + from_addr + '\n' + from_addr2 + '\n' + from_city + ',' + from_state + ' ' + from_zip)
        else:
            pdf.addLBL_From('FROM:', from_name + '\n' + from_addr + '\n' + from_city + ',' + from_state + ' ' + from_zip)

        # To address
        to_number = line.get({'BOTSID': 'LBL', 'TONUMBER': None})
        to_name = line.get({'BOTSID': 'LBL', 'TONAME': None})
        to_addr = line.get({'BOTSID': 'LBL', 'TOADDR': None})
        to_addr2 = line.get({'BOTSID': 'LBL', 'TOADDR2': None})
        to_city = line.get({'BOTSID': 'LBL', 'TOCITY': None})
        to_state = line.get({'BOTSID': 'LBL', 'TOSTATE': None})
        to_zip = line.get({'BOTSID': 'LBL', 'TOZIP': None})

        if to_addr2 is not None:
            pdf.addLBL_To('TO:', 'DFDC: ' + to_number + '\n' + to_name + '\n' + to_addr + '\n' + to_addr2 + '\n' + to_city + ',' + to_state + ' ' + to_zip)
        else:
            pdf.addLBL_To('TO:', 'DFDC: ' + to_number + '\n' + to_name + '\n' + to_addr + '\n' + to_city + ',' + to_state + ' ' + to_zip)

        # Carrier Info
        pdf.addLBL_CarrierHeading("CARRIER:")
        carrier = line.get({'BOTSID': 'LBL', 'CARRIER': None})
        pro_number = line.get({'BOTSID': 'LBL', 'PRONUMBER': None})
        bol = line.get({'BOTSID': 'LBL', 'BOL': None})
        pdf.addLBL_Carrier(carrier, "PRO#: " + pro_number, "BOL#: " + bol)

        # Store Number
        storeNumber = line.get({'BOTSID': 'LBL', 'STORENUMBER': None})
        pdf.addLBL_StoreHeading("STORE #: " + storeNumber)

        # PO Number
        poNumber = line.get({'BOTSID': 'LBL', 'PONUMBER': None})
        pdf.addLBL_PONumberHeading(poNumber)

        # Pallet Info
        palletnumber = line.get({'BOTSID': 'LBL', 'PALLETNUMBER': None})
        totalpallets = line.get({'BOTSID': 'LBL', 'TOTALPALLETS': None})
        pallet_info = palletnumber + " of " + totalpallets
        pdf.addLBL_PalletNo("PALLET NO.:", pallet_info)

        # Cartons
        cartons = line.get({'BOTSID': 'LBL', 'CARTONS': None})
        pdf.addLBL_Cartons("NO. OF CARTONS:", cartons)

        # SSCC-18
        company_prefix = line.get({'BOTSID': 'LBL', 'SSCCCOMPANYPREFIX': None}).zfill(7)
        serial = line.get({'BOTSID': 'LBL', 'SSCCSERIAL': None}).zfill(9)
        gs1128 = '0' + company_prefix + serial
        checkdigit = transform.checkDigitMOD10(gs1128)

        GS128String = "(00) 0 " + company_prefix + " " + serial + " " + checkdigit
        GS128BC = "000" + company_prefix + serial + checkdigit

        pdf.addLBL_SSCC_BC(GS128BC)
        pdf.addLBL_SSCC_BCText(GS128String)

    # Write to Byte String and encode for Text Output.
    out.root = pdf.output(dest='S').encode('latin-1')


class HOMEDEPOTPDF(FPDF):

    def addLBL_Lines(self):
        # Horizontal Lines
        self.line(0, 25.5, 102, 25.5)
        self.line(0, 51, 102, 51)
        self.line(0, 76.5, 102, 76.5)
        self.line(0, 102, 102, 102)

        # Vertical Lines
        self.line(38, 0, 38, 25.5)
        self.line(63.5, 25.5, 63.5, 51)
        self.line(51, 76.5, 51, 102)

    def addLBL_From(self, headingText, addressText):
        self.set_xy(3, 4)
        self.set_font(family='courier', style='', size=8)
        self.cell(w=15, h=3, txt=headingText, border=0, ln=0, align='L', fill=False)

        self.set_xy(4, 7)
        self.set_font(family='courier', style='', size=8)
        self.multi_cell(w=35, h=3, txt=addressText, border=0, align='L', fill=False)

    def addLBL_To(self, headingText, addressText):
        self.set_xy(40, 4)
        self.set_font(family='courier', style='', size=8)
        self.cell(w=15, h=3, txt=headingText, border=0, ln=0, align='L', fill=False)

        self.set_xy(41, 7)
        self.set_font(family='courier', style='', size=8)
        self.multi_cell(w=60, h=3, txt=addressText, border=0, align='L', fill=False)

    def addLBL_CarrierHeading(self, headingText):
        self.set_xy(3, 27.5)
        self.set_font(family='courier', style='', size=10)
        self.cell(w=60, h=3, txt=headingText, border=0, ln=0, align='L', fill=False)

    def addLBL_Carrier(self, carrierText, carrierText2, carrierText3):
        self.set_xy(4, 33)
        self.set_font(family='courier', style='', size=10)
        self.cell(w=60, h=3, txt=carrierText, border=0, ln=0, align='L', fill=False)

        self.set_xy(4, 39)
        self.cell(w=60, h=3, txt=carrierText2, border=0, ln=0, align='L', fill=False)

        self.set_xy(4, 45)
        self.cell(w=60, h=3, txt=carrierText3, border=0, ln=0, align='L', fill=False)

    def addLBL_StoreHeading(self, headingText):
        self.set_xy(65, 35)
        self.set_font(family='courier', style='', size=10)
        self.cell(w=35, h=6, txt=headingText, border=0, ln=0, align='L', fill=False)

    def addLBL_PONumberHeading(self, headingText):
        self.set_xy(32, 60)
        self.set_font(family='courier', style='', size=10)
        self.cell(w=40, h=6, txt=headingText, border=0, ln=0, align='C', fill=False)

    def addLBL_PalletNo(self, headingText, info):
        self.set_xy(3, 79)
        self.set_font(family='courier', style='', size=10)
        self.cell(w=45, h=4, txt=headingText, border=0, ln=0, align='L', fill=False)

        self.set_xy(0, 90)
        self.cell(w=51, h=6, txt=info, border=0, ln=0, align='C', fill=False)

    def addLBL_Cartons(self, headingText, info):
        self.set_xy(53, 79)
        self.set_font(family='courier', style='', size=10)
        self.cell(w=45, h=4, txt=headingText, border=0, ln=0, align='L', fill=False)

        self.set_xy(51, 90)
        self.cell(w=51, h=6, txt=info, border=0, ln=0, align='C', fill=False)

    def addLBL_SSCC_BC(self, barcode128):

        # Set options for Barcode Writer
        bc_options = {
            'format': 'PNG',
            'dpi': 600,
            'module_width': .2,
            'module_height': 15,
            'quiet_zone': 6.5,
            'text_distance': 2,
            'font_size': 8,
            'background': 'white',
            'foreground': 'black',
            'write_text': False,
            'center_text:': True
        }

        # Create the Barcode
        GS1BCClass = barcode.get_barcode_class('gs1_128')
        gs1_128 = GS1BCClass(barcode128, writer=ImageWriter())

        # Save Barcode to File
        tempname = uuid.uuid4().hex
        newfilepath = os.path.join(botsglobal.ini.directories["barcodes"], tempname)
        barcodepath = gs1_128.save(newfilepath, options=bc_options)

        # Load the File into the PDF
        self.image(barcodepath, .5, 105, type='PNG', w=101, h=38)

        # Delete the Barcode File
        os.remove(barcodepath)

    def addLBL_SSCC_BCText(self, barcode128Text):
        self.set_xy(0, 144)
        self.set_font(family='courier', style='', size=10)
        self.cell(w=102, h=4, txt=barcode128Text, border=0, ln=0, align='C', fill=False)
