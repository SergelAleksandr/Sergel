import re
import datetime
import collections
import pytz
# import parsing_log

v = '17/May/2015'
b = '18/May/2015'
n = '19/May/2015'
m = '20/May/2015'

def date_pars(data):
    with open('Apache_log.txt', 'r') as fp:
        date = []
        line = fp.readline()
        for line in fp:
            if data in line:
                date.append(line)
        total = (data + ' total ' + str(len(date)))

        uni = []
        for line in date:
            uni_line = line.split(" ")[0]
            if uni_line not in uni:
                uni.append(uni_line)
        unique = (' unique ' + str(len(uni)))

        safari = []
        firefox = []
        
        for line in date:
            select = line.rsplit(' ')[-1]
            s_sel = select.split('/')[0]
            saf = 'Safari'
            ff = 'Firefox'
            ch = 'Chrome'
            ice = 'Iceweasel'
            tri = 'Trident'
            if saf in select:
                safari.append(s_sel)
            elif ff in select:
                firefox.append(s_sel)
    bro_saf = (' Браузер Safari: ' + str(len(safari)))
    bro_fire = (' Браузер Firefox: ' + str(len(firefox)))
    print(str(total) + str(unique) + bro_saf+ bro_fire)

def main():
    print('Парсинг по дате 17/05/2015: ')
    date_pars(v)
    date_pars(b)
    date_pars(n)
    date_pars(m)


if __name__ == "__main__":
    main()