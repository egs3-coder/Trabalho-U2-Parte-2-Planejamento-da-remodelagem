# Roteiro de fala — 26/11

Fala de cada integrante, slide por slide, mais a resposta para as perguntas mais prováveis. O mesmo texto está nas notas do apresentador do deck. **Todos leem o roteiro inteiro**: o professor vai chamar pessoas diferentes para explicar o domínio, as contas e a saga.

Como ensaiar: 1) cada um apresenta a sua parte cronometrando; 2) rodada cruzada, em que cada pessoa explica uma parte que não é dela; 3) um faz o papel do professor e escolhe a pergunta.

## Abertura · Ewerton (1 min)

### Slide 1 · Rota Vital, remodelado

**FALA — EWERTON (≈20 s)**

> "Boa noite, professor. Somos o squad Hemotrack e vamos apresentar a Parte 2: o planejamento da remodelagem do Rota Vital. A ideia é mostrar o domínio que redesenhamos com DDD, a arquitetura em três camadas, como ela viraria microsserviços e quanto custa rodar isso em três tamanhos de rede."

- Dica: falar devagar, sem ler o slide.

### Slide 2 · Cada dupla apresenta uma parte

**FALA — EWERTON (≈20 s)**

> "Dividimos em duplas: Pablo e João falam do domínio, Lucas e Saulo da arquitetura e da saga, Thiago e Eloi das contas e do orçamento. Mas ensaiamos cruzado: o senhor pode chamar qualquer um de nós para explicar qualquer parte."

- Essa frase responde direto ao pedido do professor. Não pular.

### Slide 3 · A Parte 1 colocou o Rota Vital no ar

**FALA — EWERTON (≈20 s)**

> "Na Parte 1 a gente colocou o sistema no ar: a API roda em container no Render, o banco é um PostgreSQL gerenciado e toda mudança passa pelos testes e pela esteira de CI/CD. Esse ambiente é o nosso cenário baixo: é dele que partimos. Agora o Pablo explica como redesenhamos o domínio."

- Passar a palavra para o Pablo.

## A e B · Domínio · Pablo e João (3 min)

### Slide 4 · O core é entregar a bolsa certa, dentro da cadeia fria

**FALA — PABLO (≈45 s)**

> "Começamos separando o problema em subdomínios. O core, onde o Rota Vital se diferencia, são duas coisas: atender a requisição com a bolsa certa — compatível e mais perto do vencimento — e provar que ela viajou na temperatura certa. Estoque, expedição e cadastro da rede são suporte: são do negócio, mas seguem procedimento padrão. Identidade e notificações são genéricos: não vale a pena construir, a gente compra pronto, como Keycloak ou Cognito."

- SE PERGUNTAREM: "Por que o transporte é core?" → Porque a rastreabilidade da cadeia fria é o que garante que a bolsa chega utilizável; sem isso a entrega não vale.

### Slide 5 · A mesma palavra muda de sentido em cada contexto

**FALA — PABLO (≈45 s)**

> "Daí saíram cinco bounded contexts: Estoque, Requisição, Expedição, Transporte e Rede. O glossário mostra por que separar: 'bolsa' no Estoque é a unidade com tipo sanguíneo e validade; na Expedição é só um volume com código de barras para embalar. 'Entrega' na Requisição é o hospital confirmar e encerrar o pedido; no Transporte é a caixa chegar e encerrar a viagem. Se tudo estivesse num modelo só, essas palavras iam brigar. O João mostra como os contextos se conversam."

- SE PERGUNTAREM: "Por que Rede é separado?" → Hospitais e endereços mudam pouco e são consultados por todos; ela expõe um serviço aberto.

### Slide 6 · O mapa acompanha o caminho da bolsa

**FALA — JOÃO (≈40 s)**

> "O mapa segue o caminho físico da bolsa. Entre Estoque, Requisição, Expedição e Transporte a relação é cliente-fornecedor: quem vem depois depende do que o anterior publica. O sensor da caixa é de um fabricante externo e manda em Fahrenheit, então colocamos uma camada anticorrupção que traduz para a nossa leitura em Celsius. A Rede é um serviço aberto que todos consultam, e com identidade e notificações somos conformistas: usamos o modelo do provedor."

