# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
import numpy as np
import geatpy as ea


class Mutates(ea.Mutation):
    def __init__(self, Pm=None):
        self.Pm = Pm

    def do(self, Encoding, OldChrom, Field):
        NIND, L = OldChrom.shape
        NewChrom = OldChrom.copy()
        pm = self.Pm if self.Pm is not None else 0.7
        for i in range(NIND):
            backup = NewChrom[i].copy()
            NewChrom[i] = mutate_select(backup, pm=pm)
        return NewChrom

def mutate_swap(chrom):
    chrom = np.asarray(chrom).copy()
    cust_idx = np.where(chrom != 0)[0]  # 找出非0位置
    a, b = np.random.choice(cust_idx, size=2, replace=False)
    chrom[a], chrom[b] = chrom[b], chrom[a]
    return chrom


def mutate_insert(chrom):
    chrom = np.asarray(chrom).copy()
    cust_idx = np.where(chrom != 0)[0]
    a, b = np.random.choice(cust_idx, size=2, replace=False)
    gene = chrom[a]
    chrom = np.delete(chrom, a)  # 删除 a 位置
    if a < b:
        chrom = np.insert(chrom, b - 1, gene)  # 删除在前 → 插到 b-1
    else:
        chrom = np.insert(chrom, b, gene)  # 删除在后 → 插到 b
    return chrom


def mutate_invert(chrom):
    chrom = np.asarray(chrom).copy()
    cust_idx = np.where(chrom != 0)[0]
    a, b = sorted(np.random.choice(cust_idx, size=2, replace=False))
    chrom[a:b + 1] = chrom[a:b + 1][::-1]
    return chrom


def mutate_select(chrom, pm):
    chrom = np.asarray(chrom).copy()
    if np.random.rand() > pm:
        return chrom
    op = np.random.choice(["swap", "insert", "invert"])
    if op == "swap":
        end_chrom = mutate_swap(chrom)
    elif op == "insert":
        end_chrom = mutate_insert(chrom)
    elif op == "invert":
        end_chrom = mutate_invert(chrom)
    else:
        end_chrom = chrom
    return end_chrom



