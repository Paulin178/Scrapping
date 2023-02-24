class CirfaEntry:
    def __init__(self,name,address,phone,description):
        self.name = name
        self.address = address
        self.phone = phone
        self.description = description

    def getDictEntry(self):
        return {
            "name":self.name,
            "address":self.address,
            "phone":self.phone,
            "description":self.description
        }