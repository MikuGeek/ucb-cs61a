def tree(root_label, branches = []):
    for branch in branches:
        assert is_tree(branch), "branches must be trees"
    return [root_label] + branches

def label(t):
    return t[0]

def branches(t):
    return t[1:]

def is_tree(t):
    if len(t) < 1  or type(t) != list:
        return False
    else:
        for branch in branches(t):
            if not is_tree(branch):
                return False
    return True

def is_leaf(t):
    if not branches(t):
        return True
    return False

def count_binary_leaves(t):
    if is_leaf(t):
        return 1
    branch_left, branch_right = branches(t)
    return count_binary_leaves(branch_left) + count_binary_leaves(branch_right)

def combine_leaves(t):
    if is_leaf(t):
        return label(t)
    else:
        return [combine_leaves(br) for br in branches(t)] 

def fib_tree(n):
    if n == 0:
        return tree(0)
    elif n == 1 :
        return tree(1)
    tree_n1 = fib_tree(n-1)
    tree_n2 = fib_tree(n-2)
    return tree(n, [tree_n1, tree_n2])

def partition_tree(n, m):
    if n == 0:
        return tree(True)
    if n < 0 or m == 0:
        return tree(False)
    # The label of leaves represent whether it is a way that makes partition possible.
    # Why the label of the tree is m:
    # for further using where should judge whether m is reduced or not
    return tree(m, [partition_tree(n-m, m), partition_tree(n, m-1)])

def print_partition_tree(t, partition = []):
    if is_leaf(t):
        if label(t):
            print([partition])
    else:
        with_branch, without_branch = branches(t)
        now_m = str(label(t))
        print_partition_tree(with_branch, partition + [now_m])
        print_partition_tree(without_branch, partition)
    # Use a list to store all the partition to print.
