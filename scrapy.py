from bs4 import BeautifulSoup
from config import BASE_URL
import urllib.request
import html5lib
import time
import re


def get_class_info(base_url, path, args_dict):
    classes = {}
    url = format_url(base_url, path, args_dict)
    soup = BeautifulSoup(get_html(url), "html5lib").find(
        'div', class_="course-list")
    if not soup:
        return None
    course_list = soup.find_all('tr')
    for tr in course_list:
        fields = [
            td.string if td.string else format_instructor_string(str(td)) for td in tr.find_all('td')]
        if len(fields) == 17:
            class_entry = format_class_entry(fields)
            classes[class_entry['code']] = class_entry
    return classes


# get the values of the select category possible
def get_select(select_type):
    department_dict = {}
    soup = BeautifulSoup(get_html(BASE_URL), "html5lib")
    for select in soup.find_all("select"):
        if select.get('name') == select_type:
            for option in select.find_all("option"):
                department_dict[option.get('value')] = option.text
            break

    return department_dict


def format_url(base_url, path, args_dict):
    values = []
    for key, value in args_dict.items():
        values.append((key, value))
    url = base_url + path + urllib.parse.urlencode(values)
    return url


def get_html(url):
    with urllib.request.urlopen(url) as response:
        html = response.read().decode()
    return html


def format_class_entry(class_fields):
    class_fields = [field.replace('\xa0', '').replace(
        '   ', ' ') for field in class_fields]
    code = class_fields[0]
    _type = class_fields[1]
    sec = class_fields[2]
    units = class_fields[3]
    instructor = class_fields[4]
    time = class_fields[5]
    place = class_fields[6]
    final = class_fields[7]
    _max = class_fields[8]
    enr = class_fields[9]
    if '/' in enr:
        enr = enr[enr.find('/ ')+2:]
    wl = class_fields[10]
    req = class_fields[11]
    nor = class_fields[12]
    rstr = class_fields[13]
    status = class_fields[16]

    class_entry = {
        'code': code,
        'type': _type,
        'sec': sec,
        'units': units,
        'instructor': instructor,
        'time': time,
        'place': place,
        'final': final,
        'max': _max,
        'enr': enr,
        'wl': wl,
        'req': req,
        'nor': nor,
        'rstr': rstr,
        'status': status
    }

    return class_entry


def format_instructor_string(td):
    new_str = ''
    open_tag = False
    for char in td:
        if char == '<':
            open_tag = True

        if not open_tag:
            new_str += char

        if char == '>':
            open_tag = False
            new_str += '/'

    new_str = new_str.strip('/')
    return new_str
