import numpy as np
import matplotlib.pyplot as plt

def plot_shapes(original_shape, transformed_shape, title):
    plt.figure()
    if len(original_shape) == 1:
        plt.scatter(*original_shape[0], label="Original", color="blue")
        plt.scatter(*transformed_shape[0], label="Transformado", color="red", marker="x")
    else:
        plt.plot(*zip(*original_shape, original_shape[0]), label="Original")
        plt.plot(*zip(*transformed_shape, transformed_shape[0]), label="Transformado", linestyle="--")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def translacao(dx, dy):
    return np.array([[1, 0, dx],
                     [0, 1, dy],
                     [0, 0, 1]])

def escala(sx, sy):
    return np.array([[sx, 0, 0],
                     [0, sy, 0],
                     [0, 0, 1]])

def rotacao(angulo_graus):
    ang = np.deg2rad(angulo_graus)
    return np.array([[np.cos(ang), -np.sin(ang), 0],
                     [np.sin(ang),  np.cos(ang), 0],
                     [0, 0, 1]])

def reflexao_x():
    return np.array([[1, 0, 0],
                     [0, -1, 0],
                     [0, 0, 1]])

def reflexao_y():
    return np.array([[-1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]])

def cisalhamento(kx=0, ky=0):
    return np.array([[1, kx, 0],
                     [ky, 1, 0],
                     [0, 0, 1]])

def aplicar_transformacao(pontos, matriz):
    pontos_hom = np.hstack([pontos, np.ones((pontos.shape[0], 1))])
    transf = (matriz @ pontos_hom.T).T
    return transf[:, :2]

P = np.array([[2, 3]])
P_trans = aplicar_transformacao(P, translacao(4, -2))
print("Novo ponto após translação:", P_trans)
plot_shapes(P, P_trans, "Translação Simples")

triangulo = np.array([[1, 1], [3, 1], [2, 4]])
triangulo_escala = aplicar_transformacao(triangulo, escala(2, 2))
print("Triângulo após escala uniforme:", triangulo_escala)
plot_shapes(triangulo, triangulo_escala, "Escala Uniforme")

triangulo_escala_nao = aplicar_transformacao(triangulo, escala(2, 0.5))
print("Triângulo após escala não uniforme:", triangulo_escala_nao)
plot_shapes(triangulo, triangulo_escala_nao, "Escala Não Uniforme")

P_rot = np.array([[1, 0]])
P_rotado = aplicar_transformacao(P_rot, rotacao(90))
print("Ponto após rotação de 90°:", P_rotado)
plot_shapes(P_rot, P_rotado, "Rotação de 90°")

quadrado = np.array([[1, 1], [1, 4], [4, 4], [4, 1]])
centro = np.mean(quadrado, axis=0)
M = translacao(-centro[0], -centro[1]) @ rotacao(-45) @ translacao(centro[0], centro[1])
quadrado_rot = aplicar_transformacao(quadrado, M)
print("Quadrado após rotação -45°:", quadrado_rot)
plot_shapes(quadrado, quadrado_rot, "Rotação de Quadrado (-45°)")

P_reflexao = np.array([[2, 5]])
P_reflexao_trans = aplicar_transformacao(P_reflexao, reflexao_y())
print("Reflexão em relação ao eixo Y:", P_reflexao_trans)
plot_shapes(P_reflexao, P_reflexao_trans, "Reflexão no eixo Y")

tri_reflexao = np.array([[2, 3], [4, 3], [3, 5]])
tri_reflexao_trans = aplicar_transformacao(tri_reflexao, reflexao_x())
print("Triângulo após reflexão no eixo X:", tri_reflexao_trans)
plot_shapes(tri_reflexao, tri_reflexao_trans, "Reflexão no eixo X")

P_cisal = np.array([[2, 3]])
P_cisal_trans = aplicar_transformacao(P_cisal, cisalhamento(kx=2))
print("Cisalhamento horizontal:", P_cisal_trans)
plot_shapes(P_cisal, P_cisal_trans, "Cisalhamento Horizontal")

P_comp = np.array([[3, 2]])
M_comp = escala(2, 2) @ rotacao(90) @ translacao(1, -1)
P_comp_trans = aplicar_transformacao(P_comp, M_comp)
print("Ponto após composição de transformações:", P_comp_trans)
plot_shapes(P_comp, P_comp_trans, "Composição de Transformações")

retangulo = np.array([[1, 1], [5, 1], [5, 3], [1, 3]])
M_ret = reflexao_y() @ escala(1.5, 0.5) @ translacao(-2, 3)
retangulo_trans = aplicar_transformacao(retangulo, M_ret)
print("Retângulo após várias transformações:", retangulo_trans)
plot_shapes(retangulo, retangulo_trans, "Transformações no Retângulo")
