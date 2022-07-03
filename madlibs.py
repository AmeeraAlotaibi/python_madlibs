def main():
	# write your code here
	time = input("enter a time")
	item1 = input("enter an item")
	item2 = input("enter a second item")
	item3 = input("enter a third item")
	name = input("enter a name")
	scream = input("SCREAM!!")
	action = input("enter an action")

	newname = name.capitalize()
	newscream = scream.upper()
	print(f"It was {time} o'clock when I heard a knock at the door.")
	print(f"I opened the door and there was a {item1} full of {item2} with a {item3} saying {newname}")
	print(f"Just as I closed the door I heard a scream {newscream}")
	print(f"I froze in place and all I could do was {action} my head.")


if __name__ == '__main__':
	main()