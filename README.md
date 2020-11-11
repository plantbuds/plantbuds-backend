# Welcome to the backend!
This is the part of the code that does the nitty gritty stuff like messing with the database, authenticating 
users, and other fun things.

The backend of our app uses [Django](https://docs.djangoproject.com/en/3.1/intro/overview/), 
the [Django Rest Framework](https://www.django-rest-framework.org/#example) for our API, and 
[PostgreSQL](https://www.postgresql.org/about/) for our database. 
I highly recommend reading at least the front page/overview for these things to get an understanding of 
what each of them does or you might be struggling a lil.

> Hey shauna what the fuck is an API?

I'm glad you asked!! Please do a bit of research to understand what APIs do 
([this is a decent explanation](https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/)),
they're super important for SWE in general (I promise) and basically every web app you'll develop ever.

## Local dev setup
*Note: This setup uses PyCharm for development because it does a lot of things automatically and I personally use it,
but it should be possible to do all of this with any IDE. I'm pretty sure you just have to figure out how to set up a 
python virtual environment*
1. Clone the repo via the command line  
```git clone https://github.com/plantbuds/plantbuds-backend.git```
2. Get [PyCharm](https://www.jetbrains.com/pycharm/download/) and go File -> Open -> plantbuds-backend 
(wherever you put it on your computer)  
3. Follow the instructions 
   [here](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env)
   to make a virtual environment (you don't need to check "inherit global site-packages"). Hit apply and click ok,
   if successful you should have a new directory in your root project folder called `venv`
3. Open the PyCharm terminal by `ALT+F12`-ing or clicking "Terminal" in the bottom bar (next to Python Console)
4. In the terminal, run `pip install -r requirements.txt`
5. Create a file in your root project directory called `.env` and ask Shauna for the contents of that file (it's
   secret stuff)
6. Click the green play button at the top right to start the Django server, or hit `SHIFT-F10`
7. A couple things will print out and there should be a line that says something like  
`Starting development server at http://127.0.0.1:8000/`, go to that URL in your browser (there will be a 404 error but 
    don't worry about that)
8. Head over to `[server]:8000/admin` and login with the admin account, the credentials are `RDS_USER` and `RDS_PASS` 
    in the `.env` file you got from Shauna
9. Congrats you have the backend server running on your computer!! The admin page is where you can look around the
    database and stuff! Very cool

If you get stuck anywhere just PM Shauna :)

## API endpoints (in progress)
`[server]:8000/api` takes you to the REST API root, which has all of the current API endpoints that are possible to hit.
These are connected to the database too, click around and check it out. For example, if you go to 
`[server]:8000/api/users`,
you should see the admin user! woo!

## Connecting to the frontend
(TBD)
