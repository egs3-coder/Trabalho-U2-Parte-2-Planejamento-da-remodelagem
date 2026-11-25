# Pendências até a entrega (26/11, 19h15)

- [ ] **Pré-entrega (19/11, até 19h15, sem nota):** enviar [`entregas/Hemotrack-Pre-entrega-Secoes-A-e-C.pdf`](entregas/Hemotrack-Pre-entrega-Secoes-A-e-C.pdf) e [`entregas/Hemotrack-Pre-entrega-Secoes-A-e-C-Slides.pdf`](entregas/Hemotrack-Pre-entrega-Secoes-A-e-C-Slides.pdf) no Classroom.
- [x] **Devolutiva do professor (13/11) aplicada:**
    - [x] I1 considera o hemocomponente (plasma inverte a regra); Gherkin com exemplos de plasma
    - [x] ADR 0001: gatilho de extração do Transporte ajustado para ~10 leituras/s (alto tem 20/s)
    - [x] Disponibilidade composta pelos SLAs (99,93%): alto passou de 99,95% para 99,9%
    - [x] Saga: orquestração pura (Expedição responde à Requisição, que comanda o Transporte)
    - [x] Diagrama de dependência sem seta aplicação → dados
    - [x] Legendas do README com US$ 152,07 e US$ 472,88
    - [x] Uso de IA: quem conferiu cada parte
- [x] **Cada responsável confirma a validação registrada em "Uso de IA"** (confirmado em 25/11):
    - [x] Pablo e João: domínio e regra ABO de plasma
    - [x] Lucas e Saulo: camadas, saga e ADRs
    - [x] Thiago e Eloi: contas e SLAs
    - [x] Ewerton: revisão final
- [x] **Gherkin do documento (B.3) igual ao [`features/alocar_bolsa.feature`](../features/alocar_bolsa.feature)**, que é o arquivo executado na Parte 3; PDF do documento regenerado (12 páginas).
- [ ] **Parte 3:** levar `docs/arquitetura/` (mesma estrutura) e `features/` para o repositório do código, junto da esteira da Parte 1.
- [ ] **Ensaio cruzado:** cada integrante explica domínio, contas e saga (o professor vai sortear quem fala).
- [x] **Conferir os preços** (feito em 12/11/2026) na fonte oficial (o professor não aceita preço sugerido por IA):
    - [x] Render (cenário baixo): render.com/pricing
    - [x] AWS (moderado e alto): calculator.aws, região US East (N. Virginia), com Fargate ARM, ALB, RDS PostgreSQL Multi-AZ (db.t4g.small e db.t4g.large), gp3, IPv4, SQS, CloudWatch Logs e S3
    - [x] Atualizar valores e data em [`arquitetura/orcamento.xlsx`](arquitetura/orcamento.xlsx) e no documento
- [x] **Revisar a seção "Uso de IA"** com o que o squad realmente fez e validou.
- [x] **Slides** da apresentação: [`entregas/Hemotrack-Rota-Vital-Parte-2-Slides.pdf`](entregas/Hemotrack-Rota-Vital-Parte-2-Slides.pdf) (16 slides, por dupla).
- [ ] **Ensaiar** com cronômetro seguindo o [roteiro de fala](apresentacao/roteiro-de-fala.md).
- [ ] **Entrega final (26/11, até 19h15):** PDF do documento (até 12 páginas) + PDF dos slides no Classroom; diagramas, planilha e ADRs já estão em `docs/arquitetura/`.

---

# Roteiro de cada responsável (26/11)

