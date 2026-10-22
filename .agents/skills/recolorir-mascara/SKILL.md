---
name: recolorir-mascara
description: Como realizar recolorização técnica de lataria automotiva respeitando máscaras binárias estritas, sem alterar mascotes, vidros, sombras, rodas, faróis ou logos. Use ao recalibrar cores de veículos ou ícones existentes.
---

# Recolorir com Máscara Binária

Procedimento de recolorização de lataria automotiva mantendo 100% da integridade dos elementos adjacentes.

## Regras Fundamentais

1. **Máscara Binária:**
   - Apenas os pixels brancos da máscara (`#FFFFFF`) podem ter a cor alterada.
   - Pixels pretos da máscara (`#000000`) representam elementos intocáveis: mascote EiPanda, chapéu, óculos, coco verde, vidros, faróis, teto preto, rodas, pneus, placa e fundo.

2. **Calibração de Cor:**
   - Alvo do Verde Pistache oficial: **#99B0A0** (o verde B, o estúdio oficial da Geely — o padrão da identidade desde 02/10/2026, escolha do Felipe; `identidade-visual.md`). Na rua, em luz neutra, o carro aparece como **#ACB5A1**.
   - Faixa de saturação aceita pela ferramenta: **6% a 16%**. Matiz aceito: **70° a 150°**.

3. **Verificação Automatizada:**
   - Executar a ferramenta de auditoria de cor do projeto:
     `& env\node\node.exe scripts\imagens\ferramentas\conferir-arte-entregue.js <original> <entrega> --alvo #99B0A0`
   - A ferramenta avalia 4 critérios:
     1. Tamanho e transparência/fundo.
     2. Fora da lataria nada mudou (diferença média < 6 em 255 e < 3% de pixels muito diferentes).
     3. Lataria no verde certo (matiz 70-150°, saturação 6-16%, brilho dentro de +-12 do alvo).
     4. Luz e sombra acompanham o original (correlação de brilho >= 0.85).
   - O resultado DEVE ser `APROVADA: pode entrar no app`.
