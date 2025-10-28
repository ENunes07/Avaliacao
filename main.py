from classes.carro_passeio import CarroPasseio
from classes.caminhao_carga import CaminhaoCarga

def main():
    carro = CarroPasseio("Toyota", "Corolla", 2020, "CHS12345", "Prata", 45000, 4, "Gasolina")
    caminhao = CaminhaoCarga("Volvo", "FH 540", 2019, "CHS67890", "Branco", 180000, 25.0, 6)

    print("\n=== 🚗 Carro de Passeio ===")
    carro.exibir_informacoes(detalhado=True)
    carro.registrar_manutencao("Troca de óleo", 250)
    carro.calcular_depreciacao(5, taxa_extra=0.07)

    print("\n=== 🚚 Caminhão de Carga ===")
    caminhao.exibir_informacoes(detalhado=True)
    caminhao.registrar_manutencao("Revisão dos freios", 1200)
    caminhao.registrar_vistoria("Inspeção anual")

if __name__ == "_main_":
    main()