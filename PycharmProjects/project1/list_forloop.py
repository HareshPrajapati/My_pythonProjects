
list = [1,2,3,4,"harry","qwer","hdugrb"]

for item in list:
    if str(item).isnumeric() and item > 1:
        print(item)