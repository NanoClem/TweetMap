from MyOpenMap import MyOpenMap
import json
from TwitterSearch import TwitterSearch
from MyDatabase import MyDatabase
from MyMap import MyMap



def formatTweetInsertion(status) :
    """
    Formatage des donnees des tweets pour
    insertion dans la BDD
    """
    tweet = {
        "tweetID"    : status.get("id"),
        "created_at" : status.get("created_at"),
        "text"       : status.get("text"),
        "city"       : status.get("place").get("name") if status.get("place") != None else "NULL",
        "country"    : status.get("place").get("country") if status.get("place") != None else "NULL",
        "coords"     : str(status.get("geo").get("coordinates")) if status.get("geo") != None else "NULL",
        "bbox"       : str(status.get("place").get("bounding_box").get("coordinates")) if status.get("geo") != None else "NULL"
    }

    return tweet





def main() :
    """
    Fonction main
    """
    # ===========================================================================================
    #       API TWITTER
    # ===========================================================================================
    #user credentials to access Twitter API
    # access_token =
    # access_secret =
    # consumer_key =
    # consumer_secret =
    #
    # tweetSearch = TwitterSearch(access_token, access_secret, consumer_key, consumer_secret)

    # TENDANCES
    # trends = tweetSearch.getTrends("FR", "France")
    # print(trends)

    # TWEETS DANS UNE ZONE
    # query          = ""                       # n'importe quel sujet
    # STRcoords      = "45.1875602,5.7357819"
    # radius         = "10km"
    # tweetsStatus   = tweetSearch.getTweetsInArea(STRcoords, radius, query, "fr", 500)
    # tweets         = []
    #
    # # FORMATAGE AVANT L'INSERTION DANS LA BDD
    # for t in tweetsStatus :
    #     tweets.append(formatTweetInsertion(t))

    #     print("============================================ NEW TWEET ============================================")
    #     print(t.get("id"))
    #     print(t.get("created_at"))
    #     print(t.get("text"))
    #     print(t.get("hashtags"))
    #     if t.get("place") != None :
    #         print(t.get("place").get("name"))
    #         print(t.get("place").get("country"))
    #         print(t.get("place").get("bounding_box").get("coordinates"))
    #     if t.get("geo") != None :
    #         print(t.get("geo").get("coordinates"))
    #
    #     print('________USER DATA________')
    #     print(t.get("user").get("id"))
    #     print(t.get("user").get("created_at"))
    #     print(t.get("user").get("name"))
    #     print(t.get("user").get("location"))
    #     print("====================================================================================================")



    # ===========================================================================================
    #       DATABASE
    # ===========================================================================================
    # dbName = "twitterdatabase"
    # db = MyDatabase()

    # db.createDatabase(dbName)
    # db.connectToDB(dbName)

    # INSERTION DANS LA BDD
    # db.insertMultiple("tweet", tweets)    # BUG : mysql.connector.errors.DatabaseError: 1366 (HY000): Incorrect string value: '\xF0\x9F\x99\x84'


    # ===========================================================================================
    #  API NOMINATIM :
    #   Cette api a servi pour :
    #       - associer une coordonnee GPS a un nom de ville
    #       - verifier qu'une coordonnee se trouve dans une bounding-box
    # ===========================================================================================
    myOSM       = MyOpenMap()
    placeCoords = (45.1875602,5.7357819)                        # latitude et longitude du centre de Grenoble
    placeName   = "Grenoble"                                    # nom de la ville
    bbox        = [45.149988, 5.684634, 45.212302, 5.782996]    # bounding-box de Grenoble format [minLat, minLong, maxLat, maxLong]

    # ASSOCIER UNE VILLE A DES COORDONNEES
    city  = myOSM.getCity(placeCoords)
    if city in placeName :
        print("Ville associe aux coords (%r,%r) : %s" %(placeCoords[0], placeCoords[1], city))

    # SAVOIR SI DES COORDONNEES SE TROUVENT DANS UNE VILLE (BBOX)
    if myOSM.isInBbox(bbox, placeCoords) :
        print("(%r,%r) appartiennent à %s" %(placeCoords[0], placeCoords[1], placeName))


    # ===========================================================================================
    #       API FOLIUM
    # ===========================================================================================
    map = MyMap(list(placeCoords), 13)

    # SI LES COORDS SONT DANS LA BBOX, ON PLACE UN MARQUEUR AU CENTRE DE LA VILLE
    if myOSM.isInBbox(bbox, placeCoords) :
        map.placeMarker(list(placeCoords), "TestMaker", "This marker is a test")

    map.saveHTML("Grenoble.html")


if __name__ == '__main__':
    main()
