from models.restaurante import Restaurante

restaurante_praca = Restaurante('praca', 'Gourmet')
# restaurante_mexicano = Restaurante('Maxican Food', 'Mexicano')
# restaurante_japones = Restaurante('japa', 'Japonesa')

restaurante_praca.receber_avalicao('Gui', 4)
restaurante_praca.receber_avalicao('Lais', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()