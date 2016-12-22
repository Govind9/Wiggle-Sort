wiggle(arr):
  2       print arr
    3         if len(arr) == 1:
      4                 return arr
        5         m, M = 7, 9
	  6         while M > m:
	    7                 l, r = 0, len(arr) - 1
	      8                 mins = []
	        9                 maxs = []
		 10                 if arr[l] < arr[r]:
		  11                         M = arr[l]
		   12                         if arr[l + 1] > arr[r]:
		    13                                 m = arr[l + 1]
		     14                         else:
		      15                                 m = arr[r]
		       16                 else:
		        17                         M = arr[r]
			 18                         if arr[r - 1] > arr[l]:
			  19                                 m = arr[r - 1]
			   20                         else:
			    21                                 m = arr[l]
			     22                 while l <= r:
			      23                         if arr[l] < arr[r]:
			       24                                 mins.append(arr[l])
			        25                                 if arr[l] > M:
				 26                                         M = arr[l]
				  27                                 l = l + 1
				   28                         else:
				    29                                 mins.append(arr[r])
				     30                                 if arr[r] > M:
				      31                                         M = arr[r]
				       32                                 r = r - 1
				        33                         if r < l:
					 34                                 break
					  35
					   36                         if arr[l] > arr[r]:
					    37                                 maxs.append(arr[l])
					     38                                 if arr[l] < m:
					      39                                         m = arr[l]
					       40                                 l = l + 1
					        41                         else:
						 42                                 maxs.append(arr[r])
						  43                                 if arr[r] < m:
						   44                                         m = arr[r]
						    45                                 r = r - 1
						     46                 arr = mins + maxs
						      47         if len(arr) % 2 == 0:
						       48                 mid = len(arr) / 2
						else:	
							mid = (len(arr) / 2) + 1
