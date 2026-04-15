"""
Módulo de definição de tokens - Arjanov

São definidos:
1. TokenType(enum): todos os tipos de tokens reconhecidos pela linguagem
2. Token(classe): representa token individual com tipo, lexema e posição
3. KEYWORDS(dict): mapeamento de palavras reservadas

A linguagem Arjanov suporta:
  - Tipos de dados: int, float, str, bool
  - Operadores aritméticos: + - * / % ^
  - Operadores lógicos: AND, OR, XOR, XNOR
  - Operadores relacionais: == != < > <= >=
  - Estruturas: if, else, for, while, switch, case
  - Funções: func, return
  - E/S: input, puts
  - Literais: inteiros, decimais, strings (entre aspas simples), booleanos (true, false)
"""

from enum import Enum, auto


class TokenType(Enum):
    """Enumeração de todos os tipos de token reconhecidos"""

    # Literais e identificadores
    INTEIRO = auto()
    DECIMAL = auto()
    STRING = auto()

    IDENTIFICADOR = auto()

    # Palavras reservadas
    INT = auto()
    FLOAT = auto()
    STR = auto()
    BOOL = auto()

    # Booleanos
    TRUE = auto()
    FALSE = auto()

    # Estruturas de controle
    IF = auto()
    ELSE = auto()
    FOR = auto()
    WHILE = auto()
    SWITCH = auto()
    CASE = auto()

    # Funções
    FUNC = auto()
    MAIN = auto()
    RETURN = auto()

    # Entrada e saída
    INPUT = auto()
    PUTS = auto()

    # Operadores aritméticos
    MAIS = auto()
    MENOS = auto()
    MULTIPLICACAO = auto()
    DIVISAO = auto()
    MODULO = auto()
    POTENCIA = auto()

    # Operadores lógicos
    AND = auto()
    OR = auto()
    XOR = auto()
    XNOR = auto()

    # Operadores relacionais
    IGUAL = auto()
    DIFERENTE = auto()
    MENOR = auto()
    MAIOR = auto()
    MENOR_IGUAL = auto()
    MAIOR_IGUAL = auto()

    # Atribuição
    ATRIBUICAO = auto()

    # Delimitadores / Pontuação
    PAREN_ESQ = auto()
    PAREN_DIR = auto()
    CHAVE_ESQ = auto()
    CHAVE_DIR = auto()
    PONTO_VIRGULA = auto()
    VIRGULA = auto()
    DOIS_PONTOS = auto()

    # Especiais
    EOF = auto()
    ERRO = auto()


KEYWORDS = {
    # Tipos de dados
    "int": TokenType.INT,
    "float": TokenType.FLOAT,
    "str": TokenType.STR,
    "bool": TokenType.BOOL,
    # Valores booleanos
    "true": TokenType.TRUE,
    "false": TokenType.FALSE,
    # Estruturas de controle
    "if": TokenType.IF,
    "else": TokenType.ELSE,
    "for": TokenType.FOR,
    "while": TokenType.WHILE,
    "switch": TokenType.SWITCH,
    "case": TokenType.CASE,
    # Funções
    "func": TokenType.FUNC,
    "main": TokenType.MAIN,
    "return": TokenType.RETURN,
    # Entrada e saída
    "input": TokenType.INPUT,
    "puts": TokenType.PUTS,
    # Operadores lógicos (escritos em maiúsculas no código-fonte)
    "AND": TokenType.AND,
    "OR": TokenType.OR,
    "XOR": TokenType.XOR,
    "XNOR": TokenType.XNOR,
}


class Token:
    """
    Representa um token individual reconhecido pelo analisador.

    Cada token carrega quatro informações:
    1. tipo (TokenType): classe/categoria do token
    2. lexema (str): sequência exata de caracteres que originou o token
    3. linha (int): número da linha do código-fonte em que o token aparece (mensagens de erro)
    4. coluna (int): número da coluna em que token começa
    """

    def __init__(self, tipo: TokenType, lexema: str, linha: int, coluna: int):
        # Cria novo token

        self.tipo = tipo
        self.lexema = lexema
        self.linha = linha
        self.coluna = coluna

    def __repr__(self) -> str:
        # Representação de token para depuração
        return f"Token({self.tipo.name}, '{self.lexema}', {self.linha}:{self.coluna})"

    def __eq__(self, other) -> bool:
        # Compara dois tokens por tipo e lexema (para testes)
        if not is_instance(other, Token):
            return False
        return self.tipo == other.tipo and self.lexema == other.lexema


def lookup_keyword(lexema: str) -> TokenType:
    # Consulta se lexema é reservado ou identificador

    return KEYWORDS.get(lexema, TokenType.IDENTIFICADOR)


if __name__ == "__main__":
    # Demonstração: cria alguns tokens e imprime
    tokens_exemplo = [
        Token(TokenType.FUNC, "func", 1, 1),
        Token(TokenType.IDENTIFICADOR, "calcula_media", 1, 6),
        Token(TokenType.PAREN_ESQ, "(", 1, 20),
        Token(TokenType.IDENTIFICADOR, "num1", 1, 21),
        Token(TokenType.VIRGULA, ",", 1, 25),
        Token(TokenType.IDENTIFICADOR, "num2", 1, 27),
        Token(TokenType.PAREN_DIR, ")", 1, 31),
        Token(TokenType.CHAVE_ESQ, "{", 1, 33),
        Token(TokenType.FLOAT, "float", 2, 5),
        Token(TokenType.IDENTIFICADOR, "media", 2, 11),
        Token(TokenType.ATRIBUICAO, "=", 2, 17),
        Token(TokenType.PAREN_ESQ, "(", 2, 19),
        Token(TokenType.IDENTIFICADOR, "num1", 2, 20),
        Token(TokenType.MAIS, "+", 2, 25),
        Token(TokenType.IDENTIFICADOR, "num2", 2, 27),
        Token(TokenType.PAREN_DIR, ")", 2, 31),
        Token(TokenType.DIVISAO, "/", 2, 33),
        Token(TokenType.INTEIRO, "2", 2, 35),
        Token(TokenType.PONTO_VIRGULA, ";", 2, 36),
        Token(TokenType.RETURN, "return", 3, 5),
        Token(TokenType.IDENTIFICADOR, "media", 3, 12),
        Token(TokenType.PONTO_VIRGULA, ";", 3, 17),
        Token(TokenType.CHAVE_DIR, "}", 4, 1),
        Token(TokenType.EOF, "", 4, 2),
    ]

    print("=" * 60)
    print("Tokens do trecho: func calcula_media(num1, num2) { ... }")
    print("=" * 60)
    for tok in tokens_exemplo:
        print(f"  {tok}")

    print()
    print("Teste lookup_keyword:")
    for palavra in ["if", "while", "AND", "contador", "func", "true", "XNOR"]:
        resultado = lookup_keyword(palavra)
        print(f"  lookup_keyword('{palavra}') → {resultado.name}")
