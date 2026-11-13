# ADR 0001: Decomposição do Rota Vital

Status: aceito

## Contexto

O squad tem 7 pessoas (1 PO, 4 backend, 2 frontend/UI), um único repositório e uma esteira de CI/CD (Parte 1). A carga prevista vai de 3 a 120 req/s no pico (cenários baixo, moderado e alto), e só a telemetria das caixas térmicas tem volume alto. As fronteiras entre Estoque, Requisição, Expedição, Transporte e Rede ainda estão mudando, e a disciplina pede microsserviços apenas como projeção.

## Decisão

Adotar um monolito modular com cinco módulos (um por bounded context), cada um organizado em três camadas (apresentação, negócio, dados), comunicando-se apenas por casos de uso públicos e eventos. O contexto Transporte é o primeiro candidato a virar serviço separado, quando as leituras de telemetria passarem de ~10 por segundo (≈300 caixas em trânsito no pico, uma leitura a cada 30 s).

Gatilho medido nos cenários: o moderado tem 80 caixas = 2,7 leituras/s e continua no monolito; o alto tem 600 caixas = 20 leituras/s e já extrai o Transporte. O limite de 10/s deixa folga de quase 4× sobre o moderado e será confirmado no teste de carga da Parte 3: se, com 10 leituras/s, o tempo de resposta das requisições de atendimento (W = 0,20 s) piorar, a extração se antecipa.

## Consequências

- Melhora: deploy e operação simples (1 imagem, 1 esteira, 1 banco), transação ACID entre reserva e alocação de bolsas, menor custo nos cenários baixo e moderado.
- Piora: o sistema escala como um bloco; uma falha de memória em um módulo derruba todos; as fronteiras exigem disciplina, verificada com testes ArchUnit na esteira.
- Alternativa descartada: microsserviços desde já (4 serviços, broker, saga e 4 esteiras), porque o custo de operação não se justifica com a carga atual.
