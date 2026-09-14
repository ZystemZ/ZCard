# Segurança

## Sobre o projeto

ZCARD é um formato destinado a armazenar conteúdo de jogos.

Como arquivos ZCARD podem ser recebidos de fontes externas, implementações devem considerar o conteúdo como potencialmente não confiável.

## Áreas importantes

Problemas de segurança relacionados a:

* Path Traversal;
* Arquivos malformados;
* Containers maliciosos;
* Overflow;
* Corrupção de memória;
* Execução arbitrária;
* Acesso ao sistema hospedeiro;
* Esgotamento de recursos;
* Manipulação de executáveis;
* Manipulação de manifestos

devem ser tratados como prioritários.

## Implementação de referência

A implementação de referência possui mecanismos experimentais de proteção, incluindo:

* Validação de caminhos;
* Limites de tamanho;
* Verificação de CRC;
* Validação de arquivos;
* Validação de manifestos;
* Rejeição de estruturas inválidas.

## Relato

Problemas de segurança devem ser relatados de forma privada sempre que possível.

Não publique detalhes de uma vulnerabilidade explorável antes que ela possa ser analisada e corrigida.

## Futuro

A especificação poderá incorporar:

* Assinaturas digitais;
* Autenticação;
* Identidade do desenvolvedor;
* Identidade da mídia;
* Atualizações assinadas;
* Verificação de integridade.
