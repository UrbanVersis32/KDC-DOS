# KDC-DOS
#
# Note: Layout is as follows
#
# function for all commands without arguments
# function for all commands with arguments
# while True loop for prompt


# Commands without argument
def nonarguments():
	print()

# Commands with argument
def arguments():
	print()

print("Welcome to KDC-DOS!")

while True:
	prompt = input("> ")
	if prompt == "test":
		print("hi!")
