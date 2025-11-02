# -*- coding: utf-8 -*-
import numpy as np
import geatpy as ea  # 导入geatpy库
from change_geatpy_source_code.get_evaluate_fun import evaluate_route_cost


def is_feasible(chroms):
    need_time_total, all_satisfaction, all_cost = evaluate_route_cost(chroms)
    if need_time_total == 10000:
        return False
    else:
        return True


class MutInverse(ea.Mutation):
    def __init__(self, Pm=None, max_try=5):
        self.Pm = Pm
        self.max_try = max_try

    def do(self, Encoding, OldChrom, Field):
        NIND, L = OldChrom.shape
        NewChrom = OldChrom.copy()

        if self.Pm is None:
            Pm = 1
        else:
            Pm = self.Pm

        for i in range(NIND):
            if np.random.rand() < Pm:
                backup = NewChrom[i].copy()
                success = False
                for _ in range(self.max_try):
                    a, b = np.sort(np.random.choice(L, 2, replace=False))
                    trial = NewChrom[i].copy()
                    trial[a:b + 1] = trial[a:b + 1][::-1]
                    if is_feasible(trial):
                        NewChrom[i] = trial
                        success = True
                        break
                if not success:
                    NewChrom[i] = backup

        return NewChrom


class CrossoverPMX(ea.Recombination):
    def __init__(self, Pc=0.9, max_try=5, Methods=1, Parallel=False):
        self.Pc = Pc
        self.max_try = max_try
        self.Methods = Methods
        self.Parallel = Parallel

    def do(self, OldChrom):
        NIND, L = OldChrom.shape
        NewChrom = OldChrom.copy()
        for i in range(0, NIND - 1, 2):
            if np.random.rand() < self.Pc:
                parent1, parent2 = OldChrom[i].copy(), OldChrom[i + 1].copy()
                backup1, backup2 = parent1.copy(), parent2.copy()
                success = False
                for _ in range(self.max_try):
                    a, b = np.sort(np.random.choice(L, 2, replace=False))
                    child1, child2 = self._pmx_crossover(parent1, parent2, a, b)
                    if is_feasible(child1) and is_feasible(child2):
                        NewChrom[i], NewChrom[i + 1] = child1, child2
                        success = True
                        break
                if not success:  # 打回父代
                    NewChrom[i], NewChrom[i + 1] = backup1, backup2
        return NewChrom

    def _pmx_crossover(self, p1, p2, a, b):
        L = len(p1)
        c1, c2 = p1.copy(), p2.copy()
        c1[a:b + 1], c2[a:b + 1] = p2[a:b + 1], p1[a:b + 1]
        mapping1 = {p2[k]: p1[k] for k in range(a, b + 1)}
        mapping2 = {p1[k]: p2[k] for k in range(a, b + 1)}
        def repair(child, a, b, mapping):
            for i in list(range(0, a)) + list(range(b + 1, L)):
                while child[i] in mapping:
                    child[i] = mapping[child[i]]
            return child

        c1 = repair(c1, a, b, mapping1)
        c2 = repair(c2, a, b, mapping2)

        return c1, c2


