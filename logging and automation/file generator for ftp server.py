from api_error_log_tool import automated_logging as log

import random
import string


def random_headers():
    headers = ["headers"]

    for header in headers:
        new_headers.append(list(header))
    
    for index in new_headers:
        current_header = index
        indx = random.randrange(len(index))
        current_header.pop(indx)
        index = "".join(index)
        shuffled_headers.append(index)
    return print(shuffled_headers) 


log(random_headers())
