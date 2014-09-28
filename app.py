import os
from flask import Flask, Response, request, url_for
import plivoxml
from utils import joke_from_reddit

# This file will be played when a caller presses 2.
PLIVO_SONG = "https://s3.amazonaws.com/plivocloud/music.mp3"

# This is the message that Plivo reads when the caller dials in
IVR_MESSAGE = "Welcome to the Plivo IVR Demo App. Press 1 to hear a random \
                joke. Press 2 to listen to a song."

# This is the message that Plivo reads when the caller does nothing at all
NO_INPUT_MESSAGE = "Sorry, I didn't catch that. Please hangup and try again \
                    later."

# This is the message that Plivo reads when the caller inputs a wrong number.
WRONG_INPUT_MESSAGE = "Sorry, it's wrong input."

app = Flask(__name__)


@app.route('/response/ivr/', methods=['GET', 'POST'])
def ivr():
    response = plivoxml.Response()
    if request.method == 'GET':
        # GetDigit XML Docs - http://plivo.com/docs/xml/getdigits/
        getdigits_action_url = url_for('ivr', _external=True)
        getDigits = plivoxml.GetDigits(action=getdigits_action_url,
                                       method='POST', timeout=7, numDigits=1,
                                       retries=1)

        getDigits.addSpeak(IVR_MESSAGE)
        response.add(getDigits)
        response.addSpeak(NO_INPUT_MESSAGE)

        return Response(str(response), mimetype='text/xml')

    elif request.method == 'POST':
        digit = request.form.get('Digits')

        if digit == "1":
            # Fetch a random joke using the Reddit API.
            joke = joke_from_reddit()
            response.addSpeak(joke)
        elif digit == "2":
            # Listen to a song
            response.addPlay(PLIVO_SONG)
        else:
            response.addSpeak(WRONG_INPUT_MESSAGE)

        return Response(str(response), mimetype='text/xml')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)
