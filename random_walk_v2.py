import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import matplotlib.patches as ptch


#размер как зависит
rng = np.random.default_rng(42)
maxim = 3
n = 1000
time = 1000
tim = np.arange(0, time, 1)

random = rng.random((n, time, 2))*2*maxim-maxim
random2 =  rng.normal(scale=maxim*np.sqrt(1/3), size=(n, time, 2))
x = np.cumsum(random, 1)
x2 = np.cumsum(random2, 1)
rad1 = np.zeros(time)
rad2 = np.zeros(time)

fig, ax = plt.subplots(3)
sc1 = ax[0].scatter(x[:, 0, 0], x[:, 0, 1], alpha=0.1)
ax[0].set_aspect("equal")
ax[0].set_xlim(-maxim*100,maxim*100)
ax[0].set_ylim(-maxim*100,maxim*100)

sc2 = ax[1].scatter(x2[:, 0, 0], x2[:, 0, 1], alpha=0.1)
ax[1].set_aspect("equal")
ax[1].set_xlim(-maxim*100,maxim*100)
ax[1].set_ylim(-maxim*100,maxim*100)

rad1 = x*x
rad2 = x2*x2
rad1 = np.cumsum(rad1, axis=2)[:,:,1]
rad2 = np.cumsum(rad2, axis=2)[:,:,1]
rad1 = np.cumsum(rad1, axis=0)[-1]
rad2 = np.cumsum(rad2, axis=0)[-1]
rad1 = np.sqrt(rad1/n)
rad2 = np.sqrt(rad2/n)
print(rad1)

graph, = ax[2].plot(tim, rad1)
graph2, = ax[2].plot(tim, rad2)
ax[2].set_xscale('log')
ax[2].set_yscale('log')

def animate(i):
    sc1.set_offsets(x[:, i, :])
    sc2.set_offsets(x2[:, i, :])
    return sc1, sc2

ani = animation.FuncAnimation(
    fig, animate, cache_frame_data=False, interval=10, frames=time)
plt.show()

