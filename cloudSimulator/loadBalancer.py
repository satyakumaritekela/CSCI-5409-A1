import random
import resourcePool
import virtualInstance

# creating singleton class
def singleton(object):
    obj = object()
    object.__new__ = staticmethod(lambda object: obj)
    try:
        del object.__init__
    except AttributeError:
        pass
    return object


# load balancer is a singleton class
@singleton
class loadBalancer():
    requestList = []
    timeTaken = []
    resourcesList = []

    def __init__(self):
        self.requestList = []
        self.resourcesList = []
        self.requests = {
            "paid_account": [],
            "partially_paid_account": [],
            "free_account": []
        }
        self.timeTaken = {
            "paid_account": [],
            "partially_paid_account": [],
            "free_account": []
        }
        self.resourcesUsed = {
            "paid_account": [],
            "partially_paid_account": [],
            "free_account": []
        }

    def receiveRequest(self, requestId, customerUserStatus, numberOfRequests):
        if customerUserStatus == "free_account":
            freeresourcesAllocated = random.randint(1, 2)
            freeresourcesPresent = resourcePool.resourcePool().getUnPaidResources()
            resourcePool.resourcePool().setUnPaidResources(freeresourcesPresent - freeresourcesAllocated)
            self.requestList.append(requestId)
            instance = virtualInstance.virtualInstance()
            self.requests[customerUserStatus].append(requestId)
            instance.scaleService(requestId, customerUserStatus, freeresourcesAllocated, numberOfRequests)
            resource = {
                "requestId": requestId,
                "customerUserStatus": customerUserStatus,
                "resourcesAllocated": freeresourcesAllocated
            }
            self.resourcesList.append(resource)
        elif customerUserStatus == "partially_paid_account":
            partialresourcesAllocated = random.randint(1, 3)
            self.requestList.append(requestId)
            if len(self.requestList) > numberOfRequests / 2:
                partialresourcesPresent = resourcePool.resourcePool().getPartiallyPaidResources()
            else:
                partialresourcesPresent = resourcePool.resourcePool().getPartiallyPaidResources()
            resourcePool.resourcePool().setPartiallyPaidResources(partialresourcesPresent - partialresourcesAllocated)
            instance = virtualInstance.virtualInstance()
            self.requests[customerUserStatus].append(requestId)
            instance.scaleService(requestId, customerUserStatus, partialresourcesAllocated, numberOfRequests)
            resource = {
                "requestId": requestId,
                "customerUserStatus": customerUserStatus,
                "resourcesAllocated": partialresourcesAllocated
            }
            self.resourcesList.append(resource)
        elif customerUserStatus == "paid_account":
            paidresourcesAllocated = random.randint(1, 5)
            paidresourcesPresent = resourcePool.resourcePool().getPaidResources()
            resourcePool.resourcePool().setPaidResources(paidresourcesPresent - paidresourcesAllocated)
            self.requestList.append(requestId)
            instance = virtualInstance.virtualInstance()
            self.requests[customerUserStatus].append(requestId)
            instance.scaleService(requestId, customerUserStatus, paidresourcesAllocated, numberOfRequests)
            resource = {
                "requestId": requestId,
                "customerUserStatus": customerUserStatus,
                "resourcesAllocated": paidresourcesAllocated
            }
            self.resourcesList.append(resource)


    # adding all the requests to the request list and adding resources
    def completedRequest(self, customerUserStatus, requestId, resourcesUsed):
        self.requestList.remove(requestId)
        if customerUserStatus == "paid_account":
            self.resourcesUsed[customerUserStatus].append(resourcePool.resourcePool().getPaidResources())
        elif customerUserStatus == "partially_paid_account":
            self.resourcesUsed[customerUserStatus].append(resourcePool.resourcePool().getPartiallyPaidResources())
        elif customerUserStatus == "free_account":
            self.resourcesUsed[customerUserStatus].append(resourcePool.resourcePool().getUnPaidResources())
        resourcePool.resourcePool().addResources(resourcesUsed, customerUserStatus)
