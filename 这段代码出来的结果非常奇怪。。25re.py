def split_sentence(a):
	return a.split(' ')

def sort_words(a):
	return sorted(a)

def print_first_word(a):
	print a.pop(0)
	
def print_last_word(a):
	print a.pop(-1)

def sort_sentence(a):
	words = split_sentence(a)
	return sort_words(words)
	
def print_first_and_last(a):
	words = split_sentence(a)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(a):
	words = sort_sentence(a)
	print_first_word(words)
	print_last_word(words)

a = "This is a sentence which could be split"
print_first_and_last(a)
print_first_and_last_sorted(a)