# Checklist mestre do ZConsole, ZCARD e toolchains

## Objetivo

O objetivo é transformar o protótipo atual em um fluxo verificável no Windows: compilar um jogo ou runtime compatível com ZConsole, identificar o executável virtual, empacotar código e assets em um arquivo `.zcard`, montar esse arquivo no emulador e iniciar a execução pela CPU virtual.

O plano terá dois caminhos de produção. O primeiro será o caminho **C++ nativo**, validado inicialmente com o código-fonte do Overgrowth. O segundo será o caminho **Unity**, no qual um projeto Unity de teste será exportado para o formato executável do ZConsole e depois empacotado em `.zcard`.

## Estado atual

| Área | Estado | Evidência ou observação |
|---|---|---|
| Projeto Visual Studio | Parcialmente pronto | Existe solução monolítica `ZCardEmulator.sln` com projeto C++ Win32. |
| Compilação C++ | Estruturada | O projeto usa MSBuild, C++17, x64 e toolset v143. |
| GUI | Protótipo funcional | Existe dashboard Win32 com montagem, abertura de `.zcard`, prefetch, assets e eventos. |
| Host | Implementado inicialmente | Há abstração de host para tempo, espera e ciclo de vida. |
| Virtual ZCARD em diretório | Implementado | Monta diretório contendo `META/assets.zgf` e `assets`. |
| Reader `.zcard` | Implementado em primeira versão | Lê contêiner ZIP; `stored` funciona sem dependência; DEFLATE depende de ZLIB. |
| Runtime de assets | Implementado em protótipo | Cache, streaming, prefetch, cenas, dependências, canais e deadlines. |
| CPU virtual | Implementada em primeira versão | Possui `NOP`, `LOAD_IMM`, `ADD_IMM`, `STORE`, `JMP` e `HALT`. |
| Memória virtual | Implementada em primeira versão | Memória linear com leitura, escrita, limites e reset. |
| Ciclo de instruções | Implementado em primeira versão | Fetch, decode, execute e contador de instruções. |
| Formato ZEXE | Funcional mínimo | Header de 40 bytes, checksum, arquitetura ZCPU-32 e CODE flat estão implementados; segmentos avançados e símbolos continuam pendentes. |
| Carregador ZEXE | Funcional mínimo | Inspeciona e carrega CODE na memória virtual; relocação e segmentos avançados continuam pendentes. |
| Builder ZCARD nativo | Funcional por CLI | `zcard_builder` gera ZIP legado ou ZCF a partir de um projeto compilado. |
| Manifesto do jogo | Validação funcional | `META/zgame.json` é validado para formato, plataforma, executável e memória. |
| Identificação do executável | Funcional no fluxo MVP | O Builder e o boot localizam `CODE/game.zexe`; o dashboard exibe o executável. |
| Execução de jogo real | Pendente | A CPU atual é uma base experimental, não uma arquitetura final de jogos. |
| Integração Overgrowth | Não iniciada | O código-fonte deve ser estudado e compilado separadamente antes de adaptação. |
| Integração Unity | Não iniciada | Ainda falta SDK, pacote Unity, backend de compilação e exporter. |
| Teste ponta a ponta | Funcional no MVP | `runtime_tests` cobre `ZEXE -> ZCARD -> mount -> load -> run`; o teste ZCF de segurança foi adicionado. |

## Critérios de conclusão do MVP

O MVP do ZConsole será considerado concluído quando o sistema conseguir executar o fluxo abaixo sem intervenção manual nos arquivos internos:

```text
Diretório do projeto
    -> validação
    -> compilação para ZEXE
    -> geração de META/zgame.json
    -> geração de jogo.zcard
    -> montagem no emulador
    -> identificação do ZEXE
    -> carregamento na memória virtual
    -> definição do entry point
    -> boot da CPU
    -> execução observável no dashboard
```

A execução observável deve mostrar pelo menos o estado do console, o program counter, o número de instruções, o executável carregado, a cena inicial, eventos de boot e métricas do runtime.

# Fase 0 — Fundação e contratos

