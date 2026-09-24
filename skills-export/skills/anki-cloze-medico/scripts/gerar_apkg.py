#!/usr/bin/env python3
"""
gerar_apkg.py — Gerador de arquivos .apkg Anki Cloze sem genanki.
Usa apenas bibliotecas padrão: sqlite3, zipfile, json, time, random, hashlib, html, pathlib, re, argparse.
"""

import sqlite3
import zipfile
import json
import time
import random
import hashlib
import html
import re
import argparse
import os
import tempfile
from pathlib import Path


# ─── Helpers ───────────────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    """Remove acentos/espaços para nome de arquivo."""
    replacements = {
        'á':'a','à':'a','ã':'a','â':'a','ä':'a',
        'é':'e','ê':'e','ë':'e',
        'í':'i','î':'i','ï':'i',
        'ó':'o','õ':'o','ô':'o','ö':'o',
        'ú':'u','û':'u','ü':'u',
        'ç':'c','ñ':'n',
        'Á':'A','À':'A','Ã':'A','Â':'A',
        'É':'E','Ê':'E',
        'Í':'I',
        'Ó':'O','Õ':'O','Ô':'O',
        'Ú':'U',
        'Ç':'C',
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    text = re.sub(r'[^a-zA-Z0-9_\-]', '_', text)
    text = re.sub(r'_+', '_', text)
    return text.strip('_')


def new_id() -> int:
    """Gera um ID numérico único baseado em timestamp + random."""
    return int(time.time() * 1000) + random.randint(0, 999)


def note_guid(texto: str) -> str:
    """GUID estável baseado no conteúdo do card."""
    return hashlib.md5(texto.encode('utf-8')).hexdigest()[:10]


def count_cloze_ordinals(texto: str) -> list:
    """Retorna lista de ordinais únicos de cloze encontrados no texto."""
    matches = re.findall(r'\{\{c(\d+)::', texto)
    return sorted(set(int(m) for m in matches))


# ─── Criação do banco collection.anki2 ─────────────────────────────────────────

def criar_collection(db_path: str, cards_data: list, deck_name: str, tags_extras: list = None):
    """
    Cria o banco SQLite no formato interno do Anki 2.1.
    
    cards_data: list of dict com chaves 'texto' e 'extra'
    deck_name:  nome do baralho
    tags_extras: tags adicionais além das padrão
    """
    tags_base = ['cloze', 'prova', 'residencia', 'medicina']
    if tags_extras:
        tags_base.extend(tags_extras)
    tags_str = ' '.join(tags_base)

    model_id = 1645010146843   # ID fixo para modelo Cloze
    deck_id  = int(time.time() * 1000)
    conf_id  = 1

    # ── Modelo (Note Type) Cloze ─────────────────────────────────────────────
    model = {
        str(model_id): {
            "id": model_id,
            "name": "Cloze Médico",
            "type": 1,          # 1 = Cloze
            "mod": int(time.time()),
            "usn": -1,
            "sortf": 0,
            "did": deck_id,
            "tmpls": [
                {
                    "name": "Cloze",
                    "ord": 0,
                    "qfmt": "{{cloze:Texto}}",
                    "afmt": "{{cloze:Texto}}<hr id=answer>{{Extra}}",
                    "did": None,
                    "bqfmt": "",
                    "bafmt": "",
                }
            ],
            "flds": [
                {"name": "Texto", "ord": 0, "sticky": False, "rtl": False,
                 "font": "Arial", "size": 20, "media": []},
                {"name": "Extra", "ord": 1, "sticky": False, "rtl": False,
                 "font": "Arial", "size": 20, "media": []},
            ],
            "css": (
                ".card { font-family: Arial; font-size: 18px; text-align: left; "
                "color: black; background-color: white; padding: 20px; }\n"
                ".cloze { font-weight: bold; color: #2196F3; }\n"
                "hr#answer { border-top: 1px solid #ccc; margin: 16px 0; }\n"
            ),
            "latexPre": "\\documentclass[12pt]{article}\n\\special{papersize=3in,5in}\n"
                        "\\usepackage[utf8]{inputenc}\n\\usepackage{amssymb,amsmath}\n"
                        "\\pagestyle{empty}\n\\setlength{\\parindent}{0in}\n"
                        "\\begin{document}\n",
            "latexPost": "\\end{document}",
            "latexsvg": False,
            "req": [[0, "all", [0]]],
            "tags": [],
            "vers": [],
        }
    }

    # ── Deck ─────────────────────────────────────────────────────────────────
    deck = {
        str(deck_id): {
            "id": deck_id,
            "name": deck_name,
            "desc": "Gerado automaticamente — Cloze Prova",
            "mod": int(time.time()),
            "usn": -1,
            "lrnToday": [0, 0],
            "revToday": [0, 0],
            "newToday": [0, 0],
            "timeToday": [0, 0],
            "collapsed": False,
            "browserCollapsed": False,
            "dyn": 0,
            "conf": conf_id,
            "extendNew": 0,
            "extendRev": 0,
        },
        "1": {   # deck padrão obrigatório
            "id": 1,
            "name": "Default",
            "conf": 1,
            "desc": "",
            "dyn": 0,
            "mod": int(time.time()),
            "usn": -1,
            "lrnToday": [0, 0],
            "revToday": [0, 0],
            "newToday": [0, 0],
            "timeToday": [0, 0],
            "collapsed": False,
            "browserCollapsed": False,
            "extendNew": 0,
            "extendRev": 0,
        }
    }

    # ── Deck Config ───────────────────────────────────────────────────────────
    dconf = {
        "1": {
            "id": 1,
            "name": "Default",
            "replayq": True,
            "lapse": {"delays": [10], "leechAction": 0, "leechFails": 8,
                      "minInt": 1, "mult": 0},
            "rev": {"bury": False, "ease4": 1.3, "fuzz": 0.05, "ivlFct": 1,
                    "maxIvl": 36500, "minSpace": 1, "perDay": 200},
            "new": {"bury": False, "delays": [1, 10], "initialFactor": 2500,
                    "ints": [1, 4, 7], "order": 1, "perDay": 20,
                    "separate": True},
            "maxTaken": 60,
            "timer": 0,
            "autoplay": True,
            "mod": int(time.time()),
            "usn": 0,
            "dyn": False,
        }
    }

    # ── Col row ───────────────────────────────────────────────────────────────
    col_crt  = int(time.time())
    col_mod  = int(time.time())
    col_scm  = int(time.time() * 1000)
    col_conf = json.dumps({
        "nextPos": 1,
        "estTimes": True,
        "activeDecks": [deck_id],
        "sortType": "noteFld",
        "timeLim": 0,
        "sortBackwards": False,
        "addToCur": True,
        "curDeck": deck_id,
        "newBury": False,
        "newSpread": 0,
        "dueCounts": True,
        "curModel": str(model_id),
        "collapseTime": 1200,
    })

    # ── Criar banco ───────────────────────────────────────────────────────────
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.executescript("""
        CREATE TABLE IF NOT EXISTS col (
            id      INTEGER PRIMARY KEY,
            crt     INTEGER NOT NULL,
            mod     INTEGER NOT NULL,
            scm     INTEGER NOT NULL,
            ver     INTEGER NOT NULL,
            dty     INTEGER NOT NULL,
            usn     INTEGER NOT NULL,
            ls      INTEGER NOT NULL,
            conf    TEXT NOT NULL,
            models  TEXT NOT NULL,
            decks   TEXT NOT NULL,
            dconf   TEXT NOT NULL,
            tags    TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS notes (
            id      INTEGER PRIMARY KEY,
            guid    TEXT NOT NULL,
            mid     INTEGER NOT NULL,
            mod     INTEGER NOT NULL,
            usn     INTEGER NOT NULL,
            tags    TEXT NOT NULL,
            flds    TEXT NOT NULL,
            sfld    TEXT NOT NULL,
            csum    INTEGER NOT NULL,
            flags   INTEGER NOT NULL,
            data    TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS cards (
            id      INTEGER PRIMARY KEY,
            nid     INTEGER NOT NULL,
            did     INTEGER NOT NULL,
            ord     INTEGER NOT NULL,
            mod     INTEGER NOT NULL,
            usn     INTEGER NOT NULL,
            type    INTEGER NOT NULL,
            queue   INTEGER NOT NULL,
            due     INTEGER NOT NULL,
            ivl     INTEGER NOT NULL,
            factor  INTEGER NOT NULL,
            reps    INTEGER NOT NULL,
            lapses  INTEGER NOT NULL,
            left    INTEGER NOT NULL,
            odue    INTEGER NOT NULL,
            odid    INTEGER NOT NULL,
            flags   INTEGER NOT NULL,
            data    TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS revlog (
            id      INTEGER PRIMARY KEY,
            cid     INTEGER NOT NULL,
            usn     INTEGER NOT NULL,
            ease    INTEGER NOT NULL,
            ivl     INTEGER NOT NULL,
            lastIvl INTEGER NOT NULL,
            factor  INTEGER NOT NULL,
            time    INTEGER NOT NULL,
            type    INTEGER NOT NULL
        );
        CREATE TABLE IF NOT EXISTS graves (
            usn     INTEGER NOT NULL,
            oid     INTEGER NOT NULL,
            type    INTEGER NOT NULL
        );
        CREATE INDEX IF NOT EXISTS ix_notes_usn ON notes (usn);
        CREATE INDEX IF NOT EXISTS ix_cards_usn ON cards (usn);
        CREATE INDEX IF NOT EXISTS ix_cards_nid ON cards (nid);
        CREATE INDEX IF NOT EXISTS ix_cards_sched ON cards (did, queue, due);
        CREATE INDEX IF NOT EXISTS ix_revlog_usn ON revlog (usn);
        CREATE INDEX IF NOT EXISTS ix_revlog_cid ON revlog (cid);
    """)

    # Inserir col
    c.execute(
        "INSERT INTO col VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (1, col_crt, col_mod, col_scm, 11, 0, -1, 0,
         col_conf,
         json.dumps(model),
         json.dumps(deck),
         json.dumps(dconf),
         "{}")
    )

    # ── Inserir notes e cards ─────────────────────────────────────────────────
    due_counter = 1
    for card_dict in cards_data:
        texto = card_dict.get('texto', '').strip()
        extra = card_dict.get('extra', '').strip()

        # Verificar que há pelo menos um cloze
        if '{{c' not in texto:
            print(f"[AVISO] Card sem cloze ignorado: {texto[:60]}")
            continue

        note_id  = new_id()
        time.sleep(0.001)   # garantir IDs únicos
        guid     = note_guid(texto)
        flds     = texto + '\x1f' + extra   # separador de campo Anki
        sfld     = re.sub(r'\{\{c\d+::(.*?)\}\}', r'\1', texto)  # texto sem markup
        # checksum dos primeiros 9 chars do sfld
        csum_str = sfld.strip()[:9] if sfld.strip() else texto[:9]
        csum     = int(hashlib.sha1(csum_str.encode('utf-8')).hexdigest(), 16) % (2**32)
        mod_ts   = int(time.time())

        c.execute(
            "INSERT INTO notes VALUES (?,?,?,?,?,?,?,?,?,?,?)",
            (note_id, guid, model_id, mod_ts, -1,
             ' ' + tags_str + ' ',
             flds, sfld, csum, 0, '')
        )

        # Criar um card por ordinal de cloze
        ordinals = count_cloze_ordinals(texto)
        if not ordinals:
            ordinals = [1]

        for ord_num in ordinals:
            card_id = new_id()
            time.sleep(0.001)
            c.execute(
                "INSERT INTO cards VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (card_id, note_id, deck_id,
                 ord_num - 1,       # ord (0-indexed)
                 mod_ts, -1,
                 0,                 # type: new
                 0,                 # queue: new
                 due_counter,       # due
                 0, 0, 0, 0, 0, 0, 0, 0, '')
            )
            due_counter += 1

    conn.commit()
    conn.close()
    print(f"[OK] Banco criado com {due_counter - 1} card(s) em {db_path}")


