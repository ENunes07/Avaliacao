É um sistema que controla veículos de uma frota, mostrando suas informações e registrando manutenções.
Ele foi feito pra usar herança, polimorfismo e encapsulamento, que são conceitos da programação orientada a objetos.


---

Estrutura do projeto

O programa está dividido em partes (pastas e arquivos):
Veiculo → é a classe principal, com tudo que todo veículo tem.
CarroPasseio → é um tipo de veículo.
CaminhaoCarga → é outro tipo de veículo.
main → é onde o programa principal roda e mostra tudo funcionando.



---

Classe Veículo

Essa é a base.
Aqui ficam as informações que todo tipo de veículo tem, como:
marca
modelo
ano
cor
chassi
quilometragem
Ela também tem funções para:
mostrar informações (pode mostrar tudo ou só o básico)
registrar manutenções



---

Classe CarroPasseio

Essa classe herda tudo da classe Veículo (ou seja, usa tudo que ela já tem).
Mas adiciona algumas coisas que só carros de passeio têm, como:

número de portas
tipo de combustível
E também tem uma função que calcula quanto o carro desvalorizou com o tempo (depreciação).


---

Classe CaminhaoCarga

Essa também vem da classe Veículo, mas é voltada pra caminhões.
Ela tem:

capacidade de carga (em toneladas)
número de eixos
E pode registrar vistorias e multas.


---

O que o programa faz quando roda?

No arquivo principal (main):

Cria um carro e um caminhão.
Mostra as informações de cada um.
Registra manutenções.
Mostra depreciação (no carro).
Mostra vistorias (no caminhão).
Tudo aparece na tela de forma organizada.


---
Conceitos usados (explicados de forma simples)
Conceito	Significado
Herança	Quando uma classe “filha” aproveita o que a classe “mãe” já tem.
Encapsulamento	Serve pra proteger os dados do veículo (ninguém muda sem querer).
Polimorfismo	O mesmo nome de função pode fazer coisas diferentes dependendo do tipo de veículo.
Sobrescrita	A classe filha muda um comportamento da classe mãe pra adaptar ao seu tipo.



---
Em resumo:
Veiculo → base com dados comuns.
CarroPasseio → herda e adiciona coisas de carro.
CaminhaoCarga → herda e adiciona coisas de caminhão.
main → cria e testa tudo.