- [ ] Fixar a arquitetura do ZConsole em módulos: `Core`, `CPU`, `Memory`, `Runtime`, `VirtualZCard`, `Host`, `Graphics`, `Audio`, `Input` e `Tools`.
- [ ] Definir a versão inicial da arquitetura da CPU virtual.
- [ ] Definir endianness, tamanho de palavra, alinhamento e mapa de memória.
- [ ] Definir códigos de erro públicos e mensagens de diagnóstico.
- [ ] Definir o ciclo de vida: `create`, `mount`, `verify`, `boot`, `run`, `pause`, `reset`, `shutdown`.
- [ ] Manter a solução Visual Studio em formato simples, seguindo o projeto funcional de referência.
- [ ] Criar testes de contrato que não dependam de assets comerciais.

# Fase 1 — CPU virtual e executável ZEXE

## CPU

- [x] Criar registradores básicos `A`, `B` e `PC`.
- [x] Criar flag `zero`.
- [x] Criar estado `halted`.
- [x] Implementar `NOP`.
- [x] Implementar carregamento imediato.
- [x] Implementar soma imediata.
- [x] Implementar armazenamento em memória.
- [x] Implementar salto absoluto.
- [x] Implementar `HALT`.
- [x] Adicionar pausa e retomada controladas.
- [x] Definir instruções de comparação e saltos condicionais (`CMP_IMM`, `JZ`).
- [x] Definir pilha, chamadas e retorno de função (`PUSH_A`, `POP_A`, `CALL`, `RET`).
- [ ] Definir interrupções e chamadas do sistema ZConsole.
- [ ] Definir instruções SIMD ou operações vetoriais, se necessárias ao renderer.
- [x] Criar debugger básico com registrador `SP`, pausa e breakpoint por endereço.

## Formato ZEXE

- [x] Definir assinatura do arquivo, por exemplo `ZEXE`.
- [x] Definir versão e arquitetura alvo.
- [x] Definir tamanho de header.
- [x] Definir entry point.
- [ ] Definir segmentos `CODE`, `RODATA`, `DATA` e `BSS`.
- [ ] Definir alinhamento de segmentos.
- [x] Definir checksum ou hash do executável.
- [ ] Definir tabela opcional de símbolos para debug.
- [x] Criar `ZExecutableLoader`.
- [x] Validar memória requerida antes do carregamento.
- [ ] Relocar segmentos quando necessário.
- [x] Configurar `PC` e registradores iniciais.
- [x] Criar um programa ZEXE mínimo que escreva um valor na memória e execute `HALT`.
- [x] Criar exemplo completo autoral `examples/complete-game.zgame` com condição, `CALL`/`RET`, assets e geração de `.zcard`.

# Fase 2 — Builder e arquivo ZCARD

## Fase A — MVP-2 ZCF 0.1

- [x] Especificar header fixo, tabela de regiões, hashes e compatibilidade em `docs/ZCF_SPEC.md`.
- [x] Registrar ordem de implementação e critérios de pronto em `docs/PHASE_A_REPORT.md`.
- [x] Implementar `ZCardContainer` com header ZCF e regiões.
- [x] Preparar detecção ZCF e ZIP legado no `VirtualZCard`; ZIP legado segue validado pelo CTest.
- [x] Emitir ZCF com `zcard_builder --format zcf`, região MASTER alinhada e teste ponta a ponta.
- [x] Calcular e validar SHA-256 do header e da região MASTER.
- [x] Rejeitar cartão ZCF corrompido no carregamento do emulador.
- [x] Emitir regiões `UPDATE`, `DLC`, `SAVE` e `USER` com capacidade reservada.
- [x] Expor `VirtualZCard::writeStream` e bloquear escrita na `MASTER`.
- [x] Testar escrita/leitura de dados na região `SAVE`.

## Hardware virtual mínimo

