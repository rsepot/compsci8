import webbrowser as wb
import pyautogui as pg
import time as t

points = 0


show = pg.prompt ("what is your favorite show? ")
if show == "hannah montana":
    wb.open("https://www.youtube.com/watch?v=nDMIuuO_PQo")
    pg.alert ("that is such a fantastic show!")
    points += 300
elif show == "icarly":
    wb.open("https://www.youtube.com/watch?v=Zuy8unCFDcs")
    pg.alert ("i love sam, i always could relate to her ya know wanting to go to prison and stuff"
           )
    points += 125
elif show == "the office":
    wb.open("https://www.youtube.com/watch?v=uyIVAm9PVrI")
    pg.alert ("ooh that show makes me dizzy but i guess it's good")
    points -= 100
elif show == "hawaii 5-0":
    wb.open ("https://www.youtube.com/watch?v=hwhvByj8YG8")
    pg.alert ("ooh what an action bomber")
    points += 125
elif show == "friends":
    wb.open("https://www.youtube.com/watch?v=8mP5xOg7ijs")
    pg.alert ("THAT IS MY FAVORITE SHOW!")
    points += 125
elif show == "care bears":
    wb.open ("https://www.youtube.com/watch?v=y2WTARyipwU")
    pg.alert ("have you ever seen the movie? it's the best")
    points += 125
elif show == "my little pony":
    wb.open ("https://www.youtube.com/watch?v=ZcBNxuKZyN4")
    pg.alert ("i love applejack!")
    points += 125
else:
        pg.alert ("you're favorite show is " + show)
        points -= 50


movie = pg.prompt ("what is your favorite movie? ")
if movie == "hannah montana the movie":
    wb.open("https://www.youtube.com/watch?v=DrtTiBKpjD8")
    pg.alert ("that is such a fantastic movie!")
    points += 300
elif movie == "high school usa":
    wb.open ("https://www.youtube.com/watch?v=sQcjTNl7NiQ")
    pg.alert ("thats a very good classic")
    points += 125
elif movie == "annie":
    wb.open ("https://www.youtube.com/watch?v=-0bOH8ABpco")
    pg.alert ("ITS A HARD KNOCK LIFE LALALALALLA!")
    points += 125
elif movie == "star wars":
    wb.open ("https://www.youtube.com/watch?v=ziHv3zZrSZI")
    pg.alert ("luke, i am your father")
    points += 125
elif movie == "the last song":
    wb.open ("https://www.youtube.com/watch?v=vZH0Nf4KLBo")
    pg.alert ("THAT IS MY FAVORITE MOVIE! i cry every time...")
    points += 200
elif movie == "care bears the movie":
    wb.open ("https://www.youtube.com/watch?v=MGn_HHOfBRw")
    pg.alert ("oh that one was too scary for me")
    points += 125
elif movie == "my little pony":
    wb.open ("https://www.youtube.com/watch?v=hAXX_bPxIzY")
    pg.alert ("i love applejack!")
    points += 125
else:
        pg.alert ("your favorite movie is " + movie)
        points -= 50


candy = pg.prompt ("what is your favorite candy? ")
if candy == "reeses":
    pg.alert ("yummm")
    points += 300
elif candy == "kit kat":
    pg.alert ("i love the commercial for kit kats")
    points += 125
elif candy == "snickers":
    pg.alert ("not my favorite but not bad")
    points += 125
elif candy == "milky way":
    pg.alert ("oh i like those a lot")
    points += 125
elif candy == "butterfinger":
    pg.alert ("i have never had one of those")
    points += 125
elif candy == "twizlers":
    pg.alert ("those are my favorite to have at the movies")
    points += 125
elif candy == "m&ms":
    pg.alert ("have you tried the new caramels?")
    points += 125
else:
        pg.alert ("your favorite candy is " + candy)
        points -= 50


game = pg.prompt ("what is your favorite game? ")
if game == "fortnite":
    pg.alert ("bush hunting is key")
    points += 300
elif game == "black ops 4":
    pg.alert ("pretty good")
    points += 125
elif game == "flappy bird":
    pg.alert ("my whole childhood!")
    points += 125
elif game == "mario kart":
    pg.alert ("TOAD!!")
    points += 125
elif game == "madden 19":
    pg.alert ("you are probably really bad.")
    points += 100
elif game == "just dance":
    pg.alert ("omg lolzz")
    points -= 10
else:
        pg.alert ("your favorite candy is " + game)
        points -= 50


song = pg.prompt ("what is your favorite song? ")
if song == "sicko mode":
    wb.open ("https://www.youtube.com/watch?v=S_tBc20Ivuo")
    pg.alert ("good song")
    points += 300
elif song == "sweet but phsyco":
    wb.open ("https://www.youtube.com/watch?v=Ot_sMK4rVqs")
    pg.alert ("relatable")
    points += 125
elif song == "happier":
    wb.open ("https://www.youtube.com/watch?v=m7Bc3pLyij0")
    pg.alert ("the music video is so depressing!!")
    points += 125
elif song == "humble":
    wb.open ("https://www.youtube.com/watch?v=5ZYgIrqELFw")
    pg.alert ("oof that song is old")
    points += 125
elif song == "classic man":
    wb.open ("https://www.youtube.com/watch?v=MM19LvUDhEY")
    pg.alert ("love that one")
    points += 125
elif song == "mr. brightside":
    pg.alert ("all time favorite")
    wb.open ("https://www.youtube.com/watch?v=gGdGFtwCNBE")
    points += 500
elif song == "all star":
    wb.open ("https://www.youtube.com/watch?v=5ZYgIrqELFw")
    pg.alert ("lalallala")
    points += 250

else:
        pg.alert ("you have bad taste in music")
        points -= 100

pg.alert ("you scored " + str(points))
