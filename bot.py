from telegram.ext import Updater, CommandHandler
import logging
import os
from openai import OpenAI
from PIL import Image
import requests
from io import BytesIO

# Initialize logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def faregpt(update, context):
    update.message.reply_text('Generating your image, please wait...')

    # Generate an image using DALL-E 3
    response = client.images.generate(
        model="dall-e-3",
        prompt="all sorts of diverse aliens playing bright, fun and colorful casino games where all the casino chips are purple, make sure to use a fun pixel style but not too pixelly",  # Example prompt, replace with user input or specific prompt
        size="1024x1024",
        quality="standard",
        n=1,
    )

    # Extract the URL of the generated image
    image_url = response.data[0].url

    # Download the image from the URL
    response = requests.get(image_url)
    generated_image = Image.open(BytesIO(response.content))

    # Apply the overlay mask
    final_image_io = apply_overlay(generated_image, 'smalltwitterloverlay.png')

    # Send the final image back to the user
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=final_image_io)

def apply_overlay(base_image, overlay_image_path):
    # Load the overlay image
    overlay_image = Image.open(overlay_image_path).resize(base_image.size)

    # Create a new BytesIO stream for the output image
    final_image_io = BytesIO()

    # Apply the overlay
    base_image.paste(overlay_image, (0, 0), overlay_image)
    base_image.save(final_image_io, format='PNG')
    final_image_io.seek(0)

    return final_image_io

def main():
    # Telegram Bot Token
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("faregpt", faregpt))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
