import PySimpleGUI as sg

import sys

if len(sys.argv) == 1:
    event, values = sg.Window('My Script',
                    [[sg.Text('Document to open')],
                    [sg.In(), sg.FileBrowse()],
                    [sg.Open(), sg.Cancel()]]).read(close=True)
    fname = values[0]
else:
    fname = sys.argv[1]

if not fname:
    sg.popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")
else:
    sg.popup('The filename you chose was', fname)
f = open(fname, "r", encoding='utf-8')
newlist = []
i = 1

## func to delete numbers is theres any
def sort(item):
    i = 0
    while item[i].isdigit():
        i += 1
    return item[i+1:]

## textfile into list
for item in f.readlines():
    newlist.append(sort(item))
k = 1

## Delete repetitions from textfile
while k < len(newlist):
    pivot = newlist[k-1]
    if newlist[k] == pivot:
        newlist.pop(k-1)
    k += 1



### Сохр в файл
f = open(fname, "w", encoding='utf-8')
for item in sorted(newlist):
    f.writelines(str(i) + ")" + item)
    i += 1
f.close()




