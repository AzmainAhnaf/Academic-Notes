def forall(domain, predicate):
	return all(predicate(x) for x in domain)

def exists(domain, predicate):
	return any(predicate(x) for x in domain)

domain = [1, 2, 3, 4, 5]

predicate1 = lambda x: x**2 <= 16
predicate2 = lambda x: x**2 == 25

print("For all x (x^2 <= 16):", forall(domain, predicate1))
print("There exists x (x^2 == 16):", exists(domain, predicate2))
