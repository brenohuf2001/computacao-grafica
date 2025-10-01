import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('imagem.jpg', cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(img, 100, 200)
plt.imshow(edges, cmap='gray')
plt.title('Bordas Detetadas')
plt.show()

img_color = cv2.imread('imagem.jpg')
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
img_resized = cv2.resize(img_gray, (200, 200))
cv2.imwrite('imagem_editada.jpg', img_resized)

img = np.zeros((300, 300, 3), dtype=np.uint8)
cv2.circle(img, (150, 150), 50, (255, 0, 0), -1)
cv2.imwrite('sintese.png', img)

img = cv2.imread('imagem.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title("Imagem RGB")
plt.axis('off')
plt.show()