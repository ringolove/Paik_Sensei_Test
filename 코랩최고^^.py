t = int(input())

for i in range(t):
  c = list(map(int, input().split()))
  avg = sum(c[1:])/c[0]
  cnt = 0
  for i in c[1:]:
    if i > avg:
        cnt += 1

  print(f'{cnt/c[0]*100:.3f}%')
