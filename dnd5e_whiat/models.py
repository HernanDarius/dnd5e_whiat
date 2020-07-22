"""SQLAlchemy models and utility functions"""
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

char = ['Lilgrea', 'Sofri', 'Baerdal', 'Norlos', 'Lichithal',
        'Wolnoa']

race = ['Tiefling', 'Human', 'Dwarf', 'Halfling', 'Dragonborn',
        'Half-Elf']

cla = ['Warlock', 'Rogue', 'Blood Hunter', 'Monk', 'Paladin',
           'Ranger']

lvl = [1,1,1,1,1,1]

exp = [0,0,0,0,0,0]

hp = [10, 10, 11, 12, 11, 12]

st = [8, 13, 17, 12, 17, 12]

dex = [13, 16, 13, 17, 10, 16]

con = [14, 14, 12, 13, 13, 14]

intelligence = [13, 9, 14, 10, 8, 8]

wis = [10, 15, 8, 14, 12, 14]

charm = [17, 11, 12, 9, 15, 12]

class Character(DB.Model):
    """DnD Characters"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(40), nullable=False)
    race = DB.Column(DB.String(20), nullable=False)
    classs = DB.Column(DB.String(20), nullable=False)
    level = DB.Column(DB.Integer, nullable=False)
    exp = DB.Column(DB.Integer, nullable=False)
    hp = DB.Column(DB.Integer, nullable=False)
    strength = DB.Column(DB.Integer, nullable=False)
    dexterity = DB.Column(DB.Integer, nullable=False)
    constitution = DB.Column(DB.Integer, nullable=False)
    intelligence = DB.Column(DB.Integer, nullable=False)
    wisdom = DB.Column(DB.Integer, nullable=False)
    charisma = DB.Column(DB.Integer, nullable=False)

    def __repr__(self):
        return '<Character> {}'.format(self.name)

def add_character():
    for i, (n, r, c, l, e, h, s, d, co, intel, w, ch) in (
    enumerate(zip(char, race, cla, lvl, exp, hp, 
    st, dex, con, intelligence, wis, charm))):
        character = Character(id=i, name=n, race=r, classs=c,
                              level=l, exp=e, hp=h, strength=s,
                              dexterity=d, constitution=co,
                              intelligence=intel, wisdom=w,
                              charisma=ch)
        DB.session.add(character)
    DB.session.commit()
