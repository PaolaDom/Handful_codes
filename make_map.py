import numpy as np
import h5py
import matplotlib.pyplot as plt
plt.switch_backend('agg')

folder2read=#put your path here
folder2print=#put your path here
conv_clust='8mdmd001R'

file1=folder2read+conv_clust+'_v_015'
file2=folder2read+conv_clust+'_b_015'
file3=folder2read+conv_clust+'_dt_015'

f = h5py.File(file1, 'r')	#Reading your hdf5 file

print(list(f.keys()))		#Available fields in the hdf5 file

vx = f['x-velocity']		#Define your variables as arrays
vy = f['y-velocity']
vz = f['z-velocity']

print(vx.shape)

v = np.ndarray(vx.shape)
v[:,:,:] = np.sqrt(vx[:,:,:]**2 + vy[:,:,:]**2 + vz[:,:,:]**2)

#For a slice just indicate the limits on your array
#nx,ny,nz=vx.shape[0]/2,vx.shape[1]/2,vx.shape[2]/2
#v=np.ndarray(shape=(nx,ny,nz))
#v[:,:,:] = np.sqrt(vx[0:nx,0:ny,0:nz]**2 + vy[0:nx,0:ny,0:nz]**2 + vz[0:nx,0:ny,0:nz]**2)

print(v.shape)

#Making a map (x-projection)
map_x = v.sum(0)

print(map_x.shape)

#Making the plot
cmap1 = 'viridis'
fig, ax = plt.subplots(figsize=(9,9))

ax.imshow(map_x, cmap=cmap1, origin='lower')

fileout = folder2print + 'Map_test.png'
print('Saving image ->',fileout)
plt.savefig(fileout,bbox_inches='tight')

f.close()
