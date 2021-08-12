#!/bin/python3

import boto3
from time import sleep


def describe():
    print("Showing all your Instances: ")
    client = boto3.client('ec2')
    response = client.describe_instances()
    for r in response['Reservations']:
       for i in r['Instances']:
          print("ID: " + i['InstanceId'] + "\nIP Address: " + i['PrivateIpAddress'] + "\n-------------------------\n")


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


def menu():
    while (True):
        print('\n'
              '             Hello\n'
              '          -----------\n'
              '    Welcome to AWS EC2 Menu:\n'
              '--------------------------------\n'
              '1.Describe EC2 Instances\n'
              '2.Delpoy EC2\n'
              '3.Terminate EC2\n'
              '4.Start EC2\n'
              '5.Stop EC2\n')
        choice = input("Enter your Choice: ")
        if choice == "1":
            describe()
        elif choice == "2":
            deploy()
        elif choice == "3":
            terminate()
        elif choice == "4":
            start()
        elif choice == "5":
            stop()
        else:
            print("Please choose only 1-5 Only!!!")
            continue
        e = input("Do you want to Exit y/n?\nEnter Answer: ")
        if e == "y" or e == "yes":
            print("Thank You ByeBye...")
            sleep(1.5)
            break
        else:
            print("Returning to Menu...")
            sleep (1.5)


menu()