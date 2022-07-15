#! /usr/bin/env python3
#coding=utf8

import time
import re
import os
from sys import argv

# Author @Lani_Ka_Nani

def latinizator(letter, dic):
    for i, j in dic.items():
        letter = letter.replace(i, j)
    return letter

legend = {
',':'',
'а':'a',
'б':'b',
'в':'v',
'г':'g',
'д':'d',
'е':'e',
'ё':'yo',
'ж':'zh',
'з':'z',
'и':'i',
'й':'y',
'к':'k',
'л':'l',
'м':'m',
'н':'n',
'о':'o',
'п':'p',
'р':'r',
'с':'s',
'т':'t',
'у':'u',
'ф':'f',
'х':'h',
'ц':'c',
'ч':'ch',
'ш':'sh',
'щ':'shch',
'ъ':'y',
'ы':'y',
'ь':"'",
'э':'e',
'ю':'yu',
'я':'ya',

'А':'A',
'Б':'B',
'В':'V',
'Г':'G',
'Д':'D',
'Е':'E',
'Ё':'Yo',
'Ж':'Zh',
'З':'Z',
'И':'I',
'Й':'Y',
'К':'K',
'Л':'L',
'М':'M',
'Н':'N',
'О':'O',
'П':'P',
'Р':'R',
'С':'S',
'Т':'T',
'У':'U',
'Ф':'F',
'Х':'H',
'Ц':'Ts',
'Ч':'Ch',
'Ш':'Sh',
'Щ':'Shch',
'Ъ':'Y',
'Ы':'Y',
'Ь':"'",
'Э':'E',
'Ю':'Yu',
'Я':'Ya',
}

# Достаем локальную дату
result = time.localtime(time.time())

if len(argv) > 1:
    event_name = argv[1]
else:
    # Вводим название трансляции, если его не передали его при запуске скрипта - строка через пробел в кавычках после имени скрипта
    event_name = input('\nEnter event name: ')

translited_event_name = latinizator(event_name, legend)

if len(argv) > 2:
    CFlineName = argv[2]
else:
    # Вводим название линии, если его не передали при запуске скрипта - строка через пробел после имени трансляции
    CFlineName = input('Enter CF line name: ')

if len(argv) > 3:
    OKKOlineName = argv[3]
else:
    # Вводим название линии, если его не передали при запуске скрипта - строка через пробел после имени трансляции
    OKKOlineName = input('Enter OKKO line name: ')

if len(argv) > 4:
    VplaylineName = argv[4]
else:
    # Вводим название линии Vplay, если его не передали при запуске скрипта - строка через пробел после имени основной линии
    VplaylineName = input('Enter Vplay line name: ')

# Собираем первую строку CF
CF_pre_event_name = translited_event_name + ' [' + CFlineName + '] ' + str(result.tm_mday) + '/' + str(result.tm_mon)
print("-"*len(CF_pre_event_name))
print(CF_pre_event_name)

# Собираем вторую строку CF
CF_pre_event_clip_name = re.sub("[^A-Za-z0-9_ /]", "", CF_pre_event_name)
CF_event_clip_name = re.sub("[ /]", "_", CF_pre_event_clip_name)
print(CF_event_clip_name)

print()

# Собираем первую строку OKKO
OKKO_pre_event_name = translited_event_name + ' [' + OKKOlineName + '] ' + str(result.tm_mday) + '/' + str(result.tm_mon)
print(OKKO_pre_event_name)

# Собираем вторую строкуOKKO
OKKO_pre_event_clip_name = re.sub("[^A-Za-z0-9_ /]", "", OKKO_pre_event_name)
OKKO_event_clip_name = re.sub("[ /]", "_", OKKO_pre_event_clip_name)
print(OKKO_event_clip_name)

print()

# Собираем первую строку Vplay
preVplayEventName = translited_event_name + ' [' + VplaylineName + '] ' + str(result.tm_mday) + '/' + str(result.tm_mon)
print(preVplayEventName)

# Собираем вторую строку Vplay
preVplayEvenCliptName = re.sub("[^A-Za-z0-9_ /]", "", preVplayEventName)
VplayEvenCliptName = re.sub("[ /]", "_", preVplayEvenCliptName)
print(VplayEvenCliptName)
print("-"*len(CF_pre_event_name))
