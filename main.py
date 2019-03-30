from MyOpenMap import MyOpenMap



def main() :
    """
    """
    myOSM       = MyOpenMap()
    placeCoords = (45.1875602,5.7357819)     # latitude et longitude d'un lieu
    placeName   = "Grenoble"                 # nom d'un lieu
    bbox        = myOSM.getBbox(placeName)   # boundingbox associee au lieu


    # ===========================================================================================
    #       ASSOCIER UNE VILLE A DES COORDONNEES
    # ===========================================================================================
    city  = myOSM.getCity(placeCoords)
    print("Ville associe aux coords (%r,%r) : %s" %(placeCoords[0], placeCoords[1], city))

    # ===========================================================================================
    #       SAVOIR SI DES COORDONNEES SE TROUVENT DANS UNE VILLE (BBOX)
    # ===========================================================================================
    print("#TODO: getBbox() renvoie une bbox basee sur le point central de la ville")
    if myOSM.isInBbox(bbox, placeCoords) :
        print("(%r,%r) appartiennent à %s" %(placeCoords[0], placeCoords[1], placeName))


if __name__ == '__main__':
    main()
