

import logging
import sys

from irc.bot import SingleServerIRCBot

from PIL import Image
from playsound import playsound




# config
HOST = 'HOST'
PORT = 'PORT'
USERNAME = 'USERNAME'
PASSWORD = 'PASSWORD'
CHANNEL = '#CHANNEL'


class VBot(SingleServerIRCBot):
    VERSION = '1.0.0'

    def __init__(self, host, port, nickname, password, channel):
        SingleServerIRCBot.__init__(self, [(host, port, password)], nickname, nickname)
        self.channel = channel
        self.viewers = []

    def on_welcome(self, connection, event):
        connection.join(self.channel)
        connection.privmsg(event.target, 'Sup!')

    def on_pubmsg(self, connection, event):
        #logger.debug(self._parse_nickname_from_twitch_user_id(event.source))
        message = event.arguments[0]
        print(self._parse_nickname_from_twitch_user_id(event.source), ":", message)
        # Respond to messages starting with !
        if message.startswith("!"):
            self.do_command(event, message[1:])

    def do_command(self, event, message):
        message_parts = message.split()
        command = message_parts[0]
        

        if command == "version":
            version_message = 'Version: %s' % self.VERSION
            self.connection.privmsg(event.target, version_message)
        if command == "count_viewers":
            num_viewers = len(self.viewers)
            num_viewers_message = 'Viewer count: %d' % num_viewers
            self.connection.privmsg(event.target, num_viewers_message)
        if command == "test":
            img = Image.open('test.png')
            img.show()
        if command == "sound":
            playsound('test.mp3')
        elif command == 'exit':
            self.die(msg="")


    @staticmethod
    def _parse_nickname_from_twitch_user_id(user_id):
        # nickname!username@nickname.tmi.twitch.tv
        return user_id.split('!', 1)[0]


def main():
    my_bot = VBot(HOST, PORT, USERNAME, PASSWORD, CHANNEL)
    my_bot.start()


if __name__ == '__main__':
    main()


