# for (int i = N; i > 0; i--){
#       int a = 0;
#       while(a < N){
#           print(a)
#           a++;
#       }
# }     O(N*N) => O(n**2)

# for (int num = 1; num < A; num++){ -- 3
#     for(int j = A; j >=1; j--){ -- 2
#           print(j)
#     }
#     int i = B;
#     while(i > 0){ -- 1
#           print(i)
#           i++;
#     }
# }    O((B + A) * A) => O(A**2 + AB)

start = 3
while start >= 0:
    print(start)
    start -= 1

print('---------------')


def counter(num):
    print(num)
    if num > 0:
        counter(num - 1)


counter(3)
