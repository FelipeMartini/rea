---
name: gerar-icones
description: Gera ícones de aplicativos, telas de veículos e variações de cores oficiais para o ecossistema EXPandaCentral do Geely EX2 seguindo o padrão de design e controle estrito de transparência. Use quando pedirem ícones, telas do carro, variações de cor do panda ou melhorias visuais para a central e celular.
---

# Gerar Ícones e Artes para EXPandaCentral (Geely EX2)

Leia antes `Documentos/PROMPTS_PARA_GERAR_AS_IMAGENS.md` e `Documentos/PLANO_AUDITORIA_E_MELHORIA_VISUAL_IMAGENS.md` no ProjetoGeely.

## As Regras Estritas de Design

1. **Mesma Pose e Câmera nas 4 Cores:** As quatro variações do carro (Verde Pistache, Cinza Street, Branco Horizon, Prata Urban) devem ter a **mesmíssima pose de câmera, mesmo ângulo (3/4 dianteira) e mesma iluminação**. A única coisa que muda é a tinta da lataria.
2. **Fundo 100% Transparente (Canal Alfa Limpo):** Nunca desenhe chão branco, sombra dura sólida ou piso falso embaixo do carro. O fundo deve ser canal alfa transparente verdadeiro.
3. **Resoluções e Destinos Oficiais (`D:\ProjetoGeely\sources\EXPandaCentral\app\src\main\res\drawable-nodpi\`):**
   - **Telas cheias (1536×1024):**
     - `panda.png`: Verde Pistache (tela dia / automático dia)
     - `panda_dark.png`: Cinza Street (tela noite / automático noite)
     - `panda_branco.png`: Branco Horizon
     - `panda_prata.png`: Prata Urban
   - **Cartões Início (477×331):**
     - `panda_cartao.png`, `panda_dark_cartao.png`, `panda_branco_cartao.png`, `panda_prata_cartao.png`
   - **Ícone Mestre (1024×1024):**
     - `panda_icon.png`: O panda estilizado com chapéu e óculos, proporção 1:1, cantos limpos.
4. **Sem Textos ou Placas:** Não inserir textos na imagem, nem marcas d'água ou logotipos não autorizados.

## Critérios de Aceitação

- Cobertura de alfa consistente entre todas as quatro cores (medida no terço inferior).
- Sem artefatos nas bordas (sem contorno branco de recorte malfeito).
- Formato PNG com transparência RGBA de 32 bits.

## Prompts de teste

- "gera as 4 variações de cor do carro para a tela cheia da central"
- "gera o ícone mestre panda_icon.png em 1024x1024 com fundo transparente"
- "ajusta o cartão do carro branco para a tela inicial em 477x331"
