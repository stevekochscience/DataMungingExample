import csv

# Make a list of all the filenames 2012_01.txt etc.
fnamebase = ''
fnames = []
YEAR = '2013'
NUMMONTHS = 12 # For partial year usage (normally 12 of course)
for i in range(1,NUMMONTHS+1):
    ex = "_%.2d.txt" %i
    fn = fnamebase + YEAR + ex
    fnames.append(fn)
outfname = fnamebase + YEAR + '.csv'
    
def process_location(locationCodes = [], filenames = []):
    yeardata = []
    codes = []
    for month, filename in enumerate(filenames):
        csvfile = open(filename, 'rb')
        reader = csv.reader(csvfile, delimiter='|')
        ftitle = reader.next() #title row of file
        headers = reader.next()
        
        
        # from the third row on, all rows from the millennium export should have 8 columns
        data = []
        for row in reader:
            data.append(row)
        
        codelist = [] #list of found codes
        countlist = [] #list of counts (these two arrays paired as x, y
        for index, row in enumerate(data):
            newrow = row
            newrow[0] = row[0].strip()
            data[index] = newrow
        
            if data[index][0] in locationCodes:
                subrow = [data[index][0], data[index][1]]
                codelist.append(data[index][0])
                countlist.append(data[index][1])
    
        # The list is missing rows that have zero, need to add these zeros
        for index, code in enumerate(locationCodes):
            if code not in codelist:
                codelist.insert(index, code)
                countlist.insert(index, 0)
        countlist = map(int, countlist)
        yeardata.append(countlist)
        codes = codelist
    return(codes, yeardata)


def write_location(outfile, locName, locationCodes, fnames):
    headers = [locName]
    codes, counts = process_location(locationCodes, fnames)
    totals = []
    for i, month in enumerate(counts):
        sum = 0
        for count in month:
            sum += count
        totals.append(sum)
        headers.append('%d/1/%s' % ((i+1), YEAR))
    
    for header in headers:
        outfile.write('%s,' % header)
    outfile.write('\n')
    
    for index, code in enumerate(codes):
        line = "%s" % code
        for j in range(len(counts)):
            line += ",%s" % counts[j][index]
        line += '\n'
        outfile.write(line)
    
    outfile.write('TOTAL,')
    for total in totals:
        outfile.write('%d,' % total)
    outfile.write('\n\n\n')

outfile = open(outfname, 'wb')

locCodes = ['fgc', 'fmin', 'fovs', 'fsto1', 'fsto2', 'fstor', 'fxx', 'fxxov', 'zcfsa']
write_location(outfile, 'FAL', locCodes, fnames)

locCodes = ['pgc', 'pgcll', 'povs']
write_location(outfile, 'PML', locCodes, fnames)

locCodes = ['sel', 'sgc', 'sgc2', 'sovs', 'sovs2', 'sstor', 'sxx']
write_location(outfile, 'CSEL', locCodes, fnames)

locCodes = ['zcopy', 'zgc2', 'zgc3', 'zgc-2', 'zint', 'zjv', 'zjvl', 'zjvo', 'zjvol',
       'zovs', 'zpww', 'zstpr', 'zvalt', 'zww']
write_location(outfile, 'ZIMM', locCodes, fnames)

outfile.close()

