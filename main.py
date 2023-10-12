import asyncio
from colorama import Fore
import simpleaudio as sa

def reproducir_musica():
    wave_obj = sa.WaveObject.from_wave_file("DBZ.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

async def imprimir_letra(letra):
    for linea in letra:
        frase = linea["text"].center(100, "-")
        print(Fore.GREEN + frase)
        await asyncio.sleep(linea["sleep"])

letra_cancion = [
    {"sleep":11, "text":"Cha-La Head-Cha-La (versión latino)"},
    {"sleep":6, "text":"El cielo resplandece a mi alrededor (alrededor)"},
    {"sleep":6, "text":"Al volar, destellos brillan en las nubes sin fin"},
    {"sleep":6, "text":"Con libertad puedes cruzar hoy el cielo azul (el cielo azul)"},
    {"sleep":6, "text":"La verdad huye a un golpe de pronto en ti"},
    {"sleep":0, "text":""},
    {"sleep":5, "text":"Como si un volcán hiciera una erupción"},
    {"sleep":4, "text":"Derrite un gran glaciar"},
    {"sleep":6, "text":"Podrás ver de cerca un gran dragón"},
    {"sleep":0, "text":""},
    {"sleep":4, "text":"Cha-la head-cha-la"},
    {"sleep":3, "text":"No importa lo que suceda"},
    {"sleep":3, "text":"Siempre el ánimo mantendré"},
    {"sleep":0, "text":""},
    {"sleep":4, "text":"Cha-la head-cha-la"},
    {"sleep":3, "text":"Vibrante mi corazón siente emoción"},
    {"sleep":3, "text":"Haré una Genkidama"},
    {"sleep":0, "text":""},
    {"sleep":3, "text":"Cha-la head-cha-la"},
    {"sleep":3, "text":"No importa lo que suceda"},
    {"sleep":3, "text":"Siempre el ánimo mantendré"},
    {"sleep":0, "text":""},
    {"sleep":4, "text":"Cha-la head-cha-la"},
    {"sleep":3, "text":"Vibrante mi corazón siente emoción"},
    {"sleep":3, "text":"Haré una Genkidama"},
    {"sleep":0, "text":""},
    {"sleep":4, "text":"Cha-la head-cha-la"},
    {"sleep":3, "text":"No importa lo que suceda"},
    {"sleep":6, "text":"Sonreiré el día de ho-ho-ho-ho-hoy"},
    {"sleep":0, "text":""}
]

async def main():
    await asyncio.gather(
        asyncio.to_thread(reproducir_musica),
        imprimir_letra(letra_cancion)
    )

if __name__ == "__main__":
    asyncio.run(main())
