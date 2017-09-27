#coding:utf-8
import numpy as np
import rpy2.robjects as robjects
import os
print os.environ["R_HOME"]

# 从R中导入lp.transport()
robjects.r['library']('lpSolve')
transport = robjects.r['lp.transport']

def euclid_dist(feature1, feature2):
    """计算欧氏距离"""
    if len(feature1) != len(feature2):
        print "ERROR: calc euclid_dist: %d <=> %d" % (len(feature1), len(feature2))
        return -1
    return np.sqrt(np.sum((feature1 - feature2) ** 2))

def emd(dist, w1, w2):
    """R的transport()函数用来计算EMD"""
    # transport()的参数
    costs = robjects.r['matrix'](robjects.FloatVector(dist),
                                 nrow=len(w1), ncol=len(w2),
                                 byrow=True)
    row_signs = ["<"] * len(w1)
    row_rhs = robjects.FloatVector(w1)
    col_signs = [">"] * len(w2)
    col_rhs = robjects.FloatVector(w2)

    t = transport(costs, "min", row_signs, row_rhs, col_signs, col_rhs)
    flow = t.rx2('solution')

    dist = dist.reshape(len(w1), len(w2))
    flow = np.array(flow)
    work = np.sum(flow * dist)
    emd = work / np.sum(flow)
    return emd

if __name__ == "__main__":
    f1 = np.array([ [100, 40, 22], [211, 20, 2], [32, 190, 150], [2, 100, 100] ])
    f2 = np.array([ [0, 0, 0], [50, 100, 80], [255, 255, 255] ])

    # 权重一定要整数
    w1 = np.array([4, 3, 2, 1])
    w2 = np.array([5, 3, 2])

    n1 = len(f1)
    n2 = len(f2)

    # 创建一个距离矩阵
    dist = np.zeros(n1 * n2)
    for i in range(n1):
        for j in range(n2):
            dist[i * n2 + j] = euclid_dist(f1[i], f2[j])

    # 由权重和距离矩阵得到EMD
    print "emd =", emd(dist, w1, w2)
