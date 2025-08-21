main :: IO ()
main = putStrLn $
    let numbers = [1,2,4,8,9,10,14,6,3,5,7,9,13,14,15,16,17,18,200,101,211,122]
        evenNumbers = filter even numbers
        amount = length evenNumbers
    in "Liste: " ++ show numbers ++ "\nAnzahl gerader Zahlen: " ++ show amount