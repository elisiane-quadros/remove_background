# Background Remover com Segment Anything

Este projeto aplica a tecnologia de segmentação automática da Meta AI (Segment Anything) para **remover o fundo de imagens** de forma inteligente. Foi desenvolvido com o objetivo de experimentar e compreender o comportamento do modelo em situações reais, especialmente em imagens com características variadas de luz, contraste, cor e fundo.

## Objetivo

Desenvolver uma aplicação simples que permite:

- Carregar uma imagem.
- Aplicar o modelo Segment Anything.
- Remover o fundo automaticamente com base na máscara gerada.
- Salvar o resultado final com fundo transparente.

## Ferramentas Utilizadas

- **Python 3.10**
- **Segment Anything (Meta AI)**: modelo pré-treinado para segmentação automática.
- **OpenCV (cv2)**: leitura, manipulação e escrita das imagens.
- **PyTorch**: framework base para carregamento e execução do modelo.
- **Matplotlib**: visualização intermediária dos resultados.
- **PIL (Pillow)**: manipulação da imagem final com transparência.

## Como usar

1. Instale os requisitos:

   ```bash
   pip install -r requirements.txt
   ```

2. Execute o script principal:

   ```bash
   python main.py
   ```

3. O resultado será salvo na pasta `treated_images/` com fundo transparente.

## Análise Experimental

Para testar o comportamento do modelo, selecionei 4 imagens cuidadosamente, com diferentes características de iluminação, contraste e complexidade de fundo:

1. **Imagem 1 — Arara colorida com fundo desfocado e claro**  
   Resultado excelente. O modelo conseguiu contornar com precisão as cores vibrantes da arara, e removeu completamente o fundo. Foi a melhor performance entre os testes.

2. **Imagem 2 — Casal com roupas em tons pastéis, fundo claro e planta ao lado**  
   Resultado bom. As áreas com cores sólidas foram bem segmentadas, mas as regiões em que as cores da roupa se misturavam ao fundo geraram alguns borrões. Ainda assim, aceitável.

3. **Imagem 3 — Relógio de bolso antigo, fundo escuro com tons semelhantes ao objeto**  
   Resultado insatisfatório. O modelo confundiu partes do relógio com o fundo, removendo trechos importantes da imagem. Isso se deu pela baixa diferença de cor e textura.

4. **Imagem 4 — Imagem  de um casal mostando somente as pernas com All Star no meio da floresta (fundo muito detalhado)**  
   Resultado insatisfatório. Devido à grande quantidade de folhas e variação no fundo, a máscara gerada foi inconsistente, resultando em falhas visuais perceptíveis no objeto principal.

### Conclusões

- O modelo tem **excelente desempenho com objetos bem definidos**, cores vibrantes e contraste claro com o fundo.
- Em **cenários com fundos complexos** ou **baixa distinção de cor**, a qualidade da segmentação diminui.
- A aplicação é eficaz para uso geral, mas **não substitui completamente edições manuais** em imagens mais desafiadoras.

Desenvolvido por **Elisiane Quadros**
[LinkedIn](https://www.linkedin.com/in/elisiane-quadros/) • © 2025

Este projeto está licenciado sob a [MIT License](LICENSE).
