width = 1400
heigth = 1000
fontName = 'arial'

fps = 60
timeStep = 1000 / fps
sideThrusterA = 0.000002
mainThrusterA = 0.00002
sideThrusterAlpha = 0.00027
initialAngle = 0
rocketImage = "./graphics/rocket3.png"
backgroundMusic = "Space.ogg"
crashSound = "Smashing.wav"
moneySound = "classiccoin.wav"
# music from https://www.chosic.com/ and
planet1 = [[180, 300, 1.5, "./graphics/fancyPlanet4.png", 0.25], [600, 750, 0.8, "./graphics/fancyPlanet3.png", 0.6],
           [1000, 350, 1.8, "./graphics/fancyPlanet2.png", 0.4]]
moneyLoc = [[1150, 400], [580, 520], [90, 200], [950, 200], [400, 920], [850, 820], [290, 400]]
moneyName = "./graphics/gold.png"
colors = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "lightblue": (0, 155, 155),
    "pink": (255, 174, 201),
    "beige": (245, 247, 221),
    "spacegrey": (69, 69, 69)
}
backgroundColor = colors['spacegrey']

initialPosition = [1300, 900]
initialVelocity = [0, -0.01]
