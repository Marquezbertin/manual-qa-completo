# Checklist de Homologação

```
FUNCIONALIDADE
  [ ] Fluxos principais funcionam (happy path)
  [ ] Casos de borda tratados
  [ ] Mensagens de erro claras (PT-BR)

VALIDAÇÃO DE DADOS
  [ ] Campos obrigatórios validados
  [ ] Máscara/formatos (CPF, telefone, data)
  [ ] SQL injection / XSS básico bloqueados

UI / UX
  [ ] Responsivo (mobile/tablet/desktop)
  [ ] Estados de loading/erro/vazio
  [ ] Acessibilidade (foco, contraste)

SEGURANÇA
  [ ] Sem segredos em logs/console
  [ ] Logout invalida sessão
  [ ] Dados sensíveis mascarados

PERFORMANCE
  [ ] Tempo de resposta aceitável (< SLA)
  [ ] Sem memory leak óbvio

DADOS / AMBIENTE
  [ ] Build testado = build homologado
  [ ] Dados de teste anonimizados
```
