# mapping-script
import bots.transform as transform  # import div bots helper functions
from decimal import Decimal
from datetime import datetime

def get_item_number_by_qual(node, qualifier, start=6, end=25):
    ''' helper function to get to get item_number part_number by qualifier from line segment (PO1, etc) .'''

    tag = node.record['BOTSID']
    list_searchable_elements = [('%s%02d' % (tag, i), '%s%02d' % (tag, i+1)) for i in range(start, end, 2)]

    for qualifier_element, id_element in list_searchable_elements:
        result = node.get({'BOTSID': tag, qualifier_element: qualifier, id_element: None})
        if result:
            return result
       
    return None

# This mapping script maps an incoming x12 004010 850 message to a JSON message.
# Bots calls the 'main' function in this mapping script
# inn: the object for the incoming message; via get() and getloop() the content of the message can be accessed.
# out: the object for the outgoing message; via put() and putloop() content is written for this message.
def main(inn, out):
    
    # Set Constants
    D = 'urn:oasis:names:specification:ubl:schema:xsd:Order-2'
    S = 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2'
    B = 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'
    E = 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2'
    UBLVersionID = "2.1"
    CustomizationID = "LDC"
    ProfileID_Content = "Basic-v1.0"
    ProfileID_Agency = "LDC"
    ProfileID_Identifier = "Profile"
    ProfileExecutionID = "Basic-Order"
    now = datetime.utcnow()

    out.put({'BOTSID': 'ROOT', '_D': D})
    out.put({'BOTSID': 'ROOT', '_S': S})
    out.put({'BOTSID': 'ROOT', '_B': B})
    out.put({'BOTSID': 'ROOT', '_E': E})

    out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'UBLVersionID', 'IdentifierContent': UBLVersionID})
    out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'CustomizationID', 'IdentifierContent': CustomizationID})
    out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'ProfileID', 'IdentifierContent': ProfileID_Content})
    out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'ProfileID', 'IdentificationSchemeAgencyIdentifier': ProfileID_Agency})
    out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'ProfileID', 'IdentificationSchemeIdentifier': ProfileID_Identifier})
    out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'ProfileExecutionID', 'IdentifierContent': ProfileExecutionID})

    UBLExtensionLoop1 = out.putloop({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'UBLExtensions'}, {'BOTSID': 'UBLExtension'})
    UBLExtensionLoop2 = out.putloop({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'UBLExtensions'}, {'BOTSID': 'UBLExtension'})

    UBLExtensionLoop1.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'Name', 'TextContent': "Loren Data Transport"})
    UBLExtensionLoop1.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionReason', 'TextContent': "Aggregate extension component containing information for the Loren Data transport values."})
    UBLExtensionLoop1.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'LorenDataTransport'}, {'BOTSID': 'ParcelID', 'IdentifierContent': ""})
    UBLExtensionLoop1.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'LorenDataTransport'}, {'BOTSID': 'NetworkIDFrom', 'IdentifierContent': ""})
    UBLExtensionLoop1.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'LorenDataTransport'}, {'BOTSID': 'NetworkIDFrom', 'IdentificationSchemeNameText': ""})
    UBLExtensionLoop1.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'LorenDataTransport'}, {'BOTSID': 'NetworkIDTo', 'IdentifierContent': ""})
    UBLExtensionLoop1.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'LorenDataTransport'}, {'BOTSID': 'NetworkIDTo', 'IdentificationSchemeNameText': ""})
    UBLExtensionLoop1.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'LorenDataTransport'}, {'BOTSID': 'MailboxIDFrom', 'IdentifierContent': ""})
    UBLExtensionLoop1.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'LorenDataTransport'}, {'BOTSID': 'MailboxIDFrom', 'IdentificationSchemeNameText': ""})
    UBLExtensionLoop1.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'LorenDataTransport'}, {'BOTSID': 'MailboxIDTo', 'IdentifierContent': ""})
    UBLExtensionLoop1.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'LorenDataTransport'}, {'BOTSID': 'MailboxIDTo', 'IdentificationSchemeNameText': ""})
    UBLExtensionLoop1.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'LorenDataTransport'}, {'BOTSID': 'ECGridIDFrom', 'IdentifierContent': ""})
    UBLExtensionLoop1.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'LorenDataTransport'}, {'BOTSID': 'ECGridIDFrom', 'IdentificationSchemeNameText': ""})
    UBLExtensionLoop1.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'LorenDataTransport'}, {'BOTSID': 'ECGridIDTo', 'IdentifierContent': ""})
    UBLExtensionLoop1.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'LorenDataTransport'}, {'BOTSID': 'ECGridIDTo', 'IdentificationSchemeNameText': ""})
    UBLExtensionLoop1.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'LorenDataTransport'}, {'BOTSID': 'ElectronicMailFrom', 'TextContent': ""})
    UBLExtensionLoop1.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'LorenDataTransport'}, {'BOTSID': 'ElectronicMailTo', 'TextContent': ""})

    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'Name', 'TextContent': "Document Envelope"})
    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionReason', 'TextContent': "Aggregate extention component containing information for the document envelope used for translation."})
    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'ID', 'IdentifierContent': inn.ta_info['ISA13']})
    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'ID', 'IdentificationSchemeNameText': "ISA"})
    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'CopyIndicator', 'IdentifierContent': inn.ta_info['ISA15']})
    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'UUID', 'IdentifierContent': ""})
    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'SenderParty'}, {'BOTSID': 'PartyIdentification'}, {'BOTSID': 'ID', 'IdentifierContent': inn.ta_info['frompartner']})
    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'SenderParty'}, {'BOTSID': 'PartyIdentification'}, {'BOTSID': 'ID', 'IdentificationSchemeNameText': inn.ta_info['ISA05']})
    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'ReceiverParty'}, {'BOTSID': 'PartyIdentification'}, {'BOTSID': 'ID', 'IdentifierContent': inn.ta_info['topartner']})
    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'ReceiverParty'}, {'BOTSID': 'PartyIdentification'}, {'BOTSID': 'ID', 'IdentificationSchemeNameText': inn.ta_info['ISA07']})
    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'IssueDate', 'DateContent': now.strftime('%Y') + transform.datemask(inn.ta_info['ISA09'], "YYmmDD", "-mm-DD")})
    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'IssueTime', 'TimeContent': transform.datemask(inn.ta_info['ISA10'], "0000", "00:00")})
    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'SpecificationID', 'IdentifierContent': inn.ta_info['GS06']})
    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'SpecificationID', 'IdentificationSchemeNameText': "GS"})
    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'AgencyID', 'IdentifierContent': inn.ta_info['GS07']})
    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'VersionID', 'IdentifierContent': inn.ta_info['version']})
    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'DocumentType', 'TextContent': inn.ta_info['ST01']})
    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'SequenceNumberID', 'IdentifierContent': inn.ta_info['reference']})
    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'SequenceNumberID', 'IdentificationSchemeNameText': "ST"})
    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'Status'}, {'BOTSID': 'TextConent', 'TextContent': "New"})
    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'Status'}, {'BOTSID': 'ReferenceDate', 'DateContent': now.strftime('%Y-%m-%d')})
    UBLExtensionLoop2.put({'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'Status'}, {'BOTSID': 'ReferenceTime', 'TimeContent': now.strftime('%H:%M:%S')})

    # BEG Segment
    purpose_code = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG01': None})
    purpose_code_text = transform.ccode('X12_ELEM_353_TO_TEXT', purpose_code)
    ordertype_code = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG02': None})
    ordertype_code_text = transform.ccode('X12_ELEM_92_TO_TEXT', ordertype_code)

    order_number = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG03': None})
    out.ta_info['botskey'] = order_number
    order_date = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG05': None})
    contract_number = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG06': None})

    out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'PurposeCode', 'CodeContent': purpose_code})
    out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'PurposeCode', 'CodeNameText': purpose_code_text})
    out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'OrderTypeCode', 'CodeContent': ordertype_code})
    out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'OrderTypeCode', 'CodeNameText': ordertype_code_text})
    out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'ID', 'IdentifierContent': order_number})
    out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'IssueDate', 'DateContent': transform.datemask(order_date, 'YYYYmmDD', 'mm/DD/YYYY')})
    out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'Contract'}, {'BOTSID': 'ID', 'IdentifierContent': contract_number})

    # REF Segment
    EstimatedDeliveryDateQual = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'DTM', 'DTM01': None})
    EstimatedDeliveryDate = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'DTM', 'DTM01': '017', 'DTM02': None})

    if EstimatedDeliveryDateQual != '':
        out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'RequestedDeliveryPeriod'}, {'BOTSID': 'StartDate', 'DateContent': transform.datemask(EstimatedDeliveryDate, 'YYYYmmDD', 'mm/DD/YYYY')})
        out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'RequestedDeliveryPeriod'}, {'BOTSID': 'DescriptionCode', 'CodeContent': '017'})
        out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'RequestedDeliveryPeriod'}, {'BOTSID': 'DescriptionCode', 'CodeNameText': 'Estimated Delivery Date'})

    # TD5 Segment
    SCAC = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'TD5', 'TD502': '2', 'TD503': None})
    CarrierName = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'TD5', 'TD505': None})

    out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'CarrierParty'}, {'BOTSID': 'PartyIdentification'}, {'BOTSID': 'ID', 'IdentifierContent': SCAC})
    out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'CarrierParty'}, {'BOTSID': 'PartyName'}, {'BOTSID': 'Name', 'TextContent': CarrierName})

    # N1 Loops
    for party in inn.getloop({'BOTSID': 'ST'}, {'BOTSID': 'N1'}):
        PartyQual = party.get({'BOTSID': 'N1', 'N101': None})
        PartyName = party.get({'BOTSID': 'N1', 'N102': None})
        PartyAgency = party.get({'BOTSID': 'N1', 'N103': None})
        PartyNumber = party.get({'BOTSID': 'N1', 'N104': None})

        PartyAddress1 = party.get({'BOTSID': 'N1'}, {'BOTSID': 'N3', 'N301': None})
        PartyAddress2 = party.get({'BOTSID': 'N1'}, {'BOTSID': 'N3', 'N302': None})

        PartyCity = party.get({'BOTSID': 'N1'}, {'BOTSID': 'N4', 'N401': None})
        PartyCountrySubentity = party.get({'BOTSID': 'N1'}, {'BOTSID': 'N4', 'N402': None})
        PartyPostal = party.get({'BOTSID': 'N1'}, {'BOTSID': 'N4', 'N403': None})
        PartyCountry = party.get({'BOTSID': 'N1'}, {'BOTSID': 'N4', 'N404': None})

        if PartyQual == 'BT':
            out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'BuyerCustomerParty'}, {'BOTSID': 'Party'}, {'BOTSID': 'PartyIdentification', 'IdentifierContent': PartyNumber})
            out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'BuyerCustomerParty'}, {'BOTSID': 'Party'}, {'BOTSID': 'PartyIdentification', 'IdentificationSchemeIdentifier': PartyQual})
            out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'BuyerCustomerParty'}, {'BOTSID': 'Party'}, {'BOTSID': 'PartyIdentification', 'IdentificationSchemeAgencyIdentifier': PartyAgency})

            out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'BuyerCustomerParty'}, {'BOTSID': 'Party'}, {'BOTSID': 'PartyName'}, {'BOTSID': 'Name', 'TextContent': PartyName})

            out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'BuyerCustomerParty'}, {'BOTSID': 'Party'}, {'BOTSID': 'PostalAddress'}, {'BOTSID': 'StreetName', 'TextContent': PartyAddress1})
            out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'BuyerCustomerParty'}, {'BOTSID': 'Party'}, {'BOTSID': 'PostalAddress'}, {'BOTSID': 'AdditionalStreetName', 'TextContent': PartyAddress2})
            out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'BuyerCustomerParty'}, {'BOTSID': 'Party'}, {'BOTSID': 'PostalAddress'}, {'BOTSID': 'CityName', 'TextContent': PartyCity})
            out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'BuyerCustomerParty'}, {'BOTSID': 'Party'}, {'BOTSID': 'PostalAddress'}, {'BOTSID': 'PostalZone', 'TextContent': PartyPostal})
            out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'BuyerCustomerParty'}, {'BOTSID': 'Party'}, {'BOTSID': 'PostalAddress'}, {'BOTSID': 'CountrySubentity', 'TextContent': PartyCountrySubentity})
            out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'BuyerCustomerParty'}, {'BOTSID': 'Party'}, {'BOTSID': 'PostalAddress'}, {'BOTSID': 'Country'}, {'BOTSID': 'IdentificationCode', 'CodeContent': PartyCountry[:-1]})

        elif PartyQual == 'ST':
            out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'DeliveryAddress'}, {'BOTSID': 'ID', 'IdentifierContent': PartyNumber})
            out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'DeliveryAddress'}, {'BOTSID': 'ID', 'IdentificationSchemeIdentifier': PartyQual})
            out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'DeliveryAddress'}, {'BOTSID': 'ID', 'IdentificationSchemeAgencyIdentifier': PartyAgency})

            out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'DeliveryAddress'}, {'BOTSID': 'BuildingName', 'TextContent': PartyName})

            out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'DeliveryAddress'}, {'BOTSID': 'StreetName', 'TextContent': PartyAddress1})
            out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'DeliveryAddress'}, {'BOTSID': 'AdditionalStreetName', 'TextContent': PartyAddress2})
            out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'DeliveryAddress'}, {'BOTSID': 'CityName', 'TextContent': PartyCity})
            out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'DeliveryAddress'}, {'BOTSID': 'PostalZone', 'TextContent': PartyPostal})
            out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'DeliveryAddress'}, {'BOTSID': 'CountrySubentity', 'TextContent': PartyCountrySubentity})
            out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'DeliveryAddress'}, {'BOTSID': 'Country'}, {'BOTSID': 'IdentificationCode', 'CodeContent': PartyCountry[:-1]})

    # PO1 Loops
    for po1 in inn.getloop({'BOTSID': 'ST'}, {'BOTSID': 'PO1'}):

        # Out Object Array
        orderLineOut = out.putloop({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'OrderLine'})

        # Get Values
        LineNumber = po1.get({'BOTSID': 'PO1', 'PO101': None})

        # Get UOM, if empty use 'EA'
        X12_UOM = transform.useoneof(po1.get({'BOTSID': 'PO1', 'PO103': None}), 'EA')
        ISO_UOM = transform.ccode('X12_ELEM_355_TO_ISO_UOM', X12_UOM)
        QuantityOrdered = po1.get({'BOTSID': 'PO1', 'PO102': None})

        X12_PriceCode = transform.useoneof(po1.get({'BOTSID': 'PO1', 'PO105': None}), 'PE')
        ISO_PriceCode = transform.ccode('X12_ELEM_639_TO_ISO_PRICETYPE', X12_PriceCode)
        ISO_PriceCode_Text = transform.ccode('ISO_PRICETYPE_TO_TEXT', ISO_PriceCode)
        UnitPrice = po1.get({'BOTSID': 'PO1', 'PO104': None})

        # Get Item Values by Qualifier
        BuyerItem = get_item_number_by_qual(po1, 'SK')
        SellerItem = get_item_number_by_qual(po1, 'CB')
        UPC = get_item_number_by_qual(po1, 'UP')

        Description = po1.get({'BOTSID': 'PO1'}, {'BOTSID': 'PID', 'PID01': 'F', 'PID05': None})

        # Write output
        orderLineOut.put({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'ID', 'IdentifierContent': LineNumber})
        orderLineOut.put({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'Quantity', 'QuantityContent': QuantityOrdered})
        orderLineOut.put({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'Quantity', 'QuantityUnitCode': ISO_UOM})

        orderLineOut.put({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'Price'}, {'BOTSID': 'PriceAmount', 'AmountContent': UnitPrice})
        orderLineOut.put({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'Price'}, {'BOTSID': 'PriceTypeCode', 'CodeContent': ISO_PriceCode})
        orderLineOut.put({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'Price'}, {'BOTSID': 'PriceTypeCode', 'CodeNameText': ISO_PriceCode_Text})

        orderLineOut.put({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'LineExtensionAmount', 'AmountContent': Decimal(UnitPrice) * Decimal(QuantityOrdered)})

        orderLineOut.put({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'Item'}, {'BOTSID': 'BuyersItemIdentification'}, {'BOTSID': 'ID', 'IdentifierContent': BuyerItem})
        orderLineOut.put({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'Item'}, {'BOTSID': 'BuyersItemIdentification'}, {'BOTSID': 'ID', 'IdentificationSchemeIdentifier': ''})

        orderLineOut.put({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'Item'}, {'BOTSID': 'SellersItemIdentification'}, {'BOTSID': 'ID', 'IdentifierContent': SellerItem})

        orderLineOut.put({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'Item'}, {'BOTSID': 'StandardItemIdentification'}, {'BOTSID': 'ID', 'IdentifierContent': UPC})
        orderLineOut.put({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'Item'}, {'BOTSID': 'StandardItemIdentification'}, {'BOTSID': 'ID', 'IdentificationSchemeIdentifier': 'UPC'})

        orderLineOut.put({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'Item'}, {'BOTSID': 'Description', 'TextContent': Description})

    # CTT Segment
    CTT = inn.get({'BOTSID': 'ST'}, {'BOTSID': 'CTT', 'CTT01': None})
    out.put({'BOTSID': 'ROOT'}, {'BOTSID': 'Order'}, {'BOTSID': 'LineCountNumeric', 'NumericContent': CTT})
