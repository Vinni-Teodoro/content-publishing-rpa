# 📚 Content Publishing RPA

> Automação desenvolvida em **Python** para otimizar a publicação de conteúdos acadêmicos em um ERP, reduzindo significativamente o tempo operacional e eliminando tarefas repetitivas.

<p align="center">
  <img src="./images/Banner.png" alt="Content Publishing RPA Banner" width="100%">
</p>

---

# 📖 Visão Geral

Este projeto apresenta um estudo de caso de uma automação desenvolvida para otimizar o processo de publicação de conteúdos em um ERP acadêmico.

A solução automatiza a leitura de uma planilha Excel, verifica previamente se os conteúdos já existem no ambiente e realiza a publicação automática conforme regras de negócio definidas.

---

# 🚨 O Problema

Antes da automação, toda a disponibilização de conteúdos era realizada manualmente.

O processo exigia:

- Acessar diversos ambientes do ERP;
- Verificar se o conteúdo já existia;
- Cadastrar materiais manualmente;
- Inserir códigos HTML/Embed;
- Configurar categorias;
- Validar informações antes da publicação.

Cada lote consumia aproximadamente **40 a 60 minutos**, além de estar sujeito a erros operacionais e retrabalho.

---

# 💡 A Solução

Foi desenvolvido um **RPA em Python** responsável por automatizar toda a rotina operacional.

A automação:

- 📄 Lê automaticamente uma planilha Excel;
- 🔍 Valida a existência do conteúdo;
- 📚 Publica materiais automaticamente;
- 🏷️ Aplica regras específicas conforme o tipo do conteúdo;
- 📊 Gera um relatório final da execução.

---

# 🏗 Arquitetura da Solução

<p align="center">
  <img src="./images/architecture.png" alt="Architecture Diagram" width="90%">
</p>

Fluxo da automação:

```text
Excel
   │
   ▼
Python
   │
   ▼
Pandas
   │
   ▼
Selenium
   │
   ▼
ERP Acadêmico
   │
   ▼
Relatório Final
```

---

# ⚙️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
|------------|------------|
| Python | Desenvolvimento da automação |
| Selenium | Automação Web |
| Pandas | Manipulação de dados |
| Excel | Entrada e saída de informações |

---

# 📈 Resultados

## Antes

- ⏱️ 40–60 minutos por lote
- ❌ Processo totalmente manual
- ❌ Alto risco de duplicidade
- ❌ Muito retrabalho

## Depois

- ⚡ Aproximadamente 5 minutos
- ✅ Processo automatizado
- ✅ Validação automática
- ✅ Eliminação de cadastros duplicados
- ✅ Padronização das operações

---

# 📂 Estrutura do Projeto

```text
content-publishing-rpa/

├── docs/
├── examples/
├── images/
├── src/
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🚀 Próximas Melhorias

- Interface gráfica para execução;
- Dashboard de monitoramento;
- Logs estruturados;
- Integração com banco de dados;
- Containerização utilizando Docker.

---

# 📚 Aprendizados

Durante o desenvolvimento deste projeto aprofundei conhecimentos em:

- Automação Web com Selenium;
- Manipulação de dados utilizando Pandas;
- Estruturação de RPAs;
- Tratamento de exceções;
- Automação de processos corporativos.

---

# ⚠️ Aviso

Este repositório apresenta um estudo de caso baseado em um projeto desenvolvido em ambiente corporativo.

Por questões de confidencialidade, **códigos-fonte, URLs, dados e informações proprietárias não são disponibilizados**.

O objetivo deste material é demonstrar a arquitetura da solução, as tecnologias utilizadas e os resultados alcançados.

---

# 👨‍💻 Autor

**Vinícius Teodoro**

- 💼 LinkedIn: https://www.linkedin.com/in/vinicius-ateodoro
- 💻 GitHub: https://github.com/Vinni-Teodoro
