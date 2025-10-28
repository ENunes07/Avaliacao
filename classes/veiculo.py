class Veiculo:
    def _init_(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem):
        
        self.__marca = marca
        self.__modelo = modelo
        self.__ano_fabricacao = ano_fabricacao
        self.__chassi = chassi
        self.__cor = cor
        self.__quilometragem = quilometragem

    
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_quilometragem(self):
        return self.__quilometragem

    def set_quilometragem(self, nova_km):
        if nova_km >= self.__quilometragem:
            self.__quilometragem = nova_km
        else:
            print("⚠️ Quilometragem não pode ser reduzida.")

    
    def registrar_manutencao(self, tipo, custo):
        print(f"🛠️ Manutenção registrada: {tipo} — Custo: R${custo:.2f}")

    
    def exibir_informacoes(self, detalhado=False):
        if detalhado:
            print("=== INFORMAÇÕES DETALHADAS DO VEÍCULO ===")
            print(f"Marca: {self.__marca}")
            print(f"Modelo: {self.__modelo}")
            print(f"Ano de Fabricação: {self.__ano_fabricacao}")
            print(f"Chassi: {self.__chassi}")
            print(f"Cor: {self.__cor}")
            print(f"Quilometragem: {self.__quilometragem} km")
        else:
            print(f"{self._marca} {self.modelo} - {self._quilometragem} km")