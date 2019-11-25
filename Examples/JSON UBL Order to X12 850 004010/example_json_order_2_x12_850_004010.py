# mapping-script
import bots.transform as transform
from datetime import datetime


# This mapping script maps an incoming x12 004010 850 message to a JSON message.
# Bots calls the 'main' function in this mapping script
# inn: the object for the incoming message; via get() and getloop() the content of the message can be accessed.
# out: the object for the outgoing message; via put() and putloop() content is written for this message.
def main(inn, out):

    # Get Header and Partner Information
    test_indicator = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'UBLExtensions'}, {'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'CopyIndicator', 'IdentifierContent': None})
    inn.ta_info['testindicator'] = test_indicator
    out.ta_info['ISA15'] = test_indicator
    out.ta_info['testindicator'] = test_indicator

    from_partner = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'UBLExtensions'}, {'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'SenderParty'}, {'BOTSID': 'PartyIdentification'}, {'BOTSID': 'ID', 'IdentifierContent': None})
    inn.ta_info['frompartner'] = from_partner
    out.ta_info['frompartner'] = from_partner

    from_partner_qual = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'UBLExtensions'}, {'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'SenderParty'}, {'BOTSID': 'PartyIdentification'}, {'BOTSID': 'ID', 'IdentificationSchemeNameText': None})
    inn.ta_info['ISA05'] = from_partner_qual
    out.ta_info['ISA05'] = from_partner_qual

    to_partner = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'UBLExtensions'}, {'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'ReceiverParty'}, {'BOTSID': 'PartyIdentification'}, {'BOTSID': 'ID', 'IdentifierContent': None})
    inn.ta_info['topartner'] = to_partner
    out.ta_info['topartner'] = to_partner

    to_partner_qual = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'UBLExtensions'}, {'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'ReceiverParty'}, {'BOTSID': 'PartyIdentification'}, {'BOTSID': 'ID', 'IdentificationSchemeNameText': None})
    inn.ta_info['ISA07'] = to_partner_qual
    out.ta_info['ISA07'] = to_partner_qual

    isa_date = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'UBLExtensions'}, {'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'IssueDate', 'DateContent': None})
    isa_date = transform.datemask(isa_date, 'YYYY-mm-DD', 'YYmmDD')
    out.ta_info['ISA09'] = isa_date

    isa_Time = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'UBLExtensions'}, {'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'IssueTime', 'TimeContent': None})
    isa_Time = transform.datemask(isa_Time, "00:00", "0000")
    out.ta_info['ISA10'] = isa_Time

    version = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'UBLExtensions'}, {'BOTSID': 'UBLExtension'}, {'BOTSID': 'ExtensionContent'}, {'BOTSID': 'DocumentEnvelope'}, {'BOTSID': 'VersionID', 'IdentifierContent': None})
    out.ta_info['version'] = version

    # ST Segment
    out.put({'BOTSID': 'ST', 'ST01': '850'})
    out.put({'BOTSID': 'ST', 'ST02': out.ta_info['reference'].zfill(4)})

    # BEG Segemnt
    purpose_code = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'PurposeCode', 'CodeContent': None})
    ordertype_code = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'OrderTypeCode', 'CodeContent': None})

    order_number = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'ID', 'IdentifierContent': None})
    inn.ta_info['botskey'] = order_number
    out.ta_info['botskey'] = order_number

    order_date = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'IssueDate', 'DateContent': None})
    order_date = transform.datemask(order_date, 'mm/DD/YYYY', 'YYYYmmDD')

    contract_number = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'Contract'}, {'BOTSID': 'ID', 'IdentifierContent': None})

    out.put({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG01': purpose_code})
    out.put({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG02': ordertype_code})
    out.put({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG03': order_number})
    out.put({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG05': order_date})
    out.put({'BOTSID': 'ST'}, {'BOTSID': 'BEG', 'BEG06': contract_number})

    # DTM Segment
    EstimatedDeliveryDateQual = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'RequestedDeliveryPeriod'}, {'BOTSID': 'DescriptionCode', 'CodeContent': None})
    EstimatedDeliveryDate = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'RequestedDeliveryPeriod'}, {'BOTSID': 'StartDate', 'DateContent': None})
    EstimatedDeliveryDate = transform.datemask(EstimatedDeliveryDate, 'mm/DD/YYYY', 'YYYYmmDD')

    if EstimatedDeliveryDateQual == '017':
        out.put({'BOTSID': 'ST'}, {'BOTSID': 'DTM', 'DTM01': EstimatedDeliveryDateQual})
        out.put({'BOTSID': 'ST'}, {'BOTSID': 'DTM', 'DTM02': EstimatedDeliveryDate})

    # TD5 Segment
    SCAC = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'CarrierParty'}, {'BOTSID': 'PartyIdentification'}, {'BOTSID': 'ID', 'IdentifierContent': None})
    CarrierName = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'CarrierParty'}, {'BOTSID': 'PartyName'}, {'BOTSID': 'Name', 'TextContent': None})

    out.put({'BOTSID': 'ST'}, {'BOTSID': 'TD5', 'TD502': '2'})
    out.put({'BOTSID': 'ST'}, {'BOTSID': 'TD5', 'TD503': SCAC})
    out.put({'BOTSID': 'ST'}, {'BOTSID': 'TD5', 'TD505': CarrierName})

    # N1  - BT
    PartyQual = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'BuyerCustomerParty'}, {'BOTSID': 'Party'}, {'BOTSID': 'PartyIdentification', 'IdentificationSchemeIdentifier': None})
    PartyName = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'BuyerCustomerParty'}, {'BOTSID': 'Party'}, {'BOTSID': 'PartyName'}, {'BOTSID': 'Name', 'TextContent': None})
    PartyAgency = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'BuyerCustomerParty'}, {'BOTSID': 'Party'}, {'BOTSID': 'PartyIdentification', 'IdentificationSchemeAgencyIdentifier': None})
    PartyNumber = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'BuyerCustomerParty'}, {'BOTSID': 'Party'}, {'BOTSID': 'PartyIdentification', 'IdentifierContent': None})

    if PartyQual == 'BT':
        out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': PartyQual})
        out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N102': PartyName})
        out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N103': PartyAgency})
        out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N104': PartyNumber})

        PartyAddress1 = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'BuyerCustomerParty'}, {'BOTSID': 'Party'}, {'BOTSID': 'PostalAddress'}, {'BOTSID': 'StreetName', 'TextContent': None})
        PartyAddress2 = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'BuyerCustomerParty'}, {'BOTSID': 'Party'}, {'BOTSID': 'PostalAddress'}, {'BOTSID': 'AdditionalStreetName', 'TextContent': None})

        PartyCity = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'BuyerCustomerParty'}, {'BOTSID': 'Party'}, {'BOTSID': 'PostalAddress'}, {'BOTSID': 'CityName', 'TextContent': None})
        PartyCountrySubentity = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'BuyerCustomerParty'}, {'BOTSID': 'Party'}, {'BOTSID': 'PostalAddress'}, {'BOTSID': 'CountrySubentity', 'TextContent': None})
        PartyPostal = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'BuyerCustomerParty'}, {'BOTSID': 'Party'}, {'BOTSID': 'PostalAddress'}, {'BOTSID': 'PostalZone', 'TextContent': None})
        PartyCountry = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'BuyerCustomerParty'}, {'BOTSID': 'Party'}, {'BOTSID': 'PostalAddress'}, {'BOTSID': 'Country'}, {'BOTSID': 'IdentificationCode', 'CodeContent': None})

        out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': 'BT', }, {'BOTSID': 'N3', 'N301': PartyAddress1})
        out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': 'BT', }, {'BOTSID': 'N3', 'N302': PartyAddress2})

        out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': 'BT', }, {'BOTSID': 'N4', 'N401': PartyCity})
        out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': 'BT', }, {'BOTSID': 'N4', 'N402': PartyCountrySubentity})
        out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': 'BT', }, {'BOTSID': 'N4', 'N403': PartyPostal})
        out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': 'BT', }, {'BOTSID': 'N4', 'N404': PartyCountry})

    # N1  - ST
    PartyQual = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'DeliveryAddress'}, {'BOTSID': 'ID', 'IdentificationSchemeIdentifier': None})
    PartyName = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'DeliveryAddress'}, {'BOTSID': 'BuildingName', 'TextContent': None})
    PartyAgency = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'DeliveryAddress'}, {'BOTSID': 'ID', 'IdentificationSchemeAgencyIdentifier': None})
    PartyNumber = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'DeliveryAddress'}, {'BOTSID': 'ID', 'IdentifierContent': None})

    if PartyQual == 'ST':
        out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': PartyQual})
        out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N102': PartyName})
        out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N103': PartyAgency})
        out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N104': PartyNumber})

        PartyAddress1 = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'DeliveryAddress'}, {'BOTSID': 'StreetName', 'TextContent': None})
        PartyAddress2 = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'DeliveryAddress'}, {'BOTSID': 'AdditionalStreetName', 'TextContent': None})

        PartyCity = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'DeliveryAddress'}, {'BOTSID': 'CityName', 'TextContent': None})
        PartyCountrySubentity = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'DeliveryAddress'}, {'BOTSID': 'CountrySubentity', 'TextContent': None})
        PartyPostal = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'DeliveryAddress'}, {'BOTSID': 'PostalZone', 'TextContent': None})
        PartyCountry = inn.get({'BOTSID': 'Order'}, {'BOTSID': 'Delivery'}, {'BOTSID': 'DeliveryAddress'}, {'BOTSID': 'Country'}, {'BOTSID': 'IdentificationCode', 'CodeContent': None})

        out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': 'ST', }, {'BOTSID': 'N3', 'N301': PartyAddress1})
        out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': 'ST', }, {'BOTSID': 'N3', 'N302': PartyAddress2})

        out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': 'ST', }, {'BOTSID': 'N4', 'N401': PartyCity})
        out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': 'ST', }, {'BOTSID': 'N4', 'N402': PartyCountrySubentity})
        out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': 'ST', }, {'BOTSID': 'N4', 'N403': PartyPostal})
        out.put({'BOTSID': 'ST'}, {'BOTSID': 'N1', 'N101': 'ST', }, {'BOTSID': 'N4', 'N404': PartyCountry})

    # Item Lines
    for line in inn.getloop({'BOTSID': 'Order'}, {'BOTSID': 'OrderLine'}):

        # Out Object Array
        lineout = out.putloop({'BOTSID': 'ST'}, {'BOTSID': 'PO1'})

        # Get Values
        LineNumber = line.get({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'ID', 'IdentifierContent': None})

        # Get UOM, if empty use 'EA'
        ISO_UOM = transform.useoneof(line.get({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'Quantity', 'QuantityUnitCode': None}), 'EA')
        X12_UOM = transform.reverse_ccode('X12_ELEM_355_TO_ISO_UOM', ISO_UOM)

        QuantityOrdered = line.get({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'Quantity', 'QuantityContent': None})

        ISO_PriceCode = transform.useoneof(line.get({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'Price'}, {'BOTSID': 'PriceTypeCode', 'CodeContent': None}), 'PE')
        X12_PriceCode = transform.reverse_ccode('X12_ELEM_639_TO_ISO_PRICETYPE', ISO_PriceCode)
        UnitPrice = line.get({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'Price'}, {'BOTSID': 'PriceAmount', 'AmountContent': None})

        # Get Item Values by Qualifier
        BuyerItem = line.get({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'Item'}, {'BOTSID': 'BuyersItemIdentification'}, {'BOTSID': 'ID', 'IdentifierContent': None})
        SellerItem = line.get({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'Item'}, {'BOTSID': 'SellersItemIdentification'}, {'BOTSID': 'ID', 'IdentifierContent': None})

        StandardItemQual = line.get({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'Item'}, {'BOTSID': 'StandardItemIdentification'}, {'BOTSID': 'ID', 'IdentificationSchemeIdentifier': None})
        UPC = ""
        if StandardItemQual == 'UPC':
            UPC = line.get({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'Item'}, {'BOTSID': 'StandardItemIdentification'}, {'BOTSID': 'ID', 'IdentifierContent': None})

        Description = line.get({'BOTSID': 'OrderLine'}, {'BOTSID': 'LineItem'}, {'BOTSID': 'Item'}, {'BOTSID': 'Description', 'TextContent': None})

        # Write output
        lineout.put({'BOTSID': 'PO1', 'PO101': LineNumber})
        lineout.put({'BOTSID': 'PO1', 'PO102': QuantityOrdered})
        lineout.put({'BOTSID': 'PO1', 'PO103': X12_UOM})
        lineout.put({'BOTSID': 'PO1', 'PO104': UnitPrice})
        lineout.put({'BOTSID': 'PO1', 'PO105': X12_PriceCode})

        lineout.put({'BOTSID': 'PO1', 'PO106': 'IN'})
        lineout.put({'BOTSID': 'PO1', 'PO107': SellerItem})

        lineout.put({'BOTSID': 'PO1', 'PO108': 'SK'})
        lineout.put({'BOTSID': 'PO1', 'PO109': BuyerItem})

        if StandardItemQual == 'UPC' and UPC != "":
            lineout.put({'BOTSID': 'PO1', 'PO110': 'UP'})
            lineout.put({'BOTSID': 'PO1', 'PO111': UPC})

        lineout.put({'BOTSID': 'PO1'}, {'BOTSID': 'PID', 'PID01': 'F', 'PID05': Description})

    # last line (counts the segments produced in out-message)
    out.put({'BOTSID': 'ST'}, {'BOTSID': 'SE', 'SE01': out.getcount() + 1})
    out.put({'BOTSID': 'ST'}, {'BOTSID': 'SE', 'SE02': (out.ta_info['reference']).zfill(4)})
