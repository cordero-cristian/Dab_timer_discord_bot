#!/usr/bin/env python3

# please use python3.5, the discord module only works with python3.5 and lower

import discord
from datetime import *
from datetime import datetime
from time import *
import time

# end of imports
# start of globals


score_keeper = dict()


# end of globals

# start of defs

# start of class timer
class timer():
    def __init__(self):
        self = dict()

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

                    if total_seconds % 10 == 0 or total_seconds % 5 == 0:

                        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        secs = str(total_seconds)
                        text = str()
                        text = (
                                    "Take your Dab in " + secs + " Seconds\n" + "The Current time is: " + now + "\nTake your Dab at " + time_to_dab.strftime(
                                "%Y-%m-%d %H:%M:%S"))

                        if total_seconds == 0:
                            text = "Take your Dab Now!"

                        return (text)

                x = get_secs(z)
                z = z - 1
                time.sleep(.95)

                if x is not None:
                    return x

        if amount_of_seconds >= 0:

            kick_off = time_keep(amount_of_seconds)

            if kick_off is not None:

                return kick_off

            else:

                amount_of_seconds = amount_of_seconds - 1

    def update_score_keeper(self, dabber):
        i = self.get(dabber)

        if i is not None:

            if self[dabber]['Total_dabs'] == 0:

               self.update(self[dabber]['Total_dabs'][1])

            else:

               yer = self[dabber]['Total_dabs']
               yer = yer + 1
               x = {dabber: {'Total_dabs': yer}}
               self.update(x)

        else:

            x = {dabber: {'Total_dabs': 1}}
            self.update(x)

    def get_score(dabber):

        try:
            score = int(score_keeper.get(dabber).get('Total_dabs'))
            print(score)
            return score

        except:
            x = "YOU'VE NEVER USED THE TIMER LOSER"
            return x



# end of class Timer
# start of class github
class github():

    def source_code():
        text = 'https://github.com/cordero-cristian/Dab_timer_discord_bot'

        return text


# end of class github

# end of functions

client = discord.Client()


@client.event
@client.event
async def on_message(message):
    possible_message_content_for_timer = tuple()
    possible_message_content_for_timer = ('$timer',
                                          '$Timer',
                                          '$TIMER'
                                          )

    possible_message_content_for_source = tuple()
    possible_message_content_for_source = ('$source',
                                           '$Source',
                                           '$SOURCE'
                                           )

    possible_message_content_for_score = tuple()
    possible_message_content_for_score = ('$score',
                                          '$Score',
                                          '$SCORE'
                                          )

    if message.author == client.user:
        return

    if message.content.startswith(possible_message_content_for_timer):

        user = message.author
        seconds_for_timer = int(timer.find_seconds(message.content))
        timer.update_score_keeper(score_keeper, user)

        while seconds_for_timer >= 0:

            entry = timer.dab_timer(seconds_for_timer)
            seconds_for_timer = seconds_for_timer - 1

            if entry is not None:
                await message.channel.send(entry)


    if message.content.startswith(possible_message_content_for_source):

        entry = github.source_code()
        await message.channel.send(entry)

    if message.content.startswith(possible_message_content_for_score):

        user = message.author
        user_total_dabs = timer.get_score(user)
        result = isinstance(user_total_dabs, str)
        entry = "The total amount of Dabs you have taken is" + str(user_total_dabs)

        if result == True:
            entry = user_total_dabs

        await message.channel.send(entry)


token = input("Enter Bots Token Creds\n")
client.run(token)
