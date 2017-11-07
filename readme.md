#This project helps you setup a cluster spark environment, develop a python application to connect to twitter and use spark streaming to analyze real time data streaming.

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
----------------------------------------------
----------------------------------------------
1 . Topic: Trump ,Number of tweets: 47
Tweeting people:  maribeth munoz, Bram Michaelson, Abigail71Kirkw1, Юля Лебедева, Pamela Resister, Tina Jackson, Sea Foam, [GEOPOLITICS], Caran, Vince Pazienza, Mel@808, David Kilby, Juanita Phillips, Lowell, trish, sumu23150839, Geo45, Bob Griffiths, Military Stuff, Paige Lovelace, Collin, Jamie Walker, T Scott, Margaret Stockbridge, Linda Shamar, Phil De Carolis, Dwayne Rodgers, Mark Lowen, DAII, ADRIAN, Michael, Grassland Designs, Bonel Flamel, Basil Shepard, Stacy for Integrity, Rhea Crosley, jodie, Donna11Gran1, pattyblu#resistance, Covfefe Legal Advice, ElecVets, Tamara Cofman Wittes, 上海交通大学, CAPEurope, LoopyCoopy, Alien Guru Deva,
Mentioned people:  Leader McConnell, China Xinhua News, Erin'sTrump®, The Diplomat, David Beard, Joyce Karam, The Last Word, Peter Boykin, Bill D, Hosu Lee, 台灣蘋果日報 Taiwan News, Donald J. Trump, Bette Midler, Fox News, President Trump, NorthKorea Newz, Roy Zimmerman, Jim O'Hare, Kyodo News - English, Kevin W., Chris Hayes, Paul Ryan, D.C. Made Simple, Stacy for Integrity, Sexy Liberal, The Daily Caller, Rob, goktay koraltan, CGTN, CAPEurope, 云南师范大学 1805843363,
2 . Topic: AMAs ,Number of tweets: 42
Tweeting people:  💜Ngọc An💜🐥🐰🐯, Omer Oylamada, DNA🌺Best of me🌺, jhope mixtape🔥, kenya, ‘PICKXJM’, Bails, Adi, 🍁김수진🍁, yems, Vaz | PlsRT&Fav📌, STREAM AND VOTE DNA, mari 🌷| CLAP, Shii ♥ Chii, Rihanna Support TR, Never mind 😊, 올콘 뛰는 브랜들리, Spring Angel, debbie, Stand by BTS💞, Stephanie Jimenez, Dany Drew, VIOLET💜SUBLI, aurie, 🌠스타태🌠, Team Help Rihanna, 나나, 조한담, BlueW, TAEGA🐰, 강수정, 🔍aRMy 🔎, #방탄소년단_Technology, #MTVHOTTESTRihanna, SJ, The Seven Musketeers, 남태석namtaeseok, ʚTaehyungieɞ 🎶🎷🐯, Hyeyung S., HoneySunshine_JK, Chloe #LoveMyself,
Mentioned people:  방탄소년단, Westwood One, AMAs, Ralphie Aversa, Adam Bomb™, BTS_official,
3 . Topic: ARMYxAMAs ,Number of tweets: 39
Tweeting people:  💜Ngọc An💜🐥🐰🐯, Never mind 😊, jhope mixtape🔥, ‘PICKXJM’, Bails, Adi, 🍁김수진🍁, yems, Vaz | PlsRT&Fav📌, STREAM AND VOTE DNA, 🐥🐯회색휴지🐍🐰, mari 🌷| CLAP, Shii ♥ Chii, 올콘 뛰는 브랜들리, Spring Angel, debbie, Stand by BTS💞, Stephanie Jimenez, Dany Drew, VIOLET💜SUBLI, aurie, 🌠스타태🌠, 나나, DNA🌺Best of me🌺, BlueW, 고엽, TAEGA🐰, 강수정, BIGHIT-O-PHOBIA, 🔍aRMy 🔎, #방탄소년단_Technology, SJ, The Seven Musketeers, 조한담, 남태석namtaeseok, ʚTaehyungieɞ 🎶🎷🐯, Hyeyung S., HoneySunshine_JK, Chloe #LoveMyself,
Mentioned people:  방탄소년단, ᗷTᔕ . ᗷᗩᗷY . GIᖇᒪ, 감자밭할매, AMAs,
4 . Topic: MAGA ,Number of tweets: 36
Tweeting people:  G_A_Make_My_Day, Jabreakit Jabawtit, Jason Todd, Linda Meiseles, Michael 7546, Xipe, Paige Lovelace, mousseman, Juanita Phillips, Marlene Malik, Mrs.Sarah Gibson, Patriot Juliet🇺🇸, Carol Langendoerfer, whoa insanity, Edie, 🇺🇸IamMrCOVFEFE☕️, Lord X, Margaret Stockbridge, Lynn, Ari Meermans, DAII, Deborah Gerhardt, ((Venus Fly Trump)), Grassland Designs, Patti Woolley, Lisa, 👑Mikayla, jodie, Jorge Enrique, Dougie 2-Scoops, Jerry Sherman, 🇺🇸GENESIS🇺🇸, 🐸Deplorablemike🐸, Treason=45 & GOP, 🇺🇸Kaby🇺🇸, Riley Green,
Mentioned people:  KNN, Erin'sTrump®, Patriot Juliet🇺🇸, Fredon Moniteau, ⚔Hell on Wheels🔴⚪🔵, J_Patriot_Train, Scott Barbour, 🇺🇸Terre 🇺🇸, John Oberlin, 👑King Robbo👑, Donald J. Trump, 🇺🇸IamMrCOVFEFE☕️, AMERICA❤️HAS💙SPOKEN, R. Saddler 📎🗽, President Trump, Dinesh D'Souza, Eric Trump, Stephen Weever, DEPLORABLE MICHELLE, Peter Boykin, Steve Lookner, Shirtless Pundit, GOP, The Daily Caller, 🇺🇸GENESIS🇺🇸, Eric Bolling, Rep. Dave Brat, Lou Dobbs, Jim Mad Dog Maddox, Rob, Donald Trump Jr., 🐸Deplorablemike🐸, Kevin Cavanaugh (R), 🅾️🇭️🇴️🇺️🇷️❗,
5 . Topic: TexasChurchMassacre ,Number of tweets: 32
Tweeting people:  PAS, Christina Serafin, Linda Hann, deborah pachilis, ✝JESUSHasLIFE4EVER🚩, Maureen 🇺🇸🇺🇸, Mary, Dawn Arteaga, B. Goode, Wolf Tracks, Jeannie, Brandon., Vanessa Goodman, sandra Hare, SidneyB, markdade, les, Camilla Bijoux, Mary Ellen Hettinger, Cold without the Sun, Chava here, Maggie, Coach Pace, Michael Coates, Brion Adair, Charles Bunten #MAGA, Charlotte Bland👌🐷, patrice walker, Pink Freud, Michael Miller, a deadbeat cousin,
Mentioned people:  The Daily Edge, Rose 🌹Taylor, Moms Demand Action, Storm2017 🕊, Senator Ted Cruz, HumanRightsCampaign, ABC13 Houston, Jack Polakoff, Donald J. Trump, President Trump, JustJanis, CC, PROUD RESISTER 👊, PinkAboutIt 🇺🇸, Breaking911, McSpocky™ 👽🖖, infowars, Philip Schuyler, Michael Coates, Shomari Stone, No✝️ Eliza🅱️eth, Alex Jones, Joey Mannarino, Queenie Ω Goldstein, Ed Krassenstein,
6 . Topic: SutherlandSprings ,Number of tweets: 30
Tweeting people:  Nay🇺🇸, Debra, Paula, Justin Iosco, Linda Barrientos, MadisonPeale, Mark Tanner, Puffington the 12th, The Patriot Spartan, Rob N., Mary Alice Loedding, SMichie24ever, Fredra, Brandon Boyett, rebecca flores, Sam J DeMeo, Jake Linwood, D Sims, Gwen Croft, Jim Dorman, Cathy, scott morrisette, WashingtonsImmortals, Gerry Callahan, Patrick Romkema, Buzzard Skedeebeck, Freedom Forever, Don Ukens, 🍁RedRiverGirl 🍁, Reid Cross,
Mentioned people:  Andrew Stroehlein, Dana Loesch, Chelsea Handler, #ThePersistence, Francis Maxwell, The Baxter Bean, Greg Popovich, Chet Cannon, Greg Abbott, Denizcan James,
7 . Topic: BREAKING ,Number of tweets: 22
Tweeting people:  Resist & Persist, HEY MO!, Rtwingsmackdown, 🙆‍♂️, Larry McIntosh, @ Kevia04, M K, Tina Pace, VRPitts, Snow Flake, Wall of Worry!, ToddHellsKitch, Josh Jagdfeld, Jo, David Kilby, bunny, WE ARE THE MAJORITY, Tracy MSY, Gerda E Breitwieser, mom, Demo2018, Leslie Purl,
Mentioned people:  The Hill, Scott Dworkin, Bill D,
8 . Topic: Hannity ,Number of tweets: 15
Tweeting people:  DEPLORABLE4djt2016, #MAGA, Diane Elizabeth 🐾💜, Kathy Nassios, DANIEL GLENN, (((Art))), William, dwb, LCB, Charlote, Reginald Denny, Mariz, Lord Fauntleroy, Speech Defender, charlotte grey,
Mentioned people:  Sara A. Carter, Sean Hannity, Gregg Jarrett, David Weissman,
**********************************************                                  

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