from PIL import Image
from transformers import pipeline

x = Image.open("fish.webp")
x.show()
print(x)
j  = pipeline("zero shot-classificarion")
fish = []
fish = ["Red Snapper", "mackerel", "tuna"
"Mahi-Mahi", "Parrotfish", "Barracuda"
"jack"]

fish = ["Red Snapper", "mackerel", "tuna","Mahi-Mahi", "Parrotfish", "Barracuda","jack"]
inputs = classifier(images=fish.webp, text=fish,)
                    