- SE PERGUNTAREM: "Por que anticorrupção?" → Para o formato do fabricante não vazar para dentro do nosso domínio; se trocar o sensor, só o adaptador muda.

### Slide 7 · A compatibilidade depende do hemocomponente

**FALA — JOÃO (≈55 s)**

> "O agregado central é a Requisição. Ela é a raiz e protege cinco invariantes; a principal é a compatibilidade. Na primeira versão a gente olhava só o tipo sanguíneo, mas a regra depende do hemocomponente. Hemácias levam antígenos: a bolsa não pode ter antígeno que o receptor não tem, por isso O negativo serve a todos. Plasma leva anticorpos, então a regra se inverte: o plasma AB serve a todos e o Rh não conta. Na tabela, para um receptor A+, a mesma bolsa O− é aceita em hemácias e recusada em plasma. Essa regra fica no objeto de valor Hemocomponente, e o cenário Gherkin testa os dois casos. Agora o Lucas mostra a arquitetura."

- SE PERGUNTAREM: "Por que a Requisição é a raiz?" → É ela que tem todas as informações para decidir se uma alocação é válida; nada altera um item sem passar por ela.

> "E plaquetas?" → Ficaram fora até a regra ser validada pelo responsável técnico do hemocentro.

## C e D · Arquitetura e saga · Lucas e Saulo (3 min)

### Slide 8 · Todas as dependências apontam para o domínio

**FALA — LUCAS (≈45 s)**

> "Cada contexto vira um módulo com três camadas: apresentação, negócio e dados. O ponto importante é a direção das setas: todas apontam para o domínio. A aplicação nunca importa a camada de dados; ela usa interfaces que moram no domínio, como RequisicaoRepository. Quem implementa é a camada de dados, e o Spring injeta a implementação quando sobe. Isso é a inversão de dependência. Para isso não se perder, a esteira roda testes ArchUnit que quebram o build se o domínio importar Spring ou JPA, ou se a aplicação importar dados."

- SE PERGUNTAREM: "Camada lógica é a mesma coisa que tier?" → Não. Camada é organização do código; tier é onde roda. As três camadas rodam juntas num container; os tiers são navegador, container e banco.

### Slide 9 · Quatro serviços, um banco para cada

**FALA — LUCAS (≈40 s)**

> "Se o sistema crescer, esses módulos viram quatro serviços: estoque, requisição — que absorve a Rede —, expedição e transporte, cada um com seu próprio banco. REST só onde o usuário espera a resposta na tela; o resto é por eventos em SNS e SQS, gravados com outbox para não perder nenhum. A telemetria das caixas chega por MQTT. Ninguém lê a tabela do outro serviço. O Saulo explica a saga que costura esses serviços."

- SE PERGUNTAREM: "O que é outbox?" → O evento é gravado numa tabela na mesma transação do dado; um processo publica depois. Se a fila cair, o evento espera na tabela (ADR 0002).

### Slide 10 · Orquestrada: todos respondem à Requisição

**FALA — SAULO (≈50 s)**

> "Atender uma requisição envolve quatro serviços, então usamos uma saga. Escolhemos orquestração pura: a Requisição é o orquestrador. Ela manda um comando para cada serviço — reservar bolsas, montar remessa, abrir viagem — e cada serviço responde só para ela. Nenhum serviço chama o seguinte: a Expedição não avisa o Transporte, quem manda abrir a viagem é a Requisição. Cada passo tem uma compensação, menos o quinto: depois que a caixa sai, não tem como desfazer, então uma falha vira uma requisição de reposição. Escolhemos orquestrar porque, com compensação condicional e um ponto sem volta, é melhor ter o estado todo num lugar só."

- SE PERGUNTAREM: "Por que não coreografia?" → A regra 'falhou na expedição, desfaz alocação e reserva' ficaria espalhada em três serviços, difícil de rastrear e auditar.

### Slide 11 · O que acontece quando algo dá errado

**FALA — SAULO (≈40 s)**

