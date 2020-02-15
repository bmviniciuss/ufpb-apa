class Truck:
  def __init__(self, capacity):
    self._capacity = capacity
    self._load = 0
    self._current_location = 0
    self._path = []
  

  def is_full(self):
    return self._load == self._capacity

  @property
  def capacity(self):
    return self._capacity

  @property
  def load(self):
    return self._load
  
  def available_load(self):
    return self._capacity - self._load

  @property
  def current_location(self):
    return self._current_location
  
  @property
  def path(self):
    return self._path

  @current_location.setter
  def current_location(self,location):
    self._current_location = location

  def add_load(self,demand):
    self._load += demand
  
  def add_to_path(self,node):
    self._path.append(node)
  
  def __str__(self):
    return str(self.capacity)
