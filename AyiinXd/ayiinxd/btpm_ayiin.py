try:
    from AyiinXd.modules.sql_helper import SESSION, BASE
except ImportError:
    raise AttributeError

from sqlalchemy import Column, Numeric, UnicodeText


class Fbtpm(BASE):
    __tablename__ = "fbtpm"
    btpm = Column(UnicodeText, primary_key=True)
    reply = Column(UnicodeText)
    f_mesg_id = Column(Numeric)

    def __init__(self, btpm, reply, f_mesg_id):
        self.btpm = btpm
        self.reply = reply
        self.f_mesg_id = f_mesg_id


Fbtpm.__table__.create(checkfirst=True)


def get_btpm(keyword):
    try:
        return SESSION.query(Fbtpm).get(keyword)
    finally:
        SESSION.close()


def get_fbtpm():
    try:
        return SESSION.query(Fbtpm).all()
    finally:
        SESSION.close()


def add_btpm(keyword, reply, f_mesg_id):
    to_check = get_btpm(keyword)
    if not to_check:
        adder = Fbtpm(keyword, reply, f_mesg_id)
        SESSION.add(adder)
        SESSION.commit()
        return True
    else:
        rem = SESSION.query(Fbtpm).filter(Fbtpm.btpm == keyword)
        SESSION.delete(rem)
        SESSION.commit()
        adder = Fbtpm(keyword, reply, f_mesg_id)
        SESSION.add(adder)
        SESSION.commit()
        return False


def remove_btpm(keyword):
    to_check = get_btpm(keyword)
    if not to_check:
        return False
    else:
        rem = SESSION.query(Fbtpm).filter(Fbtpm.btpm == keyword)
        rem.delete()
        SESSION.commit()
        return True
