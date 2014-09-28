# Phone IVR App

IVR's (interactive voice response), also known as phone menu, is the automated
phone system that interacts with the caller via pre-recorded or dynamic
text-to-speech messages and inputs via the keypad.

You've probably experienced this every time you called your bank or cable
company. The good thing is that IVR systems can handle large call volumes
and reduce costs associated with customer service. Today, we can build the
entire system on the cloud (in any computer language) without relying on
expensive physical infrastructure.

The instructions below will teach you to build your own IVR system that can

- Read a random joke (from Reddit) if '1' is pressed
- Play a song if '2' is pressed
- Say "Sorry, I didn't catch that. Please hangup and try again later" if nothing is pressed.


The app will operate in the following sequence:

1.  The user dials the Phone IVR phone number
2.  The user is prompted with the message "Welcome to the Plivo IVR Demo App. Press 1 to hear a random joke. Press 2 to listen to a song."
3.  During the call, if the user presses '1', then Plivo reads a random joke from Reddit. If the user presses '2', then Plivo plays a song.
4.  If anything else is pressed or if the user does nothing, then Plivo says "Sorry, I didn't catch that. Please hangup and try again later." and hangs up.

Note: we use python in this tutorial, but you can write your apps in any
programming language. Check out Plivo's pre-built [helper libraries](https://plivo.com/docs/helpers/) for details.

## Prerequisites

1. Get a free Plivo trial account
    Sign up for a Free Developer account at [Plivo.com](https://manage.plivo.com/accounts/login/).

2. Get a Heroku account and install the Heroku toolbelt
    Head over to the [Heroku documentation](https://devcenter.heroku.com/articles/quickstart),
    setup an account, and install the [Heroku toolbelt](https://toolbelt.heroku.com/).

    <div class="doc-note">Note: you may also use your own servers, but to simplify things, we will use Heroku.</div>


## Get the application source code

1. Clone the source files from github. Type the below command in your console.

        git clone https://github.com/plivo/phone-ivr-python.git


2. Run the app locally. In your console, navigate to the folder `phone-ivr-python` and run the app,
    by typing the following into your console.

        cd phone-ivr-python
        virtualenv --distribute venv
        source venv/bin/activate
        python app.py


## Understand your XML

You can now access your app XML by typing the following [http://localhost:5000/response/ivr/](http://localhost:5000/response/ivr/) into
your web browser. You should be able to see the following XML.
When an incoming call comes in, the XML is what controls the call and
tells Plivo what to do with that call. The 2 XML elements we used here
are `<GetDigits>` and `<Speak>`. `<GetDigits>` will recognize the digits
pressed during the call as an HTTP request to perform the action specified
in the action url. While `<Speak>` reads the text that's specified.


{% highlight xml %}
<Response>
    <GetDigits action="Server URL to response/ivr" method="POST" numDigits="1" retries="1" timeout="10">
        <Speak>
            Welcome to the Plivo Demo App. Press 1 to hear a random joke. Press 2 to listen to a song.
        </Speak>
    </GetDigits>
    <Speak>
        Sorry, I didn't catch that. Please hangup the call and try again later.
    </Speak>
</Response>
{% endhighlight %}


## Deploy your app on Heroku

Create a Heroku app by typing the following commands in your console.

{% highlight bash %}
heroku create
git push heroku master
heroku scale web=1
{% endhighlight %}


<div class="doc-note">
Take a note of your Heroku app URL. Your output should look like
the following. In this case, our app URL is http://pacific-chamber-7397.herokuapp.com/
</div>


{% highlight bash %}
Creating pacific-chamber-7397... done, stack is cedar
http://pacific-chamber-7397.herokuapp.com/ | git@heroku.com:pacific-chamber-7397.git
Git remote heroku added
{% endhighlight %}


Verify that your app is working by visiting the Heroku app URL above.


## Let Plivo know where your app is

Create a Plivo application and point it to you Plivo phone number by opening
the [Applications Tab](https://manage.plivo.com/app/) in your browser and clicking on the
New Application button to create an application.

Give a name to your application (next to Application Name), lets call it 'Phone IVR'.
Fill in the Answer URL field with your Heroku app URL appended by **/response/ivr/**


For example, our Answer URL will look like this:

    http://pacific-chamber-7397.herokuapp.com/response/ivr/

Choose the GET Answer method and leave all other fields as is. Click on 'Create' when done.

![Plivo App](https://new-ui-cms-plivo.s3.amazonaws.com/uploads/plivo_cloud___create_application.png)


## Assign a Plivo phone number to your app

Go to the [Numbers tab](https://manage.plivo.com/number) and select the phone
number you want to use for this app. Then select the name of your app next to Plivo App.
Click 'Update' when done. If you don't yet have a number, you can purchase one in the [Numbers tab](https://manage.plivo.com/number).

![](https://new-ui-cms-plivo.s3.amazonaws.com/uploads/scree_cap_plivo_cloud_edit_numbers.png)

You're done! Give your Plivo phone number a call and enjoy your Cloud IVR app!


Is anything on this page unclear? [Suggest edits and help us improve our documentation!](https://www.plivo.com/contact/support/)
