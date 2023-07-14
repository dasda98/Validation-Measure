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
            "Recall": self.recall(),
            "Specificity": self.specificity(),
            "Precision": self.precision(),
            "Accuracy": self.accuracy(),
            "F-score": self.f_score(),
            "Matthews Correlation": self.matthews_correlation(),
            "Balanced Accuracy": self.balanced_accuracy(),
            "Cohen's Kappa": self.cohen_kappa(),
            "G-mean": self.g_mean()
        }

        return dic


test = Metric(c_11=389, c_00=31806, c_01=351, c_10=49)
full = test.all_metrics()

for k, v in full.items():
    print('{k}: {v:.4f}'.format(k=k, v=v))