"""
Uso:
    python main.py <arquivo-fonte>        Analisa o arquivo informado
    python main.py --demo                 Executa com o exemplo embutido
    python main.py --help                 Exibe esta ajuda

Exemplos:
    python main.py exemplo.arj
    python main.py tests/programa.arj
    python main.py --demo

Códigos de saída:
    0 : análise léxica concluída sem erros
    1 : análise léxica detectou erros léxicos
    2 : erro de argumentos ou de E/S (arquivo não encontrado etc.)
"""

import sys
from collections import Counter
from pathlib import Path
from token import Token, TokenType

from lexer import Lexer, LexerError

# Código embutido (modo --demo): cobre todos os recursos da linguagem

CODIGO_DEMO = """func verifica_numero(n) {
    if (n > 0) {
        puts('Positivo');
    } else {
        if (n == 0) {
            puts('Zero');
        } else {
            puts('Negativo');
        }
    }
    return n;
}

func main() {
    int contador;
    float media;
    str nome;
    bool ativo = true;

    puts('Digite seu nome: ');
    input(nome);

    if (ativo == true AND contador > 0) {
        puts('Sistema ativo.');
    } else {
        puts('Condicao nao satisfeita.');
    }

    bool r1 = true AND false;
    bool r2 = true OR  false;
    bool r3 = true XOR false;
    bool r4 = true XNOR false;

    for (int i = 0; i < 10; i = i + 1) {
        puts(i);
    }

    float resultado = (media + contador) / 2;
    float potencia  = contador ^ 2;
    int   resto     = contador % 3;

    if (contador != 0 AND media >= 5) {
        puts('valido');
    }

    return 0;
}
"""


# Impressão de tokens e diagnósticos


def imprimir_cabecalho(titulo: str):
    linha = "=" * 72
    print(linha)
    print(titulo)
    print(linha)


def imprimir_tabela_tokens(tokens: list[Token]) -> None:
    """
    Imprime uma tabela de tokens:
        TIPO | LEXEMA | LINHA:COLUNA
    """
    print(f"{'#':>4}  {'TIPO':<22} {'LEXEMA':<32} {'POSIÇÃO':<10}")
    print("-" * 72)
    for i, t in enumerate(tokens, start=1):
        # repr() coloca aspas em torno do lexema para evidenciar espaços/vazios
        lex = repr(t.lexema) if t.lexema else "''"
        pos = f"{t.linha}:{t.coluna}"
        print(f"{i:>4}  {t.tipo.name:<22} {lex:<32} {pos:<10}")


def imprimir_erros(erros: list[LexerError]) -> None:
    print()
    imprimir_cabecalho(f"Erros Léxicos Encontrados: {len(erros)}")
    for e in erros:
        print(f"  Linha {e.linha}, Coluna {e.coluna}: {e.mensagem}")


def imprimir_estatisticas(tokens: list[Token]) -> None:
    """
    Conta ocorrências por TokenType.
    """
    print()
    imprimir_cabecalho("Estatísticas")

    contagem = Counter(t.tipo.name for t in tokens)
    # Ordena por contagem desc, depois alfabética
    for tipo, qtd in sorted(contagem.items(), key=lambda x: (-x[1], x[0])):
        print(f"  {tipo:<22} {qtd:>5}")
    print(f"  {'-' * 28}")
    print(f"  {'TOTAL':<22} {len(tokens):>5}")


# Pipeline principal


def analisar_codigo(codigo: str, origem: str) -> int:
    """
    Executa o lexer sobre uma string de código e imprime o relatório.
    Retorna o código de saída a ser usado pelo processo.
    """
    lexer = Lexer(codigo)
    tokens = lexer.analisar()

    imprimir_cabecalho(f"Análise Léxica — {origem}")
    imprimir_tabela_tokens(tokens)

    imprimir_estatisticas(tokens)

    if lexer.erros:
        imprimir_erros(lexer.erros)
        print()
        print(f"Análise finalizada com {len(lexer.erros)} erro(s) léxico(s).")
        return 1

    print()
    print("Análise finalizada sem erros léxicos.")
    return 0


def mostrar_ajuda() -> None:
    print(__doc__)


# Ponto de entrada


def main(argv: list[str]) -> int:
    args = argv[1:]

    if not args or args[0] in ("-h", "--help"):
        mostrar_ajuda()
        # Se o usuário pediu help explicitamente, saída 0.
        # Se não passou argumentos, saída 2 (uso incorreto).
        return 0 if args else 2

    if args[0] == "--demo":
        return analisar_codigo(CODIGO_DEMO, "<demo embutido>")

    # Caso padrão: primeiro argumento é um caminho de arquivo
    caminho = Path(args[0])
    if not caminho.exists():
        print(f"Erro: arquivo '{caminho}' não encontrado.", file=sys.stderr)
        return 2
    if not caminho.is_file():
        print(f"Erro: '{caminho}' não é um arquivo regular.", file=sys.stderr)
        return 2

    try:
        codigo = caminho.read_text(encoding="utf-8")
    except OSError as e:
        print(f"Erro ao ler '{caminho}': {e}", file=sys.stderr)
        return 2

    return analisar_codigo(codigo, str(caminho))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
