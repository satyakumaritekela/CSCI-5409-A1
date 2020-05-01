import random
import task, loadBalancer
from concurrent.futures import ThreadPoolExecutor

# autoscale listner for auto scaling the instances
class autoScaleListner:
    resourcesList = {}
    # initializing the resources used and customeruser status
    def __init__(self, resourcesUsed, customerUserStatus):
        self.resourcesList = {
            "requestId": "",
            "customerUserStatus": "",
            "resourcesAllocated": ""
        }
        self.resourcesUsed = resourcesUsed
        self.customerUserStatus = customerUserStatus

    # auto scaling function
    def autoScale(self, numberOfRequests, requestId):
        # creating a thread pool for executing the resources
        executorService = ThreadPoolExecutor(max_workers = self.resourcesUsed)
        if self.customerUserStatus == "paid_account":
            paidTaskToDo = task.task(self.resourcesUsed)
            executorService.submit(paidTaskToDo.taskPerRequest(self.customerUserStatus))
        elif self.customerUserStatus == "free_account":
            if self.resourcesUsed > 1:
                pass
            else:
                # auto scaling is not possible for the free accounts
                unpaidTask = task.task(self.resourcesUsed)
                executorService.submit(unpaidTask.taskPerRequest(self.customerUserStatus))
        # auto scaling should be done only after 60%
        elif self.customerUserStatus == "partially_paid_account":
            partialTaskToDO = task.task(1)
            lb = loadBalancer.loadBalancer().requestList
            if partialTaskToDO.taskCompleted(60):
                finishPartialTask = task.task(self.resourcesUsed - 1)
                executorService.submit(finishPartialTask.taskPerRequest(self.customerUserStatus))
