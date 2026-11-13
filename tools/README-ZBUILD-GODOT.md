# ZBuild Godot — MVP 0.1

Primeiro backend de exportação Godot do ecossistema ZSystemZ. O MVP é uma CLI Python que usa o próprio Godot 4.x em modo headless e empacota os artefatos no contêiner ZCARD ZIP legado já aceito pelo runtime atual.

## Estado e escopo

- Hosts previstos: Windows e Linux (Python 3.10+).
- Engine: Godot 4.x, detectado em tempo de execução; versões fora da linha 4 são rejeitadas.
- Destinos: Windows x86_64, Linux x86_64, Android.
- Atalhos: `dual` = Windows + Linux; `all`/ `multiplatform` = Windows + Linux + Android.
- Android: requer preset Android configurado para Gradle, templates/export templates compatíveis, JDK/Android SDK/Gradle conforme exigência da versão Godot, e configuração de assinatura fornecida pelo desenvolvedor.
- Saída: arquivo `.zcard` ZIP legado com `META/zgame.json`, artefatos em `CODE/GODOT/<TARGET>/` e hashes em `META/SHA256SUMS.json`.

**Importante:** builds Godot continuam sendo builds nativos Godot. O ZBuild não converte executáveis Godot em ZEXE, não os executa na CPU virtual experimental e não altera o formato ZCF. O pacote usa a compatibilidade ZIP legada já existente no ZCard runtime.

## Pré-requisitos

1. Python 3.10 ou superior.
2. Godot 4.x instalado e acessível no PATH, ou caminho explícito em `--godot` / variável `GODOT_BIN`.
3. Projeto com `project.godot`.
4. Presets configurados no arquivo `export_presets.cfg`. Os nomes padrão esperados são:
   - `Windows Desktop`
   - `Linux/X11`
   - `Android`
5. Export templates da mesma versão do Godot.
6. Para Android, configure no editor o preset Gradle, SDK/JDK e credenciais. Não armazene keystores nem senhas no repositório.

## Uso

Windows (PowerShell):

```powershell
py -3 tools/zbuild-godot.py --project C:\Games\MeuJogo --output C:\Builds\MeuJogo.zcard --targets dual
```

Linux:

```bash
python3 tools/zbuild-godot.py --project ~/Games/meu-jogo --output ~/Builds/meu-jogo.zcard --targets dual
```

Android:

```bash
python3 tools/zbuild-godot.py --project ./MeuJogo --output ./dist/MeuJogo-Android.zcard --targets android
```

Multiplataforma:

```bash
python3 tools/zbuild-godot.py --project ./MeuJogo --output ./dist/MeuJogo.zcard --targets all
```

Sobrescreva nomes de presets se seu projeto usar outros:

```bash
python3 tools/zbuild-godot.py --project ./MeuJogo --output ./dist/MeuJogo.zcard --targets dual \
  --preset-windows "Windows Desktop" --preset-linux "Linux/X11"
```

A saída inclui um relatório `.build.json` ao lado do cartucho. O diretório do projeto original nunca é usado como diretório de exportação: o ZBuild copia o projeto para um workspace temporário, excluindo `.git`, `.godot` e caches do ZBuild.

## Layout do cartucho

```text
META/
  zgame.json
  SHA256SUMS.json
CODE/
  GODOT/
    WINDOWS/
    LINUX/
    ANDROID/
```

O manifesto mantém `format: zgame-native-0.1` e identifica o engine como `godot-4`. O campo `executable` aponta para um artefato principal, enquanto `executables` registra os artefatos por destino.

## Limitações conhecidas do MVP 0.1

- Não há interface gráfica ainda; esta CLI é o backend inicial para futura integração no ZConsole SDK.
- Os presets precisam existir e ter nomes compatíveis; o programa não cria presets automaticamente.
- Exportação cruzada depende dos templates e das restrições da versão Godot e dos plugins nativos do projeto.
- Android AAB é gerado pelo fluxo Gradle. Se o preset não estiver em modo Gradle ou não gerar APK e AAB, o build falha com diagnóstico em vez de declarar sucesso parcial.
- Não há ainda assinatura/verificação criptográfica do pacote ZCARD, atualização incremental, DLC nem montagem em hardware físico.
- O ZIP legado é usado intencionalmente por compatibilidade. A adoção de ZCF exigirá integração com o builder e a especificação ZCF de referência, além de testes de regressão.
- A execução de um jogo Godot no ZConsole OS depende do runtime/ambiente de execução nativo apropriado; empacotar no ZCARD não implica que o atual emulador de CPU ZEXE execute o jogo.

## Testes

Execute:

```bash
python3 -m unittest discover -s tools -p 'test_*.py' -v
python3 -m py_compile tools/zbuild-godot.py
```
