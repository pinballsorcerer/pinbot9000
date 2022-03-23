import irc
import irc.bot

class TwitchPinBot(irc.bot.SingleServerIRCBot):
    def __init__(self):
        with open('C:\\Users\\Pinball\\password.txt', 'r') as f:
            password = f.readline()
        irc.bot.SingleServerIRCBot.__init__(self, [("irc.chat.twitch.tv", 6667, password)], "pinbot9000", "pinbot9000")
        self.channel = "#pinballsorcerer"

    def on_welcome(self, c, e):
        print("We were welcomed in to the server!")
        c.join(self.channel)

    def on_join(self, c, e):
        print("We joined a channel! Sending a hello")
        c.privmsg(self.channel, "Greetings chat!")

    def on_privmsg(self, c, e):
        print("Private message received")

    def on_pubmsg(self, c, e):
        print("Public message received")
        if (e.arguments[0] == "!marco"):
            c.privmsg(self.channel, "Polo!")
        splat = e.arguments[0].split(' ')
        if (len(splat) >= 2 and
            splat[0] == "@" + self._nickname):
            if (splat[1].lower() in ("hi", "hi,", "hello", "hello,")):
                c.privmsg(self.channel, "Hi @" + e.source.nick + "!")

    def on_ping(self, c, e):
        print("Received ping")
        c.send_items("PONG", ":" + e.target)

def main():
    print("hello, I am a chatbot")
    print("starting up")
    
    bot = TwitchPinBot()
    bot.start()

if __name__ == "__main__":
    main()
