import taichi as ti
ti.init()
res = (800, 600)
x = ti.Vector.field(3, ti.uint8, shape=res)

def main():
    # x.from_numpy(ti.tools.imread('png.png'))
    x.from_numpy(ti.tools.imread('jpg.jpg'))
    gui = ti.GUI('load_img', res)
    while gui.running:
        gui.set_image(x)
        gui.show()

if __name__ == '__main__':
    main()
