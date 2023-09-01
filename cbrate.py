import xml.etree.ElementTree as E  # https://docs.python.org/3/library/xml.etree.elementtree.html

import requests


URL = "https://www.cbr.ru/scripts/XML_daily.asp"


def get_raw_xml() -> str:
    response = requests.get(URL).text
    return response


def parsing_xml(raw_xml: str) -> list:
    # parses XML from a string 
    root = E.fromstring(raw_xml)
    
    # Meta information from first parent node
    meta_information = {root.tag: root.attrib}
    
    # Create list of dict
    valute = []
    for child in root:
        node = {i.tag: i.text for i in child}
        valute.append(node)
        
    return [meta_information, valute]


def get_val_curs(print_meta=False, add_date=True, format_value=True) -> list:
    raw_xml = get_raw_xml()
    meta, valute = parsing_xml(raw_xml)
    
    if print_meta:
        print(meta)
        
    if add_date:
        for val in valute:
            val["Date"] = meta["ValCurs"]["Date"]
    
    if format_value:
        for val in valute:
            val['Nominal'] = float(val['Nominal'])
            val['Value'] = float(val['Value'].replace(',', '.'))
    
    return valute


def filtred_by_char_code(data:list, *char_codes:str) -> list:
    """filter by Alphabetic code.
    ISO 4217. https://ru.wikipedia.org/wiki/ISO_4217
    """
    key_name = 'CharCode'
    res = [i for i in data for k,v in i.items() if v in char_codes and k==key_name]
    return res
