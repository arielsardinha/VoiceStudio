"""Monta a trilha de referencia de uma cena: so voz e pausas, sem nenhum efeito.

Uso: python -I montar_cena.py <pasta> <saida.wav> [v4|bloco1]
Ex.:  python -I montar_cena.py cena01_v4 cena01_v4_referencia.wav v4

Os takes originais nao sao alterados. A trilha so concatena os WAVs com o silencio indicado no roteiro
(onde o sound design coloca bipes, passos, fogo), sem filtro, sem normalizacao e sem cortar pausas.
Takes com outra taxa de amostragem (a voz do sistema, 44.1 kHz) sao reamostrados so na trilha de referencia.
"""
import os
import sys
import wave

import numpy as np

SR = 24000

# (arquivo, pausa depois em segundos)
CENAS = {
    # roteiro_dra_lis_v4.md
    "v4": [
        ("c01_t01", 0.4), ("c01_t02", 0.3), ("c01_sis", 0.2), ("c01_t03", 0.3), ("c01_t04", 1.0),
        ("c01_t05", 0.4), ("c01_t06", 0.4), ("c01_t07", 0.5), ("c01_t08", 1.0),
        ("c01_t09", 0.5), ("c01_t10", 0.5), ("c01_t11", 0.6), ("c01_t12", 0.0),
    ],
    # roteiro_dra_lis_v2.md, bloco 1
    "bloco1": [
        ("c01_t01", 2.5), ("c01_t02", 1.5), ("c01_t03", 3.0), ("c01_t04", 1.2),
        ("c01_t05", 1.5), ("c01_t06", 0.8), ("c01_t07", 0.0),
    ],
}


def read_wav(path):
    with wave.open(path, "rb") as w:
        assert w.getnchannels() == 1 and w.getsampwidth() == 2, "esperava mono 16 bits"
        sr = w.getframerate()
        x = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2")
    if sr != SR:
        n = int(round(len(x) * SR / sr))
        x = np.interp(np.linspace(0, len(x) - 1, n), np.arange(len(x)), x.astype(np.float32))
        x = np.clip(x, -32768, 32767).astype("<i2")
    return x


def main(folder, out, cena="v4"):
    parts = []
    for nome, pausa in CENAS[cena]:
        parts.append(read_wav(os.path.join(folder, nome + ".wav")))
        if pausa:
            parts.append(np.zeros(int(pausa * SR), dtype="<i2"))
    track = np.concatenate(parts)
    with wave.open(out, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(track.tobytes())
    print("%s: %.1fs" % (out, len(track) / SR))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], *(sys.argv[3:4] or ["v4"]))
