stringOneInput = input("Enter a string: ")
lowerCaseLetters = [j for j in stringOneInput if j.islower()]
upperCaseLetters = [j for j in stringOneInput if j.isupper()]
stringOneOutput = lowerCaseLetters+upperCaseLetters
stringOneOutput = ''.join(stringOneOutput)
print(stringOneOutput)