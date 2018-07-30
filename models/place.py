#!/usr/bin/python3
'''
    Define the class Place.
'''
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.amenity import Amenity


place_amenity = Table("place_amenity", Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey("places.id"), nullable=False),
                      Column('amenities_id', String(60),
                             ForeignKey("amenities.id"), nullable=False))

class Place(BaseModel, Base):

    '''
        Define the class Place that inherits from BaseModel.
    '''
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(Review, backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship(Amenity, secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            '''
            Returns the list of Review instances with place.id==review.place_id
            '''
            from models import storage
            list_review = []
            for review_inst in storage.all(Review).values():
                if review_inst.place_id == self.id:
                    list_review.append(review_inst)
            return list_review

        @property
        def amenities(self):
            '''
            return list of Amenity instances with place.id = amenity.place_id
            '''
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            '''
            Append amenity.id to the attribute amenity_ids in place instance
            '''
            for inst in obj:
                if obj.__class.__name__ == "Amenity":
                    if inst.place_id == self.id:
                        amenity_ids.append(inst)
