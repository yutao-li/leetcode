class Address:
    def __init__(self, streetNumber, streetName, cityName, stateName):
        self.streetNumber = streetNumber
        self.streetName = streetName
        self.cityName = cityName
        self.stateName = stateName


class AddressBook:
    def __init__(self, addressList):
        self.addressList = addressList


def convertAddressToList(address):
    return [address.streetNumber, address.streetName, address.cityName, address.stateName]


class Query:
    def __init__(self, addressBook):
        self.trie = dict()
        addressLists = [convertAddressToList(address) for address in addressBook]
        for addressList in addressLists:
            node = self.trie
            for scope in addressList:
                if scope not in node:
                    node[scope] = dict()
                node = node[scope]

    def checkMatchAny(self, address):
        def recursiveMatch(node, indexInAddress):
            if indexInAddress == 4:
                return True
            if not addressList[indexInAddress]:
                for nextNode in node.values():
                    if recursiveMatch(nextNode, indexInAddress + 1):
                        return True
                return False
            if addressList[indexInAddress] not in node:
                return False
            return recursiveMatch(node[addressList[indexInAddress]], indexInAddress + 1)

        addressList = convertAddressToList(address)
        return recursiveMatch(self.trie, 0)
