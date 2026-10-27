"""Extrai o WAV (base64) de um resultado salvo do generate_speech e grava em disco.

Uso: python -I save_wav.py <arquivo_do_resultado.txt> <saida.wav>
"""
import base64
import json
import os
import sys
import wave

BS = chr(92)


def long_path(p):
    p = os.path.abspath(p)
    if p.startswith(BS * 2 + "?" + BS):
        return p
    return BS * 2 + "?" + BS + p


def main(src, out):
    with open(long_path(src), encoding="utf-8") as f:
        outer = json.load(f)
    res = outer["result"]
    res = json.loads(res) if isinstance(res, str) else res
    data = base64.b64decode(res["wav_base64"])

    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    with open(out, "wb") as f:
        f.write(data)

    with wave.open(out, "rb") as w:
        dur = w.getnframes() / w.getframerate()
        print(
            os.path.basename(out),
            "id=%s" % res["audio_id"],
            "%.2fs" % dur,
            "%dHz" % w.getframerate(),
            "%dch" % w.getnchannels(),
            "gerado em %.1fs" % res["generation_time_s"],
        )


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
