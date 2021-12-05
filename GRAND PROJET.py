import imdb
from tweepy import *
from tkinter import *
import json
import requests
import urllib
from tkinter import *
from textblob import TextBlob
import sys


# Consumer keys and access tokens
consumer_key = 'P8PgmkralDsd7W6zTcky8jPaS'
consumer_secret = 'wsUZTsJYvPdw4nnGEjVPgnVM9QSTzPmaIvdyaLH0RIcJ9SxV7s'
access_token = '1098900260393570305-5zR26Neh7296mWqPXGpMrIH3qixl8n'
access_token_secret = '8xBfMvz7e1sDxdEzZPF8VqAPOzTcwinEcDnDxksMFTanu'
 
#  Processus de connexion à Twitter
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)


def tweet():
    n = input('entrez un tweet : ')
    api.update_status(n) #permet de tweeter depuis l'interface python

def gettweet():
    search = input('entrez votre film : ') #variable 'query' mot clé entré par l'utilisateur
    '''nbretweet = int(input('combien de tweets voulez-vous ? '))''' #nombre de tweets voulus
    tweets = Cursor(api.search, q=search, lang = "en").items(5) #effectue la recherche des tweets
    G = []
    B = []
    N = []
    for tweet in tweets:
        tweet_analysis = TextBlob(tweet.text)
        '''print(tweet_analysis.sentiment)'''
        if (tweet_analysis.sentiment[0]>0):
            print('GGGGGGGGG !')
            print(tweet.text)
            G.append(tweet.text)
        elif (tweet_analysis.sentiment[0]<0):
            print('BBBBBBBBB !')
            print(tweet.text)
            B.append(tweet.text)
        else:
            print('NNNNNNNNN !')
            print(tweet.text)
            N.append(tweet.text)

    G = ''.join(G)
    B = ''.join(B)
    N = ''.join(N)
            
    print('--------')
    print(G)
    print('--------')
    print(B)
    print('--------')
    print(N)
    print('--------')
            

def film_avis():
    ia = imdb.IMDb()
    recherche = e1.get()
    movies = ia.search_movie(recherche) #effectue la recherche de film ou série sur le site spécialisé
    ID = movies[0].movieID #récupère le nom du film officiel (si différent du mot entré)
    
    print(movies[0]) #affiche le nom officiel du film (si différence légère avec le mot-clé entré)

    film = ia.get_movie(ID) #récupère les infos sur le film ou la série
    plot = film['plot']
    plot2 = str(plot[0])
    descri = plot2.split(':')
    description = descri[0]
    
    affich_description = str(description) + '\n' #procédure d'affichage de la description du film en colonne
    F1.set(affich_description)
    
    print(description+"\n\n") #afficher le résumé du film ou de la série

    for i in range(3):
        actor = film['cast'][i]
        
    print(actor," alias ",actor.notes) #afficher le casting du film ou de la série
        
    movies = ia.get_movie(ID, info=['vote details']) #récupère les votes du public à propos du film
    mean = movies.get('arithmetic mean')*2  #récupère les notes
    print("\n")
    print(mean,"/20") #affiche la moyenne d'appréciation du film ou de la série

def killme():
    fenetre.destroy() #ferme la fenêtre

#---------TKINTER----------------------#

fenetre = Tk()
fenetre.config(bg = 'grey30')
fenetre.title('Calc graphique')
'''fenetre.geometry('335x200+600+400')'''
fenetre.geometry('+{}+{}'.format(600,400))
labelfont = ('martina', 12)
labelfont2 = ('impact', 13)


p1 = PanedWindow(fenetre)
p1.config(bg = 'grey30')
p1.grid(row=0)

p2 = PanedWindow(fenetre)
p2.config(bg = 'grey30')
p2.grid(row=1)

p3 = PanedWindow(fenetre)
p3.config(bg = 'grey30')
p3.grid(row=2)

l1 = Label(p1, text="Rechercher un film / une série :", justify = CENTER)
l1.grid(row=0, columnspan=4, sticky = W+E)
l1.config(font = labelfont2, bg = 'grey30', fg ='white')

F1 = StringVar()
l2 = Label(p2, textvariable= F1, justify = CENTER, wraplength= 300)
l2.config(font=labelfont, bg = 'grey30', fg = 'white')           
l2.grid(row=1, column=1)

l3 = Label(p2, text="--------------------------------------")
l3.grid(row=0, columnspan= 4, sticky = W+E)
l3.config(font = labelfont, bg = 'grey30', fg = 'white')

l4 = Label(p1, text=" ")
l4.grid(row=2, columnspan= 4, sticky = W+E)
l4.config(font = labelfont, bg = 'grey30')

e1 = Entry(p1)
e1.config(font= labelfont)
e1.grid(row=1, columnspan=4, sticky= W+E)
e1.focus_force()

b = Button(p1, text= 'Rechercher', command = film_avis)
b.grid(row=3, column=2, sticky= W+E)
b.config(fg = 'green', font=labelfont,bg = 'white', relief= GROOVE)

b2 = Button(p1, text= 'Quitter', command = killme)
b2.grid(row=3, column=0)
b2.config(fg = 'red', font=labelfont, bg = 'white', relief = GROOVE)
