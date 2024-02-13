import requests
from bs4 import BeautifulSoup
import pandas as pd
URL='https://www.imdb.com/chart/top/' 
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent": USER_AGENT} # adding the user agent
resp = requests.get(URL, headers=headers)
soup = BeautifulSoup(resp.content, "html.parser") # use this if you want to scrape the site
title = soup.find_all('div',class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-14dd939d-7 fjdYTb cli-title')
movies = []
for movie in title:
    movies.append(movie.get_text().strip())
print(movies)

ratings = soup.find_all('span' , class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating' )
rates = []
for rate in ratings:
    rates.append(rate.get_text().strip())
print(len(rates))
print(len(movies))

data = pd.DataFrame()
data['Movie Names']=movies
data['Ratings'] = rates
print(data.head())
data.to_csv('IMDB Top Movies.csv' , index= False )