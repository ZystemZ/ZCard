# ZCARD

## Um formato aberto de mídia para jogos

**ZCARD** é um formato de mídia para jogos desenvolvido para unir a ideia dos antigos cartuchos físicos às necessidades dos jogos modernos.

O objetivo do ZCARD é permitir que um jogo possa existir como uma **mídia física persistente**, capaz de armazenar não apenas o conteúdo original do jogo, mas também dados adicionais como atualizações, saves, configurações e conteúdo adicional.

> **ZCARD não é apenas um arquivo de jogo. É uma proposta de formato de mídia para uma nova geração de cartuchos.**

---

## O problema

A distribuição de jogos mudou radicalmente.

Cartuchos e mídias físicas tradicionais foram substituídos em grande parte por:

* Downloads digitais;
* Lojas online;
* Instalações em discos internos;
* Atualizações obrigatórias;
* Conteúdo adicional baixado separadamente;
* Licenças digitais;
* Mídias físicas que funcionam apenas como uma chave para baixar o jogo.

Ao mesmo tempo, os jogos modernos ficaram muito maiores.

Um jogo atual pode ocupar dezenas ou centenas de gigabytes, tornando inviável simplesmente utilizar os conceitos tradicionais de ROM utilizados pelos antigos cartuchos.

O ZCARD propõe uma abordagem diferente:

> **Modernizar o cartucho, em vez de simplesmente abandoná-lo.**

---

# O que é ZCARD?

ZCARD é uma especificação de mídia para jogos.

A especificação define uma forma organizada de representar um jogo como uma unidade de mídia contendo diferentes tipos de dados.

Um ZCARD pode conter:

```text
ZCARD
│
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

---

# ZCARD não é somente um formato de arquivo

Um dos objetivos principais do projeto é diferenciar o **formato lógico da mídia** da tecnologia física utilizada para armazená-la.

O mesmo ZCARD lógico pode existir como:

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

A representação `.zcard` é principalmente uma ferramenta para:

* Desenvolvimento;
* Testes;
* Distribuição;
* Validação;
* Emulação;
* Automação.

A implementação física é um objetivo futuro do projeto.

---

# Objetivos

O ZCARD está sendo desenvolvido com os seguintes objetivos.

## 1. Recuperar a ideia do cartucho

O projeto busca trazer novamente a experiência de possuir um jogo fisicamente.

Um jogo não precisa necessariamente ser apenas um download associado a uma conta.

O cartucho pode voltar a ser a própria mídia do jogo.

---

## 2. Utilizar armazenamento moderno

Diferentemente de cartuchos antigos baseados principalmente em ROM, o ZCARD foi pensado para utilizar tecnologias modernas de armazenamento.

Isso permite trabalhar com capacidades muito maiores.

Exemplos de capacidades possíveis:

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

256 GB ou mais
```

Esses valores representam possibilidades de implementação física e **não são limites definidos pela especificação atual**.

---

# 3. Permitir dados graváveis

Um dos conceitos fundamentais do ZCARD é a separação entre o conteúdo original do jogo e os dados que podem ser modificados.

Conceitualmente:

```text
┌─────────────────────────────────────┐
│                ZCARD                │
├─────────────────────────────────────┤
│                                     │
│       ÁREA ORIGINAL DO JOGO         │
│                                     │
│  Executável                         │
│  Recursos                           │
│  Texturas                           │
│  Áudio                              │
│  Vídeos                             │
│  Dados                              │
│                                     │
├─────────────────────────────────────┤
│                                     │
│          ÁREA GRAVÁVEL              │
│                                     │
│  Saves                               │
│  Configurações                       │
│  Atualizações                        │
│  Conteúdo adicional                  │
│  Dados do usuário                    │
│                                     │
└─────────────────────────────────────┘
```

A forma como essa separação será implementada fisicamente ainda faz parte da pesquisa de hardware do projeto.

---

# 4. Atualizações

Um cartucho moderno não precisa necessariamente permanecer completamente estático.

O ZCARD foi projetado para permitir que o conteúdo original seja complementado por dados de atualização.

Conceitualmente:

```text
ZCARD ORIGINAL
      │
      ├── Jogo 1.0
      │
      └── Atualização
             │
             ▼
          Jogo 1.1
```

Isso pode permitir futuramente:

* Atualizações incrementais;
* Patches;
* Correções;
* Atualizações de recursos;
* Novas versões;
* Conteúdo adicional.

---

# 5. Saves

Os dados de progresso do jogador são tratados separadamente do conteúdo original.

Exemplo:

```text
CONTEÚDO DO JOGO
├── Executável
├── Recursos
├── Mapas
├── Áudio
└── Dados originais

DADOS DO USUÁRIO
├── Saves
├── Configurações
├── Perfil
└── Progresso
```

