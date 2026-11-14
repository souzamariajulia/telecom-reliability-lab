# INC-001 — Indisponibilidade da Telecom API

## Resumo
Simulação controlada de indisponibilidade da Telecom API
para validar o monitoramento e o sistema de alertas.

## Serviço afetado
Telecom API — porta 8000.

## Causa raiz
Interrupção manual do container telecom-api para
simular uma falha de serviço.

## Detecção
O Prometheus identificou que a métrica
up{job="telecom-api"} passou de 1 para 0.

## Alerta
Nome: TelecomAPIDown

Condição: up{job="telecom-api"} == 0

Tempo de espera: 1 minuto.

Estado observado: Inactive → Pending → Firing.

## Recuperação
O serviço foi restaurado com:

sudo docker compose start telecom-api

Após a recuperação, o alerta retornou para Inactive.

## Lições aprendidas
- A métrica up permite detectar falhas na coleta.
- Alertas ajudam a identificar indisponibilidade.
- A recuperação deve ser validada após a intervenção.
- O monitoramento deve contemplar também a saúde
  das dependências e dos endpoints de negócio.

## Melhorias futuras
- Criar alertas para taxa de erros HTTP 5xx.
- Monitorar latência p95.
- Configurar notificações com Alertmanager.
- Implementar testes automatizados de recuperação.