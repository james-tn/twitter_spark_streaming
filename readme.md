## This project helps you setup a cluster spark environment, develop a python application to connect to twitter and use spark streaming to analyze real time data streaming.

The spark_cluster_setup is the guideline to setup spark cluster.

On the application side, I have created two main python programs
1. twitter_app.py is the program that reads data from twitter continuously and write to a socket at port 5555
2. spark_main.py is the main spark program where I implemented logics to read stream data from socket, transform, sum data and compute statistics in using spark streaming.
In the main spark program, I extensively use spark transformation technique on DStream and RDD object like map, reduce, transform to achieve the needed summary data.
There’re two main windows: 
    - Short (current windows) that capture data over a windows of 120 seconds, then it moves 10 seconds continuously. The purpose is to show very current trends of topics and mentions
    - Long windows that that capture data over a windows of 30 minutes seconds, then it moves 10 seconds continuously so that data is sampled every 10 seconds.
The sampling frequency is short 10 seconds for both long and short windows so that we can see data in near real time.
These two windows are processed concurrently.


How to run the program


You will need 2 windows terminal, one for each program.
for terminal windows 1

step 1: run twitter app with: python lab9/twitter_app.py

for terminal windows 2

step 2: python lab9/spark_main.py 6 spark://spark1:7077


(6 is the parameter for the number of topics that are most common, spark://spark1:7077 is the parameter for the spark cluster)

Note: the twitter_app.py after being listened to by trigging the spark_main.py will start outputting. For some reason, if the spark_main.py stops, the socket is full because data is not consumed so it will cause error in twitter_app.py. Simply restart twitter_app.py and then restart spark_main.py. Any time you need to rerun the applications, you need to restart twitter_app.py






Sample output from the program

Top 8 common topics over the last 30 minutes

**********************************************
8 hot current topics right over the last 5 minutes
----------------------------------------------
----------------------------------------------
1 .Topic: Trump ,Number of tweets: 13
Tweeting people:  Margaret Stockbridge, Bob Griffiths, Tamara Cofman Wittes, Collin, Pamela Resister, Geo45, Michael, Paige Lovelace, Basil Shepard, Dwayne Rodgers, Vince Pazienza, Military Stuff, David Kilby,
Mentioned people:  Peter Boykin, Roy Zimmerman, Bill D, Kyodo News - English, Rob, Joyce Karam, Kevin W., Sexy Liberal, President Trump,

2 .Topic: MAGA ,Number of tweets: 11
Tweeting people:  Margaret Stockbridge, 🇺🇸GENESIS🇺🇸, Marlene Malik, 👑Mikayla, Deborah Gerhardt, ((Venus Fly Trump)), Paige Lovelace, 🇺🇸Kaby🇺🇸, Xipe, Lord X, Jabreakit Jabawtit,
Mentioned people:  🇺🇸GENESIS🇺🇸, Peter Boykin, Scott Barbour, Eric Bolling, Jim Mad Dog Maddox, Rob, Eric Trump, J_Patriot_Train, Donald Trump Jr., 🐸Deplorablemike🐸, 👑King Robbo👑, Donald J. Trump, 🅾️🇭️🇴️🇺️🇷️❗, R. Saddler 📎🗽,

3 .Topic: TexasChurchMassacre ,Number of tweets: 9
Tweeting people:  Mary, PAS, SidneyB, Brion Adair, Charles Bunten #MAGA, Maureen 🇺🇸🇺🇸, Camilla Bijoux, Charlotte Bland👌🐷, a deadbeat cousin,
Mentioned people:  JustJanis, No✝️ Eliza🅱️eth, The Daily Edge, Alex Jones, Joey Mannarino, PROUD RESISTER 👊, Donald J. Trump, Storm2017 🕊, Senator Ted Cruz, Philip Schuyler,

4 .Topic: ARMYxAMAs ,Number of tweets: 8
Tweeting people:  DNA🌺Best of me🌺, BIGHIT-O-PHOBIA, VIOLET💜SUBLI, Never mind 😊, Vaz | PlsRT&Fav📌, 조한담, Bails, BlueW,
Mentioned people:  방탄소년단, ᗷTᔕ . ᗷᗩᗷY . GIᖇᒪ, AMAs,

5 .Topic: AMAs ,Number of tweets: 8
Tweeting people:  DNA🌺Best of me🌺, VIOLET💜SUBLI, Omer Oylamada, Vaz | PlsRT&Fav📌, 조한담, Bails, Never mind 😊, BlueW,
Mentioned people:  방탄소년단, AMAs,

6 .Topic: BREAKING ,Number of tweets: 8
Tweeting people:  Resist & Persist, Wall of Worry!, HEY MO!, Jo, ToddHellsKitch, M K, David Kilby, VRPitts,
Mentioned people:  The Hill, Scott Dworkin, Bill D,

7 .Topic: SutherlandSprings ,Number of tweets: 5
Tweeting people:  Don Ukens, D Sims, Linda Barrientos, Sam J DeMeo, Puffington the 12th,
Mentioned people:  Chelsea Handler, #ThePersistence, Greg Popovich, Dana Loesch,

8 .Topic: Texas ,Number of tweets: 3
Tweeting people:  Don Ukens, Libertarian896, Sam J DeMeo,
Mentioned people:  #ThePersistence, Alex Jones,
**********************************************          