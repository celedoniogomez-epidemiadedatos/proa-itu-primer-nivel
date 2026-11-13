#!/usr/bin/env python3
"""Calcula los indicadores PROA-ITU a partir de un CSV con el formato de
datos_simulados.csv y genera el tablero de ejemplo (PNG).

Uso:
    python calcular_indicadores.py datos_simulados.csv

Salidas:
    indicadores_resumen.csv   indicadores por mes (todas las unidades)
    tablero_ejemplo.png       gráfica de ejemplo (requiere matplotlib)

Los datos de ejemplo son FICTICIOS. Autor: Dr. Celedonio Gómez Muñoz.
Licencia: CC BY 4.0.
"""
import csv
import sys
from collections import defaultdict


def pct(num, den):
    return round(100 * num / den, 1) if den else None


def main(ruta):
    meses = defaultdict(lambda: defaultdict(int))
    with open(ruta, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            m = int(r["mes"])
            for k, v in r.items():
                if k not in ("mes", "unidad"):
                    meses[m][k] += int(v)

    salida = []
    for m in sorted(meses):
        d = meses[m]
        salida.append({
            "mes": m,
            "I1_esquema_primera_linea_pct": pct(d["esquema_primera_linea"], d["consultas_cistitis_nc"]),
            "I2_duracion_adecuada_pct": pct(d["duracion_adecuada"], d["consultas_cistitis_nc"]),
            "I3_fluoroquinolona_pct": pct(d["fluoroquinolona"], d["consultas_cistitis_nc"]),
            "I4_urocultivo_cuando_indicado_pct": pct(d["urocultivo_realizado"], d["urocultivo_indicado"]),
            "I5_reconsulta_14d_pct": pct(d["reconsulta_14d"], d["consultas_cistitis_nc"]),
            "I6_bacteriuria_asintomatica_tratada_pct": pct(
                d["bacteriuria_asintomatica_tratada"], d["bacteriuria_asintomatica_detectada"]),
        })

    with open("indicadores_resumen.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(salida[0].keys()))
        w.writeheader()
        w.writerows(salida)
    print("Escrito indicadores_resumen.csv")

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib no está instalado: se omite la gráfica.")
        return

    azul, gris, texto = "#2a78d6", "#8a8984", "#0b0b0b"
    x = [s["mes"] for s in salida]
    paneles = [
        ("I1_esquema_primera_linea_pct", "Esquema de primera línea (%)", 80, "Meta de ejemplo: 80 %"),
        ("I3_fluoroquinolona_pct", "Uso de fluoroquinolonas (%)", 10, "Meta de ejemplo: ≤ 10 %"),
    ]
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), dpi=150, facecolor="#fcfcfb")
    for ax, (col, titulo, meta, etiqueta) in zip(axes, paneles):
        y = [s[col] for s in salida]
        ax.set_facecolor("#fcfcfb")
        ax.plot(x, y, color=azul, linewidth=2, marker="o", markersize=5)
        ax.axhline(meta, color=gris, linewidth=1, linestyle="--")
        ax.text(1, meta + 1.5, etiqueta, color="#52514e", fontsize=8, ha="left", va="bottom")
        ax.axvline(5.5, color="#d9d8d3", linewidth=1)
        ax.text(5.6, 97, " Inicio de PROA (simulado)", color="#52514e",
                fontsize=8, va="top")
        ax.set_title(titulo, loc="left", fontsize=11, color=texto)
        ax.set_xlabel("Mes (año simulado)", fontsize=9, color="#52514e")
        ax.set_xticks(range(1, 13))
        ax.set_ylim(0, 100)
        ax.grid(axis="y", color="#e8e7e2", linewidth=0.8)
        for lado in ("top", "right", "left"):
            ax.spines[lado].set_visible(False)
        ax.tick_params(colors="#52514e", labelsize=8, length=0)
    fig.suptitle("PROA-ITU · Tablero de ejemplo con datos FICTICIOS (3 unidades agregadas)",
                 x=0.01, ha="left", fontsize=10, color="#52514e")
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig("tablero_ejemplo.png")
    print("Escrito tablero_ejemplo.png")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "datos_simulados.csv")
