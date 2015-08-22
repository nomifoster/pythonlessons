movie_titles = ['Amelie','The Mummy','How To Train Your Dragon','Howls Moving Castle','Empire Records']
parental_rating = ['R','PG13','PG','PG','PG13']
bechdel_rating = ['3','1','3','3','3']
imdb_rating = ['8.4','7','8.2','8.2','6.7']
genre = ['Romance/Comedy','Fantasy/Action','Fantasy/Drama','Fantasy/Drama','Coming of Age/Cult']

n = 0

for movie in movie_titles:
	print movie_titles[n] + ", " + parental_rating[n] + ", " + imdb_rating[n] + ", " + bechdel_rating[n] + ", " + genre[n]
	n = n + 1
