import random
import string
import datetime

def GetRandomString(n):
	res = ""
	for i in range(n):
		res += random.choice(string.ascii_letters)
	return res

now = int(datetime.datetime.now().timestamp())

with open("data.sql", "w") as f:
	f.write('USE biblioteka;\n\n')

	# Generowanie czytelników
	f.write('/* Dane czytelnikow */ \n')
	for i in range(100):
		q = "INSERT INTO `czytelnik` VALUES ({}, '{}', '{}', '{}@gmail.com', {});\n".format(i + 1, GetRandomString(10), GetRandomString(10), GetRandomString(10), now)
		f.write(q)
	f.write('\n\n')

	# Generowanie autorów
	f.write('/* Dane autorow */ \n')
	for i in range(100):
		q = "INSERT INTO `autorzy` VALUES ({}, '{}', '{}');\n".format(i + 1, GetRandomString(15), GetRandomString(15))
		f.write(q)
	f.write('\n\n')

	# Generowanie gatunkow
	f.write('/* Dane gatunkow */ \n')
	gatunki = ['Fantastyka', 'Romans', 'Obyczajowe', 'Kryminal', 'Klasyka', 'Thriller', 'Historyczna', 'Przygodowa']
	for i in range(len(gatunki)):
		q = "INSERT INTO `gatunki` VALUES ({}, '{}');\n".format(i + 1, gatunki[i])
		f.write(q)
	f.write('\n\n')

	# Generowanie ksiazek
	f.write('/* Dane ksiazek */ \n')
	i = 0
	for x in range(100):
		q = "INSERT INTO `ksiazki` VALUES\n"
		f.write(q)
		for j in range(10000):
			q = "({}, '{}', {}, {}){}\n".format(i + 1, GetRandomString(50), random.randint(1, 100), random.randint(1, len(gatunki)), "," if j < 9999 else "")
			i += 1
			f.write(q)
		f.write(";\n\n")
	f.write('\n\n')

	# Generowanie wypozyczen
	f.write('/* Dane wypozyczen */ \n')
	i = 0
	for x in range(100):
		q = "INSERT INTO `wypozyczenia` VALUES\n"
		f.write(q)
		for j in range(10000):
			d = 0 if random.randint(1, 100) <= 30 else '{}'.format(now + random.randint(1, 60) * 24 * 60 * 60)
			q = "({}, {}, {}, {}, {}){}\n".format(i + 1, random.randint(1, 1000000), random.randint(1, 100), now, d, "," if j < 9999 else "")
			i += 1
			f.write(q)
		f.write(";\n\n")
	f.write('\n\n')

with open("data_add.sql", "w") as f:
	f.write('USE biblioteka;\n\n')

	# Generowanie wypozyczen
	f.write('/* Dane wypozyczen */ \n')
	i = 1000000
	for x in range(200):
		q = "INSERT INTO `wypozyczenia` VALUES\n"
		f.write(q)
		for j in range(10000):
			d = 0 if random.randint(1, 100) <= 30 else '{}'.format(now + random.randint(1, 60) * 24 * 60 * 60)
			q = "({}, {}, {}, {}, {}){}\n".format(i + 1, random.randint(1, 1000000), random.randint(1, 100), now, d, "," if j < 9999 else "")
			i += 1
			f.write(q)
		f.write(";\n\n")
	f.write('\n\n')