> "Exemplo de falha: na separação, a Expedição encontra a bolsa B-100 rompida e responde RemessaFalhou. A Requisição compensa na ordem inversa: desaloca, manda o Estoque descartar a B-100 e liberar as outras, e tenta reservar de novo. Registramos duas decisões em ADR. A primeira: começamos com monolito modular, e o Transporte é o primeiro a sair quando a telemetria passar de umas 10 leituras por segundo. No moderado são 80 caixas, 2,7 leituras por segundo, fica no monolito; no alto são 600 caixas, 20 por segundo, e sai. A segunda é o outbox. Agora o Thiago mostra as contas."

- SE PERGUNTAREM: "De onde vem leituras/s?" → Cada caixa manda uma leitura a cada 30 s: 600 ÷ 30 = 20/s. "Por que 10?" → Fica entre o moderado e o alto com folga de quase 4× sobre o moderado; será medido no teste de carga da Parte 3.

## E · Contas e orçamento · Thiago e Eloi (2,5 min)

### Slide 12 · L = λ × W diz quantas instâncias precisamos

**FALA — THIAGO (≈45 s)**

> "Para dimensionar usamos a Lei de Little: L é igual a lambda vezes W, ou seja, quantas requisições estão sendo atendidas ao mesmo tempo. No alto, 120 requisições por segundo vezes 0,25 segundo dá 30 simultâneas. Cada instância aguenta umas 7 com folga, então a conta pede 5. Mas a conta da carga não é tudo: no moderado ela cabe em uma instância, e mesmo assim usamos duas, porque 99,9% de disponibilidade exige uma segunda em outra zona. O banco não é gargalo: 120 vezes 0,05 dá só 6 conexões ocupadas."

- SE PERGUNTAREM: "De onde vem o 7?" → Estimativa de 10 simultâneas por vCPU com 70% de folga; será medida no teste de carga da Parte 3.

### Slide 13 · Em série, as disponibilidades se multiplicam

**FALA — THIAGO (≈45 s)**

> "O professor pediu para conferir a disponibilidade do cenário alto. Um pedido passa em série pelo load balancer, pelas tarefas no Fargate e pelo banco: se qualquer um cair, o pedido falha, então multiplicamos os SLAs publicados pela AWS: 99,99 vezes 99,99 vezes 99,95 dá 99,93%. Isso são uns 31 minutos fora do ar por mês. Para 99,9% podemos ficar até 44 minutos fora, então fecha. Para 99,95% seriam só 22 minutos: não fecha. Por isso ajustamos a meta do alto para 99,9%. Para chegar a 99,95% teríamos que trocar o RDS por Aurora, que tem SLA de 99,99%. O Eloi mostra os cenários e o custo."

- SE PERGUNTAREM: "E a fila SQS?" → Não entra na conta: com o outbox, se a fila cair, os eventos esperam na tabela e o pedido continua sendo atendido.

### Slide 14 · A mesma aplicação em três tamanhos

**FALA — ELOI (≈40 s)**

> "Com essas contas montamos três cenários. O baixo é o piloto em Recife e é o que já roda no Render: uma instância e um banco, 47 dólares por mês. O moderado, a rede de Pernambuco, vai para a AWS com duas instâncias em zonas diferentes, load balancer e banco Multi-AZ: 152 dólares. O alto, a rede do Nordeste, tem autoscaling de 3 a 6 tarefas e o Transporte já separado, porque passa das 10 leituras por segundo: 473 dólares. Todos os preços foram conferidos pelo squad na calculadora da AWS e no site do Render em 12/11."

- SE PERGUNTAREM: "Por que us-east-1 e não São Paulo?" → O banco em sa-east-1 custa cerca do dobro; com dados sintéticos a latência não afeta. Em produção real, a LGPD pediria revisão.

### Slide 15 · O custo sobe 10×; o custo por pedido cai 8×

**FALA — ELOI (≈30 s)**

> "A mensagem principal do orçamento: do baixo para o alto, o custo total sobe umas 10 vezes, de 47 para 473 dólares. Mas o custo por pedido cai 8 vezes, de 1 centavo para 0,13 centavo de dólar, porque a infraestrutura fixa se dilui em muito mais pedidos. Custo por pedido é só o custo do mês dividido pelos pedidos do mês. O Ewerton fecha."

