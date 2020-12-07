l= '{"status":0,":1}],"data":""}'
import re
s = l.find('"num')
j = l.find(',"voted')
print(l[s:j])
