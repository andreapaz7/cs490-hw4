import flask 
import os
import random

app = flask.Flask(__name__)


@app.route('/') # Python decorator 
def index(): 
    fav_artists = "tennis", "ftp", "strokes", "metric", "ariana grande"
    images = "/static/tennis.jpg", "/static/ftp.jpg", "/static/strokes.jpg", "/static/metric.jpg", "/static/grande.png"
    return flask.render_template(
       "index.html",
      # a1 = fav_artists[0],
      # a2 = fav_artists[1],
      # a3 = fav_artists[2]
      len = len(fav_artists),
      fav_artists = fav_artists,
      len2 = len(images),
      images = images
   )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
    #debug=True //TAKE OUT BEFORE DEPLOYING TO HEROKU
    
    )
