import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import matplotlib.patches as ptch

#2 вида блужданий (равнлм и гаус), сделать с 1 млн частиц
#использовать новый рандом

#размер как зависит
x = [0, 0]
x2 = [0, 0]
maxim = 3
rng = np.random.default_rng(42)
child_rngs = rng.spawn(2)

fig, ax = plt.subplots(1,2)

dot = ptch.Circle((x), radius=5)
ax[0].add_patch(dot)
ax[0].set_aspect("equal")
ax[0].set_xlim(-maxim*100,maxim*100)
ax[0].set_ylim(-maxim*100,maxim*100)

dot2 = ptch.Circle((x2), radius=5)
ax[1].add_patch(dot2)
ax[1].set_aspect("equal")
ax[1].set_xlim(-maxim*100,maxim*100)
ax[1].set_ylim(-maxim*100,maxim*100)

def animate(i):
    global x, y, x2, y2
    x = x + rng.random(2)*2*maxim-maxim
    x2 = x2 + rng.standard_normal(2)

    dot2.set_center((x2))
    dot.set_center((x))
    return dot, dot2



ani = animation.FuncAnimation(
    fig, animate, cache_frame_data=False, interval=10)
plt.show()

