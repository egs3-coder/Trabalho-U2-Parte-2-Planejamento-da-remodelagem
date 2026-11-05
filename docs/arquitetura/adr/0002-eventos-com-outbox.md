# ADR 0002: Eventos entre contextos com outbox transacional

Status: aceito

## Contexto

Estoque, Requisição, Expedição e Transporte precisam saber das mudanças uns dos outros (BolsasReservadas, RequisicaoAtendida, RemessaDespachada, TemperaturaForaDaFaixa, EntregaConcluida). Gravar no banco e publicar na fila em dois passos separados pode perder o evento se a aplicação cair entre eles, deixando, por exemplo, uma bolsa reservada para sempre.

## Decisão

Cada caso de uso grava o evento numa tabela `outbox` na mesma transação da mudança de estado. Um publicador lê a tabela e envia os eventos ao broker (no monolito, em processo; nos microsserviços, para Amazon SQS). Os consumidores são idempotentes pelo id do evento.

## Consequências

- Melhora: nenhum evento é perdido; o mesmo código serve ao monolito modular e à projeção com microsserviços.
- Piora: a entrega é "pelo menos uma vez", então duplicatas precisam ser tratadas; há uma tabela a mais para limpar periodicamente.
- Alternativa descartada: publicar direto no broker dentro do caso de uso, porque não é atômico com a gravação no banco.
