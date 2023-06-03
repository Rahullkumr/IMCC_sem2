# Write Python program to Find ‘n’ Character Words in a Text File

with open("file.txt") as file:
	n = 6
	words = file.read().split()
	for word in words:
		if len(word) == n:
			n_character_words = word
			print(n_character_words)
