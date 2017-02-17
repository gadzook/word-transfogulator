#word transfogulator

def transfogulate(str_list):
	"""Returns a garbled string based on multiple input strings.
	Simply iterates between each letter in all strings, sifting them together 
	into one long one.

	For example, running this function with the parameters "Hello World!" and 
	"O Shit Waddup" returns the string "HOe lSlhoi tW oWralddd!up".

	Once it reaches the end of the shortest string, it will just append the
	rest of the longer ones' letters.
	"""
	str_list_sorted = sorted(str_list,key=len,reverse=True)
	str_list_transfogulated = []
	for i in range(len(str_list_sorted[0])):
		for string in str_list_sorted:
			try:
				str_list_transfogulated.append(string[i])
			except IndexError:
				continue
	str_transfogulated = "".join(str_list_transfogulated)
	return str_transfogulated

def collect_strings():
	"""collects strings to be transfogulated"""
	str_list = []
	number_of_strings = int(input("How many strings?:  "))
	for i in range(number_of_strings):
		str_list.append(str(input("Word %s:  " % (i+1))))
	return str_list

strs = collect_strings()
print(transfogulate(strs))
