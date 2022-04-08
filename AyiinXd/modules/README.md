# PEMBARUAN MODUL, BUAT KALIAN YANG FORK REPO, JIKA INGIN MENAMBAH MODUL HASIL FORK DARI AYIIN-USERBOT IKUTI CARA DIBAWAH INI 
# ATAU BISA PC @AyiinXd UNTUK MENAMBAHKAN DI AYIIN-USERBOT

```
CARA MENAMBAH PERINTAH MODUL AYIIN-USERBOT

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.utils import ayiin_cmd, edit_or_reply


@ayiin_cmd(pattern="ayiin(?: |$)(.*)")
async def yins(ganteng):
    Ayiin = await edit_or_reply(ganteng, "**Kalian Harus Tau Sebuah Fakta...**")
    sleep(1)
    await Ayiin.edit("**Kalo Ayiin Itu Ganteng...")

CMD_HELP.update(
    {
        "gabutdoang": f"**Plugin :** `gabutdoang`\
        \n\n  »  **Perintah : **`{cmd}ayiin`\
        \n  »  **Kegunaan :** Cobain sendiri tod.\
    "
    }
)
```
