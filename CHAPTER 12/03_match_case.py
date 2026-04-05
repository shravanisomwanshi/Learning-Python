def http_status(status):
    match status:
        case 200:
            return "ok" 
        case 404:
            return "not found"
        case 500:
             return "internal server errror" 
        case _:
             return "unknown status" 
             #usage print(http_status(200)) #output: ok print(http_status(404))
             # output: not found print(http_status(500)) #output: internal server

print(http_status(5007))


