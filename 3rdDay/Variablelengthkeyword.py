def polygon(**kwds):
    print (type(kwds))
    print (kwds)

polygon(width=10,length=20)
polygon(width=10,length=20,height=5)
polygon(width=10,length=20,height=5,units='cm')

#**kwds will pack all arguments into a dict called kwds in this example

#* is used with positional argument and ** is used in eyword argument
