Notatka ta posiada tłumaczenie kodu znajdującego się w moim pliku WD oraz
kluczowe słowa potrzebne do sprawnego szukania odpowiedzi podczas kolokwium/sesji.
Nie ma wszystkiego, ale ma dużo.
Symbol ---| oznacza, że mówię z własnej interpretacji, może nie być to prawda.

4.07
	
	numpybruh
		Plik nazwany tak ze względu na fakt, że pliki nie mogą nazywać się tak samo jak biblioteki, zwróci to błąd.
		W pliku mamy importowaną bibliotekę numpy:
		
		import numpy as np										Importuje bibliotekę 'numpy' pod aliasem 'np'.
		a = np.array([1, 4, 10])								Przypisuje a jako macierz o wartościach 1, 4 oraz 10.
		a.shape													.shape zwraca krotkę w oparciu o tablicę a. indeksy tej krotki mówią nam o rozmiarach tabeli. Shape będzie zwracał indeksy tylko, gdy wymiary będą równe. https://www.w3schools.com/python/numpy/numpy_array_shape.asp
		np.sqrt(a)												Pierwiastek 2 stopnia z a.
		print(a>3)												Komenda będzie zwaracała True w miejsce wartości, która będzie większa od 3, oraz False w miejsce gdzie nie spełni warunku.
	
	Bisection
		Metoda bisekcji - jedna z metod rozwiązywania równań nieliniowych, używamy w celu obliczenia pierwiastka równania.														   https://pl.wikipedia.org/wiki/Metoda_r%C3%B3wnego_podzia%C5%82u
		ftol=1e-6												Oznacza tolerancję terminacji, ---| z mojego rozumowania ogranicza funkcję gdy liczba staje się tak mała jak 1e-6. https://stackoverflow.com/questions/9667514/what-is-the-difference-between-xtol-and-ftol-to-use-fmin-of-scipy-optimize
		def bisect(f, a, b, ftol=1e-6)							Tworzy funkcję w oparciu o podane argumenty. Kiedy podajemy w funkcji ftol=1e-6, to możemy ominąć podawanie ftol przy wywoływaniu funkcji, wtedy użyjemy domyślnie naszego 1e-6.
		abs(f(x))												Liczba bezwzględna f(x).
		
		BisectionScipy
			Jedna z metod zapisu Metody bisekcji.
		BrentQ
			Jedna z metod zapisu Metody bisekcji.
		fsolve
			Jedna z metod zapisu Metody bisekcji.
		Newton
			Jedna z metod zapisu Metody bisekcji.
			Nie ma gwarancji że się zbiegnie, potrzebne jest dobre pierwsze zgadnięcie x dla pierwiastka.
		fsolve
			Jedna z metod zapisu Metody bisekcji.
			W PyCharm otrzymujemy warning, ale może być ignorowany.
	
	array
		B.shape = (4, )											Zmienia rozmiar B z (2, 2) na (4,). [[0, 1.5], [10, 12]] na [0, 1.5, 10, 12].
		a.size													Liczba elementów w macierzy.
		a.nbytes												Rozmiar w bitach które zajmują wszystkie elementy macierzy.
		a.dtype													Typ data jakie przyjmuje a.
		a2 = np.array([1, 4, 10], float)						podanie float jako atrybut array zmusi, by ta macierz była zapisana jako typ data float64.
		np.zeros((3, 3))										Tworzy macierz wypełnioną zerami, rozmiar 3x3 (3 wiersze, 3 kolumny).
		np.zeros((4,)) = np.zeros(4)							Oba sposoby zapisu utworzą macierz wypełnioną zerami, rozmiar 1x4 (1 wiersz, 4 kolumny).
		np.ones((2, 7))											Tworzy macierz wypełnioną jedynkami, rozmiar 2x7 (2 wiersze, 7 kolumn).
		x = np.array(range(0, 10, 2))							Tworzy macierz o wartościach od 0 do 10, odstęp co 2. (wartości [0, 2, 4, 6, 8])
		x[3]													wartość z macierzy x z 4 kolumny.
		len(x)													Długość macierzy (liczy ile jest wartości w macierzy).
		C = np.arange(12)										Stworzy macierz o 12 wartościach (domyślnie zaczyna na 0, idzie co 1).
		C.shape = (3, 4)										Jeżeli shape nie ma być wypisany, ale jest jak w tym przypadku równy czemuś, to zmienia on rozmiar wybranej macierzy na nowy podany przez nas (w tym przypadku na 3 wiersze i 4 kolumny).
		print(C[2, 0])											Podaje wartość z macierzy C z 3 wiersza, a 1 kolumny.
		print(y[0:5:1])											Podaje wartości od kolumny 0 do 5, :1 oznacza, że co 1.
		print(y[:5:2])											Podaje wartości od kolumn wszystkich w lewo do 5, :2 oznacza, że co 2.
		print(y[5:0:-1])										Podaje wartości od kolumny 5 do 0, działa przez to, że bierzemy co -1.
		print(y[::-1])											Podaje wszystkie wartości od tyłu (bo wszystko bierzemy co -1).
		copy_y = y[:]											Kopiuje wszystkie kolumny i wiersze y.
		print(C[0, :])											Podaje wszystkie wartości z pierwszego wiersza.
		print(C[:, 1])											Podaje wszystkie wartości z drugiej kolumny.

