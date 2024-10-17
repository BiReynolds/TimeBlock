from datetime import datetime, timezone
from typing import Optional

## Test classes for use before creating the database

class testUser:
    def __init__(self,id,username,password):
        self.id = id
        self.username = username
        self.password = password 


class testBlockType:
    def __init__(self,id, name, daysPer, weekDay, monthDay, incType, userId):
        self.id = id
        self.name = name
        self.daysPer = daysPer
        self.weekDay = weekDay
        self.monthDay = monthDay
        self.incType = incType
        self.userId = userId

class testTimeBlock:
    def __init__(self,id,blockName,startTime,endTime,date,userId,blockTypeId):
        self.id = id
        self.blockName = blockName
        self.startTime = startTime
        self.endTime = endTime
        self.date = date
        self.userId = userId
        self.blockTypeId = blockTypeId

class testTaskType:
    def __init__(self,id,taskName,timeEst,daysPer,weekDay,monthDay,incType,blockType,userId):
        self.id = id
        self.taskName = taskName
        self.timeEst = timeEst
        self.daysPer = daysPer
        self.weekDay = weekDay
        self.monthDay = monthDay
        self.incType = incType
        self.blockType = blockType
        self.userId = userId

class testTask:
    def __init__(self,id,taskTypeId,schedDateTime,blockId):
        self.id = id
        self.taskTypeId = taskTypeId
        self.schedDateTime = schedDateTime
        self.blockId = blockId

