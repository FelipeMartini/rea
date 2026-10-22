---
name: editar-arquivo-seguro
description: Procedimento rigoroso para edição e salvamento de arquivos em repositórios concorrentes, garantindo recarregamento prévio do disco e verificação de integridade pós-gravação para prevenir arquivos zerados ou truncados. Use ao modificar qualquer arquivo existente.
---

# Editar Arquivo com Segurança e Integridade

Procedimento para evitar corrupção, sobreposição de buffers antigos ou truncamento de arquivos compartilhados entre múltiplas IAs.

## Procedimento

1. **Recarregamento Prévio Obrigatório:**
   - Antes de realizar qualquer modificação, sempre ler o arquivo diretamente do disco para garantir que a versão mais recente comitada pelas outras IAs esteja carregada.
   - Conferir se o arquivo possui conteúdo e tamanho esperado (`Length > 0`).

2. **Modificação Focada e Encoding:**
   - Aplicar alterações precisas, preservando o encoding original (UTF-8 sem BOM para arquivos comuns; scripts `.ps1` do Geely mantêm UTF-8 com BOM exigido pelo PowerShell 5.1).

3. **Validação Pós-Gravação:**
   - Imediatamente após salvar, conferir o tamanho do arquivo no disco (`Get-Item <arquivo> | Select-Object Length`).
   - Se o tamanho for 0 bytes ou menor que o esperado, restaurar imediatamente a partir do Git ou recriar com o conteúdo completo.

4. **Commit Atômico e Isolado:**
   - Realizar `git add <arquivo>` e nomear os arquivos no commit após `--` (`git commit -m "..." -- <arquivo>`) para não levar modificações concorrentes de outras sessões.