# ─── Empacotar .apkg ────────────────────────────────────────────────────────────

def empacotar_apkg(db_path: str, output_path: str):
    """Cria o .apkg (zip) com collection.anki2 e media."""
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write(db_path, 'collection.anki2')
        zf.writestr('media', '{}')
    print(f"[OK] Arquivo .apkg gerado: {output_path}")


# ─── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Gera arquivo .apkg Anki Cloze')
    parser.add_argument('--cards', required=True,
                        help='JSON string com lista de dicts {texto, extra}')
    parser.add_argument('--deck-name', required=True,
                        help='Nome do baralho Anki')
    parser.add_argument('--output', required=True,
                        help='Caminho de saída do arquivo .apkg')
    parser.add_argument('--tags', default='',
                        help='Tags extras separadas por vírgula')
    args = parser.parse_args()

    # Parse cards
    try:
        cards_data = json.loads(args.cards)
    except json.JSONDecodeError as e:
        print(f"[ERRO] JSON inválido: {e}")
        return 1

    if not isinstance(cards_data, list) or not cards_data:
        print("[ERRO] --cards deve ser uma lista JSON não vazia.")
        return 1

    # Tags extras
    tags_extras = [t.strip() for t in args.tags.split(',') if t.strip()] if args.tags else []

    # Garantir diretório de saída
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Trabalhar em temp dir
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = os.path.join(tmpdir, 'collection.anki2')
        criar_collection(db_path, cards_data, args.deck_name, tags_extras)
        empacotar_apkg(db_path, str(output_path))

    # Verificar
    size = output_path.stat().st_size
    print(f"[OK] Tamanho final: {size} bytes")
    return 0


if __name__ == '__main__':
    exit(main())
