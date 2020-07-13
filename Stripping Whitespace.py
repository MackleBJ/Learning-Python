#Stripping (whitespace not naked)

string1="   python"
string2="python   "
string3="   python   "

string1=string1.lstrip()
string2=string2.rstrip()
string3=string3.strip()

if string1 == string2 == string3:
    print("You're a good Stripper!")
else:
     print("You should stick to your day job.")


#Stripping 1.1 (Let's condense this a bit)

str1, str2, str3 = "python  ", "   python", "   python  "
str1, str2, str3 = str1.strip(), str2.strip(), str3.strip()

if str1 == str2 == str3:
    print ("Good Job!")
else:
    print ("Let's try that again.")
