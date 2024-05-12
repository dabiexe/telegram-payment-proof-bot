import telebot
import random
import time

# Bot token
TOKEN = "YOUR_TOKEN"

# Channel ID
CHANNEL_ID = "@channelusername"

# Initialize bot
bot = telebot.TeleBot(TOKEN)

# Function to generate a random payment proof
def generate_payment_proof():
    user_id = ''.join(random.choices('0123456789', k=10))  # Generate a 10-character user ID
    amount = round(random.uniform(15000, 50000), 2)  # Generate amount between 15,000 and 50,000
    return f"Payment Proof: User {user_id} received {amount} Naira from t.me/novecoincash_bot."

# Function to send payment proof to the channel
def send_payment_proof():
    payment_proof = generate_payment_proof()
    bot.send_message(CHANNEL_ID, payment_proof)

# Main loop to send payment proof every minute
while True:
    send_payment_proof()
    time.sleep(1)  # Wait for 1 minute before sending the next payment proof
