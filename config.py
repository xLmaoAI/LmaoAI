import openai
import tweepy
import time
import random
from config import config

# Initialize Twitter API
client = tweepy.Client(
    bearer_token=config['bearer_token'],
    consumer_key=config['consumer_key'],
    consumer_secret=config['consumer_secret'],
    access_token=config['access_token'],
    access_token_secret=config['access_token_secret']
)

def generate_tweet():
    """Generates a tweet using OpenAI GPT-4"""
    prompt = "Generate a viral memecoin tweet in a fun, engaging, and degen-friendly style."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()

def post_tweet():
    """Fetches a tweet from GPT and posts it to Twitter."""
    try:
        tweet_text = generate_tweet()
        client.create_tweet(text=tweet_text)
        print(f"Tweet posted: {tweet_text}")
    except Exception as e:
        print(f"Error posting tweet: {e}")

if __name__ == "__main__":
    while True:
        post_tweet()
        sleep_time = random.randint(10800, 21600)  # Between 3 to 6 hours
        print(f"Sleeping for {sleep_time / 3600:.1f} hours...")
        time.sleep(sleep_time)
