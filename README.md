# Background Remover com Segment Anything(SAM)

Este projeto demonstra a aplicação do Segment Anything Model (SAM) da Meta AI para remoção automática de fundo de imagens. O objetivo foi explorar o comportamento do SAM em diferentes cenários visuais, avaliando sua eficácia e limitações em situações reais de contraste, cor e complexidade de fundo.

## Objetivo

Desenvolver uma aplicação em Python que demonstre a capacidade do SAM na segmentação de imagens para remoção de fundo, permitindo:

- Carregar uma imagem de entrada.
- Aplicar o modelo Segment Anything para gerar máscaras de segmentação.
- Utilizar as máscaras para remover o fundo da imagem.
- Salvar a imagem resultante com fundo transparente (formato PNG).

## Ferramentas Utilizadas

- **Python 3.11**
- **Segment Anything (Meta AI)**: modelo pré-treinado para segmentação automática.
- **OpenCV (cv2)**: Utilizado para leitura, manipulação de pixels e escrita de imagens.
- **PyTorch**: Framework fundamental para o carregamento do modelo SAM e execução de inferência.
- **Matplotlib**: Para visualização intermediária e depuração das máscaras geradas.
- **PIL (Pillow)**: Essencial para manipulação de imagens, especialmente para aplicar a transparência (canal RGBA) no resultado final.

## Como usar

1. Instale os requisitos:

   ```bash
   pip install -r requirements.txt
   ```

2. Execute o script principal:

   ```bash
   python main.py
   ```

3. Os resultados processados, com o fundo removido e transparência aplicada, serão salvos na pasta treated_images/.

## Análise Experimental

Para testar o comportamento do modelo, selecionei 4 imagens cuidadosamente, com diferentes características de iluminação, contraste e complexidade de fundo:

1. **Imagem 1 — Arara colorida com fundo desfocado e claro**
   Resultado excelente. O modelo conseguiu contornar com precisão as cores vibrantes da arara, e removeu completamente o fundo. Foi a melhor performance entre os testes. Há uma clara distinção cromática. As cores da arara são muito diferentes das cores predominantes no fundo, o que permite que os algoritmos de segmentação de imagem (baseados em cor e intensidade de pixel) identifiquem facilmente os limites do objeto.

2. **Imagem 2 — Casal com roupas em tons pastéis, fundo claro e planta ao lado**  
   Resultado: A remoção foi majoritariamente bem-sucedida, especialmente onde havia contraste cromático sólido (e.g., a cor da blusa do homem vs. o fundo). No entanto, como previsto, em áreas onde os tons de pele ou das roupas claras se aproximavam dos tons do fundo (cortinas/parede), o recorte apresentou pequenas imperfeições ou "borrões". Isso demonstra a sensibilidade dos algoritmos à similaridade de pixels em regiões de transição.

3. **Imagem 3 — Relógio de bolso antigo, fundo escuro com tons semelhantes ao objeto**  
   Resultado: Desempenho insatisfatório. O modelo demonstrou dificuldade significativa, removendo partes importantes do relógio onde a distinção de cor e luminosidade era baixa, resultando em uma imagem final "falhada" ou com buracos. Este caso ilustra o desafio imposto pela baixa distinção cromática e de luminosidade em conjunto com a alta complexidade textural tanto do objeto (ornamentos, corrente) quanto do fundo.

4. **Imagem 4 — Pernas com Tênis em Floresta (fundo muito detalhado)**  
   Resultado: Fraco a máscara gerada foi inconsistente e apresentou falhas visuais perceptíveis, com partes do fundo sendo erroneamente incluídas no objeto e vice-versa. Este é o cenário mais desafiador, a baixa distinção cromática entre o objeto e o fundo, somada à alta granularidade e complexidade do fundo (texturas irregulares, múltiplos pequenos elementos), sobrecarrega o algoritmo.

### Conclusões

- O modelo tem **excelente desempenho com objetos bem definidos**, cores vibrantes e contraste claro com o fundo.
- Em **cenários com fundos complexos** ou **baixa distinção de cor**, a qualidade da segmentação diminui.
- A aplicação é eficaz para uso geral, mas **não substitui completamente edições manuais** em imagens mais detalhadas e desafiadoras.

Desenvolvido por **Elisiane Quadros**
[LinkedIn](https://www.linkedin.com/in/elisiane-quadros/) • © 2025

Este projeto está licenciado sob a [MIT License](LICENSE).
