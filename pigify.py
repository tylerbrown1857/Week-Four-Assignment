# 
# File Header
#
# Define vowels

vowels = "aeiouAEIOU"

# Ask for word

word = input("Please enter a word: ")

# Loop through word, one letter at a time

for letter in word:
	# Check if letter is a vowel
	if letter in vowels:
		# True?  We are done
		pig = word + "yay"
	else:
		# False? Conson
		i = 0
		spot = 0
		for letter in word:
			if word[i] in vowels:
				
				spot = i
				break
			i = i + 1
pig = word[spot: len(word)] + word[0: spot] + "say"
