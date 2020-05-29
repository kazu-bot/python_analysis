#arrayの計算
import numpy as np

arr1 = np.array(([1,2,3,4],[8,9,10,11]))
print(arr1)
print('**********a****')
print(arr1 * arr1)
print('**************')
print(arr1 - arr1)
print('**************')
print(1 /arr1)
print('**************')
print(arr1 ** 3)
print('array計算終了')

#arrayの添字
arr2 = np.arange(0,11)
print(arr2)
print('**************')
print(arr2[8])
print('**************')
print(arr2[1:5])
print('**************')
slice_arr = arr2[0:5]
print(slice_arr)
print('**************')
#sliceを使用すると参照渡しなので元の配列の値も書き換わる
slice_arr[:] = 99
print(slice_arr)
print(arr2)
print('**************')
#値で使用するためにはcopyをしてから操作してやる必要あり。
arr_copy = arr2.copy()
print(arr_copy)
arr_copy[:] = 50
print('**************')
print(arr_copy)
print(arr2)
print('**************')
arr2d = np.zeros((10,10))
print(arr2d)
print('**************')
#arrayの長さ
arr_length = arr2d.shape[1]
for i in range(arr_length):
    arr2d[i] = i
print(arr2d)
print('**************')
print(arr2d[[2,4,6,8]])
print('**************')

#行と列の入れ替え
arr3 = np.arange(9).reshape(3,3)
print(arr3)
print('**************')
#行と列の入れ替え
print(arr3.T)
print('**************')
print(arr3.transpose(0,1))
print(arr3.transpose(1,0))
print(arr3.swapaxes(0,1))

