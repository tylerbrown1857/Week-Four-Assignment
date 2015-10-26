#
# File Header
#
# Add your name to this

# Define a function called piggy(string) that returns a string

def piggy(word):
	
	# Magic Happens Here
	vowels = "aeiouAEIOU"

# Ask for word

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

	
	return pig

# Open the file *getty.txt* for reading.  
getty = open("getty.txt", "r")

# Open a new file *piggy.txt* for writing.  
piggys = open("piggy.txt", "w")
# Read the getty.txt file into a string.  
gettysburgStr = getty.read()
# Strip out bad characters (, - .).  
gettysburgStr.replace(',', '')
gettysburgStr.replace('-', '')
gettysburgStr.replace('.', '')

# Split the string into a list of words.  
gettysburgStr.split()
# Create a new empty string.  
newStr = ""

#1476
# Loop through the list of words, pigifying each one.  
for words in gettysburgStr:
	word = piggy(gettysburgStr[words])

# Add the pigified word (and a space) to the new string.  
	newStr = newStr + word + " "
# Write the new string to piggy.txt.  
piggys.write(newStr)
# close the files.
getty.close()
piggys.close()