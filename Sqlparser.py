# Input file name
INPUT = 'from_sqlserver_customer.sql'

# Output file name
# Existing file will be overwritten
OUTPUT = 'sqlserver_customer.sql'

# encoding
# enc = "ISO-8859-1"
enc = 'utf8'

# keywords for lines to skip
# list in list
# internal lists contain all words one line has to contain to be skipped
skipwords = [["GO\n"],
             ["print", "total", "records"],
             # ["more", "words"],
             ]


def parse():
    with open(INPUT, encoding=enc) as script:
        text = script.readlines()

    res = [""]
    for t in text:
        # skip unnecessary lines
        # if (t.find('GO') != -1) or (t.find('print') != -1 and t.find('records') != -1):
        if checkskip(t):
            continue

        # construct lines
        res[len(res) - 1] += t[:-1]
        if t[-2] == ";":
            res[len(res) - 1] += '\n'
            res += [""]
        else:
            res[len(res) - 1] += '\\n'

    # write result
    with open(OUTPUT, "w+", encoding=enc) as result:
        result.writelines(res)


def checkskip(t):
    skip = False
    for rows in skipwords:
        local = True
        for val in rows:
            local = local and (t.find(val) != -1)
        skip = skip or local
    return skip


if __name__ == '__main__':
    parse()
