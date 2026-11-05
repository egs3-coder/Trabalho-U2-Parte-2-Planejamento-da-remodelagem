# Hemotrack · Rota Vital — Trabalho U2 · Parte 2

Planejamento da remodelagem do Rota Vital: DDD, arquitetura em três camadas, projeção com microsserviços e três cenários com orçamento.
Infraestrutura de Software · ADS · CESAR School · 2026.2

## Equipe

| Integrante | Papel |
| --- | --- |
| Ewerton Guilherme da Silva | Product Owner |
| Pablo Arthur Eustáquio de Lima | Backend Developer |
| João Ricardo Alves de Brito | Backend Developer |
| Lucas Aprigio dos Santos | Backend Developer |
| Saulo Eduardo Almeida dos Santos | Backend Developer |
| Thiago Cardozo da Conceição | Frontend / UI Designer |
| Eloi de Lima Sousa | Frontend / UI Designer |

## Estrutura

```
docs/arquitetura/
├── adr/
│   ├── 0001-decomposicao.md          # monolito modular, Transporte extraído primeiro
│   └── 0002-eventos-com-outbox.md    # eventos entre contextos com outbox transacional
├── contexto/
│   ├── mapa-de-contextos.mmd
│   └── agregado-requisicao.mmd
├── camadas/regra-de-dependencia.mmd
├── microsservicos/
│   ├── comunicacao.mmd
│   └── saga-atender-requisicao.mmd
├── cenarios/
│   ├── baixo.mmd
│   ├── moderado.mmd
│   └── alto.mmd
└── orcamento.xlsx                    # Lei de Little e orçamento dos três cenários
features/alocar_bolsa.feature         # cenário Gherkin (executado na Parte 3)
```

## Resumo

- **Bounded contexts:** Estoque, Requisição (core), Expedição, Transporte (core), Rede.
- **Decisão:** monolito modular em três camadas; projeção para quatro microsserviços (ADR 0001).
- **Cenários:** baixo US$ 47/mês (US$ 0,0104 por pedido) · moderado US$ 148/mês (US$ 0,0033) · alto US$ 470/mês (US$ 0,0013). Preços on-demand consultados em 04/11/2026; fontes na planilha.

Os diagramas `.mmd` são Mermaid e renderizam direto no GitHub dentro de blocos ```` ```mermaid ````, ou em https://mermaid.live.
