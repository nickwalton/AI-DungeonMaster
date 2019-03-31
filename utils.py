def text_replace(text):
# Replace certain words
    text = text.replace("I ","you ")
    text = text.replace("we ","you ")
    text = text.replace("We ","You ")
    text = text.replace(" mine"," yours")
    text = text.replace("kill you", "hurt you")
    text = text.replace("[","")
    text = text.replace("]","")
    return text
