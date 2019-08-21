def reverseWords(input):
	input = input.split(" ")
	output = input[::-1]
	return output

def reverseChar(input):
	output = input[::-1]
	return output
	
if __name__ == "__main__":
	input = "I love Amy!"
	print(input)
	print(input[-1::-2])
	print(reverseWords(input))
	print(reverseChar(input))