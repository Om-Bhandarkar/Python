lang = ("Cpp", "Java", "Python", "Js", "Dart", 10.5, 20, 30, 40)

print(lang)

lang[3] = "Go"

print(lang)    #TypeError: 'tuple' object does not support item assignment
e