Isso permite que uma futura implementação física mantenha os dados originais protegidos enquanto fornece uma área apropriada para gravação.

---

# 6. Conteúdo adicional

O formato também pode acomodar conteúdo adicional.

Por exemplo:

```text
Jogo
├── Conteúdo original
├── Atualização
├── DLC
├── Expansão
└── Conteúdo bônus
```

A especificação ainda está em desenvolvimento quanto à forma definitiva de gerenciar versões e dependências desses conteúdos.

---

# Arquitetura

O conceito geral pode ser representado assim:

```text
                    ZCARD
                      │
        ┌─────────────┼─────────────┐
        │             │             │
    METADADOS      CONTEÚDO       DADOS
        │             │             │
        │       ┌─────┴─────┐       │
        │       │           │       │
        │    EXECUTÁVEL    ASSETS   │
        │                         ┌─┴──────┐
        │                         │        │
        │                       SAVES   CONFIG
        │
        └───────────────────────────────┐
                                        │
                                        ▼
                               ZCARD RUNTIME
                                        │
                                        ▼
                                    ZCONSOLE
```

---

# Estrutura lógica

Uma implementação de desenvolvimento pode representar um jogo aproximadamente assim:

```text
game.zcard
│
├── META/
│   ├── manifest
│   └── informações do jogo
│
├── CODE/
│   └── game.zexe
│
├── ASSETS/
│   ├── textures/
│   ├── models/
│   ├── audio/
│   ├── video/
│   └── data/
│
├── UPDATE/
│
├── DLC/
│
└── USER/
    ├── saves/
    └── config/
```

A estrutura definitiva ainda está sendo especificada.

---

# Metadados

Um ZCARD precisa ser capaz de identificar o conteúdo armazenado.

Um exemplo conceitual:

```json
{
    "formato": "ZCARD",
    "versao": 1,
    "jogo": "Exemplo",
    "desenvolvedor": "Estudio Exemplo",
    "versao_jogo": "1.0.0",
    "arquitetura": "ZConsole",
    "entrada": "game.zexe"
}
```

Os metadados poderão futuramente identificar:

* Nome do jogo;
* Desenvolvedor;
* Publicador;
* Versão;
* Região;
* Idiomas;
* Arquitetura;
* Runtime necessário;
* Requisitos mínimos;
* Recursos disponíveis;
* Controladores suportados;
* Espaço necessário;
* Dados de atualização.

---

# Executáveis

O ZCARD é responsável pela organização da mídia.

Ele não precisa definir obrigatoriamente uma única arquitetura de código executável.

No ecossistema ZConsole, está sendo desenvolvido o **ZEXE** como formato executável de referência.

A relação é:

```text
ZCARD
 │
 └── game.zexe
        │
        ▼
   ZConsole Runtime
        │
        ▼
     Hardware
```

Assim:

**ZCARD = mídia**

**ZEXE = executável**

**ZConsole = plataforma/runtime**

Essa separação permite que cada componente evolua de forma independente.

---

# Assets

Um jogo moderno pode possuir milhares ou milhões de arquivos.

O ZCARD foi pensado para permitir que os recursos sejam organizados e acessados de forma eficiente.

Exemplo:

```text
ASSETS/
├── TEXTURES/
├── MODELS/
├── MATERIALS/
├── SHADERS/
├── AUDIO/
├── VIDEO/
├── LEVELS/
└── DATA/
```

---

# Streaming

Jogos grandes não precisam necessariamente carregar todo o conteúdo para a memória.

O ecossistema ZCARD possui suporte experimental ao conceito de carregamento sob demanda.

```text
              ZCARD
                │
                │ solicitação
                ▼
          GERENCIADOR DE ASSETS
                │
       ┌────────┼────────┐
       │        │        │
     CACHE   PREFETCH  PRIORIDADE
       │        │        │
       └────────┼────────┘
                │
                ▼
              JOGO
```

Isso permite trabalhar com:

* Cache;
* Pré-carregamento;
* Dependências;
* Prioridades;
* Streaming;
* Limites de banda;
* Carregamento sob demanda.

---

# Container e sistema de arquivos

ZCARD não deve ser confundido com um sistema de arquivos convencional.

Um sistema de arquivos responde:

> Como armazenar arquivos?

O ZCARD responde:

> Como representar um jogo como uma mídia persistente?

A arquitetura pode utilizar sistemas de armazenamento internamente, mas o jogo deve enxergar uma camada de mídia orientada ao conceito de ZCARD.

```text
ARMAZENAMENTO FÍSICO
        │
        ▼
CAMADA ZCARD
        │
        ├── JOGO
        ├── ATUALIZAÇÕES
        ├── DLC
        └── DADOS DO USUÁRIO
        │
        ▼
RUNTIME
```

---

# Representação digital

