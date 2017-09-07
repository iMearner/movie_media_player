import webbrowser 
import re 
import os 

main_page_head = '''

<head>
	<meta charset="utf-8">
    <title>Fresh Tomatoes!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
</head>

'''

movie_title_content = '''
	<div>
		<h1>{title}</h1>
		<p>{storyline}</p>
		<img src="{image_source}" width=200px />
		<p> movie release : {release_date}</p>
	</div>
'''

def create_movie_tiles(movies):
	content = ''
	for movie in movies :
		content += movie_title_content.format(
				title = movie.movie_title,
				storyline = movie.movie_storyline,
				image_source = movie.poster_image_url,
				release_date = movie.release_date
			)
	return content 
	

def open_movies_page(movies):
	open_file = open('index.html','w')

	rendered_content = create_movie_tiles(movies)

	open_file.write(rendered_content)
	open_file.close()

	url = os.path.abspath(open_file.name)
	webbrowser.open('file://'+url, new=2)
