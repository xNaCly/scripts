import pynput
from time import sleep as s

mouse = pynput.mouse.Controller()
button = pynput.mouse.Button

def main():
	pos = str(mouse.position)
	pos_raw_1 = pos.replace("(", "")
	pos_raw_2 = pos_raw_1.replace(")","")
	pos_raw = pos_raw_2.split(",")

	mouse.position = int(pos_raw[0]), int(pos_raw[1]) + 1
	mouse.click(button.right, 2)

x = 0
while True:
	s(3)
	x += 1
	print(f"Moving for the: {x}'s Time'")
	main()