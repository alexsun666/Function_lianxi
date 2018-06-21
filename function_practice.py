#question 1
def f(x):
    return 6 * x - 4
print(f(4))
print(f(5))
print(f(6))

#question 2"
def f(n):
    return 1 / (3**n-1)
print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(5))
#question 3"
def f(n):
	return (-1**n) * (3)
print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(5))

# question 4
def f(x):
    f = (250*0.07*x) + 250
    return f

print(f(1))
print(f(3))
print(f(7))
print(f(20))

# question 5
def f(x):
    f = 325 * (1.04**x)
    return f

print(f(1))
print(f(3))
print(f(7))
print(f(20))
# question 6
def bills(h):
	ma = 10000 * (1.04**h)
	mb = 10000 + (10000*0.05*h)
	if ma - mb > 0
	return (ma , mb)
	

#"Functions_worksheet"
#'question a'

def m(h):
	return 1000 + (100 * h)

#'question b'

def b(m):
	return m / 20

#'question c'
def bills_get(h):
	salary = m(h) 
	bills = b(salary)
	return bills
print (bills_get(10))
#question d
def bills_dina_earns_each_month(h):
	a = 1000 + (100 * h)
	bills_dina_earns_each_month = a / 20
	return bills_dina_earns_each_month
print(bills_dina_earns_each_month(5))
#question e
def money_dina_gets_in_a_month(number_of_bills):
	money = number_of_bills * 20
	hours_dina_teaches = (money - 1000) / 100
	return hours_dina_teaches
print(money_dina_gets_in_a_month(100))