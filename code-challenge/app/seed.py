from app import db
from models import Power, Hero, Hero_Power
from datetime import datetime
import random

# Seeding powers
print("🦸‍♀️ Seeding powers...")
powers_data = [
    {"name": "super strength", "description": "gives the wielder super-human strengths"},
    {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
    {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
    {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
]

powers = [Power(**data, created_at=datetime.utcnow(), updated_at=datetime.utcnow()) for data in powers_data]
db.session.add_all(powers)
db.session.commit()

# Seeding heroes
print("🦸‍♀️ Seeding heroes...")
heroes_data = [
    {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
    {"name": "Doreen Green", "super_name": "Squirrel Girl"},
    {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
    {"name": "Janet Van Dyne", "super_name": "The Wasp"},
    {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
    {"name": "Carol Danvers", "super_name": "Captain Marvel"},
    {"name": "Jean Grey", "super_name": "Dark Phoenix"},
    {"name": "Ororo Munroe", "super_name": "Storm"},
    {"name": "Kitty Pryde", "super_name": "Shadowcat"},
    {"name": "Elektra Natchios", "super_name": "Elektra"}
]

heroes = [Hero(**data, created_at=datetime.utcnow(), updated_at=datetime.utcnow()) for data in heroes_data]
db.session.add_all(heroes)
db.session.commit()

# Adding powers to heroes
print("🦸‍♀️ Adding powers to heroes...")
strengths = ["Strong", "Weak", "Average"]
for hero in heroes:
    for _ in range(random.randint(1, 3)):
        # Get a random power
        power = Power.query.get(random.choice(powers).id)
        hero_power = Hero_Power(strength=random.choice(strengths), hero=hero, power=power, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        db.session.add(hero_power)

db.session.commit()
print("🦸‍♀️ Done seeding!")
