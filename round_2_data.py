color_def = [[(164,116,121),(186,255,255)],     #red
			 [(117,124,108),(144,190,232)],		#VIOLET
			 [(149,119,105),(170,255,255)],		#pink
			 [(170,116,153),(210,255,255)]]		#green 

bot_paths = [[],
			 []]
		 

bot = [ '192.168.251.7',
		'192.168.251.187',
		'192.168.43.126',
		'192.168.43.197']
# deifne 1 extra turn direction and limit and directions > limits by 1
is_round_1 = False
# pixel range 1200x720																#turn_path: 1 : reverse, 2 : halt
path_def = [[['W','N','S','E','E'],[650, 100,355,1190], [0,     0,650,1200],[350,360],[0,1,0,2,0,2]],
			[['W','N','S','E','E'],[800, 100,205,1190], [0,     0,780,1200],[200,210],[0,1,0,2,0,2]],
			[['W','S','N','E','E'],[120,1140,645,650], [0,  1300,300,720],[640,650]],
			[['W','S','N','E','E'],[185,1140,720,645], [0,  1300,300,720],[715,725]],
			[['W','S','N','E','E'],[500,500,340,1200], [400, 600,240,720],[340,350]],	
			[['W','E','E'],[100,600,0],[120,130]],
			[['W','E','E'],[100,600,0],[140,150]],
			[['W','E','E'],[100,600,0],[160,170]],
			[['W','E','E'],[100,600,0],[180,190]]]



#['N','W','W','S','S'],[500,1000,500,0],[500,510]