- [x] Criar framebuffer RGBA8 determinístico com `clear` e `fillRect`.
- [x] Criar fila de eventos e estado de input virtual.
- [x] Criar API de tons de áudio headless.
- [x] Conectar framebuffer, input e áudio a backend SDL2 real opcional.
- [ ] Implementar renderer 3D Vulkan com swapchain, recursos GPU e shaders.
- [x] Criar `ZVulkanRuntime` para instance e enumeração de GPUs; validar com `--vulkan-info`.
- [x] Integrar extensões SDL2, `VkSurfaceKHR` e seleção de fila gráfica/apresentação.
- [x] Criar `VkDevice`, negociar formato/extensão e criar `VkSwapchainKHR` com image views.
- [x] Criar render pass, framebuffers, command buffers, sincronização e `presentFrame()` com clear.
- [ ] Implementar backend DirectX 12 para Windows.
- [ ] Implementar fallback OpenGL compatível.
- [x] Definir perfis de resolução, backend gráfico e áudio HD em `platform/services.hpp`.
- [x] Enumerar joysticks USB via SDL2 e preservar ID/nome para mapeamentos futuros.
- [x] Criar sandbox de instalação, save, cache e user com quota e gravação atômica.
- [ ] Implementar sockets reais e transporte de rede multiplataforma.
- [x] Proteger escrita na região `MASTER`.
- [x] Verificar hash SHA-256 da região `MASTER` no boot.
- [x] Criar `tests/zcf_tests.cpp` com rejeição de sobreposição e capacidade divergente.

## Builder

- [x] Criar `ZCardBuilder` nativo (primeira versão stored ZIP).
- [x] Permitir selecionar diretório de origem pela CLI `zcard_builder --source`.
- [x] Permitir selecionar arquivo de saída pela CLI `zcard_builder --output`.
- [x] Validar a presença de `META/zgame.json`.
- [x] Localizar `CODE/game.zexe`.
- [x] Localizar assets recursivamente.
- [x] Calcular hashes dos arquivos.
- [x] Detectar arquivos duplicados.
- [x] Detectar arquivos ausentes.
- [x] Detectar caminhos inválidos para Windows e ZConsole.
- [x] Gerar `META/assets.zgf` automaticamente quando ausente, inferindo o tipo pela extensão.
- [ ] Gerar ou validar `META/zgame.json`.
- [ ] Gerar índice de assets.
- [x] Empacotar arquivos em `.zcard`.
- [x] Verificar o `.zcard` imediatamente após a criação (montagem no teste ponta a ponta).
- [x] Gerar relatório de build com tamanho, compressão, hashes e warnings.
- [x] Documentar e preservar tipos customizados opcionais no manifesto ZGF (`AssetInfo::type`).
- [x] Disponibilizar comando reproduzível `zcard_builder` e teste CTest dedicado.
- [x] Ordenar entradas e gerar saída determinística no Builder.
- [x] Reabrir e verificar o ZCARD automaticamente após a criação.

## Reader

- [x] Ler diretório ZIP central.
- [x] Localizar assets por nome.
- [x] Abrir assets como `ZAssetStream`.
- [x] Suportar entradas `stored`.
- [x] Garantir suporte DEFLATE no projeto Visual Studio sem configuração manual confusa.
- [x] Adicionar verificação de CRC32.
- [x] Rejeitar ZIP64 não suportado com mensagem clara.
- [x] Rejeitar path traversal, como `../arquivo`.
- [x] Limitar tamanho máximo de entrada e arquivo.
- [x] Implementar leitura de manifesto diretamente do `.zcard`.
- [x] Expor lista de entradas pela API do reader.

## Manifesto do jogo

Criar o formato inicial:

```json
{
  "format": "zgame-0.1",
  "title": "Meu jogo",
  "platform": "zconsole-v1",
  "executable": "CODE/game.zexe",
  "entrypoint": 0,
  "boot_scene": "menu",
  "memory_required": 16777216
}
```

- [x] Validar campos obrigatórios do manifesto e formato/plataforma.
- [x] Validar se o executável indicado existe.
- [x] Validar se o entry point está compatível com o segmento de código.
- [x] Validar compatibilidade de arquitetura e memória requerida.
- [x] Mostrar no dashboard o título, executável, entry point, registradores e cena inicial.

# Fase 3 — Emulador e dashboard

