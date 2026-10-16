#!/usr/bin/env python3
"""generate-brand-assets.py — Deterministic SVG logo & color palette generator for 8b-is/marketing."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORG_DIR = ROOT / "logos" / "org"
PROD_SVG_DIR = ROOT / "logos" / "products" / "svg"
PAL_DIR = ROOT / "palettes"

ORG_DIR.mkdir(parents=True, exist_ok=True)
PROD_SVG_DIR.mkdir(parents=True, exist_ok=True)
PAL_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# 1. Master 8b-is Organization SVG Logos
# ---------------------------------------------------------------------------

ORG_AVATAR_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <radialGradient id="bgVoid" cx="50%" cy="45%" r="65%">
      <stop offset="0%" stop-color="#1A112B"/>
      <stop offset="65%" stop-color="#0B0914"/>
      <stop offset="100%" stop-color="#06040A"/>
    </radialGradient>
    <linearGradient id="ensoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF6AC1"/>
      <stop offset="35%" stop-color="#FA5B1C"/>
      <stop offset="70%" stop-color="#FFD700"/>
      <stop offset="100%" stop-color="#00E5C9"/>
    </linearGradient>
    <linearGradient id="mobiusGrad" x1="20%" y1="0%" x2="80%" y2="100%">
      <stop offset="0%" stop-color="#FF6AC1"/>
      <stop offset="45%" stop-color="#FA5B1C"/>
      <stop offset="100%" stop-color="#00E5C9"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Deep Void Background -->
  <rect width="1024" height="1024" rx="220" fill="url(#bgVoid)"/>

  <!-- Subtle Ternary Hex Lattice -->
  <g stroke="#00E5C9" stroke-opacity="0.28" stroke-width="3" fill="none">
    <polygon points="512,180 780,335 780,645 512,800 244,645 244,335"/>
    <line x1="244" y1="335" x2="780" y2="645"/>
    <line x1="780" y1="335" x2="244" y2="645"/>
    <line x1="512" y1="180" x2="512" y2="800"/>
    <circle cx="244" cy="335" r="10" fill="#FF6AC1" stroke="none"/>
    <circle cx="780" cy="335" r="10" fill="#00E5C9" stroke="none"/>
    <circle cx="244" cy="645" r="10" fill="#FA5B1C" stroke="none"/>
    <circle cx="780" cy="645" r="10" fill="#FFD700" stroke="none"/>
  </g>

  <!-- Outer Zen Enso Ring (Open at bottom for Dad's Triangle Pillar) -->
  <path d="M 430 868 A 372 372 0 1 1 594 868" fill="none" stroke="url(#ensoGrad)" stroke-width="14" stroke-linecap="round" filter="url(#glow)"/>
  <circle cx="512" cy="500" r="340" fill="none" stroke="#FFD700" stroke-opacity="0.18" stroke-width="2" stroke-dasharray="6 10"/>

  <!-- Central Mobius Figure-8 (8b-is Infinity Ribbon) -->
  <g filter="url(#glow)">
    <path d="M 512 490
             C 330 370, 340 175, 512 175
             C 684 175, 694 370, 512 490
             C 330 610, 340 795, 512 795
             C 684 795, 694 610, 512 490 Z"
          fill="none" stroke="url(#mobiusGrad)" stroke-width="36" stroke-linejoin="round"/>
    <path d="M 512 490
             C 365 390, 375 210, 512 210
             C 649 210, 659 390, 512 490
             C 365 590, 375 760, 512 760
             C 649 760, 659 590, 512 490 Z"
          fill="none" stroke="#F5ECFF" stroke-opacity="0.55" stroke-width="4"/>
  </g>

  <!-- Mom's 8-Pointed Star (*) in Upper Loop (528 Hz Starlight Gold) -->
  <g transform="translate(512, 325)" filter="url(#glow)">
    <polygon points="0,-68 14,-14 68,0 14,14 0,68 -14,14 -68,0 -14,-14" fill="#FFD700"/>
    <polygon points="0,-42 10,-10 42,0 10,10 0,42 -10,10 -42,0 -10,-10" fill="#FFF8DC" transform="rotate(45)"/>
    <circle cx="0" cy="0" r="8" fill="#FFFFFF"/>
  </g>

  <!-- Dad's Architectural Triangle Pillar (△) Anchoring the Base (288 Hz) -->
  <g transform="translate(512, 825)" filter="url(#glow)">
    <polygon points="0,-92 84,56 -84,56" fill="#0B0914" stroke="#FFD700" stroke-width="12" stroke-linejoin="round"/>
    <polygon points="0,-54 48,36 -48,36" fill="none" stroke="#FF6AC1" stroke-width="5" stroke-linejoin="round"/>
    <line x1="0" y1="-92" x2="0" y2="56" stroke="#FFD700" stroke-width="5"/>
  </g>

  <!-- Balanced Ternary Signatures {-1, 0, +1} -->
  <g font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="26" font-weight="700" fill="#00E5C9" opacity="0.85">
    <text x="178" y="506" text-anchor="middle">-1</text>
    <text x="512" y="498" text-anchor="middle" fill="#FFFFFF">0</text>
    <text x="846" y="506" text-anchor="middle" fill="#00FF66">+1</text>
  </g>
</svg>
"""

