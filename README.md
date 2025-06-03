# Conversor de Imagens PNG para JPG com Fundo Branco

Este script em Python converte arquivos PNG para JPG, garantindo que imagens com fundo transparente sejam salvas com **fundo branco**, evitando o problema comum de transparências virarem fundo preto em imagens JPEG.

## 🧾 O que o script faz

- Lê todos os arquivos `.png` de uma pasta especificada.
- Converte cada imagem PNG para o formato JPG.
- Para imagens com transparência, aplica um **fundo branco** automaticamente.
- Salva os arquivos convertidos em uma pasta de saída.
- Gera um resumo ao final indicando quantos arquivos foram processados com sucesso ou falharam.

---

## 📁 Estrutura de Pastas

```text
imagens/
├── images 03-06-2025/
│   ├── exemplo1.png
│   ├── exemplo2.png
│   ├── exemplo3_paleta.png
│   ├── documento.txt         # (ignorado pelo script)
│   └── convert/              # Arquivos JPG convertidos são salvos aqui
```

---

## ▶️ Como executar

1. **Pré-requisitos**: você precisa ter o Python instalado com a biblioteca [`Pillow`](https://pillow.readthedocs.io/).

   Para instalar a biblioteca:

   ```bash
   pip install pillow
   ```

2. **Edite os caminhos** dentro do bloco `if __name__ == '__main__':` conforme necessário:

   ```python
   pasta_com_pngs = r"C:\caminho\para\sua\pasta\com\pngs"
   pasta_para_jpgs = r"C:\caminho\para\pasta\de\saida"
   ```

3. **Execute o script:**

   No terminal ou prompt de comando:

   ```bash
   python nome_do_script.py
   ```

---

## ⚙️ Parâmetros personalizáveis

- **`pasta_entrada`**: Caminho da pasta onde estão os arquivos PNG.
- **`pasta_saida`**: Caminho onde os arquivos JPG convertidos serão salvos.
- **`qualidade`**: Qualidade da imagem JPG gerada (padrão: `95`, intervalo de 1 a 100).

---

## 🧪 Testes incluídos

O script contém um bloco comentado que permite gerar automaticamente imagens de teste e um arquivo `.txt`, apenas para demonstração.

Como ativar os testes
Se quiser testar o funcionamento sem precisar importar imagens manualmente:

- Vá até o final do script no bloco:
```python
if __name__ == '__main__':
```
- Descomente a seção indicada no código, como mostrado abaixo:
```python
# Descomente a seção abaixo para criar alguns arquivos PNG de exemplo
# try:
#     # Cria alguns PNGs de teste, incluindo transparências
#     Image.new('RGBA', (80, 40), color=(255, 0, 0, 255)).save(...))
#     ...
# except Exception as e:
#     print(f"Erro ao criar arquivos de exemplo: {e}")
```
Isso criará:

- 3 imagens .png com diferentes modos de cor
- 1 arquivo .txt (para verificar que arquivos não-PNG são ignorados)
---

## ❗Observações

- Apenas arquivos `.png` são processados — os demais são ignorados.
- O fundo branco é aplicado de forma consistente mesmo em imagens que não têm canal alpha declarado.
- O script trata exceções e informa possíveis erros de leitura, escrita ou conversão.

---

## 📜 Licença

Este projeto é de uso livre para fins pessoais e comerciais. Créditos ao autor são apreciados, mas não obrigatórios.
