from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
  
chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train based on the english corpus
trainer.train("chatterbot.corpus.english")

# Train based on english greetings corpus
trainer.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
trainer.train("chatterbot.corpus.english.conversations")

# Get a response to an input statement
while True:
	str = input()
	response = chatbot.get_response(str)
	print(response)
