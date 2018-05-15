import numpy as np
import cv2
import immutils


img = cv2.imread("coins.jpg")
img = immutils.resize(img, 400)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

#Hämtar kanterna för bilden.
edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Orginal",img)
cv2.imshow("Edged",edged)
# cv2.waitKey(0)

#När vi nu har kanterna, dvs outlinesena av mynten, så kan vi hitta konturerna av outlinesen
(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("I count {} coins in this image".format(len(cnts)))

coins = img.copy()

# coins = np.zeros(img.shape[:2], dtype="uint8")

#Här målar vi upp konturerna för bilden
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 3)
cv2.imshow("Coins",coins)
cv2.waitKey(0)

#Nu är det dags att croppa ut varje individuellt mynt ifrån bilden.

#Vi loopar igenom våra konturer.
for (i, c) in enumerate(cnts):
    #Skapar en rektangel som tänker konturen
    (x, y, w, h) = cv2.boundingRect(c)

    print("Coin #{}".format(i+1))

    #Y till Y + H, samt x till X + w
    #Har nu en låda som täcker myntet och visar
    coin = img[y:y + h, x: x+w]
    cv2.imshow("Coin",coin)

    #Skapar en tom canavas med samma storlek som orginalbilden
    mask = np.zeros(img.shape[:2], dtype="uint8")

    #målar upp en cirkel som täcker konturn
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)

    #Målar upp en cirkel som är helfärgat vit, och applicerar på masken på den svarta canavasen, som vi ska använda som mask
    cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)

    #Vi säger att masken ska vara lika stor som området vi får av rektangeln, återigen
    mask = mask[y:y+h, x:x+w]

    #Vi applicerar en bitwise and för att maskera, de svarta områdena, och bara beräkna där de är helt vitt,
    cv2.imshow("Masked Coins",cv2.bitwise_and(coin, coin, mask = mask))
    cv2.waitKey(0)