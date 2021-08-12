#!/bin/python3

import boto3
from time import sleep


def deploy():
    ec2 = boto3.resource('ec2')
    # create a new EC2 instance
    image = input("Choose Image: ")
    num_of_ins = input("Choose number of instances:")
    instances = ec2.create_instances(
        ImageId=image,
        MinCount=1,
        MaxCount=int(num_of_ins),
        InstanceType='t2.micro',
        KeyName='aws_automation',
    )
    sleep(1)
    print("The Instances Deployed")


def terminate():
    instances = input("Enter the ID of the instance you want to terminate:\n***Example: i-05a6cf55a1622f91a, "
                      "i-03b0b31da2ac9df9f, i-097f050b310dde5a7...***\nEnter IDs: ")
    ids = ''.join(instances)
    ids = ids.split(', ')
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(InstanceIds=ids).terminate()
    print("Terminating Instances...")
    sleep(2)
    print("The Instances " + str(ids) + " Terminated")


def start():
    ec2 = boto3.resource('ec2')
    instances = input("Enter the ID of the instance you want to start:\n***Example: i-05a6cf55a1622f91a, "
                      "i-03b0b31da2ac9df9f, i-097f050b310dde5a7...***\nEnter IDs: ")
    ids = ''.join(instances)
    ids = ids.split(', ')
    ec2.instances.filter(InstanceIds=ids).start()
    print("Starting Instances...")
    sleep(2)
    print("The Instances " + str(ids) + " Started")


def stop():
    ec2 = boto3.resource('ec2')
    instances = input("Enter the ID of the instance you want to stop:\n***Example: i-05a6cf55a1622f91a, "
                      "i-03b0b31da2ac9df9f, i-097f050b310dde5a7...***\nEnter IDs: ")
    ids = ''.join(instances)
    ids = ids.split(', ')
    ec2.instances.filter(InstanceIds=ids).stop()
    print("Stopping Instances...")
    sleep(2)
    print("The Instances " + str(ids) + " Stopped")


e = "n"
while e == "n" or e == "no":
    print('\n'
          '             Hello\n'
          '          -----------\n'
          '    Welcome to AWS EC2 Menu:\n'
          '--------------------------------\n'
          '1.Delpoy EC2\n'
          '2.Terminate EC2\n'
          '3.Start EC2\n'
          '4.Stop EC2\n')
    choice = input("Enter your Choice: ")
    if choice == "1":
        deploy()
    elif choice == "2":
        terminate()
    elif choice == "3":
        start()
    elif choice == "4":
        stop()
    else:
        print("Please choose only 1-4 Only!!!")
    e = input("Do you want to Exit y/n?\nEnter Answer: ")
    if e == "n" or e == "no":
        print("Returning to Menu")
        sleep(1.5)
        continue
    elif e == "y" or e == "yes":
        print("Thank you Byebye!")
        break
    else:
        print("Enter y/n ONLY!")