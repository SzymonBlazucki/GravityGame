width = 600
heigth = 1000
fontName = 'arial'

fps = 60
timeStep = 1000/fps
sideThrusterA = 0.000003
mainThrusterA = 0.0002
sideThrusterAlpha = 0.0003
initialAngle = 0
thrusterSound = "Thruster.wav"
rocketImage = "./graphics/rocket2.png"
backgroundMusic = "Space.mp3"
crashSound = "Smashing.wav"
#music from https://www.chosic.com/ and
planet1 = [150, 300, 0.0002, "./graphics/redPlanet.png"]

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

initialPosition = [500, 900]
initialVelocity = [0,-0.01]