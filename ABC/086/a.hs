main = do
    -- input
    [a, b] <- map read . words <$> getLine

    -- compute
    let ans = if even $ a*b
        then "Even"
        else "Odd"

    -- output
    putStrLn ans