Guia rápido para cada integrante: o que falar, **onde está cada coisa no GitHub** e como responder se o professor perguntar como a parte foi validada. A fala completa, palavra por palavra, está no [roteiro de fala](apresentacao/roteiro-de-fala.md); as contas e as perguntas prováveis, no [roteiro da apresentação](apresentacao/roteiro.md). Todos os caminhos abaixo partem da raiz do [repositório](https://github.com/egs3-coder/Trabalho-U2-Parte-2-Planejamento-da-remodelagem).

**Arquivos que todos devem saber abrir:**

| O quê | Onde |
| --- | --- |
| Documento (fonte) | [`docs/arquitetura/documento.md`](arquitetura/documento.md) |
| Documento entregue (PDF, 12 páginas) | [`docs/entregas/Hemotrack-Rota-Vital-Parte-2.pdf`](entregas/Hemotrack-Rota-Vital-Parte-2.pdf) |
| Slides entregues (PDF, 16 slides) | [`docs/entregas/Hemotrack-Rota-Vital-Parte-2-Slides.pdf`](entregas/Hemotrack-Rota-Vital-Parte-2-Slides.pdf) |
| Diagramas (imagem / fonte Mermaid) | [`docs/arquitetura/img/`](arquitetura/img/) · `.mmd` em [`contexto/`](arquitetura/contexto/), [`camadas/`](arquitetura/camadas/), [`microsservicos/`](arquitetura/microsservicos/), [`cenarios/`](arquitetura/cenarios/) |
| Gherkin executado na Parte 3 | [`features/alocar_bolsa.feature`](../features/alocar_bolsa.feature) |
| ADRs | [`docs/arquitetura/adr/`](arquitetura/adr/) |
| Planilha do orçamento | [`docs/arquitetura/orcamento.xlsx`](arquitetura/orcamento.xlsx) |
| Uso de IA (quem validou o quê) | seção **Uso de IA** no fim do [documento](arquitetura/documento.md#uso-de-ia) · slide 15 |

Ordem e tempo: Ewerton (1 min) → Pablo e João (3 min) → Lucas e Saulo (3 min) → Thiago e Eloi (2,5 min) → Ewerton (0,5 min). Total ≈ 10 min.

## Ewerton · abertura, Uso de IA e fechamento (slides 1, 2, 15 e 16)

**O que falar**
- Slide 1: apresenta o squad e a divisão em duplas; avisa que **qualquer um pode responder qualquer parte** (não pular).
- Slide 2: a Parte 1 colocou o sistema no ar (container no Render, PostgreSQL gerenciado, testes e esteira de CI/CD); esse é o cenário baixo. Passa para o Pablo.
- Slide 15: a IA (Claude) gerou o rascunho; cada dupla validou a parte que apresenta; os preços foram levantados pelo squad, sem IA.
- Slide 16: agradece e abre para perguntas.

**Onde está no GitHub**
- Identificação e tabela de responsáveis: início do [`documento.md`](arquitetura/documento.md) (seção "Identificação e premissas").
- Uso de IA: seção "Uso de IA" do [`documento.md`](arquitetura/documento.md#uso-de-ia) e slide [`uso-ia.html`](apresentacao/deck/slides/uso-ia.html).
- Correções da devolutiva: [`README.md`](../README.md) (link para o PR #1) e a lista "Devolutiva do professor" acima.

**Se o professor perguntar como você validou:** "Fiz a revisão final de coerência entre documento, diagramas, README e slides antes de cada entrega: os números (US$ 47 / 152,07 / 472,88, 99,93%, 10 leituras/s) e a regra de plasma batem nos três lugares."

## Pablo · subdomínios, bounded contexts e glossário (slides 3 e 4)

**O que falar**
- Slide 3: core = atender a requisição com a bolsa certa **e** provar a cadeia fria; Estoque, Expedição e Rede são suporte; identidade e notificações são genéricos (compra pronto: Keycloak ou Cognito).
- Slide 4: os 5 bounded contexts (Estoque, Requisição, Expedição, Transporte, Rede); "Bolsa" e "Entrega" mudam de sentido conforme o contexto. Passa para o João.

**Onde está no GitHub**
- Seções **A.1 Subdomínios**, **A.2 Bounded contexts** e **A.3 Glossário** do [`documento.md`](arquitetura/documento.md).
- Slides [`subdominios.html`](apresentacao/deck/slides/subdominios.html) e [`glossario.html`](apresentacao/deck/slides/glossario.html).

**Se o professor perguntar como você validou:** "Comparei os contextos com o fluxo real do hemocentro (requisição → reserva → expedição → transporte → recebimento) e li cada termo do glossário nos dois contextos para confirmar que o sentido muda."

## João · mapa de contextos, agregado, compatibilidade e Gherkin (slides 5 e 6)

**O que falar**
- Slide 5: o mapa segue o caminho da bolsa; cliente-fornecedor entre Estoque → Requisição → Expedição → Transporte; camada anticorrupção para o sensor (Fahrenheit → Celsius); Rede como serviço aberto; conformista com identidade e notificações.
- Slide 6: a Requisição é a raiz do agregado e protege 5 invariantes; I1 depende do hemocomponente (hemácias: O− serve a todos; plasma: regra invertida, AB serve a todos, Rh não conta). Exemplo receptor A+: hemácias O− aceita, plasma O− recusa, plasma AB− aceita. Passa para o Lucas.

**Onde está no GitHub**
- **A.4 Mapa de contextos**, **B.1 Agregado Requisição**, **B.2 História de usuário** e **B.3 Cenário Gherkin** do [`documento.md`](arquitetura/documento.md).
- Diagramas: [`img/mapa-de-contextos.png`](arquitetura/img/mapa-de-contextos.png) e [`img/agregado-requisicao.png`](arquitetura/img/agregado-requisicao.png) (fontes em [`contexto/`](arquitetura/contexto/)).
- Gherkin: [`features/alocar_bolsa.feature`](../features/alocar_bolsa.feature) (igual ao B.3; é o que roda na Parte 3).
- Slides [`mapa.html`](apresentacao/deck/slides/mapa.html) e [`compatibilidade.html`](apresentacao/deck/slides/compatibilidade.html).

**Se o professor perguntar como você validou:** "Conferi a regra ABO de hemácias e de plasma em material de hemoterapia e resolvi à mão cada exemplo do Gherkin contra I1 e I2 antes de aceitar o resultado esperado." (Saber explicar a linha P-200: plasma O− tem anti-A, por isso é recusado para receptor A+.)

## Lucas · camadas, regra de dependência e microsserviços (slides 7 e 8)

**O que falar**
- Slide 7: cada contexto tem apresentação, negócio e dados; todas as setas apontam para o domínio; a aplicação usa interfaces do domínio (`RequisicaoRepository`, `EstoqueGateway`) e a camada de dados as implementa (inversão de dependência); ArchUnit quebra o build se a regra for violada.
- Slide 8: 4 serviços (a Requisição absorve a Rede), um banco para cada; REST só onde o usuário espera a resposta; o resto por eventos SNS/SQS com outbox; telemetria por MQTT. Passa para o Saulo.

**Onde está no GitHub**
- **C.1 O que fica em cada camada**, **C.2 Regra de dependência**, **D.1 Quais contextos viram serviços** e **D.2 Comunicação e dados** do [`documento.md`](arquitetura/documento.md).
- Diagramas: [`img/regra-de-dependencia.png`](arquitetura/img/regra-de-dependencia.png) e [`img/comunicacao.png`](arquitetura/img/comunicacao.png) (fontes em [`camadas/`](arquitetura/camadas/) e [`microsservicos/`](arquitetura/microsservicos/)).
- ADR do outbox: [`adr/0002-eventos-com-outbox.md`](arquitetura/adr/0002-eventos-com-outbox.md).
- Slides [`camadas.html`](apresentacao/deck/slides/camadas.html) e [`microsservicos.html`](apresentacao/deck/slides/microsservicos.html).

**Se o professor perguntar como você validou:** "Comparei cada seta do diagrama com os imports previstos na árvore de pacotes: não existe seta de aplicação para dados. E li as regras ArchUnit contra a inversão de dependência."

## Saulo · pacotes e tiers, saga e ADRs (slides 9 e 10)

**O que falar**
- Slide 9: saga **orquestrada** pela Requisição; ela manda `ReservarBolsas`, `MontarRemessa`, `AbrirViagem`, e cada serviço responde só para ela (a Expedição não fala com o Transporte); o passo 5 não tem volta (falha vira requisição de reposição).
- Slide 10: falha com a bolsa B-100 rompida → `RemessaFalhou` → compensa na ordem inversa e tenta reservar de novo. ADR 0001: monolito modular; o Transporte sai acima de ~10 leituras/s (moderado 80 ÷ 30 = 2,7/s fica; alto 600 ÷ 30 = 20/s sai). ADR 0002: outbox. Passa para o Thiago.

**Onde está no GitHub**
- **C.3 Estrutura de pacotes**, **C.4 Camada lógica × tier físico**, **D.3 Saga**, **D.4 Comparação** e **D.5 ADRs** do [`documento.md`](arquitetura/documento.md).
- Diagrama da saga: [`img/saga-atender-requisicao.png`](arquitetura/img/saga-atender-requisicao.png) (fonte em [`microsservicos/`](arquitetura/microsservicos/)).
- ADRs: [`adr/0001-decomposicao.md`](arquitetura/adr/0001-decomposicao.md) e [`adr/0002-eventos-com-outbox.md`](arquitetura/adr/0002-eventos-com-outbox.md).
- Slides [`saga.html`](apresentacao/deck/slides/saga.html) e [`falha-adr.html`](apresentacao/deck/slides/falha-adr.html).

**Se o professor perguntar como você validou:** "Percorri a saga passo a passo, conferindo que toda resposta volta ao orquestrador, e comparei o gatilho do ADR 0001 com as leituras por segundo calculadas nos três cenários."

## Thiago · Lei de Little e disponibilidade composta (slides 11 e 12)

**O que falar**
- Slide 11: L = λ × W; alto: 120 × 0,25 = 30 simultâneas ÷ 7 por instância = 5; no moderado a conta dá 1, mas usamos 2 porque 99,9% exige outra zona; o banco não é gargalo (120 × 0,05 = 6 conexões).
- Slide 12: em série as disponibilidades se multiplicam: 99,99% × 99,99% × 99,95% = 99,93% ≈ 31 min/mês fora; fecha 99,9% (44 min), não fecha 99,95% (22 min), por isso o alto mira 99,9%; para 99,95% seria preciso Aurora. Passa para o Eloi.

**Onde está no GitHub**
- **E.1 Premissas de carga** e **E.2 Lei de Little** do [`documento.md`](arquitetura/documento.md).
- Planilha [`orcamento.xlsx`](arquitetura/orcamento.xlsx), abas **Lei de Little** e **Disponibilidade**.
- Tabela das contas: [roteiro da apresentação](apresentacao/roteiro.md) ("Contas que todos precisam saber explicar").
- Slides [`little.html`](apresentacao/deck/slides/little.html) e [`disponibilidade.html`](apresentacao/deck/slides/disponibilidade.html).

**Se o professor perguntar como você validou:** "Refiz as contas na calculadora e conferi com as fórmulas da planilha; os SLAs (ALB, Fargate, RDS Multi-AZ) eu li nas páginas oficiais da AWS."

## Eloi · cenários e orçamento (slides 13 e 14)

**O que falar**
- Slide 13: baixo = piloto em Recife no Render (US$ 47); moderado = Pernambuco na AWS, 2 instâncias, ALB e RDS Multi-AZ (US$ 152,07); alto = Nordeste, autoscaling de 3 a 6 tarefas e Transporte separado (US$ 472,88). Preços conferidos pelo squad em 12/11.
- Slide 14: custo total sobe ~10×, custo por pedido cai ~8× (US$ 0,0104 → 0,0013), porque a infraestrutura fixa se dilui. Passa para o Ewerton.

**Onde está no GitHub**
- **E.3 Diagramas e o que muda** e **E.4 Orçamento por cenário** do [`documento.md`](arquitetura/documento.md).
- Diagramas: [`img/baixo.png`](arquitetura/img/baixo.png), [`img/moderado.png`](arquitetura/img/moderado.png), [`img/alto.png`](arquitetura/img/alto.png) (fontes em [`cenarios/`](arquitetura/cenarios/)).
- Planilha [`orcamento.xlsx`](arquitetura/orcamento.xlsx), abas **Baixo (Render)**, **Moderado (AWS)** e **Alto (AWS)**.
- Links das estimativas da AWS e do Render: [roteiro da apresentação](apresentacao/roteiro.md) ("Fontes").
- Slides [`cenarios.html`](apresentacao/deck/slides/cenarios.html) e [`orcamento.html`](apresentacao/deck/slides/orcamento.html).

**Se o professor perguntar como você validou:** "Os preços foram levantados por nós, sem IA, na AWS Pricing Calculator (us-east-1) e em render.com/pricing em 12/11/2026; os links das estimativas estão no roteiro. A única correção foi o RDS db.t4g.small, de 0,064 para 0,065 USD/h."
