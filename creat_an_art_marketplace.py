class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner

  def __repr__(self):
    return """{artist_name}. "{name_of_art}". {year}, {medium}. {owner}, {location}.""".format(artist_name = self.artist, name_of_art = self.title, year=self.year, medium = self.medium, owner=self.owner.name, location=self.owner.location)

class Marketplace:
  def __init__(self):
    self.listings =[]

  def add_listing(self, new_listing):
      self.listings.append(new_listing)

  def remove_listing(self, expire_list):
      self.listings.remove(expire_list)

  def show_listings(self):
    for listing in self.listings:
      print(listing)

class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.is_museum = is_museum #is_museum is a boolean
    if is_museum:
      self.location =location
    else:
      self.location = "Private Collection"

  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      list_1=listing(artwork, price, self)
      veneer.add_listing(list_1)

  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for listing in veneer.listings:
        if listing.art == artwork: #listing(art,price, seller)
          art_listing = listing #asign the listing to a new variable
          break
      if art_listing != None:
        art_listing.art.owner=self # change the owner's name
        veneer.remove_listing(art_listing)# delete the list after be bought


# list the art is going to be sold
class listing:

  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller =seller

  def __repr__(self):
    return "{art}: {price}".format(art=self.art.title, price=self.price)


#example with the data added
edytta = Client("Edytta Halpirt", None, False)
moma = Client("The MOMA", "New York", True)

girl_with_mandolin=Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", "1910", edytta)

man_with_woods=Art("Pic, Pao", "man with a Mandolin", "oil on canvas", "1800", edytta)

veneer=Marketplace()

edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")
edytta.sell_artwork(man_with_woods, "$4M (USD)")

veneer.show_listings()

moma.buy_artwork(girl_with_mandolin)

print(girl_with_mandolin)

veneer.show_listings()


  
