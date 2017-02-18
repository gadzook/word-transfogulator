# word-transfogulator
Returns a garbled string based on multiple input strings.
Simply iterates between each letter in all strings, sifting them together into one long one.
For example, running this function with the parameters "AAAAA" and 
"BBBBB" returns the string "ABABABABAB".
Once it reaches the end of the shortest string, it will just append the
rest of the longer ones' letters.
