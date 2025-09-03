# computacao-grafica
trabalho de ac
## 1. Visão Computacional

A **visão computacional** abrange detecção de objetos e reconhecimento facial.

### Exemplo: Deteção de borda

```python
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('imagem.jpg', cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(img, 100, 200)

plt.imshow(edges, cmap='gray')
plt.title('Bordas Detetadas')
plt.show()

```

----------

## 2. Processamento de Imagem

O **processamento de imagem** trata da modificação ou melhoria de imagens, como filtros, transformações e ajustes.

### Exemplo: Conversão para escala de cinza e redimensionamento

```python
img_color = cv2.imread('imagem.jpg')
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
img_resized = cv2.resize(img_gray, (200, 200))

cv2.imwrite('imagem_editada.jpg', img_resized)

```

----------

## 3. Síntese de Imagem

A **síntese de imagem** refere-se à criação de imagens artificialmente

### Exemplo: Criar imagem com formas geométricas

```python
import numpy as np
import cv2

img = np.zeros((300, 300, 3), dtype=np.uint8)

cv2.circle(img, (150, 150), 50, (255, 0, 0), -1)

cv2.imwrite('sintese.png', img)

```

----------

## 4. Visualização de Imagens

### Exemplo: Mostrar imagem com Matplotlib

```python
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('imagem.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.title("Imagem RGB")
plt.axis('off')
plt.show()
