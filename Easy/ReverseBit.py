class Solution:
    def reverse(x):
        int('{0:b}'.format(x)[::-1],2)
 
if __name__ == '__main__':
    print(Solution.reverse(x = 123))
    print(int('{0:b}'.format(123)[::-1], 2))
