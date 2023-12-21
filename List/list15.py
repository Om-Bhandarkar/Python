import copy as cp

lang = ["C", "HTML", "CSS", ["CPP", "Python", "Java", "JavaScript"]]

newList = cp.deepcopy(lang)

print(lang)

print(newList)

lang[3][1] = "javascript"

print(lang)

print(newList)
