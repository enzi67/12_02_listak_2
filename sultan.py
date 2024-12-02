"""A Török szultán születésnapján gyönyörű ajándékot kapott. Annyira megörült, hogy rögtön  valami jót akart cselekedni. Leküldte hát 400 fős szolgaseregének első szolgáját a börtönbe.  Meghagyta neki, hogy mind a 400 cella ajtaját nyissa ki. Lett is nagy riadalom. A börtönőrök  rettegtek. Ha szabadon engedik a rabokat, és őfelsége kedve változik, fejüket veszi. Leült hát  négyszáz őr a négyszáz nyitott cella elé. Teljesítették is a szultán parancsát, de a rabokat sem  engedték szabadon. Igazuk lett. A szultán megharagudott, mert a következő ajándék nem  tetszett. 
Leküldte a második szolgát. Azt parancsolta, minden második ajtót zárjon be.  Kisvártatva meggondolta magát, és leküldte a harmadik szolgát, hogy minden harmadik ajtót  nyissa ki, ha zárva van, és zárja be, ha nyitva van. Majd leküldte a negyedik szolgát, hogy  minden negyedik ajtón változtasson. Aztán az ötödiket, hatodikat… és így tovább egészen  addig, míg az utolsó, a 400. szolgának azt parancsolta: Menj le és a 400. cellát nyisd ki, ha  zárva van, De ha nyitva lenne, akkor zárd be. Így is lett. Azzal a szultán nyújtózott egyet, és  lefeküdt aludni.  
A börtönparancsnok tudta, aznap már több parancs nem jön, és a szultán soha nem vonja  vissza azokat a parancsait, amit előző nap adott. Szabadon engedte hát azokat, akiknek a  cellája nyitva volt. Kiket is?  
Az ön által ismert programnyelven készítsen programot mely, szimulálja a fenti  eseményeket, és végül megadja mely cellák ajtaja lesz nyitva a végén! 
"""

ajtok = [False] * 400

for i in range(1, 401):
    for j in range(i-1, 400, i):
        ajtok[j] = not ajtok[j]

nyitott_ajtok = []
for i in range(400):
    if ajtok[i]:
        nyitott_ajtok.append(i + 1)

print("A nyitva maradt ajtók cellái:", nyitott_ajtok)
