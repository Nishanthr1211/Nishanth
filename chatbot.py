from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('MyChatBot')

# Train the chatbot using the ChatterBot corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

# Start the conversation
while True:
    user_input = input('You: ')
    response = chatbot.get_response(user_input)
    print('Bot: ', response)
