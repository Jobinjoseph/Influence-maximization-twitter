# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 22:47:20 2025

@author: joseph
"""

from mrjob.job import MRJob
import networkx as nx
import gzip
import random
import os

class InfluenceMaxMRJob(MRJob):

    def configure_args(self):
        super(InfluenceMaxMRJob, self).configure_args()
        self.add_file_arg('--graph', help='Path to graph file')


    def load_graph(self):
        graph_path = os.path.basename(self.options.graph)  # just filename
        self.G = nx.DiGraph()
        with gzip.open(graph_path, 'rt') as f:
            for line in f:
                if line.startswith('#') or line.strip() == '':
                    continue
                src, tgt = map(int, line.strip().split())
                self.G.add_edge(src, tgt)


    def run_ic_model(self, seed_set, influence_prob=0.05):
        influenced = set(seed_set)
        newly_influenced = set(seed_set)
        while newly_influenced:
            next_newly_influenced = set()
            for node in newly_influenced:
                for nbr in self.G.successors(node):
                    if nbr not in influenced and random.random() <= influence_prob:
                        next_newly_influenced.add(nbr)
            influenced.update(next_newly_influenced)
            newly_influenced = next_newly_influenced
        return influenced

    def mapper_init(self):
        self.load_graph()

    def mapper(self, _, line):
        node_id = int(line.strip())
        mc_simulations = 5
        influence_prob = 0.05
        total_spread = 0
        for _ in range(mc_simulations):
            spread_set = self.run_ic_model({node_id}, influence_prob)
            total_spread += len(spread_set)
        avg_spread = total_spread / mc_simulations
        yield node_id, avg_spread

    def reducer(self, key, values):
        values_list = list(values)
        yield key, sum(values_list) / len(values_list)

if __name__ == '__main__':
    InfluenceMaxMRJob.run()
