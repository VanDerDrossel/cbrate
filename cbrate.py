import requests
from xml.dom.minidom import parseString


class ValCurs:
    """docstring for ValCurs"""

    def __init__(self, date, num_code, char_code, nominal, name, value):
        self.date = date
        self.num_code = num_code
        self.char_code = char_code
        self.nominal = nominal
        self.name = name
        self.value = value


def get_quotes(code: str) -> ValCurs:
    """CharCode"""
    url = 'https://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    dom = parseString(response.text)
    for char_tag in dom.getElementsByTagName("CharCode"):
        char_code = char_tag.firstChild.data
        if char_code == code.upper():
            date = dom.firstChild.getAttribute("Date")
            found = char_tag.parentNode
            num_code = found.childNodes[0].firstChild.data
            char_code = found.childNodes[1].firstChild.data
            nominal = found.childNodes[2].firstChild.data
            name = found.childNodes[3].firstChild.data
            value = float(found.childNodes[4].firstChild.data.replace(',', '.'))
            val_curs = ValCurs(date, num_code, char_code, nominal, name, value)
            return val_curs
