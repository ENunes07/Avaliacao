from classes.veiculo import Veiculo

class CarroPasseio(Veiculo):
    def _init_(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem, numero_portas, tipo_combustivel):
        super()._init_(marca, modelo, ano_fabricacao, chassi, cor, quilometragem)
        self.__numero_portas = numero_portas
        self.__tipo_combustivel = tipo_combustivel

    def calcular_depreciacao(self, anos_uso, taxa_extra=0.05):
        """Polimorfismo por simulação de sobrecarga"""
        base = 0.10 * anos_uso
        total = base + (taxa_extra * anos_uso)
        print(f"💰 Depreciação total: {total*100:.1f}% após {anos_uso} anos (Taxa extra {taxa_extra*100:.1f}%)")

    
    def exibir_informacoes(self, detalhado=False):
        super().exibir_informacoes(detalhado)
        if detalhado:
            print(f"Número de portas: {self.__numero_portas}")
            print(f"Tipo de combustível: {self.__tipo_combustivel}")