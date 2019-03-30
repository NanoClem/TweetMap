"""
author : decoopmc
"""

from geopy.geocoders import Nominatim


class MyOpenMap :
    """
    """

    def __init__(self) :
        """
        """
        self.nominatim = Nominatim()    # objet accesseurs aux fonctionnalites de Nominatim
        self.location  = None           # donnees sur la localisation du lieu demande



    def _setLocationByCoords(self, coords = ()) :
        """
        """
        self.location = self.nominatim.reverse(coords, addressdetails=True)     # recherche des donnees a partir des coords



    def _setLocationByName(self, placeName = "") :
        """
        """
        self.location = self.nominatim.geocode(placeName, addressdetails=True)  # rechercher des donnees a partir du nom du lieu



    def getCity(self, coords = ()) :
        """
        Retourne le nom de la ville associee aux
        coordonnees en parametre
        PARAM coords : latitude et longitude
        PARAM TYPE : tuple
        RETURN : nom de la ville associée à la position
        """
        self._setLocationByCoords(coords)
        city = self.location.raw['address']['county']    # recuperation de la ville associee

        return city



    def getBbox(self, placeName = "") :
        """
        Retourne la bounding box associee au lieu
        fourni en parametre
        PARAM placeName : nom du lieu dont on cherche la Bbox
        RETURN : Coordonnees de la bbox
        RETURN TYPE : list[decimal]
        """
        self._setLocationByName(placeName)
        bbox = self.location.raw['boundingbox']     # recuperation de la bbox associee au lieu
        bbox = [float(i) for i in bbox]

        return bbox



    def isInBbox(self, bbox = [], coords = ()) :
        """
        Permet de savoir les coordonnees en parametre
        se situent dans la bounding box
        PARAM bbox : bounding box de la zone courrante
        PARAM coords : coordonnees du lieu a tester
        """
        ret   = False
        lats  = bbox[0:2]   # latitudes min et max de la bbox
        longs = bbox[2:4]   # longitudes min et max de la bbox

        if min(lats) < coords[0] and coords[0] < max(lats) :            # si les coords se trouvent dans le
            if min(longs) < coords[0] and coords[0] < max(longs) :      # rectangle que forme la bbox
                ret = True

        return ret
