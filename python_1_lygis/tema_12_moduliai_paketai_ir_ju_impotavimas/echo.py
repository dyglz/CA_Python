# echo.py

def echo(text: str, repetitions: int = 10) -> str:
    """Realaus aido imitavimas."""
    echoed_text = ""
    for i in range(repetitions, 0, -1):
        echoed_text += f"{text[-i:]}\n"
    return f"{echoed_text.lower()}."


if __name__ == "__main__":
    text = input("Šaukite ką nors kalno kryptimi: ")
    print(echo(text))