- [x] Montar diretório Virtual ZCARD.
- [x] Montar arquivo `.zcard`.
- [x] Mostrar status básico.
- [x] Mostrar assets do manifesto de diretório.
- [x] Mostrar eventos de boot e prefetch.
- [x] Mostrar cache hits/misses.
- [x] Mostrar bytes lidos e streamed.
- [x] Mostrar latência estimada.
- [x] Mostrar cartão atual e tipo de origem: diretório ou arquivo (drive físico permanece futuro).
- [x] Mostrar manifesto do jogo no painel dedicado.
- [x] Mostrar executável detectado no status e no conteúdo do cartão.
- [x] Mostrar entry point no status.
- [x] Mostrar registradores da CPU.
- [ ] Mostrar memória usada e memória disponível.
- [x] Adicionar botões `Boot`, `Pause`, `Resume`, `Reset` e `Stop`.
- [x] Adicionar execução por quantidade de instruções (`Step` executa uma instrução).
- [ ] Adicionar execução por frame.
- [ ] Adicionar breakpoint por endereço.
- [x] Adicionar painel de memória hexadecimal em torno do PC.
- [x] Adicionar painel de eventos de erro/log.
- [x] Gerar manual HTML completo do dashboard e do inspetor.
- [ ] Salvar e abrir configurações do emulador.

# Fase 4 — Pipeline C++ nativo

O caminho C++ deve aceitar um projeto já compilado ou um projeto de jogo adaptado para a ABI do ZConsole.

- [ ] Definir o SDK C++ do ZConsole.
- [ ] Criar headers públicos para janela, input, áudio, filesystem, clock e renderer.
- [ ] Definir ABI e convenção de chamadas.
- [ ] Criar bibliotecas `zconsole_core`, `zconsole_graphics`, `zconsole_audio` e `zconsole_input`.
- [ ] Criar um runtime C++ de exemplo.
- [ ] Criar um compilador ou backend que produza `.zexe`.
- [ ] Criar um linker para combinar código e dados.
- [ ] Criar símbolos de debug.
- [ ] Criar template Visual Studio para um jogo ZConsole.
- [ ] Criar botão `Build ZEXE`.
- [ ] Criar botão `Build ZCARD`.
- [ ] Criar botão `Run in Emulator`.
- [x] Criar teste automatizado que gere um `.zcard` e execute o programa mínimo.
- [x] Testar jogo exemplo completo por diretório e por arquivo `.zcard` na CPU virtual.

## Uso do Overgrowth como teste C++

O Overgrowth deve ser usado em três níveis, e não como primeiro jogo executável completo:

| Nível | Objetivo | Critério |
|---|---|---|
| 1. Compilação | Confirmar que o código-fonte C++ e dependências compilam no Windows | Build reproduzível do código disponível |
| 2. Auditoria de engine | Mapear janela, input, áudio, filesystem, threads, OpenGL e dependências | Relatório de pontos de adaptação |
| 3. Portabilidade | Criar uma amostra mínima do engine para ZConsole | Programa reduzido inicia no emulador |

- [ ] Clonar o repositório oficial em uma pasta separada do SDK.
- [ ] Ler `COMPILING.md` e reproduzir primeiro o build original.
- [ ] Registrar versão do compilador, SDK e dependências.
- [ ] Separar código do engine de dados comerciais.
- [ ] Mapear APIs específicas de Windows, Linux, Steam e OpenGL.
- [ ] Mapear uso de threads, sockets, filesystem e shaders.
- [ ] Criar uma matriz de compatibilidade com o ZConsole SDK.
- [ ] Criar um fork ou branch de adaptação, sem alterar o repositório original.
- [ ] Começar por uma amostra mínima, não pelo jogo completo.
- [ ] Substituir janela/input/renderer por adaptadores ZConsole.
- [ ] Substituir carregamento de assets por `ZAssetStream`.
- [ ] Gerar um `.zexe` reduzido.
- [ ] Empacotar a amostra em `.zcard`.
- [ ] Executar a amostra no emulador.

