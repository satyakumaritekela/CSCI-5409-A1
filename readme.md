Overview:
**********

This program simulates the cloud architecture of the Cloud5409 company.

Installation:
**************

The architecture is implemented using python programming.

Files:
********

The whole program is divided into different files to solve the program

cloudSimulate.py – contains the main function that sends the multiple requests to the loadbalancer

loadBalancer.py – contains the program that distinguishes from the paid, partially paid, free users and assigns to the virtual instance

resourcePool.py – contains the fixed number of resources for the paid, partially paid and free users

task.py – contains the program that have a task to be executed for each request

virtualInstance.py – contains the program that assigns the request and sends to the autoscalelistner based upon the user type

autoScaleListner.py – contains the program that checks the task to autoscale the instances or not based on the user type

Usage:
********

import CloudSimulator project

Run cloudSimulator.py using python interpreter or pycharm that generates the random number of free user,partially paid user and paid users

Libraries used - random, matplotlib