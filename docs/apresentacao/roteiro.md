# Roteiro da apresentação — 24/11

Até **10 minutos** de apresentação + 5 minutos de perguntas. O professor vai chamar **pessoas diferentes** para explicar o domínio, as contas e a saga: no ensaio, cada integrante explica as três partes abaixo sem olhar o slide.

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

**Disponibilidade composta (série):** ALB 99,99% × Fargate em 2 zonas 99,99% × RDS Multi-AZ 99,95% = **99,93%** ≈ 31 min fora por mês (43.800 min × 0,0007). Fecha 99,9% (44 min), **não** fecha 99,95% (22 min); por isso o alto mira 99,9%. Com Aurora Multi-AZ (99,99%) daria 99,97%, mas não foi orçado. O SQS fica fora da conta porque o outbox segura os eventos se a fila cair.

**Gatilho do ADR 0001:** leituras/s = caixas ÷ 30 s. Moderado 80 ÷ 30 = 2,7/s (fica no monolito); alto 600 ÷ 30 = 20/s (passa de 10/s, extrai o Transporte).

**Conexões com o banco:** L_db = λ × W_db. No alto, 120 × 0,05 = 6 conexões ocupadas em média, por isso o banco não é o gargalo.

**Custo por pedido:** custo do mês ÷ pedidos do mês.

| Cenário | Custo/mês | Pedidos/mês | Custo por pedido |
| --- | --- | --- | --- |
| Baixo (Render) | US$ 47,00 | 4.500 | US$ 0,0104 |
| Moderado (AWS) | US$ 152,07 | 45.000 | US$ 0,0034 |
| Alto (AWS) | US$ 472,88 | 360.000 | US$ 0,0013 |

**Fontes:** preços conferidos em 12/11/2026 na [AWS Pricing Calculator (moderado)](https://calculator.aws/#/estimate?id=71d5f083738612902c899bf5a25a2fd44c668a7d), [AWS Pricing Calculator (alto)](https://calculator.aws/#/estimate?id=e9376074563bc3ece0ea5427d2302774428e035e) e em [render.com/pricing](https://render.com/pricing). Única correção em relação à primeira versão: RDS db.t4g.small de 0,064 para 0,065 USD/h.

**Mensagem central:** o custo total sobe 10×, mas o custo por pedido cai 8×, porque a infraestrutura fixa se dilui.

## Domínio: o que todos precisam saber explicar

**Compatibilidade (I1) depende do hemocomponente.** Hemácias levam antígenos: a bolsa não pode ter antígeno que o receptor não tenha (O− serve a todos). Plasma leva anticorpos, então a regra se inverte: o receptor não pode ter antígeno que a bolsa não tenha (AB serve a todos, O só para O) e o Rh não conta. Exemplo para receptor A+: hemácias O− aceita; plasma O− recusa; plasma AB− aceita.

## Saga: o que todos precisam saber explicar

**Orquestração pura.** A Requisição manda um comando (`ReservarBolsas`, `MontarRemessa`, `AbrirViagem`) e cada serviço responde só para ela (`BolsasReservadas`, `RemessaMontada`/`RemessaFalhou`, `ViagemIniciada`, `EntregaConcluida`). A Expedição não fala com o Transporte. Por quê: 5 passos, compensação condicional e um ponto sem volta; o estado fica num lugar só. Falha no passo 4 → desfaz 3 e 2 → tenta de novo do passo 2.

## Perguntas prováveis

- **Por que monolito modular e não microsserviços já?** Squad de 7, uma esteira, carga baixa; microsserviços custariam mais em operação do que a carga justifica (ADR 0001).
- **Por que o Transporte seria o primeiro a sair?** A telemetria tem carga muito diferente do resto (milhares de leituras por minuto) e precisa escalar sozinha.
- **O que acontece se a bolsa estiver danificada na expedição?** A saga compensa: desaloca, descarta a bolsa, libera a reserva e tenta reservar de novo.
- **Por que us-east-1 e não São Paulo?** O banco em sa-east-1 custa cerca do dobro; com dados sintéticos a latência não afeta. Em produção real, a LGPD pediria revisão.
- **De onde veio o "7 por instância"?** Estimativa de 10 requisições simultâneas por vCPU com 70% de folga; será medida no teste de carga da Parte 3.
- **Por que o limite de 10 leituras/s e não 50?** Precisava ficar entre o moderado (2,7/s, fica) e o alto (20/s, sai); 10/s dá folga de quase 4× sobre o moderado e será medido na Parte 3.
- **A camada de aplicação acessa a de dados?** Não. Usa as interfaces do domínio (`RequisicaoRepository`, `EstoqueGateway`); dados implementa essas interfaces e o Spring injeta. ArchUnit barra `aplicacao → dados`.
- **Por que orquestrada e não coreografada?** Com coreografia, a regra "falhou na expedição → desfaz alocação e reserva" ficaria espalhada em três serviços.
