#!/usr/bin/env python
import webbrowser
import os
import re
main_page_head = '''
<html>
	<head>
	<style>
		 .container {
            flex-wrap: wrap;
            display: flex;
            flex: 10%;
            justify-content: center;
            
        }
        header {
        text-shadow: 3px 2px rgb(180,67,141);
		    font-family:Apple Chancery,cursive;
			font-style:oblique;
			font-weight:500;
			color:rgb(26,7,82);
            height: 15px;
            text-align: center;
            font-size: 40px;
        }

        figcaption{
        text-align: center; 
        color: rgb(8,4,58);
        	font-family:Apple Chancery,cursive;
			font-style:oblique,bold;
			font-weight:1000;
			}
			
        img{
        border:5px solid rgb(218,110,166);
            height: 400px;
            width: 400px;
            border-radius: 5%;
        }
        .img1:hover,
        .img2:hover,
        .img3:hover,
        .img4:hover,
        .img5:hover,
        .img6:hover{
        box-shadow: 5px 5px 2px rgb(118,69,96) ;
           background-color: rgb(46,123,119);
            visibility: visible;
            cursor: pointer;
            border-radius:5%;
        }

        .img1,.img2,.img3,.img4,.img5,.img6{
            padding:25px;
            background-color: white;
            margin:10px;           
        }
        </style>
		<script src="https://code.jquery.com/jquery-1.12.3.min.js" integrity="sha256-aaODHAgvwQW1bFOGXMeX+pC4PZIPsvn2h1sArYOhgXQ=" crossorigin="anonymous"></script>
		<link href="https://fonts.googleapis.com/css?family=Courgette" rel="stylesheet">
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
		<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
		<script>
			function changeVideo(vId) {
				var iframe = document.getElementById("myframeY");
				iframe.src = "https://www.youtube.com/embed/" + vId;
				$("#myVideo").modal("show");
			}
			$(document).ready(function () {
				$("#myVideo").on("hidden.bs.modal", function () {
					$("#myframeX").attr("src", "#");
				})
			})
		</script>	 
		<title>Places</title>
		<meta name="viewport" content ="width=device-width, initial-scale=1.0">
	</head>'''
main_page_content = '''	<body>
	<header></i>  Know about your favourite places </i></header><br><br>
		<main>
			<div class="container">
				<div class="img1" onclick="changeVideo('kOAS3bmtSAM')">
					<img  src="https://encrypted-tbn0.gstatic.com/grid-items?q=tbn:ANd9GcQkVuw6z5E3xuFeVXDcveZGHDFcoSp_EbfAutt4nFgvn596s1Vv" alt="Statue of Liberty">
					<figcaption>Statue of Liberty</figcaption>
				</div>
				<div class="img2" onclick="changeVideo('s3bCKfPgoLQ')">
					<img src="https://encrypted-tbn0.gstatic.com/grid-items?q=tbn:ANd9GcTBblePFpfGNoAOKfRthU-tz6QUFLllhpC0KKRPuin0CRQI36u3" alt="Eiffel Tower">
					<figcaption>Eiffel Tower</figcaption>
				</div>
				<div class="img3" onclick="changeVideo('TyXrHfz9lAY')">
					<img src="https://encrypted-tbn0.gstatic.com/grid-items?q=tbn:ANd9GcQh7V89xCCCCniErs6LSOsUC_44FDdda0Eb-aPpF5MrDZ2av8Re" alt="Big Ben">
					<figcaption>Big Ben</figcaption>
				</div>
				<div class="img4" onclick="changeVideo('nGavsnu9m4A')">
					<img src="http://www.towerofpisa.org/wp-content/uploads/photo-gallery/pisa-leaning-tower.jpg" alt="Leaning Tower of Pisa">
					<figcaption>Leaning Tower of Pisa</figcaption>
				</div>           
				<div class="img5" onclick="changeVideo('G2FrANjg_OY')">
					<img src="https://s3.envato.com/files/236066482/20160214-BatterySpencer-8824-8mp.jpg" alt="Golden Gate Bridge">
					<figcaption>Golden Gate Bridge</figcaption>
				</div>     
				<div class="img6" onclick="changeVideo('F5CPHRJwdZ0')">
					<img src="https://upload.wikimedia.org/wikipedia/commons/a/a1/Sydney_Opera_House_Night.jpg" alt="Opera House">
					<figcaption>Opera House</figcaption>
				</div>      
				<div class="modal fade" id="myVideo" tabindex="0" role="history" aria-labelledby="myModalLabel">
					<div class="modal-dialog" role="history">
						<div class="modal-content">
							<div class="modal-body">
								<iframe id="myframeY" width="570" height="375" src="" frameborder="0" allowfullscreen></iframe>
							</div>
						<div class="modal-footer">
							<button type="button" class="btn btn-default" data-dismiss="modal"><b>X</b></button>
						</div>
					</div>
				</div>
			</div>
		</main>
	</body>
</html>
'''
movie_title_content = '''
<div class ="modal fade" data-trailer-youtube-id="{trailer_youtube_id}""
"data-toggle="modal" data-transfer="#trailer">
<img src="{poster_image_url}" width=220 height = "342">
    <h2 style="color:white;">{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    content = ''
    for movie in movies:
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
        content += movie_title_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    output_file = open('fplace.html', 'w')
    rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))
    output_file.write(main_page_head + rendered_content)
    output_file.close()
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
