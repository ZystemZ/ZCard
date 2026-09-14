# Especificação ZCARD

**Versão:** 0.1 — Experimental

## 1. Introdução

ZCARD é uma especificação de mídia destinada ao armazenamento e distribuição de jogos.

A especificação define uma representação lógica de uma mídia de jogo que pode ser implementada tanto digitalmente quanto em hardware físico.

---

## 2. Objetivos

A especificação busca fornecer:

* Identificação padronizada;
* Organização de conteúdo;
* Armazenamento de executáveis;
* Armazenamento de assets;
* Atualizações;
* Saves;
* Configurações;
* Conteúdo adicional;
* Compatibilidade entre implementações;
* Possibilidade de implementação física.

---

## 3. Camadas

A arquitetura é dividida conceitualmente em:

```text
Camada de aplicação
        │
Runtime
        │
ZCARD
        │
Armazenamento
        │
Hardware
```

O formato ZCARD deve permanecer independente da tecnologia física utilizada para armazenamento.

---

## 4. Identificação

Toda mídia compatível deve ser identificável como ZCARD.

A identificação deve permitir determinar:

* Tipo da mídia;
* Versão da especificação;
* Versão mínima do runtime;
* Arquitetura;
* Recursos disponíveis.

---

## 5. Conteúdo

Um ZCARD pode conter:

* Metadados;
* Executável;
* Assets;
* Atualizações;
* DLC;
* Saves;
* Configurações;
* Dados do usuário.

Nem todos os componentes são obrigatórios.

---

## 6. Regiões

A especificação trabalha conceitualmente com regiões de conteúdo.

### Região original

Contém o conteúdo distribuído pelo desenvolvedor.

### Região de atualização

Contém alterações posteriores ao conteúdo original.

### Região de usuário

Contém dados gerados pelo usuário.

A implementação física poderá utilizar mecanismos próprios para garantir a proteção das regiões apropriadas.

---

## 7. Versionamento

Cada ZCARD deve identificar sua versão de formato.

Exemplo:

```text
ZCARD v1
```

Mudanças incompatíveis deverão gerar uma nova versão principal.

---

## 8. Compatibilidade

Implementações devem verificar:

```text
Versão do ZCARD
Versão do Runtime
Arquitetura
Recursos necessários
```

antes de executar o conteúdo.

---

## 9. Integridade

Implementações podem utilizar hashes e checksums para verificar:

* Arquivos;
* Manifestos;
* Executáveis;
* Assets;
* Regiões.

A implementação de referência atualmente utiliza mecanismos de validação como CRC e hashes.

---

## 10. Segurança

Implementações devem considerar todo ZCARD externo como entrada potencialmente não confiável.

Devem ser evitados:

* Path Traversal;
* Arquivos malformados;
* Overflow;
* Consumo excessivo de recursos;
* Execução arbitrária no host;
* Acesso indevido ao sistema hospedeiro.

---

## 11. Estado

Esta especificação é experimental.

A estrutura definitiva poderá sofrer alterações antes de uma versão estável.

Alterações futuras devem preservar compatibilidade sempre que possível.

---

## 12. Implementação de referência

O projeto mantém uma implementação de referência em C++:

**ZCardEmulator**

A implementação serve para testar as decisões da especificação e não deve ser considerada a própria definição do formato.

---

## 13. Futuro

Versões futuras deverão definir formalmente:

* Header;
* Manifesto;
* Regiões;
* Índices;
* Atualizações;
* Saves;
* Segurança;
* Assinaturas;
* Hardware;
* Protocolo físico.