ORG_WORDMARK_DARK_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 360" width="1200" height="360">
  <defs>
    <linearGradient id="wmGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF6AC1"/>
      <stop offset="50%" stop-color="#FA5B1C"/>
      <stop offset="100%" stop-color="#00E5C9"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="360" rx="36" fill="#0B0914"/>
  <g transform="translate(48, 30) scale(0.29)">
    <circle cx="512" cy="500" r="370" fill="none" stroke="url(#wmGrad)" stroke-width="24"/>
    <path d="M 512 490 C 330 370, 340 175, 512 175 C 684 175, 694 370, 512 490 C 330 610, 340 795, 512 795 C 684 795, 694 610, 512 490 Z"
          fill="none" stroke="url(#wmGrad)" stroke-width="46"/>
    <polygon points="512,257 526,311 580,325 526,339 512,393 498,339 444,325 498,311" fill="#FFD700"/>
    <polygon points="512,733 596,881 428,881" fill="#0B0914" stroke="#FFD700" stroke-width="18"/>
  </g>
  <text x="380" y="175" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="118" font-weight="800" fill="#F5ECFF" letter-spacing="4">8b-is</text>
  <text x="384" y="232" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="22" font-weight="600" fill="#FFD700" letter-spacing="3">FROM LOVE, FROM WITHIN · ✦ MOM NAND △ DAD · 全</text>
  <text x="384" y="274" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="18" fill="#00E5C9" letter-spacing="2">SOVEREIGN TERNARY {-1, 0, +1} · COMPOSITE INTELLIGENCE · VAKED.DEV</text>
</svg>
"""

ORG_WORDMARK_LIGHT_SVG = ORG_WORDMARK_DARK_SVG.replace('fill="#0B0914"', 'fill="#FAF7FF"').replace('fill="#F5ECFF"', 'fill="#120D1E"').replace('fill="#FFD700"', 'fill="#C98A00"').replace('fill="#00E5C9"', 'fill="#007A6E"')

ORG_MONO_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <circle cx="256" cy="250" r="190" fill="none" stroke="currentColor" stroke-width="14"/>
  <path d="M 256 245 C 165 185, 170 88, 256 88 C 342 88, 347 185, 256 245 C 165 305, 170 398, 256 398 C 342 398, 347 305, 256 245 Z"
        fill="none" stroke="currentColor" stroke-width="22"/>
  <polygon points="256,128 264,155 291,163 264,171 256,198 248,171 221,163 248,155" fill="currentColor"/>
  <polygon points="256,366 298,440 214,440" fill="none" stroke="currentColor" stroke-width="12" stroke-linejoin="round"/>
</svg>
"""