- SE PERGUNTAREM: "Como calcula o custo por pedido?" → 472,88 ÷ 360.000 = 0,0013. Pedidos/mês = pedidos/dia × 30.

## Fechamento · Ewerton (0,5 min)

### Slide 16 · A IA gerou o rascunho; cada dupla validou a sua parte

**FALA — EWERTON (≈25 s)**

> "Sobre o uso de IA, seguimos a política da faculdade: usamos o Claude para gerar o rascunho, e cada dupla validou a parte que apresentou. Pablo e João conferiram o domínio com o fluxo real do hemocentro e a regra ABO; Lucas e Saulo conferiram as setas e a saga; Thiago e Eloi refizeram as contas, e todos os preços foram levantados por nós, sem IA. Tudo está detalhado no documento."

- ATENÇÃO: antes do dia 26, cada um confirma que fez a validação que está escrita aqui.

### Slide 17 · Perguntas?

**FALA — EWERTON (≈10 s)**

> "Está tudo no repositório. A Parte 3 transforma esse plano em código. Obrigado, ficamos à disposição para perguntas — e qualquer um de nós pode responder sobre qualquer parte."

- COLA PARA AS PERGUNTAS (quem for chamado):

- Domínio: core = atender requisição + cadeia fria; I1 depende do hemocomponente (plasma inverte, AB serve a todos).

- Contas: L = λ × W (120 × 0,25 = 30 → 5 instâncias); 99,99 × 99,99 × 99,95 = 99,93% ≈ 31 min/mês; custo por pedido = custo ÷ pedidos.

- Saga: orquestrada pela Requisição; todos respondem a ela; passo 5 sem volta; falha no 4 desfaz 3 e 2.

---

# Pré-entrega — 19/11 (seções A e C, sem nota)

Slides: [`Hemotrack-Pre-entrega-Secoes-A-e-C-Slides.pdf`](../entregas/Hemotrack-Pre-entrega-Secoes-A-e-C-Slides.pdf) (8 slides, ≈5 min). Usa as mesmas falas da entrega final para os slides de A e C; abaixo, só o que muda.

| # | Slide | Quem |
| --- | --- | --- |
| 1 | Capa da pré-entrega | Ewerton |
| 2 | Duas seções, duas duplas | Ewerton |
| 3 | Subdomínios (igual ao slide 4 da final) | Pablo |
| 4 | Glossário (igual ao slide 5) | Pablo |
| 5 | Mapa de contextos (igual ao slide 6) | João |
| 6 | Três camadas (igual ao slide 8) | Lucas |
| 7 | Pacotes e tiers (só na pré-entrega) | Saulo |
| 8 | Perguntas | Ewerton |

### Slide 1 · Capa da pré-entrega

**FALA — EWERTON (≈15 s)**

> "Boa noite, professor. Esta é a pré-entrega do squad Hemotrack: as seções A e C em versão parcial. Pablo e João mostram o domínio, Lucas e Saulo a arquitetura em três camadas. Queremos a devolutiva para fechar a entrega do dia 26."

### Slide 2 · Duas seções, duas duplas

**FALA — EWERTON (≈15 s)**

> "Hoje trazemos só as seções A e C. B, D e E entram na entrega final do dia 26. Pablo, pode começar."

### Slide 7 · Um módulo por contexto, três camadas em cada

**FALA — SAULO (≈45 s)**

> "No código, cada contexto é um pacote com as mesmas três camadas. No exemplo da Requisição, a interface EstoqueGateway fica no domínio e o EstoqueClient, que implementa, fica em dados. Os outros quatro contextos seguem a mesma estrutura. É importante não confundir camada com tier: camada é a organização do código, tier é onde roda. As três camadas rodam juntas no mesmo container; o tier de dados é o servidor PostgreSQL, e o cliente é o navegador ou o app do motorista."

- SE PERGUNTAREM: "A camada de dados roda no banco?" → Não. O código dos repositórios roda no container, no tier de aplicação; o banco é outro tier.

Thiago e Eloi não apresentam na pré-entrega, mas devem acompanhar e anotar a devolutiva.
