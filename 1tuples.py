print("Tuple creation and list manipulation")
def tuples(num):
    tuple=[(n,n*n)for n in num]
    print("list of tuples (first->n,second->n_square):\n",tuple)
n=input("Enter number of elements for list:")
if n.isdigit():
    n=int(n)
    print("Enter",n,"integers:")
    nums=[int(input()) for i in range(n)]
    tuples(nums)
else:
    print("input should be non negative-integer")
