class Song:
	def __init__(self,lyrics):
		self.lyrics = lyrics
	
	
	def songs_line(self):
		for i in self.lyrics:
			print(i)

			
song1 = Song(["I am always ready for the war again","So baby pull me closer in the backsit of your over ","Then i know you can't afford","Sixpack of your corner from your ....."])

song2 = Song(["Jonney,jonny","Yes papa","Eating Sugar","No papa","Open your mouth ","Hahahahhhahahahahahh........."])


song1.songs_line()
print("*"*30)
song2.songs_line()
	
	
