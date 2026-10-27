"""Corte seco: encurta silencios longos de um take, sem mexer na voz.

Uso: python -I apertar_pausas.py <entrada.wav> <saida.wav> [pausa_maxima_s] [pausa_final_s]

Silencios internos maiores que a pausa maxima (padrao 0.22 s) passam a durar a pausa final (padrao 0.16 s),
com microfades de 8 ms. As pontas ficam com 0.05 s. E edicao, nao efeito: sem filtro, sem ganho.
"""
import sys
import wave

import numpy as np

LIMIAR_DB = -45.0
FRAME_S = 0.02


def ler(path):
    with wave.open(path, "rb") as w:
        sr, ch, sw = w.getframerate(), w.getnchannels(), w.getsampwidth()
        assert ch == 1 and sw == 2, "esperava mono 16 bits"
        return sr, np.frombuffer(w.readframes(w.getnframes()), dtype="<i2")


def apertar(x, sr, max_gap, keep_gap):
    fr = int(FRAME_S * sr)
    n = len(x) // fr
    rms = np.array([np.sqrt(np.mean((x[i * fr:(i + 1) * fr] / 32768.0) ** 2)) + 1e-9 for i in range(n)])
    quiet = 20 * np.log10(rms) < LIMIAR_DB
    out, i = [], 0
    fade = int(0.008 * sr)
    while i < n:
        j = i
        while j < n and quiet[j] == quiet[i]:
            j += 1
        seg = x[i * fr:j * fr]
        if quiet[i]:
            dur = len(seg) / sr
            first, last = i == 0, j == n
            alvo = 0.05 if (first or last) else (keep_gap if dur > max_gap else dur)
            seg = seg[: int(min(len(seg), alvo * sr))]
        out.append(seg)
        i = j
    out.append(x[n * fr:])
    y = np.concatenate(out).astype(np.float32)
    # microfades nas emendas para nao estalar
    pos = 0
    for seg in out[:-1]:
        pos += len(seg)
        a, b = max(0, pos - fade), min(len(y), pos + fade)
        y[a:b] *= np.linspace(0.6, 1.0, b - a) if b - a > 0 else 1.0
    return np.clip(y, -32768, 32767).astype("<i2")


def main(src, dst, max_gap=0.22, keep_gap=0.16):
    sr, x = ler(src)
    y = apertar(x, sr, max_gap, keep_gap)
    with wave.open(dst, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(y.tobytes())
    print("%s: %.1fs -> %.1fs" % (dst, len(x) / sr, len(y) / sr))


if __name__ == "__main__":
    a = sys.argv
    main(a[1], a[2], *(float(v) for v in a[3:5]))