linalg
		import numpy.linalg as la								Importuje linalg z biblioteki numpy pod aliasem 'la'
		ainv = la.pinv(a)										
		a.dot(ainv)												
		la.det(a)												
		la.det(ainv)											
		la.det(a)*la.det(ainv)									
		la.eig(a)												
		
4.14
	PlottingArrays_Vectors
		import pylab as plb										Importuje bibliotekę 'pylab' pod aliasem 'plb'.
		np.pi													Wartość pi z biblioteki numpy
		t = np.arange(0, 10*np.pi, 0.01)						Przypisuje t wartości rosnące o 0.01 od 0 tak długo aż dojdzie do 10 * pi.
		y = np.cos(t)											Przypisuje y cosinus oparty o wartości t.
		
		plb.plot(t, y)											Tworzy parametr dla figury w oparciu o dwie wartości t, y.
		plb.xlabel('t')											Nadaje osi x nazwę 't'.
		plb.ylabel('y(t)')										Nadaje osi y nazwę 'y(t)'.
		plb.show()												Wyświetla funkcję w oparciu o atrybuty podane przed wywołaniem plb.show().
		
4.21
	Curve_fitting_example
		import scipy.optimize										Importuje bibliotekę scipy.optimize
		import pylab												Importuje bibliotekę pylab
		x = np.linspace(0, 5, 10)									Tworzy macierz z 10 wartościami od 0 do 5 (Z włączeniem 5).
		x += 1.5 * np.random.normal(size=len(x))					Do x dodaje 1.5 * losowa liczba oparta o rozmiar x.
p, pcov = scipy.optimize.curve_fit(model, x, y)				Figura o nazwie 'p', pcov = ???, jest to funkcja zagięta w oparciu o wartości.
		pylab.plot(x, y, 'o', label='data point')					Dodaje parametr o kolorze pomarańczowym 'o', z nazwą 'data point'.
		pylab.title('fit parameters (a,b,c)=%s' % p)				Dodaje do figury tytuł.
		pylab.legend()												Dodaje do figury legendę.
		pylab.savefig('curvefit2.pdf')								Zapisuje figurę jako plik pdf.
	Function_integration_example
		from scipy.integrate import quad							Importujemy z scipy.integrate funkcję quad.
res, err = quad(f, -2, 2)
		print("The numerical result is {:f} (+-{:g})".format(res, err)) W miejscach {:f} i (+-{:g}) podane są wartości odpowiednio res w {:f} oraz err w {:g}.
	Integration
		Nie działa
		sympy
		integrate
		symbols
	ODE
		pylab.plot(ts, p2, '-og', label='foxes')					Parametr w którym wyświetlamy zielone kropki na funkcji liniowej.
		pylab.savefig('predprey.eps')								Zapis wykresu w formacie eps.
		pylab.savefig('pregprey.png')								Zapis wykresu w formacie png.
res = odeint(rhs, p0, ts)											Wykonuje wielokrotnie funkcję dla zakresu argumentów.
	odeintExample
		Przykład wykorzystania odeint.
	odeintExample2
		Przykład wykorzystania odeint.
	Optimisation_example
	Sympy
	TaylorSeries
	WorkingWithInfinity