Durante o desenvolvimento, um ZCARD pode ser representado como:

```text
game.zcard
```

Isso permite desenvolver o ecossistema antes da existência do hardware físico.

A representação digital pode ser utilizada para:

* Testes;
* Desenvolvimento;
* Automação;
* CI/CD;
* Validação;
* Distribuição;
* Emulação;
* Testes de compatibilidade.

---

# Implementação física

O objetivo de longo prazo é desenvolver uma implementação física do ZCARD.

Conceitualmente:

```text
             ┌─────────────────┐
             │      ZCARD      │
             │                 │
             │ Flash Storage   │
             │ Controller      │
             │ Media Identity  │
             └────────┬────────┘
                      │
                Interface
                      │
                      ▼
               ┌────────────┐
               │  ZConsole  │
               └────────────┘
```

A tecnologia de armazenamento poderá evoluir independentemente da especificação lógica.

---

# Interface física

A interface física do ZCARD ainda está em pesquisa.

O projeto está investigando uma interface proprietária de alta velocidade para comunicação entre o cartucho e o console.

Entre os conceitos estudados estão:

* Comunicação diferencial;
* Controlador dedicado;
* Memória Flash;
* Identificação do cartucho;
* Gerenciamento de armazenamento;
* Dados graváveis;
* Comunicação de alta velocidade.

**A interface elétrica definitiva ainda não faz parte da especificação oficial.**

---

# Por que não simplesmente usar um cartão SD?

Um cartão SD é um dispositivo de armazenamento genérico.

O ZCARD pretende ser uma **mídia específica para jogos**.

Uma implementação dedicada pode futuramente oferecer:

* Identidade própria da mídia;
* Estrutura padronizada;
* Gerenciamento de saves;
* Atualizações;
* Identificação do jogo;
* Recursos de segurança;
* Controle de regiões;
* Streaming;
* Integração direta com o console;
* Possibilidade de autenticação física.

A memória Flash utilizada internamente pode ser semelhante à utilizada em outros dispositivos.

A diferença está na **camada de mídia, controlador e protocolo**.

---

# Segurança

Como o ZCARD pode conter dados fornecidos por terceiros, implementações devem considerar o conteúdo como potencialmente não confiável.

A implementação de referência já trabalha experimentalmente com mecanismos como:

* Validação de arquivos;
* Proteção contra Path Traversal;
* Limitação de tamanho;
* Validação de CRC;
* Validação de manifestos;
* Detecção de caminhos inválidos;
* Detecção de arquivos duplicados;
* Validação de containers.

Futuramente poderão ser estudados:

* Assinatura digital;
* Identidade do desenvolvedor;
* Identidade da mídia;
* Atualizações assinadas;
* Autenticação de cartucho;
* Proteção contra adulteração.

---

# ZCARD e ZConsole

ZCARD e ZConsole são projetos relacionados, mas possuem funções diferentes.

```text
ZCARD
│
└── Formato de mídia


ZConsole
│
└── Plataforma / console


ZEXE
│
└── Formato executável


ZCardEmulator
│
└── Ferramenta de teste e referência
```

A ideia é evitar que o formato ZCARD fique dependente exclusivamente de uma implementação.

---

# Emulador de referência

O projeto possui uma implementação de referência em C++:

**ZCardEmulator**

O emulador existe para:

* Testar a especificação;
* Montar imagens ZCARD;
* Validar conteúdos;
* Testar o runtime;
* Testar ZEXE;
* Testar streaming;
* Testar estruturas de armazenamento;
* Identificar problemas na especificação;
* Permitir desenvolvimento antes do hardware físico.

O emulador é, portanto, **uma ferramenta do ecossistema ZCARD**, e não a definição do formato.

```text
                  ESPECIFICAÇÃO ZCARD
                           │
              ┌────────────┼────────────┐
              │            │            │
           SOFTWARE      HARDWARE      TESTES
              │            │            │
              │            │       ZCardEmulator
              │            │
              │       futuro hardware
              │
        ferramentas/SDK
```

---

# Ferramentas

O ecossistema ZCARD pretende possuir ferramentas para todo o ciclo de desenvolvimento.

```text
              PROJETO DO JOGO
                     │
                     ▼
              ZCARD BUILDER
                     │
                     ▼
                  .zcard
                     │
            ┌────────┴────────┐
            │                 │
       VALIDATOR          EMULADOR
            │                 │
            └────────┬────────┘
                     │
                     ▼
               ZCARD FÍSICO
```

Ferramentas atuais ou planejadas:

* ZCARD Builder;
* ZCARD Validator;
* ZCARD Inspector;
* ZCardEmulator;
* ZCARD SDK;
* Ferramentas para desenvolvedores;
* Ferramentas para hardware.

---

# Estado atual

