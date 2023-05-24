class Details:

  def __init__(self, url, name, price, shipping, da1, da2, da3):
    self.__url = url
    self.__name = name
    self.__price = price
    self.__shipping = shipping.replace(" shipping", "")
    self.__dynamicAttr1 = da1
    self.__dynamicAttr2 = da2
    self.__dynamicAttr3 = da3
    self.__image = "N/A"

  def __str__(self):       
    return "URL: " + self.__url + "\nName: " + self.__name + "\nPrice: " + self.__price + "\nShipping: " + self.__shipping + "\nda1: " + self.__dynamicAttr1 + "\nda2: " + self.__dynamicAttr2 + "\nda3: " + self.__dynamicAttr3

  def getCSVHeader(self):
    return ["URL","Title","Price","Shipping","Dynamic Attribute 1","Dynamic Attribute 2","Dynamic Attribute 3"]

  def getCSVRow(self):
    return [self.__url,self.__name,self.__price,self.__shipping,self.__dynamicAttr1,self.__dynamicAttr2,self.__dynamicAttr3]
