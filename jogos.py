import random


class Aposta:
    def __init__(
        self,
        qtdd_numeros=6,
        limite=60,
        tem_trevo=False,
        qtdd_trevos=2,
        limite_trevos=6,
    ):
        self.numeros = []
        self.trevos = []
        self.qtdd_numeros = qtdd_numeros
        self.limite = limite
        self.tem_trevo = tem_trevo
        self.qtdd_trevos = qtdd_trevos
        self.limite_trevos = limite_trevos

    def sortear_numeros(self, quantidade, limite):
        numeros = set()
        while len(numeros) < quantidade:
            numeros.add(random.randrange(1, limite + 1))
        return sorted(numeros)

    def palpite(self):
        self.numeros = self.sortear_numeros(self.qtdd_numeros, self.limite)
        self.trevos = (
            self.sortear_numeros(self.qtdd_trevos, self.limite_trevos)
            if self.tem_trevo
            else []
        )
        return self.numeros, self.trevos


megasena = Aposta(qtdd_numeros=6, limite=60)
quina = Aposta(qtdd_numeros=5, limite=80)
lotofacil = Aposta(qtdd_numeros=15, limite=25)
milionaria = Aposta(qtdd_numeros=6, limite=50, tem_trevo=True)
numeros, trevos = milionaria.palpite()

print("MEGASENA:", megasena.palpite())
print("QUINA:", quina.palpite())
print("LOTOFÁCIL:", lotofacil.palpite())
print("MILIONÁRIA NÚMEROS:", numeros, "TREVOS:", trevos)
