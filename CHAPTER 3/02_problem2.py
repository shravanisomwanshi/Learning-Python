letter = ''' Dear <|name|>,
             you are selected! 
             <|Date|> '''


print(letter.replace("<|name|>", "Harry").replace("<|Date|>", "24 september 2005"))