4.28
	WstawianieNaN
		df = pd.DataFrame([x for x in range(10)])					Tworzy spis danych od 0 do 9.
		print(df.replace(2, np.nan))								Zamienia wartość data z numerem 2 na Not assigNed, jednakże tylko to wyświetla, samo df nie ulega zmianie.
		print(df.replace({9: 100, 5: np.NaN}))						Zamienia wartość data z numerem 9 na 100 oraz wartość data z numerem 5 na Not assigNed, jednakże tylko to wyświetla, samo df nie ulega zmianie.
		df = df.replace(2, np.nan)									Zamienia wartość data z numerem 2 na Not assigNed i w tym przypadku permanentnie zmienia w dataframe.

	Formaty
		"""
		Formaty plikow
			df.to_csv('plik.csv', index=False)
			df.to_excel('plik.xls', index=False)
			df.to_csv('plik.txt', index=False)
		"""
		d = {'one': [1, 1, 1, 1, 1], 'two': [2, 2, 2, 2, 2], 'letter': ['a', 'a', 'b', 'b', 'c']}		Tworzy słownik d z kluczami 'one', 'two', 'letter' i przydziela im wartości?
		df = pd.DataFrame(d)										Tworzy dataframe w oparciu o słownik powyżej.

		print(os.getcwd())
		df.to_csv('plik.txt', index=False)							Zapisuje dataframe do pliku tekstowego w lokalnym directory.

		FileNames = []
		os.chdir('.')       # . to current directory
		for files in os.listdir('.'):
			if files.endswith(".txt"):
				FileNames.append(files)								Szuka nazw plików w foldzerze o typie .txt i dodaje do listy z nazwami FileNames.


		print(FileNames)											Drukuje wszystkie nazwy plików w folderze.
5.12
	kody do wczytywania plików
	W placeholder jest jak usuwać NaN
5.19
	kody do modyfikacji wyglądu wykresów
	
	Wczytywanie plików:
	
	df = pd.read_excel('sprzedaz11.xlsx')
	grupa = df.groupby(["Produkt"])
	df1 = grupa.sum()
	print(df1)
	
	df = pd.read_csv("dosw21.csv", sep="$")
	df = df.dropna(axis="rows", how="any")
	
	df = pd.read_excel("sprzedaz21.xlsx")
	df = pd.DataFrame(df)
	grupa = df.groupby(["Produkt"])["Sprzedaż"].sum()
	
	zad3 = pd.read_csv('dosw11.csv', sep=';')
	zad3c = zad3.dropna(axis="rows", how="any")
	

	plt.show()
///////////////////////////////////////////////
# wczytujesz dane i transponujesz je czyli kolumne zmieniasz w wiersz a wiersz w kolumne
df = pd.read_excel("./2020i2021/z3/handel3.xlsx").T
# po transpozycji kolumny nazywają się 0 i 1 więc zmieniasz ich nazwy na takie jakie chcesz
# po transpozycji na indexach czyli tak jakby nazwie każdego wiersza masz zduplikowane nazwy czyli 2x hipermarkety i żeby nie bawić sie w regex(bo przy duplikatach dodaje ci .1) to standaryzujesz nazwy
df = df.rename(columns={0: "Rok", 1: "Wartosc"}, index={
               "hipermarkety.1": "hipermarkety", "supermarkety.1": "supermarkety", "domy towarowe.1": "domy towarowe", "domy handlowe.1": "domy handlowe"})
# usuwasz indexy czyli wspomiane wyżej opisania wierszy
df.reset_index(inplace=True)
# zmieniasz nazwe index(domyślnie po resecie) na typ czy co tam sobie wyśnisz
df = df.rename(columns={"index": "Typ"})
# i tutaj już normalne rzeczy
wszystko1 = df[df["Rok"] == 2017]["Wartosc"].sum()
x1 = df[df["Rok"] == 2017].groupby("Typ")["Wartosc"].sum()
x1 /= wszystko1
plt.pie(x1, labels=df["Typ"].unique())
plt.show()
/////////////////////////////////////////////////

df = pd.read_csv("./2020i2021/z2/nieruchomosci2.csv", sep=";").T
df = df.rename(columns={0: "metraż", 1: "rok", 2: "cena"}, index={"rynek pierwotny.1": "rynek pierwotny", "rynek pierwotny.2": "rynek pierwotny",
                                                                  "rynek pierwotny.3": "rynek pierwotny", "rynek wtórny.1": "rynek wtórny", "rynek wtórny.2": "rynek wtórny", "rynek wtórny.3": "rynek wtórny", })
df.reset_index(inplace=True)
df = df.rename(columns={"index": "rynek"})
df["cena"] = df["cena"].str.replace(" ", "")
df["cena"] = df["cena"].apply(pd.to_numeric)
wszystko = df["cena"].sum()
pogrupowane = df.groupby("rynek")["cena"].sum()
pogrupowane /= wszystko
plt.pie(pogrupowane, labels=df["rynek"].unique(),
        autopct='%1.1f%%')
plt.title("Procentowy zysk od metra w zależności od rynku w roku 2018")
plt.show()
////////////////////////////////////
