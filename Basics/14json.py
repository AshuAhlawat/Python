#timer 
import time as t
initial = t.time()

    # ACTUAL CODE

import json

money=list(input("Money you have "))
print(money,type(money))

#creats JSON
scraps=json.dumps(money)
print(scraps,type(scraps))

#parsing JSON
money=json.loads(scraps)
print(money,type(money))

print("\n\n",round(t.time()-initial,4))