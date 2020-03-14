import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
	w = w.lower()
	if w in data:
		result = []
		result = data[w]
		return result
	elif len(get_close_matches(w,data.keys()))>0:
		yn= input("Did you mean {} instead? Enter 'Y' if yes and 'N' if no:  ".format(get_close_matches(w,data.keys())[0]))
		if yn.upper() == "Y":
			return data[get_close_matches(w,data.keys())[0]]
		elif yn.upper() == "N":
			return "The word Doesn't exist"
	else:
		return "The word doesn't exist.Please Check the word"

a = True
while (a==True):
	word = input("Enter Word Here: ")
	x = translate(word)

	if type(x) == list:
		for item in x:
			print(item)
		
	else:
		print(x)
				
'''result = []
result = translate(word)
'''
