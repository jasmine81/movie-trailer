#!usr/bin/env python
import media
import fplace
liberty = media.Movie(
    "Statue of Liberty",
    "https://encrypted-tbn0.gstatic.com/grid-items?q=tbn:ANd9GcQkVuw6z5E3x"
    "uFeVXDcveZGHDFcoSp_EbfAutt4nFgvn596s1Vv",
    "https://www.youtube.com/embed/kOAS3bmtSAM"
    )
eiffel = media.Movie(
    "Eiffel Tower",
    "https://encrypted-tbn0.gstatic.com/grid-items?"
    "q=tbn:ANd9GcTBblePFpfGNoAOKfRthU-tz6QUFLllhpC0KKRPuin0CRQI36u3",
    "https://www.youtube.com/embed/s3bCKfPgoLQ"
    )
bigben = media.Movie(
    "Big Ben",
    "https://encrypted-tbn0.gstatic.com/grid-items?"
    "q=tbn:ANd9GcQh7V89xCCCCniErs6LSOsUC_44FDdda0Eb-aPpF5MrDZ2av8Re",
    "https://www.youtube.com/embed/fKmpld1PoPQ"
    )
pisa = media.Movie(
    "Leaning Tower of Pisa",
    "http://www.towerofpisa.org/wp-content/uploads/"
    "photo-gallery/pisa-leaning-tower.jpg",
    "https://www.youtube.com/embed/nGavsnu9m4A"
    )
ggb = media.Movie(
    "Golden Gate Bridge",
    "https://s3.envato.com/files/236066482"
    "/20160214-BatterySpencer-8824-8mp.jpg",
    "https://www.youtube.com/embed/G2FrANjg_OY"
    )
opera = media.Movie(
    "Opera House",
    "https://upload.wikimedia.org/wikipedia/commons"
    "/a/a1/Sydney_Opera_House_Night.jpg",
    "https://www.youtube.com/embed/F5CPHRJwdZ0")
Movies = [liberty, eiffel, bigben, pisa, ggb, opera]
fplace.open_movies_page(Movies)
