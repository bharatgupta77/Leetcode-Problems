class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        #my solution
        
        x=arr[0]
        mid_index = 0
        
        # #to check whether there is only decreasing slope
        # k = arr[:]
        # k.sort(reverse = True)
        # if (k == arr):
        #     return False
        
        
        
        for i in range(1,len(arr)):
            if x<arr[i]:
                x = arr[i]
                continue
            elif x==arr[i]:
                return False
            else:
                mid_index = i-1
                break
        
        if(mid_index == 0 or mid_index == len(arr)-1):
            return False;
        
        
                
        #after getting highest point will check the decrasing slope
        l = arr[mid_index:]
        l.sort(reverse = True)
        if (l == arr[mid_index:] and len(set(l)) == len(l)):
            return True


          #simple approach (time complexity will be more)
            
#         n = len(arr);
#         i = 0;

#         #walk up
#         while (i+1 < n and arr[i] < arr[i+1]):
#             i+=1;

#         #peak can't be first or last
#         if(i == 0 or i == n-1):
#             return False;

#         #walk down
#         while(i+1 < n and arr[i] > arr[i+1]):
#             i+=1;

#         return i == n-1;
            
            
                
            
                
            
            
        