from classes.veiculo import Veiculo

class CaminhaoCarga(Veiculo):
    def _init_(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem, capacidade_toneladas, eixos):
        super()._init_(marca, modelo, ano_fabricacao, chassi, cor, quilometragem)
        self.__capacidade_toneladas = capacidade_toneladas
        self.__eixos = eixos

    def registrar_vistoria(self, motivo, multa=0):
        """Simula sobrecarga com parâmetro opcional"""
        print(f"🚨 Vistoria registrada: {motivo}. Multa: R${multa:.2f}")

    def exibir_informacoes(self, detalhado=False):
        super().exibir_informacoes(detalhado)
        if detalhado:
            print(f"Capacidade de carga: {self.__capacidade_toneladas} toneladas")
            print(f"Número de eixos: {self.__eixos}")