********
Problème
********

Vous allez découvrir les notions de base de la programmation orientée objets
en observant bien le code ci-dessous qui définit la classe 

..	code-block:: python
	:linenos:

	class Recipient(object):

    def __init__(self, contenance, no):
       self.no = no                         
       self.contenance = contenance
       self.volume = 0

    def vider(self):
       self.volume = 0

    def transferer(self, autre):
        quantite_transferee = min(autre.contenance - autre.volume, self.volume)
        autre.volume += quantite_transferee
        self.volume -= quantite_transferee
    
    def remplir(self, quantite = None):
       self.volume = self.contenance

    def __str__(self):
        return "Récipient no {}, Contenance : {}, Volume : {}".format(self.no,
                                                                      self.contenance,
                                                                      self.volume)

    def __repr__(self):
        return str(self)

