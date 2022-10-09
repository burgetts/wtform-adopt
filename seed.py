from models import db, Pet

# Create 4 pets
pet1 = Pet(name="Spot", species="dog", photo_url="https://i.natgeofe.com/n/4f5aaece-3300-41a4-b2a8-ed2708a0a27c/domestic-dog_thumb_4x3.jpg")
pet2 = Pet(name="Stanley", species="dog", photo_url="https://www.thedogandfriends.com/assets/img/index/img-hero_dog.png")
pet3 = Pet(name="Ginger", species="cat", photo_url="https://styles.redditmedia.com/t5_2r5i1/styles/communityIcon_x4lqmqzu1hi81.jpg")
pet4 = Pet(name="Ted", species="turtle", photo_url="https://us.123rf.com/450wm/jahmaica/jahmaica1409/jahmaica140900055/31642352-turtle-on-the-road.jpg?ver=6")

db.session.add_all([pet1,pet2,pet3,pet4])
db.session.commit()