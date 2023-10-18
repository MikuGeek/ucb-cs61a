def tree(root_label, branches = []):
    for branch in branches:
        assert is_tree(branch), "branches must be trees"
    return [root_label] + branches

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if len(tree) < 1  or type(tree) != list:
        return False
    else:
        for branch in branches(tree):
            if not is_tree(branch):
                return False
    return True

def is_leaf(tree):
    if not is_tree(tree):
        return False
    if not len(tree) == 1:
        return False
    return True

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    branch_left, branch_right = branches(tree)
    return count_leaves(branch_left) + count_leaves(branch_right)

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

def print_partition_tree(tree, partition = []):
    if is_leaf(tree):
        if label(tree):
            print([partition])
    else:
        with_branch, without_branch = branches(tree)
        now_m = str(label(tree))
        print_partition_tree(with_branch, partition + [now_m])
        print_partition_tree(without_branch, partition)
    # Use a list to store all the partition to print.
