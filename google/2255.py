def findFirstTimeOut(logs, timeout):
    rpc2ts = dict()
    while True:
        try:
            log = next(logs)
            id, ts, state = log.split(',')
            ts = int(ts)
            id = int(id)
            if rpc2ts:
                earliestRpc = next(iter(rpc2ts))
                if ts - rpc2ts[earliestRpc] >= timeout:
                    return earliestRpc, ts
            if state == 'Start':
                rpc2ts[id] = ts
            else:
                del rpc2ts[id]
        except StopIteration:
            if rpc2ts:
                return next(iter(rpc2ts)), ts
            else:
                return -1, -1


logs = ["1,0,Start", "2,1,Start", "1,2,End", "3,6,Start", "2,7,End", "3,8,End"]
print(findFirstTimeOut(iter(logs), 3))
