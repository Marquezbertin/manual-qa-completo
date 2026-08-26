# Módulo 01: Visão Geral do QA

## 1.1 Quem é o Analista de Testes / QA

O Analista de Testes (ou QA - Quality Assurance) é o profissional responsável por garantir que o software atendam aos requisitos e expectativas do cliente, preventivamente, e não apenas encontrando defeitos após o desenvolvimento.

### Atribuições principais:
- **Prevenção**: Participar da elaboração de requisitos, reviews de documentação e planejamento de testes para evitar defeitos
- **Detecção**: Executar testes funcionais e não funcionais para encontrar defeitos antes da entrega
- **Comunicação**: Atuar como elo entre equipe de negócio, desenvolvimento e stakeholders
- **Melhoria Contínua**: Identificar padrões de defeitos e sugerir melhorias nos processos

### Perfil recomendado:
- Visão crítica e objetiva
- Boas habilidades de comunicação
- Curiosidade para entender como o sistema funciona
- Organização e capacidade de documentação
- Empatia com usuários finais e equipe de desenvolvimento

## 1.2 Campo de Atuação do QA

O trabalho de QA abrange diversas áreas, que podem ser classificadas em:

### Testes Funcionais
- Testes de unidade, integração, sistema
- Testes de smoke, sanity, regressão
- Testes de aceitação (UAT)

### Testes Não Funcionais
- **Performance**: testes de carga, de estresse, de resistência
- **Segurança**: testes de vulnerabilidades, penetration test básico
- **Usabilidade**: testes com usuários reais, heurísticas
- **Compatibilidade**: navegadores, dispositivos, sistemas operacionais
- **Estabilidade**: confiabilidade, disponibilidade

### Tipos de teste adicionais
- **Exploratórios**: testes sem script pré-definido, baseados na criatividade do tester
- **Behavior Driven (BDD)**: testes baseados em comportamento do usuário, usando Given/When/Then
- **Alpha/Beta**: testes em ambientes controlados (alpha) ou com usuários reais (beta)

## 1.3 Certificações e Referências

### Certificações Internacionais
- **ISTQB Foundation Level**: a certificação mais reconhecida mundialmente
- **ASTFC-AICS**: certificação brasileira de Analista de Testes de Software
- **CSQE**: Certified Software Quality Engineer (ASQ)
- **CQT**: Certified Quality Tester

### Referências e Padrões
- **IEEE 829**: padrão para documentação de testes
- **ISO 9126**: qualidade de software (substituído por ISO 25010)
- **ISO 9001**: sistemas de gestão da qualidade
- **CMMI**: modelo de capacidade de integração e melhoria

### Referências Brasileiras
- **PROTESTE**: programa de qualidade de software do MCTI
- **Q&A**: comunidade e eventos brasileiros de qualidade

## 1.4 Metodologias de Desenvolvimento

### Agile (Metodologias Ágeis)
- **Scrum**: roles (Product Owner, Scrum Master, Development Team), events (Sprint, Daily, Review, Retrospective), artifacts (Product Backlog, Sprint Backlog, Increment)
- **Kanban**: visualização do fluxo, WIP limits, continuously delivery
- **XP (Extreme Programming)**: programação em pares, testes TDD, integração contínua

### Modelos Tradicionais
- **Cascata**: requisitos definidos upfront, fases sequenciais
- **Spiral**: iterações com foco em risco
- **V-Model**: relação direta entre requisitos e testes

## 1.5 O Papel do QA nas Metodologias

### Em Scrum
- Participar do Sprint Planning (estimativa de esforço de testes)
- Daily Standup (compartilhar status e impedimentos)
- Sprint Review (demonstrar resultados aos stakeholders)
- Sprint Retrospective (melhorar o processo baseado em aprendizados)

### Em Kanban
- Visualizar o fluxo de testes no quadro Kanban
- Definir WIP limits para testes
- Medir lead time e cycle time dos testes
- Melhorar continuamente o fluxo

### Em Cascata
- Participar da fase de requisitos
- Revisar documentos de teste antes da execução
- Executar testes em ambiente de homologação
- Entregar relatórios finais ao cliente

## 1.6 Ferramentas Comuns

### Gerenciamento de Testes
- **Jira** + **Xray** ou **TestRail**
- **Quality Center (ALM)** da Micro Focus
- **Testlink**

### Automação
- **Selenium** (WebDriver)
- **Playwright** (recomendado moderno)
- **Cypress** (front-end focado)
- **Pytest** + **unittest** (Python)
- **Jest** (JavaScript)

### Relatórios e Defeitos
- **Allure** (relatórios bonitos e detalhados)
- **Jira** (gerenciamento de defeitos)
- **GitLab Issues** / **GitHub Issues**

## 1.7 Carreira e Expectativas de Salário

### Níveis Comuns
- **QA Trainee/Júnior**: 0 a 2 anos de experiência, foco em execução de testes
- **QA Pleno**: 2 a 5 anos, automação básica, participação em planejamento
- **QA Senior**: 5+ anos, liderança de automação, definição de estratégia
- **QA Lead / Manager**: liderança de equipe, definição de política de qualidade

### Expectativas de Salário (Brasil - 2024)
- **Júnior**: R$ 3.000 a R$ 7.000
- **Pleno**: R$ 7.000 a R$ 12.000
- **Senior**: R$ 12.000 a R$ 20.000
- **Lead/Manager**: R$ 20.000+

> *"O QA não é um departamento, é uma mentalidade que deve permear toda a organização."* — *Autor desconhecido*

## 1.8 Próximos Passos

Ao final deste módulo, o leitor deverá ser capaz de:
1. Definir o papel do QA em diferentes metodologias de desenvolvimento
2. Identificar quais tipos de testes são mais apropriados para cada situação
3. Listar as certificações mais relevantes e seus benefícios
4. Entender como o QA se encaixa na equipe e processo

---

> **Próximo módulo**: [Módulo 02: Fundamentais da Qualidade de Software](02/PT/indice.md)