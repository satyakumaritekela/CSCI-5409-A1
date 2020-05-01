# creating singleton class
def singleton(object):
    obj = object()
    object.__new__ = staticmethod(lambda object: obj)
    try:
        del object.__init__
    except AttributeError:
        pass
    return object

# creating static pool size of resources
@singleton
class resourcePool:
    def __init__(self):
        self.totalNumberOfResources = 100
        self.paidResources = 50
        self.unPaidResources = 20
        self.partiallyPaidResources = 30

    # getters and setters for the resources
    def getTotalNumberOfResources(self):
        return self.totalNumberOfResources

    def setTotalNumberOfResources(self, value):
        self.totalNumberOfResources = value

    def getPaidResources(self):
        return self.paidResources

    def setPaidResources(self, value):
        self.paidResources = value

    def getUnPaidResources(self):
        return self.unPaidResources

    def setUnPaidResources(self, value):
        self.unPaidResources = value

    def getPartiallyPaidResources(self):
        return self.partiallyPaidResources

    def setPartiallyPaidResources(self, value):
        self.partiallyPaidResources = value

    # adding resources after completing the task
    def addResources(self, numberOfResources, customerUserStatus):
        if customerUserStatus == "paid_account":
            self.paidResources += numberOfResources
        elif customerUserStatus == "partially_paid_account":
            self.partiallyPaidResources += numberOfResources
        elif customerUserStatus == "free_account":
            self.unPaidResources += numberOfResources