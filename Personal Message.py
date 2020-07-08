#Personal Message 1.0 (Python 3.6 and on method)

name= "Brett J. McElvain"
print(f"Hello, {name.title()}! Would you like to learn Python today?")


#Personal Message 1.1 (Python 3.5 and earlier method)

fname="Brett"
minit="J."
lname="McElvain"
full_name="Hello, {} {} {}! Would you like to learn Python today?".format(fname, minit, lname)
print(full_name)


#Personal Message 2.0

name="Brett J. McElvain"
print(f"Hello, {name.title()}! Would you like to learn Python today?")
print(f"Hello, {name.upper()}! Would you like to learn Python today?")
print(f"Hello, {name.lower()}! Would you like to learn Python today?")
