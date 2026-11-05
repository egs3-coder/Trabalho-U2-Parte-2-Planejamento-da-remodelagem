# language: pt
Funcionalidade: Alocar bolsas a uma requisição
  Para que o hospital receba apenas bolsas seguras
  Como atendente do hemocentro
  Quero que o sistema recuse bolsas incompatíveis ou que vencem antes da entrega

  Contexto:
    Dado que agora são "2026-11-24 19:00"
    E existe a requisição "REQ-001" de prioridade "URGENCIA" do "Hospital Sintético A"
    E a requisição tem o item "ITEM-1" de "CONCENTRADO_HEMACIAS" para receptor "A+" com quantidade 2

  Cenário: Alocar bolsa compatível e válida
    Quando a atendente alocar a bolsa "B-100" do tipo "O-" com validade "2026-12-10 00:00" ao item "ITEM-1"
    Então a alocação é aceita
    E o item "ITEM-1" tem 1 bolsa alocada

  Esquema do Cenário: Recusar bolsa que viola uma invariante
    Quando a atendente alocar a bolsa "<bolsa>" do tipo "<tipo>" com validade "<validade>" ao item "ITEM-1"
    Então a alocação é recusada com a mensagem "<mensagem>"
    E o item "ITEM-1" tem 0 bolsas alocadas
    E a requisição "REQ-001" continua com status "EM_ATENDIMENTO"

    Exemplos:
      | bolsa | tipo | validade         | mensagem                              |
      | B-200 | B+   | 2026-12-10 00:00 | Tipo sanguíneo incompatível           |
      | B-300 | O-   | 2026-11-24 21:00 | Bolsa vence antes da entrega prevista |
