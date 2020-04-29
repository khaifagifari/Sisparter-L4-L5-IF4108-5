# import mpi4py
from mpi4py import MPI

# import library random untuk generate angka integer secara random
import random as rd

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# generate angka integer secara random untuk setiap proses
number = rd.randint(10,100)
print("rank %d%d mempunyai nilai %d" %(rank,size,number))

# lakukam penjumlahan dengan teknik reduce, root reduce adalah proses dengan rank 0
sum = comm.reduce(number, op=MPI.SUM, root=0)

# jika saya proses dengan rank 0 maka saya akan menampilkan hasilnya
if rank== 0:
    print("rank 0 mempunyai jumlah, jumlahnya adalah %d" %sum)

