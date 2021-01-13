# Script to clean up OCR

file_in = 'docs/filein.txt'
file_out = 'docs/fileout.txt'

margin = 'རྙིང་རྒྱུད།'
tibvol = 'འ '
newpage = True
premargin = True
pgtxt = ''
pgnum = 600
lnnum = 1

with open(file_in, 'r') as fin, open(file_out, 'w') as fout:
    fout.write("<div>\n")
    for ln in fin.readlines():
        ln = ln.strip()
        if ln.isnumeric() and len(ln) == 3:
            if len(pgtxt) > 0:
                fout.write(pgtxt)
                pgtxt = ''
            elif pgnum > 0:
                print("**** Page {} is blank! ****".format(pgnum))
            pgnum = int(ln) + 1
            lnnum = 1
            print("Page {}".format(pgnum))
            newpage = True
            premargin = True
            pgtxt += '<milestone unit="page" n="{0}"/>'.format(pgnum)
            continue
        elif ln == '༄༅།':
            continue
        elif ln == margin or ln.startswith(tibvol):
            print("margin: {}".format(ln))
            premargin = False
        elif not premargin and len(ln) > 0:
            if lnnum == 1:
                ln = ln[1:] if ln[0] == '།' else ln
                pgtxt += '<milestone unit="line" n="{}.{}"/>'.format(pgnum, lnnum)
                lnnum += 1
            elif ln[0] != '།':
                pgtxt += '<milestone unit="line" n="{}.{}"/>'.format(pgnum, lnnum)
                lnnum += 1

            pgtxt += ln.replace('༄༅། ', '')

    fout.write(pgtxt)
    fout.write("\n</div>")

print("Done!")

