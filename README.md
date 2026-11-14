# Telecom Reliability Lab

Laboratório prático de DevOps, Site Reliability Engineering (SRE) e Observabilidade, inspirado em cenários de infraestrutura de telecomunicações.

## Objetivo

Construir e evoluir uma aplicação distribuída para estudar confiabilidade, monitoramento, resposta a incidentes e automação de infraestrutura.

## Arquitetura inicial

- **Telecom API:** API Python com FastAPI que recebe requisições de consulta de conectividade.
- **Network Service:** serviço que simula consultas de rede, latência e falhas ocasionais.

A Telecom API se comunica com o Network Service por HTTP.

## Tecnologias

- Python
- FastAPI
- HTTP
- Linux (Fedora)
- Git e GitHub

## Funcionalidades implementadas

- Health check da API e do serviço de rede.
- Consulta simulada de conectividade de clientes.
- Simulação de latência e falhas HTTP.
- Tratamento de falhas de comunicação entre serviços.
- Experimento manual de indisponibilidade de dependência.

## Roadmap

- [x] Implementar os serviços Python.
- [x] Simular e investigar falha de dependência.
- [ ] Containerizar com Docker e Docker Compose.
- [ ] Implementar métricas com Prometheus.
- [ ] Construir dashboards no Grafana.
- [ ] Adicionar logs estruturados e tracing distribuído.
- [ ] Definir SLIs, SLOs e alertas.
- [ ] Criar testes automatizados e pipeline CI/CD.
- [ ] Documentar incidentes e análises de causa raiz.
