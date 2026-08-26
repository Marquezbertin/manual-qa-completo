# Módulo 04: Testes Manuais e Exploratórios

## 4.1 Teste Manual vs Exploratório

| Aspecto | Manual (Scripted) | Exploratório |
|---------|-------------------|--------------|
| Preparação | Casos de teste detalhados | Charter de sessão |
| Execução | Segue passos exatos | Livre, baseado em intuição |
| Quando usar | Regressão, conformidade | Novos recursos, bugs escondidos |
| Vantagem | Reprodutível | Encontra defeitos inesperados |

## 4.2 Caso de Teste (Test Case) Estruturado

Todo caso de teste deve ter:
- **ID** único
- **Pré-condições**: estado necessário antes de iniciar
- **Passos**: ações numeradas
- **Dados de entrada**: valores usados
- **Resultado esperado**: o que deve acontecer
- **Resultado obtido**: o que aconteceu (preenchido na execução)
- **Status**: Pass / Fail / Blocked / Not Run

Exemplo:
```
ID: TC-LOGIN-001
Pré-condição: Usuário cadastrado (user@teste.com / Senha123)
Passos:
  1. Acessar /login
  2. Informar e-mail válido
  3. Informar senha válida
  4. Clicar em "Entrar"
Resultado esperado: Redirecionamento para /dashboard com nome do usuário
```

## 4.3 Session-Based Test Management (SBTM)

Metodologia de **tester exploratório estruturado** (James Bach / Jon Bach):
- **Charter**: missão da sessão ("Explorar a tela de checkout em busca de problemas de usabilidade")
- **Tempo**: sessão de 60-90 min, sem interrupções
- **Oportunidades (Opportunities)**: bugs, dúvidas, riscos encontrados
- **Bug**: defeitos reportados
- **Test Notes**: anotações livres
- **Debrief**: revisão rápida pós-sessão

Template de charter:
```
Charter: Explorar o fluxo de recuperação de senha verificando mensagens de erro
Áreas: /forgot-password, e-mail, SMS
Duração: 60 min
```

## 4.4 Checklists de Teste (Heurísticas)

Checklist prático para homologação de uma feature web:
- [ ] Campos obrigatórios validados
- [ ] Formatação (CPF, telefone, data) aceita e rejeita inválidos
- [ ] Mensagens de erro claras e em PT-BR
- [ ] Estados de loading exibidos
- [ ] Responsivo (mobile/tablet/desktop)
- [ ] Acessibilidade básica (contraste, foco, leitor de tela)
- [ ] Logs de erro não expõem dados sensíveis

## 4.5 Bug Report Completo

Um bom bug report economiza tempo de toda a equipe.

| Campo | Descrição |
|-------|-----------|
| **Título** | Resumo da falha (o que acontece) |
| **Ambiente** | Navegador, SO, versão do build |
| **Passos para reproduzir** | Numerados e exatos |
| **Resultado esperado** | O que deveria acontecer |
| **Resultado obtido** | O que aconteceu |
| **Severidade** | Crítico / Alto / Médio / Baixo (impacto no negócio) |
| **Prioridade** | Urgente / Alta / Média / Baixa (urgencia de correção) |
| **Evidência** | Screenshot, vídeo, logs |
| **Anexos** | `.har`, console log |

### Exemplo real (anônimo)
```
Título: Botão "Finalizar Compra" some após erro de cartão
Ambiente: Chrome 120 / Windows 11 / Build 2.3.1
Passos:
  1. Adicionar item ao carrinho
  2. Ir para checkout
  3. Inserir cartão inválido (1234 5678 9012 3456)
  4. Submeter
Resultado esperado: Mensagem de erro e botão permanece visível
Resultado obtido: Tela de erro e botão desaparece (impossível retry)
Severidade: Alto (bloqueia venda)
Prioridade: Alta
Evidência: screenshot_erro.png
```

## 4.6 Testes de Usabilidade e Heurísticas de Nielsen

As **10 heurísticas de Nielsen (1994)**:
1. Visibilidade do estado do sistema
2. Correspondência com o mundo real
3. Controle e liberdade do usuário
4. Consistência e padrões
5. Prevenção de erros
6. Reconhecimento em vez de recordação
7. Flexibilidade e eficiência de uso
8. Estética e design minimalista
9. Ajudar usuários a reconhecer, diagnosticar e recuperar erros
10. Documentação de ajuda

## 4.7 Citações e Referências

- **Bach, J. & Bach, J. (2004)** — Session-Based Test Management
- **Nielsen, J. (1994)** — "10 Heuristics for User Interface Design"
- **ISTQB®** — "Test Techniques" (manual testing)
- **Kaner, C. (2008)** — Exploratory Testing

---

## 4.8 Próximos Passos

Ao final deste módulo, o leitor deverá:
1. Escrever casos de teste estruturados
2. Criar um charter de sessão exploratória
3. Montar uma checklist de homologação
4. Escrever um bug report completo e útil
5. Aplicar as heurísticas de Nielsen

---

> **Próximo módulo**: [Módulo 05: Testes Automatizados](05/PT/indice.md)