"""Program to read a short string and re-create each alternate characters as upper and lower case;
and part two, re-creates each alternative word as lower and upper case."""

# get a short sentence and store as short_string variable
short_string = input('Enter a short sentence: ')
print(f'You entered - "{short_string}" \n') #print to show captured string and add new line

# using the enumerate() assign indexes
string_enm = enumerate(short_string)

# using an if...else and a for loop, convert even charaters to lowercase and odd to uppercase
string_alt = ''.join([a.lower() if i % 2 else a.upper() for i, a in enumerate(short_string)])
print(f'We recreated - "{string_alt}" \n') #print output with alternate upper & lower characters

# Part two
# split sentence for next task, convert into iterable list of items and enumerate it
string_sp = short_string.split()
string_sp_enu = enumerate(string_sp)

# using an if...else and a for loop, convert even items to uppercase and odd to lowercase
string_up = ' '.join([b.upper() if i % 2 else b.lower() for i, b in enumerate(string_sp)])
print(f'And again - "{string_up}"') #print output showing alternate lower & upper case joined words
