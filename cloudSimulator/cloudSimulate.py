from random import choices
import matplotlib.pyplot as plt
import random
import loadBalancer, autoScaleListner, virtualInstance, resourcePool
import time

if __name__ == '__main__':
    # type of accounts in cloud5409 company
    userStatus = ["paid_account", "partially_paid_account", "free_account"]

    # count of different type of customers out of 100_000 customers
    customersCount = [0.5, 0.3, 0.2]

    numberOfRequests = 1000
    # sending requests from different types of accounts
    for i in range(numberOfRequests):
        startingTime = time.process_time()
        # retrieving customer status using a random choice of total customers
        customerUserStatus = choices(userStatus, customersCount)

        # generating random requestId
        requestId = random.randint(0, 100000)
        lb = loadBalancer.loadBalancer()
        # sending request to the load balancer
        lb.receiveRequest(requestId = requestId, customerUserStatus = ''.join(customerUserStatus), numberOfRequests= numberOfRequests)

    lb = loadBalancer.loadBalancer()
    print(lb.resourcesUsed)
    #for i in lb.resourcesList:
        #print(i)

    # plot the graph
    x1 = range(len(lb.resourcesUsed["free_account"]))
    y1 = lb.resourcesUsed["free_account"]
    plt.plot(x1, y1, color='green', label="free_account")

    x2 = range(len(lb.resourcesUsed["partially_paid_account"]))
    y2 = lb.resourcesUsed["partially_paid_account"]
    plt.plot(x2, y2, color='red', label="partially_paid_account")

    x3 = range(len(lb.resourcesUsed["paid_account"]))
    y3 = lb.resourcesUsed["paid_account"]
    plt.plot(x3, y3, color='brown', label="paid_account")

    plt.xlabel('Number of requests for each type of user')
    plt.ylabel('Number of resources used for each type of user')

    plt.legend()

    plt.show()