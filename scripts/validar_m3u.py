#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
files = sorted((root / "playlists").glob("*.m3u"))
errors = []
total = 0
for path in files:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if not lines or not lines[0].strip().startswith("#EXTM3U"):
        errors.append(f"{path.name}: cabeçalho #EXTM3U ausente")
        continue
    extinf = 0
    missing_url = 0
    for i, line in enumerate(lines):
        if line.startswith("#EXTINF:"):
            extinf += 1
            j = i + 1
            while j < len(lines) and (not lines[j].strip() or lines[j].startswith("#")):
                j += 1
            if j >= len(lines) or not lines[j].strip().lower().startswith(("http://", "https://")):
                missing_url += 1
    total += extinf
    if missing_url:
        errors.append(f"{path.name}: {missing_url} entrada(s) sem URL após metadados")
    print(f"{path.name}: {extinf} entradas")
print(f"\n{len(files)} arquivos; {total} entradas")
if errors:
    print("ERROS:")
    print("\n".join(errors))
    sys.exit(1)
print("Estrutura básica válida. Disponibilidade dos canais não foi testada.")
