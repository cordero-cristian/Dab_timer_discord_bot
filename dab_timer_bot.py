#!/usr/bin/env python3

#please use python3.5, the discord module only works python3.5 and lower

import discord
from datetime import *
from datetime import datetime
from time import *
import time
#end of imports
#start of globals

#end of globals

#start of defs

#start of class timer
class timer():

    def __int__(self):
        self = self()

    def find_seconds(str):

        position1 = str.index('|')
        position2 = position1 + 2
        secs = str[position2:]
        return secs

    def dab_timer(int):

        amount_of_seconds = int
        t1 = datetime.now()
        t2 = timedelta(seconds=amount_of_seconds)
        time_to_dab = t1 + t2

        def time_keep(z):

            if z >= 0:

                def get_secs(total_seconds):
                    def __int__(self):
                        self = self()

                    if total_seconds % 10 == 0 or total_seconds % 5 == 0 or total_seconds == 0:

                        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        secs = str(total_seconds)
                        text = str()
                        text = ("Take your Dab in " + secs + " Seconds\n" + "The Current time is: " + now + "\nTake your Dab at " + time_to_dab.strftime("%Y-%m-%d %H:%M:%S"))
                        if total_seconds == 0:
                            text = "Take your Dab Now!"

                        return(text)

                x = get_secs(z)
                z = z - 1
                time.sleep(.95)

                if x != None:
                    return x

        if amount_of_seconds >= 0:

            kick_off = time_keep(amount_of_seconds)

            if kick_off != None:
                return kick_off
            else:
                amount_of_seconds = amount_of_seconds - 1
#end of class Timer

#end of functions





client = discord.Client()

@client.event

@client.event
async def on_message(message):

    possible_message_content = tuple ()
    possible_message_content = ('$timer',
                                '$Timer',
                                '$TIMER',
                                )

    if message.author == client.user:
        return

    if message.content.startswith(possible_message_content):

        seconds_for_timer = int(timer.find_seconds(message.content))

        while seconds_for_timer >= 0:
            entry = timer.dab_timer(seconds_for_timer)
            seconds_for_timer = seconds_for_timer - 1

            if entry != None:

                await message.channel.send(entry)





token = input("Enter Bots Token Creds\n")
client.run(token)