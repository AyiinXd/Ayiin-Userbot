import os
from os import listdir, path
from typing import Any, Dict, List, Union

from AyiinXd import LOGS
from AyiinXd.ayiin.logger import logging

from google_trans_new import google_translator
from yaml import safe_load

LOGS = logging.getLogger(__name__)

language = [os.environ.get("language") or "id"]
languages = {}

Trs = google_translator()

strings_folder = path.join(path.dirname(path.realpath(__file__)), "strings")

for file in listdir(strings_folder):
    if file.endswith(".yml"):
        code = file[:-4]
        try:
            languages[code] = safe_load(open(path.join(strings_folder, file), encoding="UTF-8"),
            )
        except Exception as er:
            LOGS.info(f"Kesalahan dalam {file[:-4]} file bahasa")
            LOGS.exception(er)


def get_string(key: str) -> Any:
    lang = language[0]
    try:
        return languages[lang][key]
    except KeyError:
        try:
            id_ = languages["id"][key]
            tr = Trs.translate(id_, lang_tgt=lang).replace("\ N", "\n")
            if id_.count("{}") != tr.count("{}"):
                tr = id_
            if languages.get(lang):
                languages[lang][key] = tr
            else:
                languages.update({lang: {key: tr}})
            return tr
        except KeyError:
            return f"Peringatan: tidak dapat memuat string apa pun dengan kunci `{key}`"
        except Exception as er:
            LOGS.exception(er)
            return languages["id"].get(key) or f"Gagal Memuat Pengaturan Bahasa  '{key}'"


def get_languages() -> Dict[str, Union[str, List[str]]]:
    return {
        code: {
            "nama": languages[code]["nama"],
            "asli": languages[code]["asli"],
            "penulis": languages[code]["penulis"],
        }
        for code in languages
    }