| Componente             | Estado                      |
| ---------------------- | --------------------------- |
| Conceito ZCARD         | 🟢 Definido                 |
| Modelo lógico da mídia | 🟡 Em desenvolvimento       |
| Representação `.zcard` | 🟢 Protótipo                |
| ZCARD Builder          | 🟢 Protótipo funcional      |
| Validação              | 🟢 Protótipo                |
| ZCF                    | 🟡 Experimental             |
| ZEXE                   | 🟡 Experimental             |
| Runtime ZConsole       | 🟡 Experimental             |
| Streaming de assets    | 🟡 Protótipo                |
| Saves                  | 🟡 Em desenvolvimento       |
| Atualizações           | 🟡 Em desenvolvimento       |
| Emulador               | 🟢 Ferramenta de referência |
| Cartucho físico        | 🔵 Pesquisa                 |
| Interface física       | 🔵 Pesquisa                 |
| Hardware ZCARD         | 🔵 Futuro                   |

**Legenda:**

* 🟢 Implementado/protótipo funcional
* 🟡 Em desenvolvimento
* 🔵 Pesquisa/futuro

---

# Roadmap

## Especificação

* [x] Definir conceito ZCARD
* [x] Definir modelo lógico
* [x] Definir representação digital inicial
* [ ] Definir cabeçalho oficial
* [ ] Definir manifesto
* [ ] Definir regiões de armazenamento
* [ ] Definir metadados
* [ ] Definir versionamento
* [ ] Definir compatibilidade
* [ ] Definir sistema de atualização
* [ ] Definir saves
* [ ] Definir segurança

## Software

* [x] ZCARD Builder
* [x] Representação `.zcard`
* [x] Validação
* [x] ZCardEmulator
* [x] Runtime experimental
* [x] ZEXE experimental
* [x] Streaming experimental
* [ ] ZCARD Validator independente
* [ ] ZCARD Inspector
* [ ] SDK
* [ ] Ferramentas para desenvolvedores

## Hardware

* [ ] Definição do cartucho
* [ ] Protótipo de armazenamento
* [ ] Controlador ZCARD
* [ ] Interface física
* [ ] Protocolo de comunicação
* [ ] Identificação do cartucho
* [ ] Região gravável
* [ ] Protótipo funcional
* [ ] ZConsole de referência

---

# Documentação

A documentação da especificação será separada da implementação do emulador.

Planejamento:

```text
docs/
│
├── ZCARD-SPECIFICACAO.md
├── ZCARD-FORMATO.md
├── ZCARD-CABECALHO.md
├── ZCARD-MANIFESTO.md
├── ZCARD-ARMAZENAMENTO.md
├── ZCARD-ATUALIZACOES.md
├── ZCARD-SAVES.md
├── ZCARD-SEGURANCA.md
├── ZCARD-HARDWARE.md
├── ZCF.md
└── ZEXE.md
```

---

# Contribuindo

O projeto está aberto a contribuições.

Áreas de interesse:

* Especificação de formatos;
* Armazenamento;
* Sistemas de arquivos;
* Desenvolvimento de jogos;
* C++;
* Emulação;
* Sistemas embarcados;
* Hardware;
* Memórias Flash;
* Protocolos de comunicação;
* Segurança;
* Ferramentas de desenvolvimento;
* Documentação.

Alterações que possam quebrar a compatibilidade do formato devem ser discutidas antes da implementação.

---

# Licença

A especificação ZCARD e suas implementações estão em desenvolvimento.

Consulte o arquivo `LICENSE` deste repositório para conhecer os termos de utilização, modificação e distribuição.

Componentes de terceiros podem possuir licenças próprias.

---

# Estado do projeto

O ZCARD é atualmente um projeto experimental de pesquisa e desenvolvimento.

A especificação está sendo desenvolvida simultaneamente com implementações de software para validar suas decisões técnicas.

O **ZCardEmulator** permite testar o formato antes da existência do hardware físico.

O objetivo final é criar um ecossistema no qual desenvolvedores independentes possam criar ferramentas, jogos, emuladores e hardware compatíveis com a especificação.

---

# A ideia

Os cartuchos físicos não precisam desaparecer simplesmente porque os jogos ficaram maiores.

A tecnologia do cartucho pode evoluir.

```text
CARTUCHO TRADICIONAL
        │
        ▼
       ROM
        │
        │
        ▼
       ZCARD
        │
 ┌──────┼────────┐
 │      │        │
GAME  UPDATE   USER
DATA    DATA    DATA
 │       │        │
CODE    PATCH    SAVE
ASSETS  DLC      CONFIG
 │
 └──────────────┐
                ▼
             ZCONSOLE
```

**ZCARD é uma proposta para tornar a mídia física novamente relevante na era dos jogos modernos.**

---

## ZCARD

### Um formato aberto de mídia para a próxima geração de jogos físicos.
