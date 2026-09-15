# ZCARD

## Um formato aberto de mídia para jogos

**ZCARD** é um formato de mídia para jogos desenvolvido para unir a ideia dos antigos cartuchos físicos às necessidades dos jogos modernos.

O objetivo é permitir que um jogo exista como uma **mídia física persistente**, capaz de armazenar o conteúdo original, atualizações, saves, configurações e conteúdo adicional.

> **ZCARD não é apenas um arquivo de jogo. É uma proposta de formato de mídia para uma nova geração de cartuchos.**

## O problema

A distribuição de jogos mudou. Downloads, lojas digitais, instalações e atualizações passaram a fazer parte da experiência, enquanto mídias físicas muitas vezes funcionam apenas como uma licença ou como uma forma de iniciar um download.

Ao mesmo tempo, jogos modernos podem ocupar dezenas ou centenas de gigabytes.

O ZCARD propõe modernizar o conceito do cartucho em vez de simplesmente abandoná-lo.

## O que é ZCARD?

ZCARD é uma especificação de mídia para jogos. Ela define uma forma organizada de representar um jogo como uma unidade de mídia contendo diferentes tipos de dados.

Um ZCARD pode conter:

```text
ZCARD
├── Identificação
├── Metadados
├── Executável
├── Recursos do jogo
├── Dados adicionais
├── Atualizações
├── Conteúdo adicional
├── Configurações
└── Dados do usuário
```

O formato foi pensado para funcionar tanto em uma representação digital para desenvolvimento e testes quanto em uma futura implementação física.

## Princípios

- Mídia física persistente
- Armazenamento moderno
- Separação entre conteúdo original e dados graváveis
- Atualizações
- Saves
- Conteúdo adicional
- Streaming de recursos
- Compatibilidade entre implementações
- Evolução independente da tecnologia física
- Especificação aberta

## Representação digital e física

O formato lógico pode ser representado durante o desenvolvimento por um arquivo `.zcard`.

```text
                  ZCARD
                    │
          ┌─────────┴─────────┐
          │                   │
       DIGITAL             FÍSICO
          │                   │
       .zcard             Cartucho
          │                   │
          └─────────┬─────────┘
                    │
                    ▼
             ZCARD Runtime
```

A representação digital permite desenvolver e testar o ecossistema antes da existência do hardware físico.

## Conteúdo

```text
ZCARD
├── META/
├── CODE/
├── ASSETS/
├── UPDATE/
├── DLC/
└── USER/
    ├── saves/
    └── config/
```

Nem todos os componentes são obrigatórios.

## Capacidade

O formato lógico não define uma capacidade física fixa. Implementações podem utilizar diferentes capacidades conforme o tipo de mídia.

Exemplos:

```text
16 MB
32 MB
64 MB
128 MB

8 GB
16 GB
32 GB
64 GB
128 GB
256 GB+
```

Esses valores são possibilidades de implementação e não limites oficiais da especificação.

## ZCARD, ZConsole, ZEXE e ZCardEmulator

Os projetos possuem responsabilidades diferentes:

```text
ZCARD
└── Formato de mídia

ZConsole
└── Plataforma / console

ZEXE
└── Formato executável

ZCardEmulator
└── Ferramenta de referência e testes
```

O **ZCardEmulator não define o ZCARD**. Ele existe para validar e demonstrar a especificação.

## Emulador de referência

A implementação de referência em C++ permite:

- Montar imagens ZCARD
- Validar conteúdos
- Inspecionar metadados
- Testar ZEXE
- Testar streaming
- Testar o runtime
- Simular a mídia antes do hardware físico

## Estado do projeto

| Componente | Estado |
|---|---|
| Conceito ZCARD | Definido |
| Modelo lógico | Em desenvolvimento |
| `.zcard` | Protótipo |
| Builder | Protótipo funcional |
| Validação | Protótipo |
| ZCF | Experimental |
| ZEXE | Experimental |
| Runtime | Experimental |
| Streaming | Protótipo |
| Emulador | Ferramenta de referência |
| Hardware físico | Pesquisa |

## Roadmap

### Especificação
- [x] Conceito
- [x] Modelo lógico
- [x] Representação digital inicial
- [ ] Cabeçalho oficial
- [ ] Manifesto
- [ ] Regiões
- [ ] Versionamento
- [ ] Compatibilidade
- [ ] Atualizações
- [ ] Saves
- [ ] Segurança

### Software
- [x] Builder
- [x] Representação `.zcard`
- [x] Validação
- [x] Emulador de referência
- [ ] Inspector
- [ ] Validator independente
- [ ] SDK

### Hardware
- [ ] Cartucho físico
- [ ] Controlador
- [ ] Interface
- [ ] Protocolo
- [ ] Identificação da mídia
- [ ] Região gravável
- [ ] Protótipo funcional

## Documentação

A documentação técnica está em [`docs/`](docs/).

## Contribuição

Contribuições são bem-vindas em especificação, software, hardware, segurança, ferramentas e documentação.

Alterações que possam quebrar a compatibilidade do formato devem ser discutidas antes da implementação.

## Licença

Consulte [`LICENSE`](LICENSE) para os termos de utilização do projeto.

## A ideia

> **ZCARD é uma proposta para tornar a mídia física novamente relevante na era dos jogos modernos.**
