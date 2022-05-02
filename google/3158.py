def parseCsv(filePath):
    def parseLine(line):
        if line.count('"') % 2:
            raise ValueError("row has odd quotes")
        res = []
        i = 0
        while True:
            bound = line.find(',', i)
            while line[i:bound].count('"') % 2:
                bound = line.find('"', bound + 1)
                bound = line.find(',', bound + 1)
            if bound == -1:
                res.append(line[i:])
                break
            res.append(line[i:bound])
            i = bound + 1
        if any(segment == '' or segment == '""' for segment in res):
            raise ValueError("row contains empty value")
        return res

    try:
        with open(filePath) as f:
            columns = f.readline().split(',')
            n = len(columns)
            data = []
            for i, line in enumerate(f.readlines()):
                try:
                    line = parseLine(line)
                except ValueError as e:
                    raise ValueError("parse error at row " + str(i + 2), e)
                if len(line) != n:
                    raise ValueError("inconsistent columns at row " + str(i + 2))
                row = {field: value for field, value in zip(columns, line)}
                data.append(row)
            return data
    except OSError as e:
        raise ValueError("file read failed", e)
