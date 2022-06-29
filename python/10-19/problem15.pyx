import time
from libc.stdlib cimport malloc, free

cdef route_num(short cube_size):
   cdef unsigned long *L = <unsigned long *>malloc((cube_size + 1) * sizeof(unsigned long))
   cdef short j,i = 0
   while i <= cube_size:
       L[i] = 1
       i += 1
   i = 1
   while i <= cube_size:
       j = 1
       while j < i:
           L[j] = L[j]+L[j-1]
           j += 1
       L[i] = 2 * L[i - 1]
       i += 1
   cdef unsigned long c = L[cube_size]
   free(L)
   return c

start = time.time()
cdef unsigned long n = route_num(20)
elapsed = (time.time() - start)
print "%s found in %s seconds" % (n,elapsed)
