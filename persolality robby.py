import webbrowser as wb
import pyautogui as pg
import time as t
points = 0
show = pg.prompt("what is your favorite show? ")

if show == "stranger things":
    pg.alert("we can not be friends")
    points += 2
    wb.open("https://www.google.com/search?q=Gaten+Matarazzo&rlz=1C1GCEA_enUS752US752&stick=H4sIAAAAAAAAAONgFuLWz9U3MDQ2zMkzr1SCcAyMLU2Ky7TEspOt9EvKgCi-oCg_vSgx1yo5sbjkEWMwt8DLH_eEpbwmrTl5jdGFC4dCIS0uNte8ksySSiEFLn4pZIs0GKR4uZAFeAAKnJppigAAAA&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjrgN3n443eAhVlmuAKHfAxAMsQ_AUIDigB&biw=950&bih=602#imgrc=S7VtXGV7zLuOKM:")
    t.sleep(5)
elif show == "whick tunna":
    pg.alert("I love catipilers")
    points += 2
    wb.open("https://www.youtube.com/watch?v=tlBUpONWANU")
    t.sleep(5)
elif show == "pepa pig":
    pg.alert("I love you")
    points += 4
    wb.open("https://www.youtube.com/watch?v=hiEdMIAy4q4")
    t.sleep(5)
elif show == "kawow":
    pg.alert ("I love a kavoo kid")
    points += 4000000000
    wb.open("https://www.youtube.com/watch?v=cRpdIrq7Rbo")
    t.sleep(5)
elif show == "Balistic squid":
    pg.alert("cool")
    points += 10
    wb.open("https://www.youtube.com/watch?v=lWUmb-7dUOY")
    t.sleep(5)
elif show == "kittens":
    pg.alert("kitten")
    wb.open("https://www.youtube.com/watch?v=kMkptSACs9Y")
    t.sleep(5)
else:
    pg.alert("You favorite show is " + show)
    
food = pg.prompt("what is your favorite food")

if food == "sharke fin soup":
    pg.alert("wow")
    points += 1
    wb.open("https://www.google.com/search?q=shark+fin+soup&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjwtNKG543eAhWOZd8KHY-jDu4Q_AUIDigB&biw=1821&bih=834#imgrc=ByjoOqnSTYEKQM:")
elif food == "taco":
    pg.alert("wow")
    points += 500000000000000000000000
    wb.open("https://www.google.com/search?q=taco+party&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiCvJ-m543eAhWFMd8KHWFtDJwQ_AUIDigB&biw=1821&bih=834&dpr=0.75#imgrc=gtem5hIKarBdiM:")
elif food == "rice gum":
    pg.alert ("hello rice gum")
    points += 500000000000000000000000000
    wb.open("https://www.youtube.com/watch?v=K_EsxukdNXM")
elif food =="poprocks":
    pg.alert ("wow")
    points += 100
    wb.open("https://www.youtube.com/watch?v=5K7QlFHxV-s")
elif food== "chicken loman":
    pg.alert("wow")
    wb.open ("https://www.youtube.com/watch?v=M6EamT2VYpQ")
elif food== "cricket":
    pg.alert("wow")
    wb.open ("https://www.youtube.com/watch?v=U9c_KttvQPU")

else:
    pg.alert(" you must be cool")

name = pg.prompt("what is your name")
if name == " string bean":
    pg.alert ("hello mr string bean")
    wb.open("https://www.youtube.com/watch?v=5K7QlFHxV-s")

elif name==" robby" and show== "pepa pig":
    pg.alert ("that is cool")
    points += 2000000000
    wb.open("https://www.youtube.com/watch?v=5K7QlFHxV-s")
    t.sleep(5)
elif name == "mr kim":
    pg.alert("hello mr kim")
    points += 1203887
    wb.open("https://www.youtube.com/watch?v=zrAj9h8HbmY")
    t.sleep(5)
elif name == "fin":
    pg.alert (" hello shark fin soup")
    points += 10
    wb.open("https://www.youtube.com/watch?v=K_EsxukdNXM")
    t.sleep(5)
