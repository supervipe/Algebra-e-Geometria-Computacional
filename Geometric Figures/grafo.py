from collections import defaultdict
from matrix import Matrix

class Edge(object):
  def __init__(self, u, v, w):
    self.source = u
    self.target = v
    self.capacity = w

  def __repr__(self):
    return "%s->%s:%s" % (self.source, self.target, self.capacity)


class FlowNetwork(object):
  def __init__(self):
    self.adj = defaultdict(list)
    self.flow = defaultdict(list)

  def AddVertex(self, vertex):
    self.adj[vertex] = []

  def GetEdges(self, v):
    return self.adj[v]

  def AddEdge(self, u, v, w=0):
    if u == v:
      raise ValueError("u == v")
    edge = Edge(u, v, w)
    redge = Edge(v, u, 0)
    edge.redge = redge
    redge.redge = edge
    self.adj[u].append(edge)
    self.adj[v].append(redge)
    # Intialize all flows to zero
    self.flow[edge] = 0
    self.flow[redge] = 0

  def FindPath(self, source, target, path):
    if source == target:
      return path
    for edge in self.GetEdges(source):
      residual = edge.capacity - self.flow[edge]
      if residual > 0 and not (edge, residual) in path:
        result = self.FindPath(edge.target, target, path + [(edge, residual)])
        if result != None:
          return result

  def MaxFlow(self, source, target):
    path = self.FindPath(source, target, [])
    ini = []
    fim = []
    print ('path after enter MaxFlow: %s' % path)
    for key in self.flow:
      print ('%s:%s' % (key, self.flow[key]))
    print ('-' * 20)
    while path != None:
      flow = min(res for edge, res in path)
      for edge, res in path:
        self.flow[edge] += flow
        self.flow[edge.redge] -= flow
      for key in self.flow:
        print ('%s:%s' % (key, self.flow[key]))
      path = self.FindPath(source, target, [])
      print ('path inside of while loop: %s' % path)
    for key in self.flow:
      v = ('%s' % (key))
      if "10" not in v:
        if "0" not in v and self.flow[key] != 0:
          print ('%s:%s' % (key, self.flow[key]))
          div = v.split("->")
          ini.append(div[0])
          div = div[1].split(":")
          fim.append(div[0])
      else:
        print ('%s:%s' % (key, self.flow[key]))
        div = v.split("->")
        ini.append(div[0])
        div = div[1].split(":")
        fim.append(div[0])
    return sum(self.flow[edge] for edge in self.GetEdges(source)),ini,fim


if __name__ == "__main__":
  g = FlowNetwork()
  map(g.AddVertex, ['brasil', 'usa', 'canada', 'russia', 'portugal', 'argentina', 'africaSul', 'egito', 'india', 'australia', 'japao'])
  g.AddEdge('brasil', 'usa', 7)
  g.AddEdge('brasil', 'africaSul', 8)
  g.AddEdge('brasil', 'argentina', 10)
  g.AddEdge('argentina', 'australia', 15)
  g.AddEdge('usa', 'canada', 4)
  g.AddEdge('canada', 'russia', 10)
  g.AddEdge('usa', 'portugal', 5)
  g.AddEdge('canada', 'portugal', 8)
  g.AddEdge('portugal', 'egito', 4)
  g.AddEdge('portugal', 'russia', 6)
  g.AddEdge('russia', 'portugal', 8)
  g.AddEdge('africaSul', 'egito', 7)
  g.AddEdge('egito', 'india', 5)
  g.AddEdge('india', 'japao', 6)
  g.AddEdge('india', 'australia', 10)
  g.AddEdge('australia', 'india', 10)
  g.AddEdge('australia', 'japao', 11)
  g.AddEdge('russia', 'japao', 7)
  print(g.MaxFlow('brasil', 'japao'))