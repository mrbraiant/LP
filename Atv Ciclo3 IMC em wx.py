# -*- codin:latin1 -*-

import wx

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, size=(250, 200))

        nomeBox = wx.TextEntryDialog(None, 'Digite seu Nome?', 'Cálculo do IMC - Índice de Massa Corporal', 'Seu Nome')
        if nomeBox.ShowModal() == wx.ID_OK:
            nome = nomeBox.GetValue()

        enderecoBox = wx.TextEntryDialog(None, 'Digite seu Endereço?', 'Cálculo do IMC - Índice de Massa Corporal', 'Seu Endereço')
        if enderecoBox.ShowModal() == wx.ID_OK:
            endereco = enderecoBox.GetValue()

        alturaBox = wx.TextEntryDialog(None, 'Digite sua Altura separada por PONTO:', 'Cálculo do IMC - Índice de Massa Corporal', 'Sua Altura')
        if alturaBox.ShowModal() == wx.ID_OK:
            altura = float(alturaBox.GetValue())
            a2 = float(altura*altura)

        pesoBox = wx.TextEntryDialog(None, 'Digite seu peso?','Cálculo do IMC - Índice de Massa Corporal', 'Seu Peso')
        if pesoBox.ShowModal() == wx.ID_OK:
            peso = int(pesoBox.GetValue())

        IMC = float(peso/a2)
        print(IMC)

        resultado = wx.MessageDialog(None, 'Nome do Paciente: %s\nEndereço Completo: %s'
                                           '\nAltura: %.2fm\nPeso: %dKg\n\nSeu IMC é: %.2f'
                                           '\n\nObrigado!\n:D'%(nome,endereco,altura,peso,IMC),
                                            'Cálculo do IMC - Índice de Massa Corporal')
        if resultado.ShowModal() == wx.ID_OK:
            self.Destroy()
        self.Show(True)

app = wx.App()
frame = Frame()
app.MainLoop()
