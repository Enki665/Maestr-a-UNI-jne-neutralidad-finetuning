from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import warnings

warnings.filterwarnings("ignore")

BASE_DIR = Path(__file__).resolve().parents[1]

FILE = BASE_DIR / "data" / "training" / "reporte_sije_eleccia_20260423_1625.xlsx"
OUTPUT_DIR = BASE_DIR / "outputs" / "reports"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

HEADER_ROW = 2

if not FILE.exists():
    raise FileNotFoundError(f"No se encontró el archivo: {FILE}")

# ── Carga ─────────────────────────────────────────────────────────────────────
df = pd.read_excel(FILE, header=HEADER_ROW)
df["FECHA_REGISTRO"] = pd.to_datetime(df["FECHA_REGISTRO"])
df["FECHA_RECEPCION"] = pd.to_datetime(df["FECHA_RECEPCION"])
df["MES"] = df["FECHA_REGISTRO"].dt.to_period("M")

# ── 1. Resumen general ─────────────────────────────────────────────────────────
print("=" * 60)
print("RESUMEN GENERAL")
print("=" * 60)
print(f"Filas   : {df.shape[0]:,}")
print(f"Columnas: {df.shape[1]}")
print(f"\nRango de fechas: {df['FECHA_REGISTRO'].min()} → {df['FECHA_REGISTRO'].max()}")
print("\nTipos de dato:")
print(df.dtypes)
print("\nEstadísticas numéricas:")
print(df.describe())

# ── 2. Valores nulos ───────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("VALORES NULOS")
print("=" * 60)
nulls = df.isnull().sum()
nulls_pct = (nulls / len(df) * 100).round(1)
null_df = pd.DataFrame({"nulos": nulls, "%": nulls_pct})
print(null_df[null_df["nulos"] > 0].sort_values("nulos", ascending=False))

# ── 3. Distribuciones categóricas ─────────────────────────────────────────────
CAT_COLS = [
    "TXPROCESOELECTORAL",
    "TXMATERIA",
    "ESTADO_EXPEDIENTE_JEE",
    "PROCESADO_EN_ELECCIA",
    "TIENE_PRONUNCIAMIENTO_DESCARGADO",
    "PRONICIAMIENTO_ELECCIA_EN_SIJE",
]
print("\n" + "=" * 60)
print("DISTRIBUCIONES CATEGÓRICAS")
print("=" * 60)
for col in CAT_COLS:
    print(f"\n{col}:")
    vc = df[col].value_counts(dropna=False)
    pct = (vc / len(df) * 100).round(1)
    print(pd.concat([vc, pct.rename("%")], axis=1).to_string())

# ── 4. Tiempo de procesamiento ─────────────────────────────────────────────────
print("\n" + "=" * 60)
print("TIEMPO DE PROCESAMIENTO (segundos) — solo > 0")
print("=" * 60)
tp = df.loc[df["TIEMPO_PROCESAMIENTO_SEGUNDOS"] > 0, "TIEMPO_PROCESAMIENTO_SEGUNDOS"]
print(tp.describe().round(2))

# ── 5. Top geografías ──────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("TOP 10 DEPARTAMENTOS")
print("=" * 60)
print(df["DEPARTAMENTO_EXPED"].value_counts().head(10))

# ══════════════════════════════════════════════════════════════════════════════
# GRÁFICOS
# ══════════════════════════════════════════════════════════════════════════════
BLUE   = "#378ADD"
GREEN  = "#1D9E75"
AMBER  = "#BA7517"
PURPLE = "#7F77DD"
RED    = "#E24B4A"
GRAY   = "#888780"

plt.style.use("seaborn-v0_8-whitegrid")
fig = plt.figure(figsize=(18, 22))
fig.suptitle("EDA — Reporte SIJE ELECCIA  |  Corte: 23 abr 2026", fontsize=15, fontweight="bold", y=0.98)

# ── Paleta doughnut estados ────────────────────────────────────────────────────
ESTADO_COLORS = [GREEN, GRAY, AMBER, BLUE, "#B4B2A9", PURPLE, "#D85A30", "#D4537E", "#5DCAA5"]

# ── G1: Proceso electoral ──────────────────────────────────────────────────────
ax1 = fig.add_subplot(4, 2, 1)
proc = df["TXPROCESOELECTORAL"].value_counts()
labels_short = ["EG 2026", "ERM 2026", "EMC 2025"]
bars = ax1.barh(labels_short, proc.values, color=[BLUE, GREEN, AMBER])
ax1.set_title("Proceso electoral", fontweight="bold")
ax1.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
for bar, val in zip(bars, proc.values):
    ax1.text(bar.get_width() + 150, bar.get_y() + bar.get_height() / 2,
             f"{val:,}", va="center", fontsize=9)
