import autoScaleListner, loadBalancer;

# class that hols the instance ID and resources allocated
class virtualInstance:
    def __init__(self):
        self.instanceId = 0
        self.resouceAllocated = 0
        self.accountStatus = ""

    def getinstanceId(self):
        return self.instanceId

    def setinstanceId(self, value):
        self.instanceId = value

    def getresouceAllocated(self):
        return self.resouceAllocated

    def setresouceAllocated(self, value):
        self.resouceAllocated = value

    def getaccountStatus(self):
        return self.accountStatus

    def setaccountStatus(self, value):
        self.accountStatus = value

    # auto scaling the resources for the paid and partially paid accounts
    def scaleService(self, requestId, customerUserStatus, resourcesAllocated, numberOfRequests):
        # autoscale the resources allocated
        autoScale = autoScaleListner.autoScaleListner(resourcesAllocated, customerUserStatus)
        autoScale.autoScale(numberOfRequests, requestId)
        loadBalancer.loadBalancer().completedRequest(requestId = requestId, customerUserStatus = customerUserStatus, resourcesUsed = resourcesAllocated)

