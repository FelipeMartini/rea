---
name: nova-skill
description: Como criar, testar e guardar uma skill nova no padrão da casa (SKILL.md com descrição-gatilho, passos com comando exato e critério de pronto, o que nunca fazer, três prompts de teste), onde ela mora por ferramenta (Claude Code, plugin, Antigravity) e quando NÃO é skill. Use quando pedirem para criar uma skill, transformar um roteiro/documento/memória em skill, ou quando a mesma coisa for pedida pela terceira vez.
---

# Uma skill nova

## 0. É skill?

- **Ordem que vale sempre** → não é skill: `AGENTS.md`/regra. **O que não pode acontecer** → hook (skill `novo-portao`). **Fato** → memória.
- **Passo a passo que se repete** (colado pela terceira vez; um documento-roteiro; uma memória com "How to apply" de cinco passos) → skill.

## 1. Três prompts antes do corpo

Três frases reais que a pessoa diria ("instala a central no carro", "compila e me diz a versão", "o carro voltou, atualiza"). Elas definem a `description` — é ela que decide quando a skill entra (nome + descrição ficam sempre no contexto, ~100 tokens; o corpo só quando casa ou por `/nome`).

## 2. A pasta e o arquivo

`<lugar>/<nome-kebab>/SKILL.md`:

```markdown
---
name: <nome-kebab>
description: <o que faz + "Use quando pedirem para …" com os verbos dos prompts. Até 1.536 caracteres.>
disable-model-invocation: true # só se tem efeito colateral (instalar, publicar, reiniciar): só o dono chama por /nome
paths: # só se vale para arquivos específicos
  - "sources/x/**"
---

# Título

## 1. Passo — com o COMANDO exato e o critério de "deu certo"

## Nunca — o que esta skill não faz

## Prompts de teste

- "…" (os três)
```

Até 500 linhas; arquivos de apoio ao lado (`reference.md`, `scripts/`), carregados sob demanda. `` !`comando` `` injeta saída de comando no texto antes de a IA ler.

## 3. Onde mora

| ferramenta                                              | projeto                                                 | global                          |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------- |
| Claude Code                                             | `.claude/skills/`                                       | `~/.claude/skills/`             |
| plugin `ia-comum` (todas as IAs)                        | `plugin/skills/`                                        | —                               |
| Antigravity / Gemini CLI                                | `.agents/skills/` (cópia por `scripts/sincronizar.ps1`) | `~/.gemini/antigravity/skills/` |
| O formato é o mesmo (`SKILL.md`); o que muda é a pasta. |

## 4. Testar

Numa sessão nova: o prompt com a skill (ela carregou? fez o que o passo diz?) e, se der, sem ela. `/skill-doctor` avalia a descrição. Num plugin, `claude plugin validate <pasta>`.

## 5. Guardar e revisar

Commit (por arquivo), push. Skill que precisou de ajuste à mão duas vezes é skill com revisão pendente: o passo errado se corrige na skill, não na cabeça.

## Prompts de teste

- "transforma o roteiro da rodada no carro numa skill"
- "cria uma skill para publicar o Reels"
- "isso devia virar skill?"
