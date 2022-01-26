from fastapi import FastAPI

app = FastAPI()


@app.get("/saudacao/{nome}")
def home(nome: str):
    nome = nome.title()
    mensagem = f"Olá {nome}!"
    return {"mensagem": mensagem}


@app.get("/quadrado/{numero}")
def quadrado(numero: int):
    quadrado = numero * numero
    return {"mensagem": f"O quadrado de {numero} é {quadrado}"}


@app.get("/dobro")
def dobro(numero: int):
    dobro = numero * 2
    return {"mensagem": f"O dobro de {numero} é {dobro}"}


@app.get("/area-retangulo")
def area_retangulo(largura: int, altura: int = 2):
    area = largura * altura
    return {"mensagem": f"A área do retângulo é {area}"}
