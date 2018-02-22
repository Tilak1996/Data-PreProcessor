from StatFunc import StatFunc

# arr = [0.02**3,0.04**3,0.06**3,0.08**3,0.1**3,0.12**3,0.14**3,0.16**3,0.18**3,0.2**3]
# fun = StatFunc().doubleDerivative(arr,0.02)
# print(fun)

fun = StatFunc()
arr = [1,4,8,16,32,64,128,256,512,1024,2048]
ans,x,y = fun.arburg(arr,4)
print(ans)