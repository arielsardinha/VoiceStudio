"""Junta os trechos da Dra. Lis com pausas e gera uma versao limpa e uma com efeito de radio.

Uso: python -I assemble.py <pasta_audio> <prefixo>
"""
import os
import sys
import wave

import numpy as np

SR = 24000

# (arquivo, pausa depois do trecho em segundos)
BEATS = [
    ("01_contato", 0.9),
    ("02_a_seiva", 0.7),
    ("03_a_virada", 0.6),
    ("04_o_frasco", 0.5),
    ("05_por_que_voce", 0.9),
    ("06_guardioes", 0.0),
]


def read_wav(path):
    with wave.open(path, "rb") as w:
        assert w.getframerate() == SR and w.getnchannels() == 1 and w.getsampwidth() == 2
        raw = w.readframes(w.getnframes())
    return np.frombuffer(raw, dtype="<i2").astype(np.float32) / 32768.0


def write_wav(path, x):
    x = np.clip(x, -1.0, 1.0)
    pcm = (x * 32767.0).astype("<i2")
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())


def bandpass(x, lo, hi):
    spec = np.fft.rfft(x)
    freqs = np.fft.rfftfreq(len(x), 1.0 / SR)
    # bordas suaves para nao soar "metalico" demais
    gain = np.clip((freqs - lo) / 150.0, 0, 1) * np.clip((hi - freqs) / 600.0, 0, 1)
    return np.fft.irfft(spec * gain, n=len(x)).astype(np.float32)


def normalize(x, peak=0.89):
    m = float(np.max(np.abs(x))) or 1.0
    return x * (peak / m)


def main(folder, prefix):
    rng = np.random.default_rng(7)
    parts = []
    for name, gap in BEATS:
        parts.append(read_wav(os.path.join(folder, "%s_%s.wav" % (prefix, name))))
        if gap:
            parts.append(np.zeros(int(gap * SR), dtype=np.float32))
    voice = np.concatenate(parts)

    lead = int(1.2 * SR)
    tail = int(1.2 * SR)
    clean = np.concatenate([np.zeros(lead, np.float32), voice, np.zeros(tail, np.float32)])
    write_wav(os.path.join(folder, "%s_completo_limpo.wav" % prefix), normalize(clean))

    # --- versao radio ---
    v = np.concatenate([np.zeros(lead, np.float32), voice, np.zeros(tail, np.float32)])
    v = bandpass(v, 320.0, 3300.0)
    v = np.tanh(2.2 * v) / np.tanh(2.2)  # leve saturacao
    v = normalize(v, 0.8)

    n = len(v)
    noise = bandpass(rng.standard_normal(n).astype(np.float32), 250.0, 4500.0)
    noise /= float(np.max(np.abs(noise)))
    env = np.full(n, 0.035, dtype=np.float32)  # chiado de fundo sob a voz
    env[:lead] = 0.16  # estatica antes da conexao
    env[-tail:] = 0.16  # estatica depois do corte
    # a estatica "abaixa" em 0.25s quando a conexao pega
    fade = int(0.25 * SR)
    env[lead - fade:lead] = np.linspace(0.16, 0.035, fade)
    # estalo de squelch no inicio e no fim
    click = int(0.06 * SR)
    env[lead - click:lead - click // 2] = 0.5
    end = n - tail
    env[end:end + click] = 0.5
    radio = v + noise * env
    write_wav(os.path.join(folder, "%s_completo_radio.wav" % prefix), normalize(radio, 0.89))

    print("limpo + radio gerados: %.1fs" % (n / SR))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
