main = do
    -- input
    s <- getLine

    -- output
    print . length . filter (== '1') $ s
