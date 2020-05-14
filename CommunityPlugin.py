class CommunityPlugin:
   def input(self,filename):
      # Parameter file
      self.parameters = dict()
      paramfile = open(filename, 'r')
      for line in paramfile:
         contents = line.split('\t')
         self.parameters[contents[0]] = contents[1].strip()

      # Abundances
      self.abundances = dict()
      abundfile = open(self.parameters['abundances'], 'r')
      header = abundfile.readline() # Header
      for line in abundfile:
         contents = line.split('\t')
         self.abundances[contents[0]] = float(contents[1])

      # Clusters
      self.clusters = []
      clusterfile = open(self.parameters['clusters'], 'r')
      clustercount = 0
      for line in clusterfile:
         if (line.strip() == "\"\",\"x\""):
            self.clusters.append([])
            clustercount += 1
         else:
            contents = line.split(',')
            self.clusters[clustercount-1].append(contents[1].strip())
      
      # Centroids
      self.centroids = []
      centroidfile = open(self.parameters['centroids'], 'r')
      header = centroidfile.readline()
      for line in centroidfile:
         contents = line.split(',')
         self.centroids.append(contents[1].strip())

   def run(self):
      target = self.parameters['target']
      
      self.results = dict()
      found = False
      for i in range(len(self.clusters)):
         if (target in self.clusters[i]):
            found = True
            self.results['centroid'] = self.centroids[i]
            self.results['clusters'] = []
            for j in range(len(self.clusters[i])):
               self.results['clusters'].append((self.clusters[i][j], self.abundances[self.clusters[i][j]]))
      if (not found):
        print("WARNING: Node "+target+" NOT FOUND IN ANY CLUSTER.")

   def output(self, filename):
      outputfile = open(filename, 'w')
      outputfile.write("Name\tAbundance\tTarget\tCentroid\n")
      for taxontuple in self.results['clusters']:
         outputfile.write(taxontuple[0]+"\t"+str(taxontuple[1])+"\t")
         if (taxontuple[0] == self.parameters['target']):
            outputfile.write(str(1)+"\t")
         else:
            outputfile.write(str(0)+"\t")
         if (taxontuple[0] == self.results['centroid']):
            outputfile.write(str(1)+"\n")
         else:
            outputfile.write(str(0)+"\n")
