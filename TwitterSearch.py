import json
import tweepy


class TwitterSearch :
    """
    Cette classe utilise l'api Twitter "tweepy" pour rechercher differents types
    de tweets selon certains parametres.
    Les resultats sont fournis en JSON.
    """


    def __init__(self, access_token, access_secret, consumer_key, consumer_secret) :
        """
        CONSTRUCTEUR de la classe TwitterSearch
        PARAMS : cles d'acces pour l'api
        ATTRIBUTE api : objet selecteur de l'api pour utiliser les fonctionnalites
        """
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)



    def getTweetsInArea(self, center, radius, query = "", lang = "fr", nbTweets = 200) :
        """
        Recupere les tweets localises dans une zone circulaire
        dont le rayon est en km
        Le resultat est ecrit dans un fichier txt

        PARAM center   : coordonnees du centre de la zone
        PARAM radius   : rayon de la zone en kilometres
        PARAM query    : mots a chercher dans les tweets
        PARAM lang     : langue du tweet
        PARAM nbTweets : nombre max de tweets a retourner

        Ex : Une zone de 20km autour du centre de Grenoble, avec maximum 100 tweets en français et en rapport avec "Grenoble"
            center   = "45.1875602, 5.7357819"
            radius   = "20km"
            query    = "Grenoble"
            lang     = "fr"
            nbTweets = 100
        """
        ret = []
        geo = center + "," + radius
        tweets = tweepy.Cursor(self.api.search, q = query, geocode = geo, lang = lang)

        for status in tweets.items(nbTweets) :
            ret.append(status._json)

        return ret



    def getTrends(self, countryCode = "FR", placeName = "France") :
        """
        Recupere les tendances twitter selon le pays et le lieu.
        Par exemple, les villes disponibles pour les tendances en France sont
            Bordeaux, Lille, Lyon, Marseille, Montpellier, Nantes
            Paris, Rennes, Strasbourg, Toulouse

        PARAM countryCode : code pays
        PARAM placeName : nom de lieu (ville, ...)
        """
        world_trends = self.api.trends_available()     # lieux disponibles des tendances
        idPlace = 0
        for wt in world_trends :
            if wt['countryCode'] == countryCode and wt['name'] == placeName :
                idPlace = wt['woeid']
                break

        trends = self.api.trends_place(id = idPlace)
        return json.dumps(trends, indent=4)
