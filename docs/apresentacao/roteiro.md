# Roteiro da apresentação — 24/11

Até **10 minutos** de apresentação + 5 minutos de perguntas. Qualquer integrante pode ser chamado para explicar qualquer parte, inclusive as contas.

| Bloco | Tempo | Quem | O que mostrar |
| --- | --- | --- | --- |
| 1. O que a Parte 1 entregou | 1 min | Ewerton | Container Docker, testes (TDD) e esteira de CI/CD funcionando |
| 2. Domínio remodelado | 3 min | Pablo + João | Subdomínios (core × suporte × genérico), 5 bounded contexts, glossário ("Bolsa" e "Entrega" com dois sentidos), [mapa de contextos](../arquitetura/img/mapa-de-contextos.png), agregado Requisição e o cenário Gherkin |
| 3. Três camadas e microsserviços | 3 min | Lucas + Saulo | [Regra de dependência](../arquitetura/img/regra-de-dependencia.png), árvore de pacotes, lógico × físico, [microsserviços](../arquitetura/img/comunicacao.png), [saga com compensação](../arquitetura/img/saga-atender-requisicao.png), ADR 0001 e ADR 0002 |
| 4. Três cenários e orçamento | 3 min | Thiago + Eloi | Premissas, Lei de Little, diagramas [baixo](../arquitetura/img/baixo.png) · [moderado](../arquitetura/img/moderado.png) · [alto](../arquitetura/img/alto.png), orçamento e custo por pedido |

## Contas que todos precisam saber explicar

**Lei de Little:** L = λ × W (requisições sendo atendidas ao mesmo tempo).

| Cenário | λ (pico) | W | L | Instâncias pela conta (L ÷ 7) | Adotadas | Por quê |
| --- | --- | --- | --- | --- | --- | --- |
| Baixo | 3 req/s | 0,20 s | 0,6 | 1 | 1 | 99,0% tolera reinício |
| Moderado | 20 req/s | 0,20 s | 4 | 1 | 2 | 99,9% exige uma segunda instância em outra zona |
| Alto | 120 req/s | 0,25 s | 30 | 5 | 3 a 6 + 2 do Transporte | autoscaling com folga N+1 no pico |

**Conexões com o banco:** L_db = λ × W_db. No alto, 120 × 0,05 = 6 conexões ocupadas em média, por isso o banco não é o gargalo.

**Custo por pedido:** custo do mês ÷ pedidos do mês.

| Cenário | Custo/mês | Pedidos/mês | Custo por pedido |
| --- | --- | --- | --- |
| Baixo (Render) | US$ 47,00 | 4.500 | US$ 0,0104 |
| Moderado (AWS) | US$ 148,40 | 45.000 | US$ 0,0033 |
| Alto (AWS) | US$ 469,78 | 360.000 | US$ 0,0013 |

**Mensagem central:** o custo total sobe 10×, mas o custo por pedido cai 8×, porque a infraestrutura fixa se dilui.

## Perguntas prováveis

- **Por que monolito modular e não microsserviços já?** Squad de 7, uma esteira, carga baixa; microsserviços custariam mais em operação do que a carga justifica (ADR 0001).
- **Por que o Transporte seria o primeiro a sair?** A telemetria tem carga muito diferente do resto (milhares de leituras por minuto) e precisa escalar sozinha.
- **O que acontece se a bolsa estiver danificada na expedição?** A saga compensa: desaloca, descarta a bolsa, libera a reserva e tenta reservar de novo.
- **Por que us-east-1 e não São Paulo?** O banco em sa-east-1 custa cerca do dobro; com dados sintéticos a latência não afeta. Em produção real, a LGPD pediria revisão.
- **De onde veio o "7 por instância"?** Estimativa de 10 requisições simultâneas por vCPU com 70% de folga; será medida no teste de carga da Parte 3.
