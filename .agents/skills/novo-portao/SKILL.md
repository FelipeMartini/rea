---
name: novo-portao
description: Como criar um portão novo no padrão da casa — hook do Claude Code (bloqueia antes), portão de auditoria (julga o repositório quando chamado) ou portão-teste (falha na suíte) — com a decisão de qual dos três, o esqueleto em perl, o caso de teste "deve recusar" E "deve liberar", a bancada e o registro. Use quando uma ordem do dono foi quebrada, quando pedirem para "garantir que isso nunca mais aconteça", ou para criar hook, portão, trava, guarda.
---

# Um portão novo

## 1. Qual dos três?

| a regra é sobre…                                                        | vira                                                                                             | exemplo                                    |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------ |
| uma **ação** que não pode acontecer nunca (comando, escrita de arquivo) | **hook** `PreToolUse` (bloqueia antes, custo zero de contexto)                                   | `logcat -c`, `git add .`, segredo em `.md` |
| o **estado** do repositório/servidor, conferido de tempos em tempos     | **portão de auditoria** (script em `scripts/auditoria/`, chamado pela bancada e pela publicação) | só DataStore, distribuição em dia          |
| o **código** (toda chave tem leitor, toda id existe no retrato)         | **portão-teste** (JUnit/Dart que lê o fonte)                                                     | `CicloDePreferenciaTest`                   |
| a sessão terminar sem algo feito                                        | hook `Stop` (devolve a palavra uma vez; `stop_hook_active` evita o laço)                         | commit sem push                            |

Regra escrita é contexto; **ordem já quebrada uma vez vira hook**.

## 2. O esqueleto de um hook (perl, Git Bash no Windows, sem jq)

```perl
#!/usr/bin/perl
# CABECALHO: por que existe (a data e o incidente), o que recusa, o que libera DE PROPOSITO.
use strict; use warnings; use FindBin qw($RealBin); use lib "$RealBin/lib"; use Portao;
my $e = Portao::entrada();                       # hashref; sai calado se nao e JSON
Portao::liberar() unless ($e->{tool_name} // '') eq 'Bash';
my $cmd = Portao::comando($e);
Portao::liberar() unless $cmd =~ /<o que interessa>/;   # filtrar cedo: custo
# ... decidir ...
Portao::negar("[nome] motivo, com o incidente e a SAIDA (o que fazer em vez disso)");   # exit 2 + JSON deny
Portao::avisar("contexto", "mensagem curta");                                            # exit 0 + additionalContext
```

`Portao.pm` (em `.claude/hooks/lib/` do Geely e `plugin/scripts/lib/` do ia-comum) garante: **na dúvida, libera** (qualquer erro → exit 0). Para `alarm` dentro de `eval`, `local $SIG{__DIE__};`. Registrar em `.claude/settings.json` (`hooks.PreToolUse[].hooks[]` com `matcher`, `timeout` curto, `statusMessage`); não usar `if` para filtrar (casa por prefixo e `cd x && git …` escapa).

## 3. Os casos — metade LIBERA, de propósito

Um portão que reprova trabalho legítimo é desligado na primeira semana. Para cada padrão: um caso "deve recusar" e um "deve liberar" (o parecido que é legítimo). Segredos de mentira **montados em pedaços em tempo de execução** (o próprio portão recusaria o arquivo de teste). Caminhos absolutos entram por parâmetro, nunca no arquivo.

Bancada: `bash .claude/hooks/testes/rodar.sh` (Geely) / `bash plugin/testes/rodar.sh` (ia-comum): a função `julga <hook> '<comando>' deny|livre|aviso '<descrição>'`. <!-- md-ok: plugin/testes/rodar.sh e a bancada do repositorio ia-comum, nao deste -->

## 4. Registrar

Uma linha no `AGENTS.md` do projeto (a ordem) e a história em `ORDENS_DO_DONO_E_O_PORQUE.md`; o hook na seção "Se você é o Claude Code (o que só vale para ele)" do `AGENTS.md` (lista dos portões; o `CLAUDE.md` só importa o `AGENTS.md`, ordem comum 16); se vale para todas as IAs, no `plugin/hooks/hooks.json` do ia-comum com `${CLAUDE_PLUGIN_ROOT}`.

## 5. Nunca

Lista de exceção dentro do portão sem o motivo escrito e a medição (é onde a regra morre calada). Portão que trava (timeout longo, rede sem limite). Portão que não tem caso "deve liberar".

## Prompts de teste

- "garante que nunca mais um reboot remoto no carro"
- "cria um portão para o git add de pasta"
- "isso devia ser hook, portão ou teste?"