elif name == "peter":
    pg.alert (" hello mr peter")
    points += 12000046674663746738473874839478347838473847838473847378473483748374837383747383
    wb.open("https://www.youtube.com/watch?v=K_EsxukdNXM")
    t.sleep(5)
elif name == "mr cow":
    pg.alert("hello mr cow")
    points += 1203887
    wb.open("https://www.google.com/search?q=cow&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiOif7rtJ_eAhWlUt8KHW8cDfUQ_AUIDigB&biw=1134&bih=624#imgrc=SpeA_QSxwJ4PRM:")
    t.sleep(5)
else:
    pg.alert("your're name is " + name)
game = pg.prompt("what is your favorite game? ")

if game == "fortnite":
    pg.alert("we can not be friends")
    points += 2
    wb.open("https://www.google.com/search?q=ninja&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiDvPi5sp_eAhWPmuAKHX4sCrwQ_AUIDygC&biw=1134&bih=624#imgrc=Bn4ylr4Y0JdbZM:")

elif game == "stranger things":
    pg.alert("we can not be friends")
    points += 2
    wb.open("https://www.google.com/search?q=Gaten+Matarazzo&rlz=1C1GCEA_enUS752US752&stick=H4sIAAAAAAAAAONgFuLWz9U3MDQ2zMkzr1SCcAyMLU2Ky7TEspOt9EvKgCi-oCg_vSgx1yo5sbjkEWMwt8DLH_eEpbwmrTl5jdGFC4dCIS0uNte8ksySSiEFLn4pZIs0GKR4uZAFeAAKnJppigAAAA&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjrgN3n443eAhVlmuAKHfAxAMsQ_AUIDigB&biw=950&bih=602#imgrc=S7VtXGV7zLuOKM:")
    t.sleep(5)
elif game == "pubg":
    pg.alert("I love catipilers")
    points += 2
    wb.open("https://www.youtube.com/watch?v=tlBUpONWANU")
    t.sleep(5)
elif game == "rider":
    pg.alert("I love you")
    points += 4
    wb.open("https://www.youtube.com/watch?v=hiEdMIAy4q4")
    t.sleep(5)
elif game == "kawow":
    pg.alert ("I love a kavoo kid")
    points += 4000000000
    wb.open("https://www.youtube.com/watch?v=cRpdIrq7Rbo")
    t.sleep(5)
elif game == "Balistic squid":
    pg.alert("cool")
    points += 10
    wb.open("https://www.youtube.com/watch?v=lWUmb-7dUOY")
    t.sleep(5)
elif game == "kittens":
    pg.alert("kitten")
    wb.open("https://www.youtube.com/watch?v=kMkptSACs9Y")
    t.sleep(5)
else:
    pg.alert("You favorite game is " + game)

sport = pg.prompt("what is your favorite sport?")

if sport == "football":
    pg.alert("we can not be friends")
    points += 2
    wb.open("https://www.google.com/search?q=benjamin+franklin&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwinkd20tJ_eAhWQm-AKHW1AALoQ_AUIDigB&biw=1134&bih=624#imgrc=YFh1MOzc3wAntM:")
    t.sleep(5)
elif show == "whick tunna":
    pg.alert("I love catipilers")
    points += 2
    wb.open("https://www.google.com/search?q=wicked+tuna&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjZitj6v_feAhXJhOAKHdv_ASAQ_AUIECgD&biw=908&bih=821#imgrc=C80wKoS9LkKQGM:")
    t.sleep(5)
elif show == "crokay":
    pg.alert("I love you")
    points += 4
    wb.open("https://www.youtube.com/watch?v=bUA4Z_Fe_nM")
    t.sleep(5)
elif show == "kawow":
    pg.alert ("I love a kavoo kid")
    points += 4000000000
    wb.open("https://www.youtube.com/watch?v=yfjnahzAPSc")
    t.sleep(5)
elif show == "socceer":
    pg.alert("cool")
    points += 10
    wb.open("https://www.youtube.com/watch?v=UCM4b61nZpM")
    t.sleep(5)
elif show == "kittens":
    pg.alert("kitten")
    wb.open("https://www.youtube.com/watch?v=kMkptSACs9Y")
    t.sleep(5)
else:
    pg.alert("You favorite sport is " + sport)
pg.alert(points)

