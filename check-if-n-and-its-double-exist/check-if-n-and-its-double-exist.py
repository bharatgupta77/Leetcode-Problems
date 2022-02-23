class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        l =[]
        for i in arr:
            if(i==0 and arr.count(i)==1):
                continue
            if(i%2==0):
                l.append(i//2)
            l.append(i*2)
            
        s = set(l)
        print(s)
        k = set(arr)
        
        if len(s.intersection(k)) ==  0 :
            return False
        else:
            return True
            
        
        
            
        
        
        
        
        # for i in range(0,len(arr)):
        #     for j in range(i+1,len(arr)):
        #         if(arr[i] == 2*arr[j]) or (arr[i] == arr[j]/2):
        #             return True
        # return False