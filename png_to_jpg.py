import os
from PIL import Image

def converter_png_para_jpg_pasta(pasta_entrada, pasta_saida, qualidade=95):
    if not os.path.exists(pasta_entrada):
        print(f"Erro: A pasta de entrada '{pasta_entrada}' não foi encontrada.")
        return

    if not os.path.exists(pasta_saida):
        try:
            os.makedirs(pasta_saida)
            print(f"Pasta de saída '{pasta_saida}' criada.")
        except OSError as e:
            print(f"Erro ao criar a pasta de saída '{pasta_saida}': {e}")
            return

    arquivos_convertidos = 0
    arquivos_nao_convertidos = 0

    for nome_arquivo in os.listdir(pasta_entrada):
        if not nome_arquivo.lower().endswith(".png"):
            print(f"Ignorado: '{nome_arquivo}' não é um arquivo PNG.")
            continue

        caminho_png_completo = os.path.join(pasta_entrada, nome_arquivo)
        nome_base_arquivo = os.path.splitext(nome_arquivo)[0]
        caminho_jpg_completo = os.path.join(pasta_saida, nome_base_arquivo + ".jpg")

        try:
            img = Image.open(caminho_png_completo)

            # 1) Forçar conversão para RGBA (para garantir canal alpha, mesmo que a imagem não tenha)
            img = img.convert("RGBA")

            # 2) Criar um fundo branco em RGB
            fundo_branco = Image.new("RGB", img.size, (255, 255, 255))

            # 3) Colar a imagem RGBA sobre o fundo branco usando o canal alpha como máscara
            fundo_branco.paste(img, mask=img.split()[3])

            # Agora 'fundo_branco' é uma imagem RGB sem transparência, com áreas “transparentes” em branco
            fundo_branco.save(caminho_jpg_completo, "JPEG", quality=qualidade)
            print(f"Convertido: '{caminho_png_completo}' -> '{caminho_jpg_completo}'")
            arquivos_convertidos += 1

        except FileNotFoundError:
            print(f"Erro: Arquivo '{caminho_png_completo}' não encontrado durante a iteração.")
            arquivos_nao_convertidos += 1
        except Exception as e:
            print(f"Erro ao converter '{caminho_png_completo}': {e}")
            arquivos_nao_convertidos += 1

    print(f"\n--- Resumo da Conversão ---")
    total = arquivos_convertidos + arquivos_nao_convertidos
    print(f"Total de arquivos PNG encontrados e processados: {total}")
    print(f"Convertidos com sucesso: {arquivos_convertidos}")
    print(f"Falhas na conversão: {arquivos_nao_convertidos}")
    if arquivos_convertidos > 0:
        print(f"Arquivos JPG salvos em: '{pasta_saida}'")


if __name__ == '__main__':
    pasta_com_pngs = r"C:\Users\Dados\Desktop\SQL\Python\Conversor png to jpg"
    pasta_para_jpgs = r"C:\Users\Dados\Desktop\SQL\Python\Conversor png to jpg\convert" 

    if not os.path.exists(pasta_com_pngs):
        os.makedirs(pasta_com_pngs)
        print(f"Pasta de exemplo '{pasta_com_pngs}' criada.")
    
    # Descomente a seção abaixo para criar alguns arquivos PNG de exemplo
    # try:
    #     # Cria alguns PNGs de teste, incluindo transparências
    #     Image.new('RGBA', (80, 40), color=(255, 0, 0, 255)).save(os.path.join(pasta_com_pngs, "exemplo1.png"))
    #     Image.new('RGB', (60, 30), color='blue').save(os.path.join(pasta_com_pngs, "exemplo2.png"))
    #     Image.new('P', (100, 50), color='green').save(os.path.join(pasta_com_pngs, "exemplo3_paleta.png"))
    #     with open(os.path.join(pasta_com_pngs, "documento.txt"), "w") as f:
    #         f.write("Este não é um PNG.")
    #     print(f"Arquivos PNG de exemplo criados em '{pasta_com_pngs}'.")
    # except ImportError:
    #     print("Pillow não está instalado. Instale com: pip install Pillow")
    #     exit()
    # except Exception as e:
    #     print(f"Erro ao criar arquivos de exemplo: {e}")
    
    converter_png_para_jpg_pasta(pasta_com_pngs, pasta_para_jpgs, qualidade=90)