O repositório oficial informa que o código está sob Apache-2.0, mas os assets artísticos e níveis comerciais não estão incluídos. O teste deve respeitar essa separação e não deve redistribuir dados comerciais sem autorização [1] [2].

# Fase 5 — Suporte Unity

O suporte Unity não deve tentar converter um `.exe` comum do Windows para ZConsole. O caminho correto é fornecer um **Unity SDK** e um backend de build que gere código/bytecode compatível com ZConsole.

## Arquitetura Unity proposta

```text
Unity Editor
    ├── ZConsole package
    ├── ZConsole settings
    ├── Asset postprocessor
    ├── Build pipeline
    └── ZConsole exporter
             │
             ▼
        game.zexe + assets
             │
             ▼
        ZCARD Builder
             │
             ▼
        game.zcard
```

## Pacote Unity

- [x] Criar pacote importável `com.zconsole.exporter` (base para `com.zcard.zconsole`).
- [ ] Criar assembly definitions.
- [ ] Criar APIs de plataforma para tempo, input, filesystem e janela.
- [ ] Criar `ZConsolePlatform`.
- [x] Criar perfil configurável `ZConsoleBuildProfile`.
- [x] Criar menus `ZConsole > Create Build Profile` e `ZConsole > Export ZGAME...`.
- [ ] Criar validação de projeto antes do build.
- [ ] Criar definição de versão do SDK.
- [x] Criar documentação de instalação do pacote.

## Exportação de assets

- [ ] Interceptar assets incluídos na cena inicial.
- [ ] Detectar dependências de prefabs, materiais, texturas, meshes, animações, áudio e shaders.
- [ ] Mapear assets para grupos ZGF.
- [ ] Gerar cenas e prioridades de prefetch.
- [ ] Calcular hash de cada asset.
- [ ] Converter formatos incompatíveis para formatos ZConsole.
- [x] Evitar incluir arquivos `.meta` do Unity por padrão.
- [x] Gerar `META/assets.zgf` com tipos inferidos por extensão.
- [x] Gerar `META/zgame.json` a partir do perfil.

## Backend de compilação

- [ ] Definir se o código de gameplay será convertido para C++/ZEXE, bytecode ou uma VM intermediária.
- [ ] Implementar primeiro o caminho de bytecode/VM, se a compilação direta de C# para ZEXE não estiver disponível.
- [ ] Definir como scripts C# acessarão a API ZConsole.
- [ ] Criar bindings para input, transform, câmera, áudio e assets.
- [ ] Proibir APIs Unity não suportadas com erros de build claros.
- [ ] Gerar arquivo de símbolos para debug.
- [ ] Criar teste Unity mínimo com uma cena, câmera, mesh e input.
- [ ] Gerar `game.zexe` ou equivalente virtual.
- [ ] Gerar `game.zcard` automaticamente ao final do build.
- [ ] Abrir o resultado diretamente no ZConsole Emulator.

## Jogo Unity de teste do usuário

- [ ] Criar projeto Unity mínimo.
- [ ] Criar cena `Boot`.
- [ ] Criar cena `Menu`.
- [ ] Criar uma cena jogável simples.
- [ ] Usar somente assets próprios ou redistribuíveis.
- [ ] Instalar o pacote ZConsole.
- [ ] Configurar plataforma ZConsole.
- [ ] Executar validação de compatibilidade.
- [ ] Gerar `.zexe`.
- [ ] Gerar `.zcard`.
- [ ] Abrir `.zcard` no emulador.
- [ ] Confirmar boot e execução.
- [ ] Confirmar cache e prefetch no dashboard.
- [ ] Depurar o jogo com símbolos e breakpoints.

# Fase 6 — Drive ZCARD físico

