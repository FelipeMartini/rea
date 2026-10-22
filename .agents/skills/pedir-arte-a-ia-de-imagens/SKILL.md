---
name: pedir-arte-a-ia-de-imagens
description: Como pedir uma arte, um ícone, uma recoloração ou um vídeo à IA de imagens (ProjetoImagem, Antigravity) sem deixar margem para ela inventar — o que muda e só aquilo (com máscara), o que fica idêntico item por item, a cor medida com a foto de onde saiu, os tamanhos e fundos medidos, as referências reais, o teste antes do lote e o aceite medido por ferramenta. Use quando for pedir qualquer imagem à ProjetoImagem, ou quando uma entrega dela chegar.
---

# Pedir arte à IA de imagens

A IA de imagens erra quando o pedido deixa espaço: em 01/10/2026 ela gerou 12 artes e nenhuma era o EX2 (outro carro, outro painel, outro panda). O dono decidiu (02/10): a arte final é dela, as IAs Claude não mexem em pixel de arte final — então o **pedido** é o controle. Regra de identidade: `identidade-visual.md` deste repositório (o carro é sempre o EX2 do Brasil, nas cores reais medidas).

## A passagem tem estas seções, nesta ordem

1. **O QUE** (uma frase) e **POR QUÊ** (a ordem do dono, com data e as palavras dele).
2. **A COR (ou a forma) com a fonte:** o hex medido (luz, médio, sombra) e **a foto de onde saiu** (caminho). Nunca hex de código como "cor do carro". Se o dono ainda escolhe entre dois alvos, o teste vem nos dois.
3. **O QUE MUDA — e só isso:** de preferência uma **máscara** por arquivo (branco = pode mudar), gerada por ferramenta e conferida numa sobreposição antes de mandar. Dentro dela, o que muda e o que se preserva (luz, reflexo, sombra no mesmo lugar).
4. **O QUE NÃO PODE MUDAR, item por item:** personagem (cada peça), placa e texto, faróis, partes pretas, vidros, rodas, fundo (opaco ou transparente, com a cor), enquadramento (mesma câmera, mesmo recorte, pixel a pixel), resolução. Sem texto, logotipo ou marca d'água novos.
5. **OS ARQUIVOS:** tabela com caminho do original (a ENTRADA), tamanho e fundo **medidos** (não de memória), e a observação de enquadramento (ícones pequenos não são o grande reduzido).
6. **AS REFERÊNCIAS REAIS:** fotos oficiais, renders de fábrica, a cartela de cores, a prévia-guia (só guia, não entrega).
7. **COMO ENTREGAR:** primeiro **um teste** (o arquivo mestre); depois o lote, com os mesmos caminhos e nomes, numa pasta de entrega fora do código; um `LEIA-ME.md` com o que mudou em cada arquivo; recado em `inbox/<quem pediu>/`. Ela não comita no repositório do projeto.
8. **O ACEITE MEDIDO:** o comando da ferramenta de conferência e o que ela exige (no Geely: `scripts/imagens/ferramentas/conferir-arte-entregue.js` — tamanho e fundo, fora da máscara nada mudou, a cor dentro da faixa, a luz acompanha). Ela roda antes de entregar.
9. **O QUE NÃO FAZER** e **ONDE CONFERIR**.

Modelo completo: `D:\ProjetoGeely\Documentos\passagens\2026-10-02-para-a-ia-de-imagens-verde-real.md`. Recado em `inbox/ProjetoImagem/` apontando para a passagem; quem coordena a ProjetoImagem é a IA do Social — avise-a.

## Quando a entrega chega

Rodar a ferramenta de conferência em cada arquivo; reprovou → devolver com as linhas que falharam; aprovou → olhar lado a lado com a referência real e mostrar ao dono **antes** de aplicar. Aplicar, ver no produto (no Geely, no carro) e só então publicar.

## Nunca

- Pedir "no estilo de", "parecido com" ou por texto puro: sempre com a imagem de referência como entrada.
- Deixar de dizer o que NÃO muda (é o que ela mais estraga).
- Mandar tamanho ou fundo de memória.
- Aplicar entrega sem a conferência medida e sem alguém olhar.

## Prompts de teste

- "pede para a IA de imagens refazer os ícones na cor certa"
- "a IA de imagens entregou, o que eu confiro?"
- "como peço um vídeo do carro para os Reels sem ela inventar outro carro?"
