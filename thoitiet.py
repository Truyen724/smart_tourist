def getWeather(weather,temperature):
    HOT = ["clear sky", "mist"]
    RAIN = ["shower rain", "rain","thunder storm", "light rain","moderate rain","heavy intensity rain"]
    BEAUTYFUL_DAY = ["few clouds"]
    COLD = ["snow"]
    CLOUDY =["scattered cloud","broken cloud", "overcast clouds"]
    OUT = []
    if(weather in HOT):
        OUT.append("HOT")
    if(weather in RAIN):
        OUT.append("RAIN")
    if(weather in BEAUTYFUL_DAY):
        OUT.append("BEAUTYFUL_DAY")
    if(weather in COLD):
        OUT.append("COLD")
    if(weather in CLOUDY):
        OUT.append("CLOUDY")
    if(int(temperature)>30):
        OUT.append("HOT")
    if(int(temperature)<17):
        OUT.append("COLD")
    return OUT

