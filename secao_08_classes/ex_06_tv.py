class Televisao:

    def __init__(self, canal=3, volume=2):
        self.canal = canal
        self.volume = volume

    def mudar_canal(self, valor):
        try:
            valor = int(valor)
        except ValueError:
            if valor == '+':
                if self.canal == 20:
                    raise ValueError
                self.canal += 1
            elif valor == '-':
                if self.canal == 1:
                    raise ValueError
                else:
                    self.canal -= 1
            else:
                print('Valor inválido.')
        else:
            if valor in range(1, 20):
                self.canal = valor
            else:
                raise ValueError
        return self.canal

    def mudar_volume(self, valor):
        if valor == '+':
            if self.volume == 10:
                raise ValueError
            self.volume += 1
        elif valor == '-':
            if self.volume == 0:
                raise ValueError
            else:
                self.volume -= 1

        return self.volume


if __name__ == '__main__':
    televisao = Televisao()
    print(televisao)
    try:
        televisao.mudar_volume('+')
    except ValueError:
        print('Este canal não existe.')
    print(televisao.__dict__)
    while True:
        try:
            televisao.mudar_volume('-')
        except ValueError:
            print('Este canal não existe.')
            break
        else:
            print(televisao.__dict__)

    try:
        televisao.mudar_canal(5)
    except:
        print('Deu errado')
    else:
        print(f'O canal agora é {televisao.canal}')
    try:
        televisao.mudar_canal(21)
    except ValueError:
        print('Canal não existe')
    except:
        print('Deu outro trem ai')
    else:
        print(f'O canal agora é {televisao.canal}')
    try:
        televisao.mudar_canal('-')
    except ValueError:
        print('Canal não existe')
    except:
        print('Deu outro trem ai')
    else:
        print(f'O canal agora é {televisao.canal}')

