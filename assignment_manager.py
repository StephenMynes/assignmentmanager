import discord
import csv
import time

def dateArrayCreator():
    dateArray = []
    dateArray.append(time.strftime("%d"))
    dateArray.append(time.strftime("%m"))
    return(dateArray)

def csvChecker():
    returnArray = []
    with open("assignments.csv", "r") as db:
        reader = csv.reader(db, lineterminator = '\n')
        for i in db:
            returnArray.append(i)

    return(returnArray)

def lineRemover(array):
    with open("assignments.csv", "r+") as f:
        lines = f.readlines()
        returnArray = sum([x.rstrip('\n').split(',') for x in lines],[])

    return(returnArray)


def dateSimplifier(array):
    dateNumbers = []
    
    with open("temp.csv", "w") as db:
        writer = csv.writer(db, lineterminator = '\n')
        writer.writerows(array)
    
    with open("temp.csv", "r+") as f:
        lines = f.readlines()
        returnArray = sum([x.rstrip('\n').split(',') for x in lines],[])

    for i in returnArray:
        try:
            dateNumbers.append(int(i))

        except:
            print("INVALID")
        
    return(dateNumbers)

def assignmentLooper(assignmentArray, passThrough):
    return(assignmentArray[passThrough])


def assignmentPrinter(loopLength, assignmentArray, counter):
        return(assignmentLooper(assignmentArray, counter))

def dayMonthCreator(date):
    togetherDate = []
    string = ""

    print(date)

    string = string + str(date[0])
    string = string + str(date[1])
    togetherDate.append(string)
    string = ""

    string = string + str(date[2])
    string = string + str(date[3])
    togetherDate.append(string)
    
    return(togetherDate)

def itemRemover(date, assignment, allAssignments):
    newAssignments = []
    assignmentDate = dayMonthCreator(dateSimplifier(date))
    currentDate = dateArrayCreator()
    if int(currentDate[0]) > int(assignmentDate[0]) and int(currentDate[1]) > int(assignmentDate[1]):
        for i in allAssignment:
            if i != assignment:
                newAssignments.append()

    with open("assignments.csv", "w") as db:
        writer = csv.writer(db, lineterminator = '\n')
        writer.writerows(newAssignments)

TOKEN = 'NTE0NTMxNjUxMTI5MzExMjM2.DtX7aA.1TGMqeEOw1Ofgs1RRGnkMXSTB7Y'

client = discord.Client()

currentWorkDue = lineRemover(csvChecker())
print(currentWorkDue)
date = dateSimplifier(currentWorkDue[2])
#itemRemover(date, currentWorkDue)
loopLength = len(currentWorkDue)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!assignments'):
        msg = '{0.author.mention}, the assignments due are:'.format(message)
        await client.send_message(message.channel, msg)
        for i in range(0, loopLength):
            await client.send_message(message.channel, assignmentPrinter(loopLength, currentWorkDue, i))

    if message.content.startswith('!homework'):
        msg = '{0.author.mention}, this feature is coming soon, i.e when Stephen can be bothered'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
