from bisect import bisect_right


class IpSystem:
    def __init__(self, ipRecords):
        self.ipRecords = sorted(
            [[int(i) for i in ip1.split('.')], [int(i) for i in ip2.split('.')], city] for ip1, ip2, city
            in ipRecords)

    def findCity(self, ip):
        ip = [int(i) for i in ip.split('.')]
        index = bisect_right(self.ipRecords, [ip, [float('inf')]])
        assert index > 0 and ip <= self.ipRecords[index - 1][1], "ip falls out of recorded range"
        return self.ipRecords[index - 1][2]


ipRecords = [['1.0.1.1', '1.0.1.10', 'NYC'],
             ['1.0.1.20', '1.0.1.30', 'SF']]
ipSystem = IpSystem(ipRecords)
print(ipSystem.findCity('1.0.1.9'))
