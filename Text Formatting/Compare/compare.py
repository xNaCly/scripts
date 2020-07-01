# compare strs:
print("Compare 2 strings and point out differences: ")
str1 = input("First string: ")
str2 = input("Second string: ")
def compare():
	if str1 == str2:
		raise ValueError("Strings are identical.")

	result1 = ''
	result2 = ''

	maxlen=len(str2) if len(str1)<len(str2) else len(str1)

	for i in range(maxlen):
		letter1=str1[i:i+1]
		letter2=str2[i:i+1]
		if letter1 != letter2:
			result1+=letter1
			result2+=letter2

	if result1 == "" and result2 == "":
		raise ValueError("Strings are identical.")

	print ("Letters different in string 1:",result1)
	print ("Letters different in string 2:",result2)

compare()

