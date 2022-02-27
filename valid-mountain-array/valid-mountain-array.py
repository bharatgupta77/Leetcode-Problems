class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        x=arr[0]
        mid_index = 0
        
        
        k = arr[:]
        k.sort(reverse = True)
        if (k == arr):
            return False
        
        for i in range(1,len(arr)):
            if x<arr[i]:
                x = arr[i]
                continue
            elif x==arr[i]:
                return False
            else:
                mid_index = i-1
                break
        l = arr[mid_index:]
        l.sort(reverse = True)
        if (l == arr[mid_index:] and len(set(l)) == len(l)):
            return True
            
            
                
            
                
            
            
        