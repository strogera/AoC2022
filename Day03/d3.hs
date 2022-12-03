import System.IO
import Data.List
import Data.Char

main = do
    input <- lines <$> readFile "input.txt"
    print $  part1 input
    print $  part2 input

part1 input = sum $ score <$> map (\x ->  head $ uncurry intersect $ splitAt (length x `div` 2)  x) input

part2:: [[Char]] -> Int
part2 [] = 0
part2 input = score (head $ foldl1 intersect $ take 3 input) + (part2 $ drop 3 input)

score:: Char -> Int
score c 
    | isLower c = ord c - ord 'a' + 1
    | otherwise = ord c - ord 'A' + 27