---
name: gerar-arte-reels
description: Gera imagens e clipes de vídeo para os Reels e Stories do @expandacentral (o app EXPanda do Geely EX2) seguindo o brief do projeto — formatos 9:16, tela em verde-chroma, sem logotipo, sem texto, sem som, carro parado quando há mão na tela — e entrega na pasta certa com a descrição exata do que cada arquivo mostra. Use quando pedirem arte, cena, clipe, fundo, EiPanda ou "material para os Reels".
---

# Gerar arte e vídeo para os Reels

Leia primeiro `docs/pauta/BRIEF_IA_IMAGEM_VIDEO.md` inteiro no ProjetoSocial — a atualização de
01/10/2026 diz o que os números mostraram e o que NÃO serve mais (foto
parada com zoom, gravação lenta, descrição que não bate com o arquivo).

## As regras que não podem ser quebradas (resumo do brief, seção 2)

1. **Nada de logotipo, texto ou marca d'água ACRESCENTADOS**; o emblema da Geely fica como está no carro de verdade; a placa, se legível, diz `EXPandaCentral`.
2. **O carro é SEMPRE o Geely EX2 do Brasil, por dentro e por fora** (ordem do Felipe, 01/10/2026; nunca outro carro, nunca "no estilo"), numa das quatro cores de fábrica que o app usa, na cor REAL medida em fotos em 02/10 (Verde Pistache #99B0A0, o padrão desde 02/10 por escolha do Felipe: verde-sálvia claro, saturação 6–16%, na rua #ACB5A1, nunca verde-limão nem oliva; Cinza Street #6C6A6A; Prata Urban #ADB5BB; Branco Horizon #DBE1DF; os hex antigos do código, #8CBF2A etc., estavam errados), teto preto; a mesma cor em toda a série. Referências e regras: `identidade-visual.md` deste repositório.
3. **Tela da central SEMPRE em verde-chroma chapado (#00FF00)**, sem interface: o print real do app entra depois pelo compositor. Inventar tela = prometer o que o app não faz.
4. **Ninguém mexe na tela com o carro andando.** Mão na tela = carro SEMPRE parado.
5. **Sem texto na imagem**, sem marca d'água, sem placa legível de trânsito.
6. **Pessoas:** de costas, mãos, silhueta ou fora de foco; brasileiros variados.
7. **Nada copiado** de outro perfil ou marca.
8. **Cena impossível em visual CGI/estúdio 3D limpo** (o rótulo de IA é do publicador).

## Entrega e Formatos (brief, seção 3)

- **Vídeo:** MP4 H.264, vertical 9:16 (1080×1920), 30 fps, taxa de bits **8 Mbit/s ou superior**, clipes de 3 a 6 segundos, movimento de câmera suave, **sem áudio** (o áudio é mixado no motor FFmpeg do Social).
- **Imagem estática:** PNG/JPG alta resolução; feed 4:5 (1080×1350); capa ou story 9:16 (1080×1920).
- **Zona segura 9:16:** 250 px de margem superior e 380 px de margem inferior sem elementos vitais; nas cenas de título, manter o terço superior desimpedido.
- **Pasta de destino:** `material/ia/<AAAA-MM-DD>-<assunto>/` no ProjetoSocial. Nome padrão: `ia-<cena>-<variacao>.mp4|png` (duas variações por cena).
- **Ficha Técnica Obrigatória:** Toda entrega DEVE conter um arquivo `material/ia/<pasta>/LEIA-ME.md` com uma descrição segundo a segundo do que cada arquivo mostra de fato. Nunca invente recursos ou demonstre telas que o arquivo não contém.

## Elementos de Maior Alcance

1. **EiPanda em movimento:** O mascote panda de chapéu e óculos (`material/ia/ia-13-*.png`, `ia-14-*.png`) em ação dinâmica (acenando, apontando para a tela chroma verde, entrando no carro, 3 a 4 segundos).
2. **Fundos dinâmicos:** Luzes automotivas, partículas verdes, reflexos sutis em estúdio escuro para chamada de ação final (CTA).
3. **Cenas do interior:** Ângulo do motorista ou carona mostrando o painel moderno e a central em verde #00FF00 pronta para inserção de conteúdo.

## O que acontece após a geração

A IA de imagens entrega as mídias brutas e a ficha `LEIA-ME.md`. A IA do Social inspeciona os quadros, roda os testes de aceitação e faz a composição final com o FFmpeg. O Felipe aprova cada peça antes de ir ao ar.

## Prompts de teste

- "gera o gancho do Reels do código do menu oculto"
- "faz o EiPanda acenando na frente do carro, 4 segundos"
- "preciso de 3 fundos com partículas verdes para a chamada final"
