main :: IO ()
main = putStrLn $
    let zahlen = [1,2,4,8,9,10,14,6,3,5,7,9,13,14,15,16,17,18,200,101,211,122]
        gerade = filter even zahlen
        anzahl = length gerade
    in "Liste: " ++ show zahlen ++ "\nAnzahl gerader Zahlen: " ++ show anzahl