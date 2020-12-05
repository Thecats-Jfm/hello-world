a = {0:0}
try :
    print(a[1])
except KeyError as e:
    print("here")
    print(e)
finally:
    print("GN")