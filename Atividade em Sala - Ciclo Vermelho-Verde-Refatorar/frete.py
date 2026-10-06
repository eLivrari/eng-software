# Padrão de projeto aplicado: STRATEGY
#
# Participantes:
#   - Strategy ........... FretePadrao, FreteExpresso e RetiradaNaLoja
#                          (todas têm o método calcular(peso_kg))
#   - Context ............ CalculadoraFrete


class FretePadrao:
    def calcular(self, peso_kg):
        return 10.00 + 2.00 * peso_kg


class FreteExpresso:
    def calcular(self, peso_kg):
        return 20.00 + 3.50 * peso_kg


class RetiradaNaLoja:
    def calcular(self, peso_kg):
        return 0.00


class CalculadoraFrete:
    estrategias = {
        "padrao": FretePadrao(),
        "expresso": FreteExpresso(),
        "retirada": RetiradaNaLoja(),
    }

    def calcular(self, modalidade, peso_kg):
        if peso_kg < 0:
            raise ValueError("peso não pode ser negativo")
        if modalidade not in self.estrategias:
            raise ValueError(f"modalidade desconhecida: {modalidade}")
        return self.estrategias[modalidade].calcular(peso_kg)


def calcular_frete(modalidade, peso_kg):
    return CalculadoraFrete().calcular(modalidade, peso_kg)


# AUTOAVALIAÇÃO
#
# Última execução da suíte: 5 passed (saída em resultado_testes.txt).
#
# Critérios:
#   1. Testes em arquivo separado, um para cada variação ........ ATINGIDO
#   2. Três commits: red, green e refactor ...................... ATINGIDO
#   3. Commit red só com os testes .............................. ATINGIDO
#   4. Padrão Strategy aplicado e nomeado em comentário ......... ATINGIDO
#   5. Todos os testes passando, saída registrada em arquivo .... ATINGIDO
#
# O que mudou da fase verde para a refatorada:
#   Na verde era uma função só com if/elif para cada modalidade. Na refatorada
#   cada modalidade virou uma classe com o método calcular, e a
#   CalculadoraFrete escolhe a classe certa por um dicionário. Para criar uma
#   modalidade nova basta criar uma classe e colocá-la no dicionário.
#
# O que deu mais trabalho: fazer a refatoração sem mudar o comportamento, para
# os testes continuarem passando sem alteração.
#
