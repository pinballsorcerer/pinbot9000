'''Starts a Twitch chatbot for my channel'''
import random
import irc
import irc.bot

class TwitchPinBot(irc.bot.SingleServerIRCBot):
    '''A specific implementation of SingleServerIRCBot for my channel'''
    def __init__(self):
        with open('C:\\Users\\Pinball\\password.txt', 'rt', encoding='utf_8') as file:
            password = file.readline()
        irc.bot.SingleServerIRCBot.__init__(
            self,
            [("irc.chat.twitch.tv", 6667, password)],
            "pinbot9000",
            "pinbot9000")
        # Note: channel names appear to be case sensitive
        self.channel = "#pinballsorcerer"
        self.greetings = []

    def on_welcome(self, connection, _):
        '''Join the main stream channel after connecting to the server'''
        connection.join(self.channel)

    def on_join(self, connection, _):
        '''Send an announcement to the channel upon joining'''
        connection.privmsg(self.channel, "Greetings chat!")

    def on_pubmsg(self, connection, event):
        '''Parse each user's message to look for bot interaction'''
        print("Public message received")
        if event.arguments[0].lower() == "!marco":
            connection.privmsg(self.channel, "Polo!")
        splat = event.arguments[0].split(' ')
        if (len(splat) >= 2 and
            splat[0].lower() == "@" + self._nickname.lower()):
            if splat[1].lower() in ("hi", "hi,", "hello", "hello,"):
                greeting = random.choice(self.greetings) if self.greetings else ""
                connection.privmsg(self.channel, f"Hi @{event.source.nick}! {greeting}")

    #We think this needs to be a member function for it to be called by the base class
    #pylint: disable-next=no-self-use
    def on_ping(self, connection, event):
        '''Reply to ping messages with a pong, as expected by Twitch IRC'''
        print("Received ping")
        connection.send_items("PONG", ":" + event.target)

def main():
    '''Setup and start the chatbot'''
    print("hello, I am a chatbot")
    print("starting up")

    bot = TwitchPinBot()

    try:
        with open('greetings.txt', 'rt', encoding='utf_8') as file:
            bot.greetings = [line.strip() for line in file.readlines()]
    except OSError:
        print("No 'greetings.txt' file found - create one for random responses")

    bot.start()

if __name__ == "__main__":
    main()
