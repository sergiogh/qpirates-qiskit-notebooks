# Copyright 2019 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Import networkx for graph tools
import networkx as nx

# Import dwave_networkx for d-wave graph tools/functions
import dwave_networkx as dnx

# Import matplotlib.pyplot to draw graphs on screen
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt

# Set the solver we're going to use
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

# Using Real Device
#sampler = EmbeddingComposite(DWaveSampler())
# Using Simulator
from neal import SimulatedAnnealingSampler
sampler = SimulatedAnnealingSampler()

# Create empty graph
G = nx.Graph()

# Add edges to graph - this also adds the nodes
#G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (3, 5), (4, 5), (4, 6), (5, 6), (6, 7)])
#G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (3, 5), (4, 5), (4, 6), (5, 6), (6, 7), (1,7), (2,7), (8,7), (9,8), (10,9), (11,10) ])
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (3, 5), (4, 5), 
                  (4, 6), (5, 6), (6, 7), (1, 7), (2, 7), (8, 7), 
                  (9, 8), (10,9), (11,10), (1,11), (3,5), (13,14),
                  (1,14), (15,16), (16,17), (17,18), (18,19), (19,20),
                  (20,21), (21,22), (22,23), (22,24), (22,25), (22, 26),
                  (22,27), (22, 28), (22,29), (22,30), (23,30), (19,9) ])

# Find the maximum independent set, S
S = dnx.maximum_independent_set(G, sampler=sampler, num_reads=10, label='Example - Antenna Selection')

# Print the solution for the user
print('Maximum independent set size found is', len(S))
print(S)

# Visualize the results
k = G.subgraph(S)
notS = list(set(G.nodes()) - set(S))
othersubgraph = G.subgraph(notS)
pos = nx.spring_layout(G)
plt.figure()

# Save original problem graph
original_name = "antenna_plot_original.png"
nx.draw_networkx(G, pos=pos, with_labels=True)
plt.savefig(original_name, bbox_inches='tight')

# Save solution graph
# Note: red nodes are in the set, blue nodes are not
solution_name = "antenna_plot_solution.png"
nx.draw_networkx(k, pos=pos, with_labels=True, node_color='r', font_color='k')
nx.draw_networkx(othersubgraph, pos=pos, with_labels=True, node_color='b', font_color='w')
plt.savefig(solution_name, bbox_inches='tight')

print("Your plots are saved to {} and {}".format(original_name, solution_name))
