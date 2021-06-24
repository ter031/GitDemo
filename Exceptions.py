#ItemsInCart = 0

#if ItemsInCart != 2:#raise Exception("products cart count not matching")
 #   pass

#assert(ItemsInCart == 2)

## try, except
#try:
 #   with open('deepak.txt','r') as reader:
  #      reader.read()

#except:
 #   print("somehow i reached this block because there is failure in try block ")

try:
    with open('deepak.txt','r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning up records")