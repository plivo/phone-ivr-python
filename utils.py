import random
import requests
import json

# Enter your own joke handy in case reddit goes down
PLIVO_JOKE = "What do you get when you cross a snowman with a vampire? \
            A frostbite"


def joke_from_reddit():
    random_joke = random.randint(0, 20)
    try:
        # Fetch a list of jokes from reddit
        data = requests.get("http://www.reddit.com/r/cleanjokes.json",
                            timeout=4)
        data = json.loads(data.content)
        content = data['data']['children']

        # Select a random joke from the list
        joke = content[random_joke]
        joke_title = joke['data']['title']
        joke_selftext = joke['data']['selftext']

        # Return the title and joke
        return "%s %s" % (joke_title, joke_selftext)
    except Exception:
        return PLIVO_JOKE


if __name__ == "__main__":
    print joke_from_reddit()
