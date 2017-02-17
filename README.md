# word-transfogulator
Returns a garbled string based on multiple input strings.
Simply iterates between each letter in all strings, sifting them together into one long one.
For example, running this function with the parameters "Hello World!" and 
"O Shit Waddup" returns the string "HOe lSlhoi tW oWralddd!up".
Once it reaches the end of the shortest string, it will just append the
rest of the longer ones' letters.
