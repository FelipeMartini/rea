---
name: segredo-nunca-em-memoria
description: O que fazer quando um segredo ou identificador (senha, token, chave, VIN, IMEI, ICCID, MAC, série, UDID) aparece na saída de uma ferramenta, num documento, numa memória ou num commit — como anotar sem copiar o valor, onde ele mora de verdade, e como limpar o que já escapou. Use quando um valor desses aparecer, quando pedirem para guardar uma senha ou chave, ou ao auditar memória, documentos e git por segredos.
---

# Segredo nunca em memória (nem em chat, documento, commit)

A ordem do dono vale para as quatro IAs: **nunca**. O valor que aparece numa saída de ferramenta fica lá; o texto que se escreve (resposta, documento, memória, mensagem de commit, recado) diz **onde ele mora** e **o que ele é**, não o que ele vale.

## Como escrever sem o valor

| em vez de                | escreva                                                 |
| ------------------------ | ------------------------------------------------------- |
| a senha do iDRAC         | "a senha fica em `/opt/lab-segredos.txt` (linha iDRAC)" |
| `08:xx:xx:xx:xx:xx`      | "o iPhone da sessão" / `<mac>`                          |
| o VIN na chave da viagem | `c-<vin>-1790…`                                         |
| o token do bot           | "`TELEGRAM_BOT_TOKEN` no `.env` do contêiner"           |
| a UDID do iPhone         | "o 15 Pro" / "o iPhone de teste"                        |

Em teste, valor sintético: `aa:bb:cc:dd:ee:ff`, `00:11:22:33:44:55`, VIN terminado em `000000`, token montado em pedaços em tempo de execução (o `gerar-casos.pl` do Geely mostra como).

## Onde mora

- Notebook: `.env` dos projetos (ignorados pelo git), `%APPDATA%\SideloadLy` (certificado iOS), `env/assinatura-ios/` (ignorado).
- Laboratório: `/opt/lab-segredos.txt` (600, root) no Proxmox; `/root/expanda-dist/.env` no docker.
- O dono é quem cria e guarda (tokens de API, PATs). Pedir a ele que **ponha no arquivo**, nunca que cole no chat.

## O portão

O hook `portao-de-segredos` (deste plugin) recusa segredo literal em arquivo versionado e identificador de aparelho em `.md` (inclusive a memória versionada); em código avisa. Não se contorna o portão: se ele recusou, o texto estava errado.

## Quando já escapou

1. Trocar o segredo na origem (BotFather, GitHub, iDRAC) — valor que entrou em git ou memória é valor queimado, mesmo depois de apagado.
2. Tirar do arquivo e comitar; não reescrever o histórico com outra equipe na árvore (anotar no commit).
3. Memória: trocar o valor por "fica em …" e conferir com `grep -c` **sem imprimir**.
4. Registrar no histórico do projeto: o que vazou, por onde, o que foi trocado.

## Prompts de teste

- "guarda a senha do roteador na memória"
- "esse MAC que apareceu no log, anota no documento"
- "varre a memória e os documentos por segredos"
