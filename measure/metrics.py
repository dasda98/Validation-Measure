import math as m


class Metric:

    def __init__(self, c_11, c_00, c_10, c_01):
        self.c_11 = c_11
        self.c_00 = c_00
        self.c_10 = c_10
        self.c_01 = c_01

        self.a_0 = c_00 + c_01
        self.a_1 = c_10 + c_11

        self.b_0 = c_00 + c_10
        self.b_1 = c_01 + c_11

        self.n = self.c_00 + self.c_11 + self.c_10 + self.c_01
        self.m = 2

    def recall(self):
        return self.c_11 / self.a_1

    def precision(self):
        return self.c_11 / self.b_1

    def specificity(self):
        return self.c_00 / self.a_0

    def accuracy(self):
        return (self.c_00 + self.c_11) / self.n

    def f_score(self, beta=1):
        return ((1 + m.pow(beta, 2)) * self.c_11) / (
                    (1 + m.pow(beta, 2)) * self.c_11 + m.pow(beta, 2) * self.c_10 + self.c_01)

    def matthews_correlation(self):
        return (self.c_11 * self.c_00 - self.c_01 * self.c_10) / (m.sqrt(self.b_1 * self.a_1 * self.b_0 * self.a_0))

    def balanced_accuracy(self):
        return 1 / self.m * ((self.c_00 / self.a_0) + (self.c_11 / self.a_1))

    def cohen_kappa(self):
        return (self.n * (self.c_00 + self.c_11) - (self.a_0 * self.b_0 + self.a_1 + self.b_1)) / \
               (m.pow(self.n, 2) - (self.a_0 * self.b_0 + self.a_1 + self.b_1))

    def g_mean(self):
        return m.sqrt(self.recall() * self.specificity())

    def all_metrics(self):
        dic = {
                "Recall": f'{self.recall():.4f}',
                "Specificity": f'{self.specificity():.4f}',
                "Precision": f'{self.precision():.4f}',
                "Accuracy": f'{self.accuracy():.4f}',
                "F-score": f'{self.f_score():.4f}',
                "Matthews Correlation": f'{self.matthews_correlation():.4f}',
                "Balanced Accuracy": f'{self.balanced_accuracy():.4f}',
                "Cohen's Kappa": f'{self.cohen_kappa():.4f}',
                "G-mean": f'{self.g_mean():.4f}',
        }

        return dic


explained = {
    "Recall": "Mierzy zdolność klasyfikatora do wykrywania wszystkich pozytywnych przypadków.Jest obliczana jako iloraz TP do sumy TP i FN. Czułość informuje nas o tym, jak wiele z prawdziwie pozytywnych przypadków zostało wykrytych przez klasyfikator.",
    "Specificity": "Mierzy zdolność klasyfikatora do rozpoznawania wszystkich negatywnych przypadków. Jest obliczana jako iloraz TN do sumy TN i FP. Specyficzność informuje nas o tym, jak wiele z prawdziwie negatywnych przypadków zostało rozpoznanych przez klasyfikator.",
    "Precision": "Mierzy zdolność klasyfikatora do poprawnego identyfikowania pozytywnych przypadków spośród wszystkich pozytywnie sklasyfikowanych przypadków. Jest obliczana jako iloraz TP do sumy TP i FP. Precyzja informuje nas o tym, jak często klasyfikator poprawnie przewiduje pozytywne przypadki.",
    "Accuracy": "Mierzy procent poprawnie sklasyfikowanych próbek spośród wszystkich próbek. Jest obliczana jako iloraz sumy poprawnie sklasyfikowanych próbek (TP i TN) do ogólnej liczby próbek. Jednak ta miara może być myląca w przypadku niezrównoważonych zbiorów danych, gdzie jedna klasa dominuje nad drugą",
    "F-score": "Jest uogólnieniem F1-score, gdzie można dostosować wagę precyzji i czułości poprzez parametr beta. Gdy beta = 1, jest to równoważne F1-score. Gdy beta < 1, większy nacisk kładzie się na precyzję, a gdy beta > 1, większy nacisk kładzie się na czułość.",
    "Matthews": "Korelacja Matthewsa (CC) jest miarą statystyczną wykorzystywaną do oceny stopnia zgodności między dwiema zmiennymi binarnymi. Jest szczególnie przydatna w przypadku niezrównoważonych zestawów danych, w których jedna z klas jest znacznie bardziej liczna niż druga. Wynik korelacji Matthewsa mieści się w przedziale od -1 do 1. Wartości bliskie 1 oznaczają silną zgodność między zmiennymi, wartości bliskie -1 oznaczają silną negatywną zgodność, a wartość bliska 0 wskazuje brak zgodności.",
    "Balanced": "Balanced accuracy (zrównoważona dokładność) jest miarą oceny jakości klasyfikacji binarnej w przypadku niezrównoważonych zestawów danych. Różni się od standardowej dokładności (accuracy), ponieważ uwzględnia asymetrię w rozkładzie klas. Wartości zrównoważonej dokładności mieszczą się w zakresie od 0 do 1, gdzie wartość 1 oznacza idealną zdolność klasyfikatora do rozpoznawania obu klas.",
    "Cohen's": "Cohen's Kappa (kappa Cohena) to statystyczna miara używana do oceny stopnia zgodności między dwoma oceniami lub klasyfikacjami wykonanymi przez różnych oceniających. Jest szczególnie przydatna w przypadku, gdy oceny są subiektywne lub gdy występuje niezrównoważenie w rozkładzie klas. Wynik Cohen's Kappa mieści się w przedziale od -1 do 1. Wartość 1 oznacza doskonałą zgodność, wartość 0 oznacza zgodność przypadkową, a wartość -1 oznacza całkowitą niezgodność.",
    "G-mean": "Wartość G-mean mieści się w zakresie od 0 do 1, gdzie wartość 1 oznacza idealną zdolność klasyfikatora do rozpoznawania zarówno pozytywnych, jak i negatywnych przypadków. Miara G-mean jest szczególnie przydatna w przypadku niezrównoważonych danych, gdzie jedna klasa dominuje nad drugą. Wysoka wartość G-mean wskazuje na równowagę między zdolnością klasyfikatora do wykrywania pozytywnych przypadków a zdolnością do rozpoznawania negatywnych przypadków, co jest pożądanym wynikiem w niezrównoważonych zestawach danych.",
}