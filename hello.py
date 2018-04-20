import kivy
from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.colorpicker import ColorPicker
from kivy.graphics import Color, Ellipse, Triangle
from kivy.properties import StringProperty, ObjectProperty

class Titulo(Label):
  cadena=StringProperty("Jesus te ama...")
  triangle=ObjectProperty(None)

  def __init__(self, **kwargs):
    super(Titulo, self).__init__(**kwargs)
    with self.canvas:
      self.triangle=Triangle(points= [40, 40, 200, 200, 160, 40])

  def on_touch_down(self, touch):
    if self.collide_point(*touch.pos):
      self.cadena="Collide: "+str(touch.pos)
      print("on_touch_down-->Collide")
      return True
    return super(Titulo, self).on_touch_down(touch)

  def on_cadena(self, obj, pos):
    print("Se ha actualizado 'Cadena'")

  def on_triangle(self, obj, pos):
    print("Se ha actualizado 'triangle'")

class SaludoApp(App):
  def build(self):
    self.paleta=ColorPicker()
    self.pintor=Titulo()
    self.pintor.bind(on_touch_down=self.dentro)
    return self.pintor

  def dentro(self, obj, st):
    lista=self.pintor.triangle.points
    tu=st.x, st.y
    rpta = True
    py=lista[-1]
    px=lista[-2]
    for i in range(0, len(lista), 2):
      px0=px
      py0=py
      px=lista[i]
      py=lista[i+1]
      a=px - px0
      b=py - py0
      c=tu[0] - px0
      d=tu[1] - py0
      if (b*c - a*d) < 0:
        rpta = False
        print(rpta)
        break
    if rpta == True:
      self.pintor.add_widget(self.paleta)

    return rpta

  def eleccion(self, obj, st):
    print("Pos X: %g, Pos Y: %g" %(st.x, st.y))
    ca,cb,cc = .5, .5, .6
    a,b = 150,45
    radio = 50
    with self.pintor.canvas:
        Color(ca, cb, cc, mode = 'hsv' )
        Triangle(
            points = [0, 0, 100, 100, 80, 20])

if __name__ in ["__main__", "__android__"]:
  SaludoApp().run()
