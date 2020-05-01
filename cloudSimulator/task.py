class task:
    def __init__(self, resourcesAllocated):
        self.resourcesAllocated = resourcesAllocated

    def taskPerRequest(self, customerUserStatus, percentageCompleted = 100):
        if customerUserStatus == "paid_account":
            for i in range(100):
                pass
        for i in range(self.resourcesAllocated):
            for j in range(percentageCompleted):
                if j + 1 == percentageCompleted:
                    return True
        i = 0
        if customerUserStatus == "partially_paid_account":
            while i <= 60:
                i = i + 1
        else:
            for i in range(100):
                pass

    def taskCompleted(self, percentageCompleted):
        return self.taskPerRequest(percentageCompleted)