ax1.set_xlim(0, proc.values.max() * 1.15)

# ── G2: Materia ────────────────────────────────────────────────────────────────
ax2 = fig.add_subplot(4, 2, 2)
mat = df["TXMATERIA"].value_counts()
mat_labels = [t[:25] + "…" if len(t) > 25 else t for t in mat.index]
ax2.barh(mat_labels[::-1], mat.values[::-1], color=PURPLE)
ax2.set_title("Materia del expediente", fontweight="bold")
ax2.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
ax2.tick_params(axis="y", labelsize=7)

# ── G3: Estado JEE (doughnut) ─────────────────────────────────────────────────
ax3 = fig.add_subplot(4, 2, 3)
estado = df["ESTADO_EXPEDIENTE_JEE"].value_counts(dropna=True)
wedges, _, autotexts = ax3.pie(
    estado.values, labels=None, autopct="%1.1f%%",
    colors=ESTADO_COLORS[:len(estado)], startangle=90,
    wedgeprops={"width": 0.55}, pctdistance=0.78
)
for at in autotexts:
    at.set_fontsize(7)
ax3.legend(estado.index, loc="lower center", fontsize=7,
           bbox_to_anchor=(0.5, -0.25), ncol=2)
ax3.set_title("Estado del expediente JEE", fontweight="bold")

# ── G4: Indicadores SI/NO ─────────────────────────────────────────────────────
ax4 = fig.add_subplot(4, 2, 4)
ind_labels = ["Procesado\nen ELECCIA", "Pronunciamiento\ndescargado", "Pronunciamiento\nen SIJE"]
si_vals  = [8059,  3183,  2122]
no_vals  = [17806, 22682, 23743]
x = range(len(ind_labels))
w = 0.35
ax4.bar([i - w/2 for i in x], si_vals, width=w, label="Sí", color=BLUE)
ax4.bar([i + w/2 for i in x], no_vals, width=w, label="No", color=RED)
ax4.set_xticks(list(x))
ax4.set_xticklabels(ind_labels, fontsize=8)
ax4.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{int(v):,}"))
ax4.set_title("Indicadores de procesamiento (Sí / No)", fontweight="bold")
ax4.legend()

# ── G5: Tendencia mensual ─────────────────────────────────────────────────────
ax5 = fig.add_subplot(4, 1, 3)
monthly = df["MES"].value_counts().sort_index()
ax5.fill_between(monthly.index.astype(str), monthly.values, alpha=0.15, color=BLUE)
ax5.plot(monthly.index.astype(str), monthly.values, marker="o", color=BLUE, linewidth=1.8, markersize=4)
ax5.set_title("Tendencia mensual de registro de expedientes", fontweight="bold")
ax5.set_xticklabels(monthly.index.astype(str), rotation=45, ha="right", fontsize=8)
ax5.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{int(v):,}"))
for i, (x_val, y_val) in enumerate(zip(monthly.index.astype(str), monthly.values)):
    if y_val == monthly.values.max():
        ax5.annotate(f"Pico: {y_val:,}", xy=(x_val, y_val),
                     xytext=(0, 10), textcoords="offset points",
                     ha="center", fontsize=8, color=BLUE, fontweight="bold")

# ── G6: Top 10 departamentos ──────────────────────────────────────────────────
ax6 = fig.add_subplot(4, 2, 7)
top_dep = df["DEPARTAMENTO_EXPED"].value_counts().head(10)
colors_dep = [BLUE if d == "LIMA" else GREEN for d in top_dep.index]
ax6.barh(top_dep.index[::-1], top_dep.values[::-1], color=colors_dep[::-1])
ax6.set_title("Top 10 departamentos", fontweight="bold")
ax6.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{int(v):,}"))

# ── G7: Distribución tiempo de procesamiento (> 0) ───────────────────────────
ax7 = fig.add_subplot(4, 2, 8)
tp_pos = df.loc[df["TIEMPO_PROCESAMIENTO_SEGUNDOS"] > 0, "TIEMPO_PROCESAMIENTO_SEGUNDOS"]
ax7.hist(tp_pos, bins=40, color=AMBER, edgecolor="white")
ax7.set_title("Distribución tiempo de procesamiento\n(solo expedientes > 0 s)", fontweight="bold")
ax7.set_xlabel("Segundos")
ax7.set_ylabel("Frecuencia")
ax7.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{int(v):,}"))

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig("eda_sije_eleccia.png", dpi=150, bbox_inches="tight")
plt.show()
print("\nGráfico guardado como 'eda_sije_eleccia.png'")