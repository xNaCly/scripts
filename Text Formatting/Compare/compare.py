# compare strs:
class Compare:
	def __init__(self):
		self.str1 = ""
		self.str2 = ""

	def strr(self):
		self.str1 = input("First string: ")
		self.str2 = input("Second string: ")

	def file(self):
		self.str1 = input("Filename 1: ")
		self.str2 = input("Filename 2: ")
		try:
			with open(f"{self.str1}","r") as f:
				self.str1 = f.read()
			with open(f"{self.str2}","r") as f:
				self.str2 = f.read()
		except:
			raise FileNotFoundError(f"files: '{self.str1}' or '{self.str2}' not found")

	def compare(self):
		if self.str1 == self.str2:
			raise ValueError("Strings are identical.")

		result1 = ''
		result2 = ''

		maxlen=len(self.str2) if len(self.str1)<len(self.str2) else len(self.str1)

		for i in range(maxlen):
			letter1=self.str1[i:i+1]
			letter2=self.str2[i:i+1]
			if letter1 != letter2:
				result1+=letter1
				result2+=letter2
			else:
				result1+="_"
				result2+="_"

		if result1 == "" and result2 == "":
			raise ValueError("Strings are identical.")

		print ("Letters different in string 1:",result1)
		print ("Letters different in string 2:",result2)

	def main(self):
		print("Compare 2 strings and point out differences: ")
		choice = input("Str/file: ")
		if choice.lower() == "str":
			self.strr()
		elif choice.lower() == "file":
			self.file()
		else:
			raise ValueError("invalid argument, should be: [str/file]")
		self.compare()

f = Compare()
f.main()