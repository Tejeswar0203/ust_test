line = "which is better python 2 or python 3"

words = line.split(" ")
emp_dict={}

for word in words:
    if word in emp_dict:
        emp_dict[word] = emp_dict[word]+1
    else:
        emp_dict[word]=1

output=tuple(emp_dict.items())
print("all words count:",output)