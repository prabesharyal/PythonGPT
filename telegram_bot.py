# Set up the Telegram bot

# Set up the OpenAI API
import telegram
import openai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters , CallbackContext

#This will load API keys from '.env' file
from dotenv import load_dotenv
load_dotenv()


# Set up the Telegram bot
bot = telegram.Bot(os.getenv('TG_BOT_TOKEN'))

# Set up the OpenAI API
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define a function to generate responses using ChatGPT
def generate_response(text):
    response = openai.Completion.create(
        engine='davinci',
        prompt=text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm your personal AI assistant. How can I help you today?")

def echo(update, context):
    user_input = update.message.text
    response = "I'm sorry, I didn't understand. Can you please rephrase?"
    # Use OpenAI API to generate response
    response = generate_response(user_input)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def main():
    # Replace 'YOUR_TOKEN_HERE' with your bot token
    updater = Updater('6088146021:AAHzfrDc53rGBsc9HOzNP0gxNUvzTmdSzEM', use_context=True)
    dispatcher = updater.dispatcher

    # Add handlers for start command and echo message
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
