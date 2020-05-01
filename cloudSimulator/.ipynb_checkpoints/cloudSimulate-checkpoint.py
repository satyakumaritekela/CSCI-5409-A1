from random import choices
import matplotlib.pyplot as pl
import random
import loadBalancer, autoScaleListner, virtualInstance, resourcePool

if __name__ == '__main__':
    # type of accounts in cloud5409 company
    userStatus = ["paid_account", "partially_paid_account", "free_account"]

    # count of different type of customers out of 100_000 customers
    customersCount = [0.5, 0.2, 0.3]

    # virtualInstances list
    virtualInstanceList = []

    # sending 1000 requests from different types of accounts
    for i in range(1000):
        # retrieving customer status using a random choice of total customers
        customerUserStatus = choices(userStatus, customersCount)

        # generating random requestId
        requestId = random.randint(0, 100000)

        lb = loadBalancer.loadBalancer()
        # sending request to the load balancer
        lb.receiveRequest(requestId = requestId, customerUserStatus = ''.join(customerUserStatus))

    lb = loadBalancer.loadBalancer()
    print(lb.resourcesUsed)

    pl.plot(range(len(lb.resourcesUsed["free_account"])), lb.resourcesUsed["free_account"], label = 'free_account')
    pl.plot(range(len(lb.resourcesUsed["partially_paid_account"])), lb.resourcesUsed["partially_paid_account"], label = 'partially_paid_account')
    pl.plot(range(len(lb.resourcesUsed["paid_account"])), lb.resourcesUsed["paid_account"], label='paid_account')
    pl.legend(loc = 'lower right')
    pl.show()