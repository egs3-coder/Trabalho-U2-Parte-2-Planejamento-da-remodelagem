# language: pt
Funcionalidade: Alocar bolsas a uma requisição
  Para que o hospital receba apenas bolsas seguras
  Como atendente do hemocentro
  Quero que o sistema recuse bolsas incompatíveis ou que vencem antes da entrega

  # I1: a compatibilidade depende do hemocomponente.
  #   Hemácias: os antígenos ABO da bolsa precisam existir no receptor; receptor Rh- só recebe Rh-.
  #   Plasma: regra invertida; os antígenos do receptor precisam existir na bolsa (AB serve a todos); Rh não conta.

  Contexto:
    Dado que agora são "2026-11-24 19:00"
    E existe a requisição "REQ-001" de prioridade "URGENCIA" do "Hospital Sintético A"
    E a requisição tem o item "ITEM-1" de "CONCENTRADO_HEMACIAS" para receptor "A+" com quantidade 2
    E a requisição tem o item "ITEM-2" de "PLASMA_FRESCO_CONGELADO" para receptor "A+" com quantidade 2

  Cenário: Alocar bolsa compatível e válida
    Quando a atendente alocar a bolsa "B-100" de "CONCENTRADO_HEMACIAS" do tipo "O-" com validade "2026-12-10 00:00" ao item "ITEM-1"
    Então a alocação é aceita
    E o item "ITEM-1" tem 1 bolsa alocada

  Esquema do Cenário: A compatibilidade depende do hemocomponente
    Quando a atendente alocar a bolsa "<bolsa>" de "<hemocomponente>" do tipo "<tipo>" com validade "2026-12-10 00:00" ao item "<item>"
    Então a alocação é <resultado>

    Exemplos:
      | item   | bolsa | hemocomponente          | tipo | resultado                                             |
      | ITEM-1 | B-100 | CONCENTRADO_HEMACIAS    | O-   | aceita                                                |
      | ITEM-1 | B-200 | CONCENTRADO_HEMACIAS    | B+   | recusada com a mensagem "Tipo sanguíneo incompatível" |
      | ITEM-2 | P-100 | PLASMA_FRESCO_CONGELADO | AB-  | aceita                                                |
      | ITEM-2 | P-200 | PLASMA_FRESCO_CONGELADO | O-   | recusada com a mensagem "Tipo sanguíneo incompatível" |

  Cenário: Recusar bolsa de hemocomponente diferente do item
    Quando a atendente alocar a bolsa "P-300" de "PLASMA_FRESCO_CONGELADO" do tipo "AB-" com validade "2026-12-10 00:00" ao item "ITEM-1"
    Então a alocação é recusada com a mensagem "Hemocomponente diferente do pedido"
    E o item "ITEM-1" tem 0 bolsas alocadas

  Esquema do Cenário: Recusar bolsa que viola uma invariante sem alterar a requisição
    Quando a atendente alocar a bolsa "<bolsa>" de "CONCENTRADO_HEMACIAS" do tipo "<tipo>" com validade "<validade>" ao item "ITEM-1"
    Então a alocação é recusada com a mensagem "<mensagem>"
    E o item "ITEM-1" tem 0 bolsas alocadas
    E a requisição "REQ-001" continua com status "EM_ATENDIMENTO"

    Exemplos:
      | bolsa | tipo | validade         | mensagem                              |
      | B-200 | B+   | 2026-12-10 00:00 | Tipo sanguíneo incompatível           |
      | B-300 | O-   | 2026-11-24 21:00 | Bolsa vence antes da entrega prevista |
