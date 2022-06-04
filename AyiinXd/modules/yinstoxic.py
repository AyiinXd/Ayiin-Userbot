
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eor
from Stringyins import get_string


@ayiin_cmd(pattern="d(?: |$)(.*)")
async def _(a):
    await eor(a, get_string("yitxc_1"))


@ayiin_cmd(pattern="e(?: |$)(.*)")
async def _(y):
    await eor(y, get_string("yitxc_2"))


@ayiin_cmd(pattern="f(?: |$)(.*)")
async def _(i):
    await eor(i, get_string("yitxc_3"))


@ayiin_cmd(pattern="i(?: |$)(.*)")
async def _(n):
    await eor(n, get_string("yitxc_4"))


@ayiin_cmd(pattern="r(?: |$)(.*)")
async def _(x):
    await eor(x, get_string("yitxc_5"))


@ayiin_cmd(pattern="t(?: |$)(.*)")
async def _(d):
    await eor(d, get_string("yitxc_6"))


@ayiin_cmd(pattern="u(?: |$)(.*)")
async def _(a):
    await eor(a, get_string("yitxc_7"))


@ayiin_cmd(pattern="w(?: |$)(.*)")
async def _(a):
    await eor(a, get_string("yitxc_8"))


@ayiin_cmd(pattern="bct(?: |$)(.*)")
async def _(a):
    await eor(a, get_string("yitxc_9"))


@ayiin_cmd(pattern="n(?: |$)(.*)")
async def _(a):
    await eor(a, get_string("yitxc_10"))


@ayiin_cmd(pattern="b(?: |$)(.*)")
async def _(a):
    await eor(a, get_string("yitxc_11"))


@ayiin_cmd(pattern="m(?: |$)(.*)")
async def _(y):
    await eor(y, get_string("yitxc_12"))


@ayiin_cmd(pattern="c(?: |$)(.*)")
async def _(y):
    await eor(y, get_string("yitxc_13"))


@ayiin_cmd(pattern="x(?: |$)(.*)")
async def _(a):
    await eor(a, get_string("yitxc_14"))


@ayiin_cmd(pattern="v(?: |$)(.*)")
async def _(y):
    await eor(y, get_string("yitxc_15"))


@ayiin_cmd(pattern="j(?: |$)(.*)")
async def _(i):
    await eor(i, get_string("yitxc_16"))


@ayiin_cmd(pattern="z(?: |$)(.*)")
async def _(i):
    await eor(i, get_string("yitxc_17"))


@ayiin_cmd(pattern="g(?: |$)(.*)")
async def _(n):
    await eor(n, get_string("yitxc_18"))


@ayiin_cmd(pattern="yy(?: |$)(.*)")
async def _(x):
    await eor(x, get_string("yitxc_19"))

@ayiin_cmd(pattern="h(?: |$)(.*)")
async def _(d):
    await eor(d, get_string("yitxc_20"))


@ayiin_cmd(pattern="o(?: |$)(.*)")
async def _(a):
    await eor(a, get_string("yitxc_21"))


@ayiin_cmd(pattern="a(?: |$)(.*)")
async def _(a):
    await eor(a, get_string("yitxc_22"))


CMD_HELP.update(
    {
        "yinstoxic": f"**Plugin : **`yinstoxic`\
        \n\n  »  **Perintah :** `{cmd}d`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}e`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}f`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}i`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}r`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}t`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}u`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}w`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}z`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}n`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}b`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}m`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}c`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}x`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}v`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}a`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}j`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}g`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}yy`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}h`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}o`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}bct`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
