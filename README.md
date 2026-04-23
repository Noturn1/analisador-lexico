# Analisador Léxico — Linguagem Arjanov

Implementação da Parte 1 de um compilador para a linguagem **Arjanov**, desenvolvida na disciplina de Compiladores.

---

## Estrutura do projeto

```
analisador-lexico/
├── token.py                              # Definição dos tipos de tokens e palavras reservadas
├── lexer.py                              # Lógica principal de tokenização
├── main.py                               # Ponto de entrada — lê o arquivo e exibe os tokens
├── AutomatoArjanov.jpeg                  # Diagrama do autômato finito da linguagem
└── Especificação Analisador Léxico.docx  # Documentação formal da especificação
```

---

## Como executar

**Requisitos:** Python 3.10 ou superior. Sem dependências externas.

**Analisar um arquivo:**
```bash
python main.py <arquivo.arj>
```

---

## Funcionamento

O lexer lê o código-fonte caractere a caractere e agrupa os caracteres em **tokens**, cada um com tipo, lexema e posição (linha:coluna).

**Estratégias aplicadas:**
- **Maximal munch** — consome sempre o maior prefixo válido (ex: `>=` em vez de `>` + `=`)
- **Reservada vence identificador** — o lexema é lido por completo e consultado no dicionário de palavras reservadas ao final
- **Lookahead de 1** — necessário para distinguir `=` de `==`, `<` de `<=`, etc.
- **Modo pânico** — ao encontrar um erro, registra e continua; todos os erros do arquivo são reportados

---

## Tokens reconhecidos

| Categoria | Exemplos |
|---|---|
| Tipos | `int` `float` `str` `bool` |
| Literais | `42` `3.14` `'texto'` `true` `false` |
| Identificadores | `contador` `_var` `media2` |
| Estruturas | `if` `else` `while` `for` `switch` `case` |
| Funções | `func` `main` `return` |
| E/S | `input` `puts` |
| Aritméticos | `+` `-` `*` `/` `%` `^` |
| Relacionais | `==` `!=` `<` `>` `<=` `>=` |
| Lógicos | `AND` `OR` `XOR` `XNOR` |
| Pontuação | `(` `)` `{` `}` `;` `,` `:` |

---

## Erros detectados

| Tipo | Exemplo |
|---|---|
| Caractere inválido | `@` `#` `$` |
| Número mal formado | `3.` |
| String não fechada | `'texto sem fechar` |
| `!` isolado | `!` (válido apenas como `!=`) |
