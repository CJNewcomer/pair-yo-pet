from app.models import db, Pet, User

# Adds a demo user
def seed_pets():

    user1 = User.query.filter_by(username="Demo").first()
    user2 = User.query.filter_by(username="Demo2").first()
    user3 = User.query.filter_by(username="Lisa").first()
    user4 = User.query.filter_by(username="Sky").first()
    user5 = User.query.filter_by(username="hellooo").first()
    user6 = User.query.filter_by(username="maya").first()
    user7 = User.query.filter_by(username="India").first()
    user8 = User.query.filter_by(username="Madellin").first()
    user9 = User.query.filter_by(username="Alaska").first()
    user10 = User.query.filter_by(username="Cecily").first()
    user11 = User.query.filter_by(username="Zaki").first()
    user12 = User.query.filter_by(username="Minerva").first()
    user13 = User.query.filter_by(username="Zoe").first()
    user14 = User.query.filter_by(username="Pillsbury").first()
    user15 = User.query.filter_by(username="Joe").first()
    user16 = User.query.filter_by(username="Kennedy").first()
    user17 = User.query.filter_by(username="Jesse").first()
    user18 = User.query.filter_by(username="Malcolm").first()
    user19 = User.query.filter_by(username="Aniya").first()
    user20 = User.query.filter_by(username="Jeff").first()

    bruno = Pet(
        owner=user1,
        name="Bruno",
        petType="Dog",
        age=7,
        imageURL="https://flask-pairyopet.s3.us-east-2.amazonaws.com/Finnish_Spitz_600.jpg",
        energy=5,
        social=5,
        behaved=5,
        size=2,
        env=3,
        description="Bruno is a Finnish Spitz who loves people and other dogs. He respects all creatures alike, wouldn't harm even his own fleas.",
    )
    cal = Pet(
        owner=user2,
        name="Cal",
        petType="Dog",
        age=6,
        imageURL="https://flask-pairyopet.s3.us-east-2.amazonaws.com/Akita.jpg",
        energy=5,
        social=5,
        behaved=5,
        size=2,
        env=3,
        description="Cal is a sweetheart, super-active, and he prefers to be outside, but I keep him inside because I want all his attention!",
    )
    mylo = Pet(
        owner=user3,
        name="Mylo",
        petType="Dog",
        age=1,
        imageURL="https://pair-yo-pet.s3.amazonaws.com/dog-1246610_640.jpg",
        energy=3,
        social=2,
        behaved=1,
        size=1,
        env=3,
        description="Look at my cute face. I love going for long walks and seeing all the world has to offer.",
    )
    melody = Pet(
        owner=user4,
        name="Melody",
        petType="Dog",
        age=5,
        imageURL="https://pair-yo-pet.s3.amazonaws.com/dog-3139757_640.jpg",
        energy=4,
        social=3,
        behaved=5,
        size=3,
        env=3,
        description="Melody is a husky who loves people and other dogs. She respects all creatures alike, wouldn't harm even her own fleas.",
    )
    rover = Pet(
        owner=user5,
        name="Rover",
        petType="Dog",
        age=7,
        imageURL="https://pair-yo-pet.s3.amazonaws.com/dog-316459_640.jpg",
        energy=5,
        social=2,
        behaved=5,
        size=2,
        env=2,
        description="Small on the outside, ferocious on the inside",
    )
    coco = Pet(
        owner=user6,
        name="Coco",
        petType="Dog",
        age=2,
        imageURL="https://pair-yo-pet.s3.amazonaws.com/dog-4167361_640.jpg",
        energy=3,
        social=5,
        behaved=4,
        size=3,
        env=2,
        description="Coco is the fluffiest fluff ball you will ever meet",
    )
    midnight = Pet(
        owner=user7,
        name="Midnight",
        petType="Dog",
        age=1,
        imageURL="https://pair-yo-pet.s3.amazonaws.com/dog-4427396_640.jpg",
        energy=5,
        social=5,
        behaved=5,
        size=2,
        env=2,
        description="Midnight is the sweetest baby you'd ever meet. Loves kids and is constantly looking for a play mate",
    )
    mylo = Pet(
        owner=user8,
        name="Mylo",
        petType="Dog",
        age=5,
        imageURL="https://pair-yo-pet.s3.amazonaws.com/dog-5964172_640.jpg",
        energy=5,
        social=5,
        behaved=3,
        size=3,
        env=3,
        description="Mylo is an american akita with tons of energy. He loves the cold and playing in the snow.",
    )
    mystic = Pet(
        owner=user9,
        name="Mystic",
        petType="Dog",
        age=8,
        imageURL="https://pair-yo-pet.s3.amazonaws.com/havanese-5938608_640.jpg",
        energy=5,
        social=5,
        behaved=5,
        size=1,
        env=1,
        description="Mystic is a real life teddy bear. Super cute and super cuddly",
    )
    doodle = Pet(
        owner=user10,
        name="Doodle",
        petType="Dog",
        age=7,
        imageURL="https://pair-yo-pet.s3.amazonaws.com/labradoodle-2330320_640.jpg",
        energy=5,
        social=3,
        behaved=3,
        size=3,
        env=2,
        description="Doodle is super energetic and sometimes hard to keep up with. She needs someone on her level to run around with all day",
    )
    snow = Pet(
        owner=user11,
        name="Snow",
        petType="Dog",
        age=9,
        imageURL="https://pair-yo-pet.s3.amazonaws.com/nature-1845066_640.jpg",
        energy=5,
        social=5,
        behaved=2,
        size=1,
        env=2,
        description="Snow is slightly mischevious and stubborn. She never fails to be the sweetest sweetheart playing the occasional trick on her mom.",
    )
    moshi = Pet(
        owner=user12,
        name="Moshi",
        petType="Dog",
        age=5,
        imageURL="https://flask-pairyopet.s3.us-east-2.amazonaws.com/Screen+Shot+2021-02-27+at+9.47.18+PM.png",
        energy=5,
        social=5,
        behaved=5,
        size=2,
        env=2,
        description="Moshi is a japanse akita. Super poised with a lot of style. She enjoys being around other more sophisticated dogs.",
    )
    polo = Pet(
        owner=user13,
        name="Polo",
        petType="Dog",
        age=10,
        imageURL="https://flask-pairyopet.s3.us-east-2.amazonaws.com/Screen+Shot+2021-02-27+at+9.36.24+PM.png",
        energy=2,
        social=5,
        behaved=5,
        size=3,
        env=2,
        description="Polo is a dalmation with a lot of spunk. He loves treats and is constantly looking for an adventure.",
    )
    sponge = Pet(
        owner=user14,
        name="Sponge",
        petType="Dog",
        age=9,
        imageURL="https://pair-yo-pet.s3.amazonaws.com/pexels-fabrizio-avila-6682225.jpg",
        energy=5,
        social=3,
        behaved=3,
        size=2,
        env=3,
        description="Sponge is a bit of a drama queen. Constantly using his favorite trick 'playing dead' to get what he wants.",
    )
    rose = Pet(
        owner=user15,
        name="Rose",
        petType="Dog",
        age=3,
        imageURL="https://pair-yo-pet.s3.amazonaws.com/pexels-julia-volk-5272934.jpg",
        energy=5,
        social=5,
        behaved=3,
        size=1,
        env=2,
        description="Rose loves a party. Can be territorial at times. Looking for a companion to get her more socialized.",
    )
    mario = Pet(
        owner=user16,
        name="Mario",
        petType="Dog",
        age=1,
        imageURL="https://flask-pairyopet.s3.us-east-2.amazonaws.com/Screen+Shot+2021-02-27+at+10.14.44+PM.png",
        energy=5,
        social=3,
        behaved=3,
        size=1,
        env=2,
        description="Mario is a smooth criminal. He knows how to get out of tricky situations and he somehow always finds the treats his parents try to hide.",
    )
    mimi = Pet(
        owner=user17,
        name="Mimi",
        petType="Dog",
        age=10,
        imageURL="https://pair-yo-pet.s3.amazonaws.com/pug-801826_640.jpg",
        energy=5,
        social=5,
        behaved=5,
        size=2,
        env=3,
        description="Drooling is my love language. I love cuddling, looking for another avid cuddler.",
    )
    choco = Pet(
        owner=user18,
        name="Choco",
        petType="Dog",
        age=0,
        imageURL="https://pair-yo-pet.s3.amazonaws.com/puppy-1047722_640.jpg",
        energy=5,
        social=5,
        behaved=5,
        size=1,
        env=2,
        description="Choco is a spoiled little boy. But look at his cute face how could anyone say no to that. Looking for a companion to get into trouble with.",
    )
    boots = Pet(
        owner=user19,
        name="Boots",
        petType="Dog",
        age=3,
        imageURL="https://pair-yo-pet.s3.amazonaws.com/swimming-1502563_640.jpg",
        energy=5,
        social=3,
        behaved=2,
        size=1,
        env=3,
        description="Boots has really bad seperation anxiety. In need of a companion to help him get over his loneliness.",
    )
    star = Pet(
        owner=user19,
        name="Star",
        petType="Dog",
        age=7,
        imageURL="https://pair-yo-pet.s3.amazonaws.com/animal-598305_640.jpg",
        energy=5,
        social=5,
        behaved=5,
        size=3,
        env=2,
        description="Her names speaks for itself. Star is the best doggone dog you'll ever meet. She invented poise.",
    )
    rodger = Pet(
        owner=user20,
        name="Rodger",
        petType="Dog",
        age=5,
        imageURL="https://flask-pairyopet.s3.us-east-2.amazonaws.com/GermanShepherdFootball.png",
        energy=5,
        social=5,
        behaved=5,
        size=3,
        env=2,
        description="In the process of being recruited. Green Bay, here I come. Looking for someone to run some plays with.",
    )

    bruno.bst_frnds.append(cal)

    # db.session.bulk_save_objects([
    #     bruno, 
    #     cal, 
    #     mylo, 
    #     melody, 
    #     rover, 
    #     coco, 
    #     midnight, 
    #     mylo, 
    #     mystic, 
    #     doodle, 
    #     snow, 
    #     moshi, 
    #     polo, 
    #     sponge, 
    #     rose, 
    #     mario, 
    #     mimi, 
    #     choco, 
    #     boots, 
    #     star
    # ])
    db.session.add(bruno)
    db.session.add(cal)
    db.session.add(mylo)
    db.session.add(melody)
    db.session.add(rover)
    db.session.add(coco)
    db.session.add(midnight)
    db.session.add(mylo)
    db.session.add(mystic)
    db.session.add(doodle)
    db.session.add(snow)
    db.session.add(moshi)
    db.session.add(polo)
    db.session.add(sponge)
    db.session.add(rose)
    db.session.add(mario)
    db.session.add(mimi)
    db.session.add(choco)
    db.session.add(boots)
    db.session.add(star)
    db.session.add(rodger)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_pets():
    db.session.execute("TRUNCATE pets CASCADE;")
    db.session.commit()
