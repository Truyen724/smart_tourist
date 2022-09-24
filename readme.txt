
python main.py

API predict 

{
    "image": "",  		#picture base68
    "color": "",  		# RED, YELLOW, SKYBLUE, GREEN, PINK, PURPLE,BROWN, ORANGE
    "weather": "",		# ["clear sky","shower rain", "rain","thunder storm","few clouds","snow","scattered cloud","broken cloud","light rain","mist","overcast clouds","moderate 							rain","heavy intensity rain"]
    "temperature":"",		#nhiet do vd 25
    "day_or_night": "", 	# MORNING, NIGHT, MORNING_A_NIGHT
    "day_of_birth": ""  	# 24/3
}

API trả về: 'ID', 'Name', 'ADDRESS', 'ADDRESS_LINK','IMG2'

ví dụ cho api

{
    "image": "xxx",  		
    "color": "RED",  		
    "weather": "clear sky",	
    "temperature":"25",		
    "day_or_night": "NIGHT", 	
    "day_of_birth": "24/3"  	
}