- [x] Definir protocolo do ZCARD físico.
- [x] Definir identificação de dispositivo.
- [x] Definir transporte inicial USB CDC para desenvolvimento e reservar transporte dedicado para versões futuras.
- [x] Definir permissões e segurança.
- [x] Criar `ZHSDevice` separado de `VirtualZCard`.
- [ ] Detectar unidades removíveis no Windows.
- [ ] Mostrar dispositivos no dashboard.
- [x] Montar em modo somente leitura inicialmente.
- [ ] Implementar verificação de firmware e integridade.
- [x] Adicionar testes sem hardware real.
- [x] Implementar dispatcher de `GET_INFO`, `READ`, `VERIFY` e `GET_STATUS` sobre `ZHSDevice`.
- [x] Validar montagem e boot dos exemplos C0-C8 como diretórios.
- [x] Separar C8 como payload Windows externo sem `game.zexe`.
- [x] Adicionar exportação de `.zcard` pela GUI/Builder.
- [x] Adicionar criação de pacote `.zuf` pela GUI/Builder.
- [x] Implementar resolvedor de ROMs por extensão e `rom-runtime.json`.
- [x] Preparar invocação externa sem shell e com expansão segura de `{rom}`.
- [ ] Implementar execução efetiva em núcleo interno ou processo externo configurado.
- [x] Distinguir ZIP legado (`PK`) de ZCF (`ZCF0`) ao abrir arquivos `.zcard`.
- [x] Testar geração, reabertura e boot de um `.zcard` ZIP e de um `.zcard` ZCF.
- [x] Classificar ISO pelo sistema declarado: console para emulador e PC para montagem Windows.

# Fase 7 — Qualidade, segurança e distribuição

- [ ] Testar caminhos inválidos e path traversal.
- [ ] Testar arquivos ZCARD corrompidos.
- [ ] Testar assets truncados.
- [ ] Testar manifestos inválidos.
- [ ] Testar executáveis incompatíveis.
- [ ] Testar falta de memória.
- [ ] Testar cancelamento durante prefetch.
- [ ] Testar deadlines perdidos.
- [ ] Testar falhas de ZLIB.
- [ ] Adicionar logs em arquivo.
- [ ] Adicionar dump de diagnóstico.
- [ ] Criar builds Debug e Release.
- [ ] Criar pacote ZIP reproduzível.
- [ ] Criar instalador opcional.
- [ ] Documentar licenças de dependências.
- [ ] Não incluir assets comerciais de terceiros no pacote.

# Ordem recomendada de execução

A ordem que reduz mais risco financeiro e técnico é a seguinte:

| Ordem | Entrega | Resultado esperado |
|---:|---|---|
| 1 | ZEXE mínimo | CPU carrega e executa um programa próprio |
| 2 | Manifesto `zgame.json` | Emulador identifica executável e entry point |
| 3 | Builder ZCARD | Diretório vira `.zcard` automaticamente |
| 4 | Dashboard completo | Usuário acompanha boot, CPU, cache e prefetch |
| 5 | SDK C++ | Um jogo C++ mínimo compila para ZConsole |
| 6 | Overgrowth nível 1 | Código-fonte compila no ambiente de referência |
| 7 | Overgrowth nível 2 | APIs incompatíveis são catalogadas |
| 8 | Unity SDK | Projeto Unity pode ser validado e exportado |
| 9 | Jogo Unity de teste | Usuário gera seu primeiro `.zcard` funcional |
| 10 | Overgrowth nível 3 | Amostra reduzida roda no emulador |
| 11 | Drive físico | Hardware é conectado sem alterar o runtime de jogo |

# Definição de pronto do primeiro marco

O primeiro marco recomendado será chamado **ZConsole MVP-1**. Ele estará pronto quando um programa próprio mínimo, compilado para `.zexe`, puder ser empacotado em `.zcard`, montado pela GUI, identificado pelo manifesto, carregado na memória virtual e executado com PC e contador de instruções visíveis.

Unity e Overgrowth devem entrar depois desse marco. Sem um formato executável e um contrato de plataforma estáveis, tentar converter diretamente um jogo C++ grande ou um projeto Unity produzirá erros difíceis de diagnosticar.

## Referências

[1]: https://github.com/WolfireGames/overgrowth "Repositório oficial do código-fonte do Overgrowth"
[2]: https://www.wolfire.com/blog/2022/04/Overgrowth-Open-Source-Announcement/ "Anúncio oficial da abertura do código do Overgrowth"