class moea_NSGA2_templetss(ea.MoeaAlgorithm):
    """
moea_NSGA2_templet : class - 多目标进化NSGA-II算法类

算法描述:
    采用NSGA-II进行多目标优化，算法详见参考文献[1]。

参考文献:
    [1] Deb K , Pratap A , Agarwal S , et al. A fast and elitist multiobjective
    genetic algorithm: NSGA-II[J]. IEEE Transactions on Evolutionary
    Computation, 2002, 6(2):0-197.

    """

    def __init__(self,
                 problem,
                 population,
                 MAXGEN=None,
                 MAXTIME=None,
                 MAXEVALS=None,
                 MAXSIZE=None,
                 logTras=None,
                 verbose=None,
                 outFunc=None,
                 drawing=None,
                 dirName=None,
                 selectStyle='tour',
                 prophetPop=None,
                 **kwargs):
        # 先调用父类构造方法
        super().__init__(problem, population, MAXGEN, MAXTIME, MAXEVALS, MAXSIZE, logTras, verbose, outFunc, drawing,
                         dirName, **kwargs)
        if prophetPop is not None:
            if not isinstance(prophetPop, ea.Population):
                raise TypeError('prophetPop 必须是 geatpy.Population 类型')
            elif prophetPop.sizes < 1:
                raise ValueError('先知种群至少包含1个个体')
            else:
                self.prophetPop = prophetPop
        else:
            self.prophetPop = None

        if population.ChromNum != 1:
            raise RuntimeError('传入的种群对象必须是单染色体的种群类型。')
        self.name = 'NSGA2'
        if self.problem.M < 10:
            self.ndSort = ea.ndsortESS  # 采用ENS_SS进行非支配排序
        else:
            self.ndSort = ea.ndsortTNS  # 高维目标采用T_ENS进行非支配排序，速度一般会比ENS_SS要快
        self.selFunc = selectStyle  # 选择方式，采用锦标赛选择
        if population.Encoding == 'P':
            self.recOper = CrossoverPMX(Pc=0.8)  # 生成部分匹配交叉算子对象
            self.mutOper = MutInverse(Pm=0.1)  # 生成交换
        elif population.Encoding == 'BG':
            self.recOper = ea.Xovud(XOVR=1)  # 生成均匀交叉算子对象
            self.mutOper = ea.Mutbin(Pm=None)  # 生成二进制变异算子对象，Pm设置为None时，具体数值取变异算子中Pm的默认值
        elif population.Encoding == 'RI':
            self.recOper = ea.Recsbx(XOVR=1, n=20)  # 生成模拟二进制交叉算子对象
            self.mutOper = ea.Mutpolyn(Pm=1 / self.problem.Dim, DisI=20)  # 生成多项式变异算子对象
        else:
            raise RuntimeError('编码方式必须为''BG''、''RI''或''P''.')

    def reinsertion(self, population, offspring, NUM):

        """
        描述:
            重插入个体产生新一代种群（采用父子合并选择的策略）。
            NUM为所需要保留到下一代的个体数目。
            注：这里对原版NSGA-II进行等价的修改：先按帕累托分级和拥挤距离来计算出种群个体的适应度，
            然后调用dup选择算子(详见help(ea.dup))来根据适应度从大到小的顺序选择出个体保留到下一代。
            这跟原版NSGA-II的选择方法所得的结果是完全一样的。

        """

        # 父子两代合并
        population = population + offspring
        [levels, _] = self.ndSort(population.ObjV, NUM, None, population.CV, self.problem.maxormins)  # 对NUM个个体进行非支配分层
        dis = ea.crowdis(population.ObjV, levels)  # 计算拥挤距离
        population.FitnV[:, 0] = np.argsort(np.lexsort(np.array([dis, -levels])), kind='mergesort')  # 计算适应度
        chooseFlag = ea.selecting('dup', population.FitnV, NUM)  # 调用低级选择算子dup进行基于适应度排序的选择，保留NUM个个体

        return population[chooseFlag]

    def run(self, prophetPop=None):  # prophetPop为先知种群（即包含先验知识的种群）
        # ==========================初始化配置===========================
        if self.prophetPop is not None:
            prophetPops = self.prophetPop
        else:
            prophetPops = None
        population = self.population
        NIND = population.sizes
        self.initialization()  # 初始化算法类的一些动态参数
        # ===========================准备进化============================
        population.initChrom()  # 初始化种群染色体矩阵
        # 插入先验知识（注意：这里不会对先知种群prophetPop的合法性进行检查）
        if prophetPops is not None:
            population = (prophetPops + population)[:NIND]  # 插入先知种群
        self.call_aimFunc(population)  # 计算种群的目标函数值
        [levels, _] = self.ndSort(population.ObjV, NIND, None, population.CV, self.problem.maxormins)  # 对NIND个个体进行非支配分层
        population.FitnV = (1 / levels).reshape(-1, 1)  # 直接根据levels来计算初代个体的适应度
        # ===========================开始进化============================
        while not self.terminated(population):
            # 选择个体参与进化
            # 默认
            if isinstance(self.selFunc, str):
                offspring = population[ea.selecting(self.selFunc, population.FitnV, NIND)]
            else:
                res1, res2 = self.selFunc.do(population, population.FitnV)
                if isinstance(res1, str):
                    offspring = population[ea.selecting("tour", population.FitnV, NIND)]
                else:
                    offspring = res1
            # 对选出的个体进行进化操作
            offspring.Chrom = self.recOper.do(offspring.Chrom)  # 重组
            offspring.Chrom = self.mutOper.do(offspring.Encoding, offspring.Chrom, offspring.Field)  # 变异
            self.call_aimFunc(offspring)
            population = self.reinsertion(population, offspring, NIND)  # 重插入生成新一代种群
        return self.finishing(population)  # 调用finishing完成后续工作并返回结果
