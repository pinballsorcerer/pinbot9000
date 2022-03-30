import random
import irc
import irc.bot

class TwitchPinBot(irc.bot.SingleServerIRCBot):
    def __init__(self):
        with open('C:\\Users\\Pinball\\password.txt', 'r') as f:
            password = f.readline()
        irc.bot.SingleServerIRCBot.__init__(self, [("irc.chat.twitch.tv", 6667, password)], "pinbot9000", "pinbot9000")
        # Note: channel names appear to be case sensitive
        self.channel = "#pinballsorcerer"
        self.greetings = []

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
        if (e.arguments[0].lower() == "!marco"):
            c.privmsg(self.channel, "Polo!")
        splat = e.arguments[0].split(' ')
        if (len(splat) >= 2 and
            splat[0].lower() == "@" + self._nickname.lower()):
            if (splat[1].lower() in ("hi", "hi,", "hello", "hello,")):
                greeting = random.choice(self.greetings) if self.greetings else ""
                c.privmsg(self.channel, f"Hi @{e.source.nick}! {greeting}")

    def on_ping(self, c, e):
        print("Received ping")
        c.send_items("PONG", ":" + e.target)

def main():
    print("hello, I am a chatbot")
    print("starting up")

    bot = TwitchPinBot()

    with open('greetings.txt', 'r') as f:
        bot.greetings = [line.strip() for line in f.readlines()]
    bot.start()

if __name__ == "__main__":
    main()
