main = do
    -- input
    a <- readLn
    [b, c] <- map read . words <$> getLine
    s <- getLine

    -- output
    putStrLn $ unwords [show $ a + b + c, s]
