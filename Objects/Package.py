class Package:

    def __init__(self, id, address, city, state, zip, deadline, weight, status):
        self._id = id
        self._address = address
        self._city = city
        self._state = state
        self._zip = zip
        self._deadline = deadline
        self._weight = weight
        self._status = status

    def id(self):
        return self._id

    def address(self):
        return self._address

    def city(self):
        return self._city

    def state(self):
      return self._state

    def zip(self):
      return self._zip

    def deadline(self):
      return self._deadline

    def weight(self):
      return self._weight

    def status(self):
      return self._status
