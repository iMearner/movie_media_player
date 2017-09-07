import webbrowser 

class Movie(object):
	def __init__(self,movie_title, movie_storyline, poster_image_url, youtube_video_url, release_date):
		self.movie_title = movie_title
		self.movie_storyline = movie_storyline
		self.poster_image_url = poster_image_url
		self.youtube_video_url = youtube_video_url
		self.release_date = release_date

	def play_video(self):
		webbrowser.open(self.youtube_video_url)