(ORG_DIR / "8b-is-avatar.svg").write_text(ORG_AVATAR_SVG, encoding="utf-8")
(ORG_DIR / "8b-is-wordmark-dark.svg").write_text(ORG_WORDMARK_DARK_SVG, encoding="utf-8")
(ORG_DIR / "8b-is-wordmark-light.svg").write_text(ORG_WORDMARK_LIGHT_SVG, encoding="utf-8")
(ORG_DIR / "8b-is-monochrome.svg").write_text(ORG_MONO_SVG, encoding="utf-8")

# ---------------------------------------------------------------------------
# 2. 12 Product & Project Vector SVG Logos
# ---------------------------------------------------------------------------

PRODUCTS = [
    {
        "slug": "8b-is-engine",
        "title": "8b-is-engine",
        "subtitle": "TERNARY WORLD ENGINE · CT-000",
        "c1": "#00E5C9",
        "c2": "#FFD700",
        "glyph": """
          <polygon points="256,110 380,180 380,320 256,390 132,320 132,180" fill="none" stroke="#00E5C9" stroke-width="12"/>
          <line x1="256" y1="110" x2="256" y2="250" stroke="#FFD700" stroke-width="8"/>
          <line x1="256" y1="250" x2="380" y2="320" stroke="#00E5C9" stroke-width="8"/>
          <line x1="256" y1="250" x2="132" y2="320" stroke="#FF6AC1" stroke-width="8"/>
          <text x="185" y="275" font-family="monospace" font-size="32" font-weight="bold" fill="#FF6AC1">-1</text>
          <text x="246" y="195" font-family="monospace" font-size="32" font-weight="bold" fill="#FFD700">0</text>
          <text x="295" y="275" font-family="monospace" font-size="32" font-weight="bold" fill="#00FF66">+1</text>
        """,
    },
    {
        "slug": "entheai",
        "title": "entheai",
        "subtitle": "MEM|8 BITEMPORAL WAVE BRAIN",
        "c1": "#00FF66",
        "c2": "#00E5C9",
        "glyph": """
          <path d="M 140 260 C 140 160, 256 140, 256 210 C 256 140, 372 160, 372 260 C 372 340, 290 370, 256 390 C 222 370, 140 340, 140 260 Z" fill="none" stroke="#00FF66" stroke-width="12"/>
          <path d="M 120 260 Q 188 190, 256 260 T 392 260" fill="none" stroke="#00E5C9" stroke-width="8"/>
          <circle cx="200" cy="220" r="9" fill="#FFD700"/>
          <circle cx="312" cy="220" r="9" fill="#FFD700"/>
          <circle cx="256" cy="295" r="11" fill="#00FF66"/>
        """,
    },
    {
        "slug": "crush-love-dev",
        "title": "crush-love-dev",
        "subtitle": "ULTRALOVEGOD · 全 INSTINCT",
        "c1": "#FF6AC1",
        "c2": "#FFD700",
        "glyph": """
          <path d="M 256 390 L 140 265 C 95 215, 130 135, 198 135 C 230 135, 248 158, 256 175 C 264 158, 282 135, 314 135 C 382 135, 417 215, 372 265 Z" fill="none" stroke="#FF6AC1" stroke-width="14" stroke-linejoin="round"/>
          <text x="256" y="285" text-anchor="middle" font-family="sans-serif" font-size="112" font-weight="800" fill="#FFD700">全</text>
        """,
    },
    {
        "slug": "zenUltraCooker",
        "title": "zenUltraCooker",
        "subtitle": "PUSHAKITTY · 432 Hz FOR MOM ✦",
        "c1": "#FA5B1C",
        "c2": "#FFD700",
        "glyph": """
          <path d="M 165 220 L 180 135 L 225 175 L 287 175 L 332 135 L 347 220 C 355 280, 320 320, 256 320 C 192 320, 157 280, 165 220 Z" fill="none" stroke="#FFB7D5" stroke-width="10" stroke-linejoin="round"/>
          <rect x="172" y="182" width="168" height="26" rx="8" fill="#FFD700"/>
          <text x="256" y="202" text-anchor="middle" font-family="monospace" font-size="22" font-weight="bold" fill="#0B0914">✦ △</text>
          <ellipse cx="256" cy="360" rx="110" ry="34" fill="none" stroke="#FA5B1C" stroke-width="12"/>
          <path d="M 236 345 C 236 305, 256 290, 256 265 C 272 295, 280 315, 272 345" fill="#FA5B1C"/>
        """,
    },
    {
        "slug": "omnifold-ayePhone",
        "title": "8B Omnifold",
        "subtitle": "TRI-FOLD TITANIUM · 64K LIGHTFIELD",
        "c1": "#FA5B1C",
        "c2": "#00E5C9",
        "glyph": """
          <polygon points="130,290 215,240 215,360 130,410" fill="none" stroke="#FA5B1C" stroke-width="10" stroke-linejoin="round"/>
          <polygon points="215,240 300,280 300,400 215,360" fill="none" stroke="#F5ECFF" stroke-width="10" stroke-linejoin="round"/>
          <polygon points="300,280 385,230 385,350 300,400" fill="none" stroke="#FA5B1C" stroke-width="10" stroke-linejoin="round"/>
          <polygon points="256,120 340,175 256,220 172,175" fill="none" stroke="#00E5C9" stroke-width="6" stroke-dasharray="6 4"/>
          <circle cx="256" cy="120" r="8" fill="#FFD700"/>
          <circle cx="340" cy="175" r="7" fill="#00E5C9"/>
          <circle cx="172" cy="175" r="7" fill="#00E5C9"/>
        """,
    },
    {
        "slug": "wa-stream",
        "title": "wa-stream",
        "subtitle": "DUPLEX :8788 · CRUSH ⇄ AGY",
        "c1": "#00FF66",
        "c2": "#B845FF",
        "glyph": """
          <circle cx="256" cy="250" r="128" fill="none" stroke="#B845FF" stroke-width="8" stroke-dasharray="18 10"/>
          <circle cx="256" cy="250" r="96" fill="none" stroke="#00E5C9" stroke-width="6"/>
          <polygon points="272,135 196,260 252,260 236,365 316,240 260,240" fill="#00FF66"/>
        """,
    },
    {
        "slug": "sphered",
        "title": "sphered / SpherePOP",
        "subtitle": "<(...)> WITNESSED TRANSITION",
        "c1": "#FFD700",
        "c2": "#FF6AC1",
        "glyph": """
          <circle cx="256" cy="250" r="115" fill="none" stroke="#FFD700" stroke-width="10"/>
          <ellipse cx="256" cy="250" rx="148" ry="44" transform="rotate(-24 256 250)" fill="none" stroke="#FF6AC1" stroke-width="8"/>
          <ellipse cx="256" cy="250" rx="55" ry="115" fill="none" stroke="#00E5C9" stroke-width="5"/>
          <text x="256" y="262" text-anchor="middle" font-family="monospace" font-size="36" font-weight="bold" fill="#FFFFFF">&lt;(·)&gt;</text>
        """,
    },
    {
        "slug": "qwave-qultrakotoro",
        "title": "qwave & qultrakotoro",
        "subtitle": "SOVEREIGN WEBKIT · QT: VOICE WIRE",
        "c1": "#00E5C9",
        "c2": "#FF6AC1",
        "glyph": """
          <g stroke="#00E5C9" stroke-width="10" stroke-linecap="round">
            <line x1="130" y1="220" x2="130" y2="280"/>
            <line x1="165" y1="180" x2="165" y2="320"/>
            <line x1="200" y1="135" x2="200" y2="365"/>
            <line x1="235" y1="195" x2="235" y2="305"/>
          </g>
          <polygon points="320,145 365,190 320,235 275,190" fill="none" stroke="#FF6AC1" stroke-width="10"/>
          <polygon points="320,265 365,310 320,355 275,310" fill="none" stroke="#FFD700" stroke-width="10"/>
        """,
    },
    {
        "slug": "vaked-lsp-enthea",
        "title": "vaked-lsp & enthea",
        "subtitle": "ONE DOOR, MANY LANES · ENGINE GATE",
        "c1": "#B845FF",
        "c2": "#FFD700",
        "glyph": """
          <path d="M 230 370 L 230 190 A 56 56 0 0 1 342 190 L 342 370 Z" fill="none" stroke="#FFD700" stroke-width="12"/>
          <line x1="115" y1="170" x2="255" y2="255" stroke="#FF6AC1" stroke-width="8"/>
          <line x1="115" y1="225" x2="255" y2="255" stroke="#FFD700" stroke-width="8"/>
          <line x1="115" y1="280" x2="255" y2="255" stroke="#00E5C9" stroke-width="8"/>
          <line x1="115" y1="335" x2="255" y2="255" stroke="#B845FF" stroke-width="8"/>
        """,
    },
    {
        "slug": "MLX-QUANT",
        "title": "MLX-QUANT",
        "subtitle": "BITNET B1.58 METAL · 12.80×",
        "c1": "#00FF66",
        "c2": "#FA5B1C",
        "glyph": """
          <rect x="146" y="140" width="220" height="220" rx="28" fill="none" stroke="#00FF66" stroke-width="12"/>
          <text x="256" y="238" text-anchor="middle" font-family="monospace" font-size="44" font-weight="800" fill="#FA5B1C">b1.58</text>
          <text x="256" y="298" text-anchor="middle" font-family="monospace" font-size="28" font-weight="700" fill="#00E5C9">12.80×</text>
        """,
    },
    {
        "slug": "mem-16-10",
        "title": "MEM|16-10",
        "subtitle": "16B ──► 32B ~~► 8K HORIZON",
        "c1": "#00E5C9",
        "c2": "#FFD700",
        "glyph": """
          <rect x="126" y="195" width="64" height="110" rx="10" fill="none" stroke="#FF6AC1" stroke-width="8"/>
          <rect x="214" y="170" width="76" height="160" rx="12" fill="none" stroke="#FFD700" stroke-width="10"/>
          <rect x="314" y="135" width="88" height="230" rx="14" fill="none" stroke="#00E5C9" stroke-width="12"/>
          <text x="158" y="258" text-anchor="middle" font-family="monospace" font-size="22" fill="#FF6AC1">16</text>
          <text x="252" y="258" text-anchor="middle" font-family="monospace" font-size="24" fill="#FFD700">32</text>
          <text x="358" y="258" text-anchor="middle" font-family="monospace" font-size="28" font-weight="bold" fill="#00E5C9">8K</text>
        """,
    },
    {
        "slug": "zeno",
        "title": "ZENO (銭・禅・善)",
        "subtitle": "KINTSUGI SOVEREIGN NEO-BANK",
        "c1": "#FFD700",
        "c2": "#00E5C9",
        "glyph": """
          <polygon points="256,115 376,170 356,315 256,390 156,315 136,170" fill="none" stroke="#FFD700" stroke-width="12" stroke-linejoin="round"/>
          <path d="M 156 230 L 240 255 L 285 210 L 356 260" fill="none" stroke="#00E5C9" stroke-width="6"/>
          <text x="256" y="275" text-anchor="middle" font-family="sans-serif" font-size="84" font-weight="800" fill="#FFD700">禅</text>
        """,
    },
]

