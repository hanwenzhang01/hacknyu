#import flask from Flask
from flask import Flask, render_template, request, redirect, url_for

import pandas as pd
#above code will import all the packages

app = Flask(__name__)

# creating the database to store the persons answers 
answers_df=pd.DataFrame({'answers': ['', '', '', '']})

#The quiz route accepts POST requests when the user submits an answer to a question, and saves the answer to the database using a Pandas DataFrame.
@app.route('/quiz', methods=['GET', 'POST'])
#variables set to 0
streetwear= 0
casual= 0
formal= 0
edgy= 0

def quiz():
    if request.method == 'POST':
      #saving the user's answers to the db
      user= request.cookies.get('user')
      answers_df.iloc[0:1]=request.form['a1']
      answers_df.iloc[0:2]=request.form['a2']
      answers_df.iloc[0:3]=request.form['a3']
      answers_df.iloc[0:4]=request.form['a4']
      

  if a1=="Bold and confident":
    streetwear+=1
  elif a1=="Easy-going and relaxed":
    casual+=1
  elif a1== "Disciplined and well-groomed":
    formal+=1
  elif a1== "Quiet and reserved":
    edgy+=1
  if a2=="Red":
    streetwear+=1
  elif a2=="Beige":
    casual+=1
  elif a2=="Blue":
    formal+=1
  elif a2=="Black/grey":
    edgy+=1
  if a3=="Varsity Jacket":
    streetwear+=1
  elif a3=="Top/Blouse":
    casual+=1
  elif a3== "Tie/Button-up Shirt":
    formal+=1
  elif a3=="Leather Pants":
    edgy+=1
top_aesthetic= max(streetwear, casual, formal, edgy)

if top_aesthetic== streetwear:
  return ("You seem to like the aesthetic StreetWear!")
elif top_aesthetic == casual:
  return ("You seem to like the aesthetic Casual!")
elif top_aesthetic == formal:
  return ("You seem to like the aesthetic Formal!")
elif top_aesthetic ==edgy:
  return ("You seem to like the aesthetic Edgy!")
  
    
      

#


