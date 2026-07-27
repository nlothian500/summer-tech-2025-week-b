from PIL import Image
from transformers import pipeline

x = Image.open("Barracuda_laban.jpg")
x.show()
print(x)
classifier  = pipeline("zero-shot-image-classification")

fish = ["Red Snapper", "mackerel", "tuna",
"Mahi-Mahi", "Parrotfish", "Barracuda",
"jack"]

inputs = classifier(x, candidate_labels=fish)

print(inputs)

                    







