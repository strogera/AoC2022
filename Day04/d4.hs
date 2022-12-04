parseInput:: [[Char]] -> [[Int]]
parseInput = map(\y -> read ("[" ++ [if x == '-' then ',' else x | x <- y] ++ "]")) 

main = do
    input <- parseInput . lines <$> readFile "input.txt"
    print $ part1 input
    print $ part2 input

part1 input = sum $ fullyContains <$> input
part2 input = sum $ overlap <$> input

fullyContains [a, b, x, y] 
  | (a >= x && b <= y) || (x >= a && y <= b) = 1
  | otherwise = 0

overlap [a, b, x, y] 
  | (a <= x && x <= b) || (a <= y && y <= b) = 1
  | otherwise = fullyContains [a, b, x, y]
