# 🤖 DIO Agent

> Seu mentor de Inteligência Artificial para aprender mais e melhor na [DIO](https://dio.me).

O **DIO Agent** é um agente de IA que acompanha você na sua jornada de estudos. Ele conhece as experiências da DIO (Bootcamps, Formações, Cursos e Desafios) e ajuda você a estudar com mais clareza, destravar desafios e entender qualquer conceito.

E você não precisa instalar nada complicado. Em **3 passos simples**, o seu mentor de IA estará pronto para usar.

---

## ✨ Antes de começar: dois conceitos rápidos

Para usar o DIO Agent, basta entender duas palavras. As duas estão no [Glossário completo](docs/glossary.md), mas aqui vai o resumo:

- 🧠 **Agente de IA**: um programa de inteligência artificial que não só responde, mas também ajuda você a realizar tarefas. O DIO Agent é um agente focado em estudos.
- 🚗 **Harness**: o programa onde o agente "roda". Se o agente é o motorista, o harness é o carro. Você escolhe um no Passo 1.

Pronto. Com isso já dá para começar.

---

## 🎯 O que o DIO Agent faz por você

| Você precisa de... | O DIO Agent... |
|--------------------|----------------|
| Saber por onde começar | Monta um plano de estudos no seu ritmo |
| Destravar um desafio | Te guia até a solução, sem entregar a resposta pronta |
| Entender um conceito | Explica de forma simples, com analogias e exemplos |

Ele conhece os formatos da DIO: Bootcamps, Formações, Cursos, Desafios de Código, Desafios de Projeto, Desafios Criativos, Lives e Mentorias. Assim, as recomendações sempre apontam para algo que você já tem na plataforma.

---

## 🚀 Comece em 3 passos

### 1️⃣ Instale um Harness

O harness é o programa que dá vida ao agente. Escolha um e instale seguindo a documentação oficial dele:

| Harness | Onde encontrar |
|---------|----------------|
| Claude Code | https://docs.claude.com/en/docs/claude-code |
| Antigravity | Documentação oficial do Antigravity |
| Hermes | Documentação oficial do Hermes |

> 💡 **Exemplo com Claude Code:** no terminal, rode o instalador oficial.
> - macOS, Linux ou WSL: `curl -fsSL https://claude.ai/install.sh | bash`
> - Windows (PowerShell): `irm https://claude.ai/install.ps1 | iex`
>
> Os comandos podem mudar com o tempo. Confira sempre a documentação oficial do harness escolhido.

Qualquer harness moderno serve. O DIO Agent foi feito para funcionar em todos eles.

### 2️⃣ Configure o DIO Agent

Baixe este repositório e entre na pasta dele:

```bash
git clone https://github.com/digitalinnovationone/dio-agent.git
cd dio-agent
```

Agora abra essa pasta no harness que você instalou. No Claude Code, por exemplo, basta rodar:

```bash
claude
```

E é só isso. ✅ O harness lê automaticamente o arquivo `AGENTS.md` e o agente já sabe quem é: o seu mentor de estudos da DIO.

### 3️⃣ Hands On!

Agora é só conversar. Experimente pedir, com as suas palavras:

- 🗺️ **Plano de estudos**
  > "Quero ser desenvolvedor back-end. Tenho 1 hora por dia. Monta um plano de estudos pra mim."

- 🔓 **Destravar desafio**
  > "Estou travado em um Desafio de Código sobre laços de repetição. Me ajuda a destravar?"

- 💡 **Explicar conceito**
  > "Me explica, de forma simples, o que é uma API."

O agente conduz a conversa a partir daí. Não precisa de comando especial: fale naturalmente.

---

## 🧩 As skills do agente

Uma **skill** é uma habilidade do agente, descrita em um guia passo a passo. O DIO Agent vem com três:

| Skill | Para que serve |
|-------|----------------|
| [Plano de estudos](skills/study-plan/SKILL.md) | Organiza o que estudar, em que ordem e em quanto tempo |
| [Destravar desafio](skills/unblock-challenge/SKILL.md) | Conduz você até a solução de um desafio, sem dar a resposta pronta |
| [Explicar conceito](skills/explain-concept/SKILL.md) | Explica conceitos de forma didática, com analogias e exemplos |

Você não precisa "chamar" uma skill. O agente percebe o que você precisa e usa a skill certa sozinho.

---

## 🗂️ Estrutura do repositório

```
dio-agent/
├── README.md                  Este guia
├── AGENTS.md                  Definição do agente (lida por qualquer harness)
├── CLAUDE.md                  Atalho para o Claude Code
│
├── agent/
│   ├── persona.md             A personalidade e o tom do agente
│   └── knowledge/
│       ├── dio-platform.md          O que é a DIO
│       └── learning-experiences.md  Os formatos de aprendizado da DIO
│
├── skills/
│   ├── README.md              O que são skills
│   ├── study-plan/            Skill: plano de estudos
│   ├── unblock-challenge/     Skill: destravar desafio
│   └── explain-concept/       Skill: explicar conceito
│
└── docs/
    └── glossary.md            Glossário de termos
```

> 🔍 **Por que funciona em qualquer harness?** O coração do projeto é o arquivo `AGENTS.md`, um padrão aberto que harnesses modernos sabem ler. O `CLAUDE.md` apenas aponta para ele. Trocou de harness? O agente continua o mesmo.

---

## 📖 Glossário rápido

Termos como *agente*, *harness*, *skill* e *prompt* estão explicados com analogias simples no **[Glossário completo](docs/glossary.md)**. Se algum termo soar estranho, comece por lá.

---

## 💬 Sobre este projeto

O DIO Agent foi criado para acompanhar você desde o início dos Bootcamps e Formações da DIO. A ideia é simples: aprender na era da IA fica mais fácil quando você tem um mentor disponível a qualquer hora.

Bons estudos, e vem com a gente. 🚀
