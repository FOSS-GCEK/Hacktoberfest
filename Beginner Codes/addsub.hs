main:: IO()
main = do
    putStrLn "Enter number A: "
    first <-getLine
    putStrLn "Enter number B: "
    second <-getLine
    putStrLn "A + B = "
    print ((read first) + (read second))
    putStrLn "A - B = "
    print ((read first) - (read second))
