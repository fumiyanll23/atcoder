main = do
    -- input
    n <- getLine
    as <- map read . words <$> getLine

    -- output
    print $ minimum $ map canDivTwo as


canDivTwo :: Int -> Int
canDivTwo x = if even x
    then 1 + canDivTwo (x `div` 2)
    else 0
