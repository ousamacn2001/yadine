
import hashlib
import os
os.system ('clear')
txt = input ('entre the text: ')
#md5 
hash_hash = hashlib.new('md5')
txt= txt.encode ("utf-8")
txt=hash_hash.update (txt)
#md4 
hash_hash1 = hashlib.new('md4')
txt2= hash_hash.hexdigest().encode("utf-8")
txt2=hash_hash1.update  (txt2)
# sha
hash_hash2 = hashlib.new('sha')
txt3= hash_hash1.hexdigest().encode("utf-8")
txt3=hash_hash2.update (txt3)
#SHA512
hash_hash3 = hashlib.new('SHA512')
txt4= hash_hash2.hexdigest().encode("utf-8")
txt4=hash_hash3.update (txt4)
#SHA384
hash_hash4 = hashlib.new('SHA384')
txt5= hash_hash3.hexdigest().encode("utf-8")
txt5=hash_hash4.update (txt5)
#DSA-SHA
hash_hash5 = hashlib.new('DSA-SHA')
txt6= hash_hash4.hexdigest().encode("utf-8")
txt6=hash_hash5.update (txt6)
#DSA
hash_hash6 = hashlib.new('DSA')
txt7= hash_hash5.hexdigest().encode("utf-8")
txt7=hash_hash6.update (txt7)
#RIPEMD160
hash_hash7 = hashlib.new('RIPEMD160')
txt8= hash_hash6.hexdigest().encode("utf-8")
txt8=hash_hash7.update (txt8)
#SHA1
hash_hash8 = hashlib.new('SHA1')
txt9= hash_hash7.hexdigest().encode("utf-8")
txt9=hash_hash8.update (txt9)
#dsaEncryption
hash_hash9 = hashlib.new('dsaEncryption')
txt10= hash_hash8.hexdigest().encode("utf-8")
txt10=hash_hash9.update (txt10)
#whirlpool
hash_hash10= hashlib.new('whirlpool')
txt11= hash_hash9.hexdigest().encode("utf-8")
txt11=hash_hash10.update (txt11)
#sha256
hash_hash11 = hashlib.new('sha256')
txt12= hash_hash10.hexdigest().encode("utf-8")
txt12=hash_hash11.update (txt12)
#ecdsaw-with-SHA1
hash_hash12 = hashlib.new('ecdsa-with-SHA1')
txt13= hash_hash11.hexdigest().encode("utf-8")
txt13=hash_hash12.update (txt13)
#md4 
hash_hash13 = hashlib.new('md4')
txt14= hash_hash12.hexdigest().encode("utf-8")
txt14=hash_hash13.update  (txt14)
#md5 
hash_hash14 = hashlib.new('md5')
txt15=hash_hash13.hexdigest().encode("utf-8")
txt15=hash_hash14.update (txt15)
#RIPEMD160
hash_hash15 = hashlib.new('RIPEMD160')
txt16= hash_hash14.hexdigest().encode("utf-8")
txt16=hash_hash14.update (txt16)
print ("-----------------------------------------")
print ( hash_hash15.hexdigest() )
print ("-----------------------------------------")
