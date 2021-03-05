# mission_gen
Flask based app that streamlines game set-up in Wh40k

Wrote as my first big python project. Stack used: Flask, MongoDB, py-mongo. 
Directory FlaskServer contains the main part of the app: __init__ file with flask build with factory method and the bleuprints with the views. 
Dir DataModel contains dataclasses which are used as broker beetwen the app and the database. Becouse the project is based upon the noSQL database a way to make sure the datasets will be identical in structure. 
Dir Database driver contains classes build upon PyMongo which encapsulates connection with our DB and particular collections. Writing those classes made building logic behind the views much easier. Plus gave some room to optimize imports from Mongo.

The development of the project was paused due to Covid and freezing of real table top gaming. Will be picked upon again in future.

Can be seen up and running here: http://missiongen.herokuapp.com
