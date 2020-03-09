arr1 =[1,2,3]
arr2 =[]

for i in arr1:
    arr2.append(i * 2)

print(arr2)

arr1 =[1,2,3]
arr2 = list(map(lambda arr1 : arr1 * 2, arr1))

print(arr2)

birthYear =[1975,1997, 2002, 1995, 1985]

ages= list(map(lambda birthYear: 2018-birthYear, birthYear))

print(ages)

birthYear =[1975,1997, 2002, 1995, 1985]
ages =[]

for i in birthYear:
    ages.append(2018 - birthYear)

print(ages)



