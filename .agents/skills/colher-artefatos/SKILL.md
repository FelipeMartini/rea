---
name: colher-artefatos
description: Executa a rotina de colheita dos brains do Antigravity (~/.gemini/antigravity/brain/) para o repositório Git do projeto atual, garantindo que relatórios, planos de implementação e imagens finais nunca se percam. Use quando concluir uma sessão de trabalho, quando pedirem para arquivar o brain ou colher os artefatos gerados.
---

# Colher Artefatos do Antigravity para o Git

O Antigravity salva dados de conversas em `~/.gemini/antigravity/brain/<id>/` (arquivos Markdown de planejamento, relatórios e imagens geradas). Para cumprir a regra de ouro do ecossistema ("Tudo o que vale guardar vive em git"), esta skill executa a colheita dos arquivos valiosos para a pasta de artefatos do repositório.

## Procedimento de Execução

1. **Identificar a Conversa e o Projeto:**
   - Obter o ID da conversa atual ou a conversa alvo.
   - Definir o repositório de destino:
     - No **ProjetoSocial**: `D:\ProjetoSocial\docs\artefatos\antigravity\<data>-<assunto>\`
     - No **ProjetoGeely**: `D:\ProjetoGeely\Documentos\artefatos\antigravity\<data>-<assunto>\`

2. **Comando de Colheita PowerShell:**

   ```powershell
   powershell -ExecutionPolicy Bypass -File D:\ia-comum\scripts\colher-brain.ps1 -Id <id_da_conversa> -Projeto <pasta_do_projeto> -Assunto <assunto-kebab>
   ```

3. **Verificação dos Arquivos Colhidos:**
   - Conferir se o relatório principal (`.md`), planos (`implementation_plan.md`, `walkthrough.md`) e imagens finais foram copiados.
   - O arquivo `ORIGEM.txt` é gerado automaticamente registrando a data e o ID de origem do brain.

4. **Commit e Versionamento:**
   - Avisar o operador ou preparar o commit com `git add <arquivo>` por arquivo.
   - Mensagem padrão: `docs: artefatos do antigravity: <assunto>`.

## O que NUNCA fazer

- Nunca commitar caches de navegadores, logs transitórios ou arquivos de tamanho superior a 50 MB no Git sem autorização.
- Nunca apagar o diretório original do `brain/` sem confirmar que os arquivos foram transferidos com sucesso.

## Prompts de teste

- "colha os artefatos desta conversa para o projeto social"
- "arquive o relatório mestre do brain no repositório"
- "rode a rotina de colheita do antigravity"
