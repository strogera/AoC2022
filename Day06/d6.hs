import Data.List

main = do
    input <- readFile "input.txt"
    print $ getAns input 4 0
    print $ getAns input 14 0

getAns inp l i 
    | nub marker == marker = i + l
    | otherwise = getAns (tail inp) l i + 1
    where
        marker = take l inp