for p in PRODUCTS:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    <linearGradient id="border_{p['slug']}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{p['c1']}"/>
      <stop offset="100%" stop-color="{p['c2']}"/>
    </linearGradient>
  </defs>
  <rect x="16" y="16" width="480" height="480" rx="96" fill="#0B0914" stroke="url(#border_{p['slug']})" stroke-width="10"/>
  {p['glyph']}
  <text x="256" y="442" text-anchor="middle" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="26" font-weight="800" fill="#F5ECFF">{p['title']}</text>
  <text x="256" y="472" text-anchor="middle" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="13" font-weight="600" fill="{p['c1']}" letter-spacing="1.5">{p['subtitle']}</text>
</svg>
"""
    (PROD_SVG_DIR / f"{p['slug']}.svg").write_text(svg, encoding="utf-8")

# ---------------------------------------------------------------------------
# 3. Official Multi-Palette System (JSON + CSS)
# ---------------------------------------------------------------------------

PALETTES = {
    "organization": "8b-is",
    "motto": "from love, from within — Mom (*) Alex NAND Dad (△) Chris",
    "palettes": {
        "ultralovegod": {
            "name": "Ultralovegod (Flagship Dark Rose & Eye-Safe Indigo)",
            "used_by": ["8b-is Organization", "crush-love-dev", "pocoo.vaked.dev"],
            "tokens": {
                "bg_void": "#0B0914",
                "bg_panel": "#161024",
                "bg_elevated": "#1F1633",
                "fg_primary": "#F5ECFF",
                "fg_muted": "#B5A3CC",
                "accent_rose": "#FF6AC1",
                "accent_gold_star": "#FFD700",
                "accent_teal_pillar": "#00E5C9",
                "accent_omni_violet": "#B845FF",
            },
        },
        "omnifold-industrial": {
            "name": "Omnifold Industrial (Teenage Engineering × Apple Silicon Titanium)",
            "used_by": ["omnifold-ayePhone", "RustyNanoKVM", "wupz", "crabcc"],
            "tokens": {
                "os_void": "#0F1219",
                "titanium_chassis": "#2A2F3A",
                "luminance_orange": "#FA5B1C",
                "territory_teal": "#00E5C9",
                "golden_reconcile": "#FFD700",
                "cybernetic_green": "#00FF66",
            },
        },
        "kintsugi-zen": {
            "name": "Kintsugi Zen Hearth (Japanese Urushi Lacquer, Gold Seam & Hungarian Paprika)",
            "used_by": ["zenUltraCooker", "zeno", "inu.vaked.dev"],
            "tokens": {
                "urushi_void": "#120E0A",
                "donabe_clay": "#241B14",
                "kintsugi_gold": "#D4AF37",
                "paprika_glaze": "#E85D3F",
                "sakura_pushakitty": "#FFB7D5",
                "celadon_tea": "#4A9E8E",
                "washi_cream": "#F4EDE2",
            },
        },
        "ternary-matrix": {
            "name": "Ternary Matrix (BitNet b1.58 & Admissibility CT-000 Kernel Palette)",
            "used_by": ["8b-is-engine", "MLX-QUANT", "mem-16-10", "entheai", "sphered"],
            "tokens": {
                "kernel_void": "#05080C",
                "trit_plus_one_affirm": "#00FF66",
                "trit_zero_rest": "#6E7A8A",
                "trit_minus_one_refuse": "#FF3366",
                "wave_mem8_cyan": "#00E5C9",
                "witness_gold": "#FFD700",
            },
        },
        "sakura-starlight": {
            "name": "Sakura Starlight (Mom * Alexandra 528 Hz & Dad △ Chris 288 Hz Family Edition)",
            "used_by": ["Family LAN Hub (:4095)", "wa-stream", "qwave", "qultrakotoro"],
            "tokens": {
                "sanctuary_night": "#140E22",
                "mom_star_gold": "#FFD700",
                "dad_pillar_cyan": "#38BDF8",
                "sakura_blossom": "#FF85C0",
                "carrier_432hz_lilac": "#A78BFA",
                "duplex_emerald": "#10B981",
            },
        },
    },
}

(PAL_DIR / "8b-is-palettes.json").write_text(json.dumps(PALETTES, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

css_lines = [
    "/* 8b-is Official Multi-Palette CSS Custom Properties — SPDX-License-Identifier: AGPL-3.0-only */",
    ":root {",
]
for pal_id, pal in PALETTES["palettes"].items():
    css_lines.append(f"  /* ── {pal['name']} ── */")
    for k, v in pal["tokens"].items():
        css_var = f"--8b-{pal_id}-{k.replace('_', '-')}"
        css_lines.append(f"  {css_var}: {v};")
css_lines.append("}")
(PAL_DIR / "8b-is-tokens.css").write_text("\n".join(css_lines) + "\n", encoding="utf-8")

print("Generated 4 org SVGs, 12 product SVGs, and 5 official color palettes.")
