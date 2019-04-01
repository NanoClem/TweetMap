"""
author : decoopmc
"""

import folium


class MyMap :
    """
    """

    def __init__(self, base_map_location = [], zoom = 13) : #bbox = []) :
        """
        CONSTRUCTEUR de la classe MyMap

        PARAM base_map_location :
        """
        self.baseMap = folium.Map(location = base_map_location, zoom_start = zoom)



    def saveHTML(self, filename) :
        """
        Sauvegarde le contenu de la carte courrante dans un
        fichier html

        PARAM filename : nom du fichier html
        """
        if "html" not in filename :
            print(".html extension required")

        self.baseMap.save(filename)



    def placeMarker(self, location = [], hooverContent="", clickContent="") :
        """
        Place un marqueur sur la carte a la position indiquee, avec les informations
        textuelles associees

        PARAM location : coordonnees du marqueur
        PARAM hooverContent : contenu du marqueur au survolement de la souris
        PARAM clickContent : contenu du marqueur au click de la souris
        """
        folium.Marker(location = location,
                      popup    = clickContent,
                      tooltip  = hooverContent).add_to(self.baseMap)



    def placeCircleMarker(self, location = [], radius = 20, hooverContent = "", clickContent = "") :
        """
        Place une zone circulaire sur la carte a la position indiquee, avec les informations
        textuelles associees

        PARAM location : coordonnees du marqueur
        PARAM radius : rayon du marqueur
        PARAM hooverContent : contenu du marqueur au survolement de la souris
        PARAM clickContent : contenu du marqueur au click de la souris
        """
        folium.CircleMarker(location = location,
                            popup    = clickContent,
                            tooltip  = hooverContent,
                            color    = '#3186cc',
                            fill     = True,
                            fill_color = '#3186cc').add_to(self.baseMap)
