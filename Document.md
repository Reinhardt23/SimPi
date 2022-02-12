## JSON between client and server format
```
{
    data: int/string/array
    type: int
}
```
### Type 0: server message
Display on screen

### Type 1: client message
Start/Suspend/Resume/Stop actions of SimPi

### Type 2: simpi config queue
Queue of actions 

### Type 3: Multi-client management
The number of current connected clients


## SimPi Queue Options
```
{
    type: int
    options: int/string/array
}
```
#### 1. Start
Start `type: 10` \
Click to start `type: 11`

~#### 2. Suspend~
~Suspend `type: 20` \~
~Click to suspend `type: 21`~

~#### 3. Resume ~
~Resume `type: 30` \~
~Click to resume `type: 31`~

#### 4. Stop
Stop `type: 40` \
~Click to stop `type: 41`~

#### 5. Wait
Wait X mins `type: 50` \
Wait until X `type: 5X`

#### 6. Source
Open Source `type: 61` \
Close Source `type: 62`

#### 7. If Statement
If X `type: 7X` \
End if `type: 70`

#### 8. loop several times

# Documents
 - Bootstrap v5.1.3 [Documation](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
 - websockets  Documations: [Python](https://websockets.readthedocs.io/en/stable/index.html), [Javascript](https://javascript.info/websocket)