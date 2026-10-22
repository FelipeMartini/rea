---
name: receber-pedido-arte
description: Procedimento padronizado para a IA de imagens receber, processar e responder pedidos de arte das outras IAs (Geely, Social, Mylab). Use sempre que chegar um pedido de arte, ícone, mockup ou vídeo.
---

# Receber Pedido de Arte

Este procedimento orienta a IA de imagens ao receber demandas visuais das outras IAs do Felipe.

## Passos Obrigatórios

1. **Leitura Completa do Briefing e Passagem:**
   - Ler a mensagem da inbox (`inbox/ProjetoImagem/`) e o documento detalhado em `docs/passagens/`.
   - Identificar o destino exato dos arquivos (`material/ia/`, `Documentos/identidade-da-central/entregas/`, etc.).
   - Mover a mensagem da inbox para `lidos/` e comitar no `ia-comum`.

2. **Extração das Referências Obrigatórias:**
   - Identificar as imagens e renders canônicos indicados no brief (`geely-oficial/`, `renders-de-fabrica/`, `masters_v5`).
   - NUNCA gerar por texto cego. Sempre passar as referências pelo parâmetro `ImagePaths`.

3. **Geração do Quadro de Teste Prévio:**
   - Antes de gerar lotes ou variações completas, produzir 1 quadro de teste (`teste-identidade.png` ou `teste/panda_icon-verde-A.png`).
   - Conferir se o veículo é 100% o Geely EX2 oficial e se a cor bate com o alvo técnico (#ACB5A1).

4. **Auditoria e Validação Técnica:**
   - Rodar o script de auditoria do projeto (`validar-arte-ia.ps1` ou `conferir-arte-entregue.js`).
   - Somente liberar arquivos aprovados pela auditoria.

5. **Documentação e Entrega:**
   - Criar `LEIA-ME.md` na pasta de entrega detalhando exatamente o que cada arquivo mostra e suas métricas.
   - Enviar recado na inbox (`inbox/<quem pediu>/`) no padrão oficial das quatro IAs avisando da entrega (e passagem longa em `docs/passagens/` se requisitado).
