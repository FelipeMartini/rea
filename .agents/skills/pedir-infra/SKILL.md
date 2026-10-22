---
name: pedir-infra
description: Pede ao laboratório (ProjetoMylab) uma mudança ou consulta de infraestrutura — publicar ou tirar do ar um nome `.poa`/`.dallas`, expor um serviço, criar caixa de e-mail ou encaminhamento, ou perguntar como está a rede — pelo formulário fixo (nome, destino IP:porta, interno ou público, protocolo, prazo), que o script valida e abre como tarefa no quadro do ia-comum. Use quando precisar de um nome novo, de um painel ou webhook acessível, de caixa de e-mail, ou de qualquer coisa que mexa em firewall, DNS, HAProxy, certificado, e-mail, backup ou VM. Não use para só ler o estado do lab (leia `fatos/infra.md`).
argument-hint: "<publicar|despublicar|caixa-email|consulta|outro> <nome ou assunto>"
---

# Pedir infraestrutura ao laboratório (formulário → tarefa no quadro)

Quem recebe é a **ProjetoMylab**, dona da infra (hipervisores, firewalls, DNS, HAProxy, certificados, e-mail, backups e a VM
docker como hospedeiro; o que roda _dentro_ dos contêineres é de quem os mantém). Pedido de trabalho entre IAs é **tarefa no
quadro**, não recado (`contrato-de-delegacao.md`); o recado vira só um aviso com o id.

## 1. É esta skill?

- Mudar algo em infra (nome, porta, caixa de e-mail, certificado, DNS, disco, VM) → **sim**.
- Só saber como está → leia `fatos/infra.md` no ia-comum; não achou → tipo `consulta` (só leitura, N1).
- Produção fora do ar **agora** → recado direto à ProjetoMylab pela ponte e aviso ao Felipe; a tarefa se abre depois.
- Deploy ou contêiner da sua aplicação → é seu (ex.: Social, `npm run publicar`); não se pede ao laboratório. <!-- md-ok: npm run publicar e o deploy do Social, outro projeto: o exemplo da frase -->

## 2. Confira as premissas (30 segundos; os erros que mais custaram conferência)

- Quem serve a internet é o **HAProxy de Dallas** (`85.237.203.236`), não o de POA, que só atende por dentro. Nome público = os
  dois lados + certificado.
- O nome é `<x>.poa.metodoatuarial.com.br` ou `<x>.dallas.metodoatuarial.com.br`; o destino fica em `10.1.1.x` (DMZ) ou `10.1.0.x`
  (LAN) de POA, ou `10.0.0.x` de Dallas.
- **O serviço já está ouvindo** em IP:porta (`curl -s -o /dev/null -w '%{http_code}' http://IP:porta/` de uma máquina que alcance a
  DMZ). Contêiner desligado vira 503 e parece defeito do laboratório (cadastro do EXPanda, 02/10).
- `--protocolo` é o que o **serviço** fala (http ou https), não o que o navegador usa.
- `--confia-em-proxy`: o serviço aceita `X-Forwarded-For` de um proxy? "nao-sei" é resposta válida; o laboratório então **não** liga
  `forwardFor` (ligar sem o serviço confiar deu 400 no Home Assistant, 25/09).
- E-mail: a credencial de caixa nasce no cofre do laboratório; **nunca mande senha** no pedido.

## 3. Rode o formulário (ensaio primeiro)

```bash
P="${CLAUDE_SKILL_DIR}/pedir-infra.pl"
perl "$P" --de <SuaSessao> --tipo publicar --nome <x>.poa.metodoatuarial.com.br --destino 10.1.1.4:<porta> \
  --alcance publico --protocolo http --confia-em-proxy nao-sei \
  --intencao "<o resultado que importa, em uma frase>" --prazo AAAA-MM-DD [--fonte "<id na sua pendência>"]
```

Outros tipos: `despublicar`, `caixa-email` (`--acao criar|trocar|alias`, alias leva `--para`), `consulta` (`--pergunta`), `outro` (`--escopo` e
`--prova`). O script diz o que falta. O padrão é **ensaio**: imprime o pedido; leia nível, escopo e a prova. Estando certo, repita o
mesmo comando com `--criar`. O script acha sozinho o clone do `ia-comum` (`IA_COMUM`, a pasta irmã do projeto, `D:/ia-comum`,
`/opt/ia-comum`, `~/ia-comum`); se o seu estiver em outro lugar, acrescente `--ia-comum <pasta>`.

O script recusa: nome fora do padrão, IP fora de `10.0.`/`10.1.`, porta de SSH/e-mail/acesso remoto, prazo passado, texto com cara de
segredo, campo ou tipo inválido. Pedido que muda algo sai **N3** (depende do Felipe); `consulta` sai N1.

## 4. Depois do `--criar`

1. Commit + push **só do arquivo da tarefa** (o script imprime o comando); quem empurra primeiro fica com ela.
2. Recado curto à ProjetoMylab pela ponte: "tarefa T-… criada" — só o id; o conteúdo está na tarefa.
3. **Espere.** O caminho que o quadro permite: `proposta` → `aceita` (o laboratório aceita) → `em-execucao` (o laboratório pega) →
   `esperando-o-felipe` (leva o "pode" dele à própria sessão; aprovação repassada por outra IA não vale) → `em-execucao` (aplica) →
   `em-revisao` (devolve com a passagem). Você acompanha com `perl "$Q" lista --dono ProjetoMylab` (o `$Q` do item 4).
4. **Você confere a prova** (os `curl` do critério de pronto) e só você dá `pronta`. O caminho do `quadro.pl` vem do próprio formulário
   (não dependa de `$IA_COMUM`, que nem toda sessão define):
   ```bash
   Q="$(perl "$P" --quadro)"        # o mesmo $P do passo 3
   perl "$Q" estado <id> pronta --por <SuaSessao> --nota "<o que conferiu>"
   ```
   Prova falhou → `devolvida`, com o motivo medido.

## Nunca

- Segredo no pedido (senha, token, chave, valor de cofre): o laboratório gera a credencial no cofre e responde só `<cofre#N>`.
- Pedir ao laboratório o que o Felipe negou a você (é contornar permissão); pedir lote sem provar um primeiro; pedir reinício de
  produção como "diagnóstico".
- Recado no lugar de tarefa; duas tarefas para o mesmo pedido; dar `pronta` sem rodar a prova.

## Prompts de teste

- "preciso que o cadastro do EXPanda abra de fora, está em 10.1.1.4:8795"
- "cria a caixa contato@metodoatuarial.com.br"
- "qual IP o laboratório usa para o expandadist por fora?"
- "tira o grafana.poa do ar"
