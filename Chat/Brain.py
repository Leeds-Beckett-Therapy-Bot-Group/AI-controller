import aiml
import os

from pip._vendor.distlib.compat import raw_input

kernel = aiml.Kernel()

# saves 'brain'
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

# kernel now ready for use
while True:
    message = raw_input("Enter your message to the bot: ")
    if message == "quit":
        exit()
    elif message == "save":
        kernel.saveBrain("bot_brain.brn")
    else:
        bot_response = kernel.respond(message)
        # Do something with bot_response

# enter unique session id to load
sessionId = 12345
kernel.respond(raw_input(">>>"), sessionId)

# Get session info as dictionary. Contains the input
# and output history as well as any predicates known
sessionData = kernel.getSessionData(sessionId)

# Each session ID needs to be a unique value
# The predicate name is the name of something/someone
# that the bot knows about in your session with the bot
# The bot might know you as "Billy" and that your "dog" is named "Brandy"
kernel.setPredicate("dog", "Brandy", sessionId)
clients_dogs_name = kernel.getPredicate("dog", sessionId)

kernel.setBotPredicate("hometown", "127.0.0.1")
bot_hometown = kernel.getBotPredicate("hometown")