from big_ol_pile_of_manim_imports import *

COLOR_P="#3EFC24"

class ColorTexto(Scene): 
    def construct(self): 
        texto = TextMobject("A","B","C","D","E","F")
        texto[0].set_color(RED)
        texto[1].set_color(BLUE)
        texto[2].set_color(GREEN)
        texto[3].set_color(ORANGE)
        texto[4].set_color("#DC28E2") #Los colores son hexadecimales
        texto[5].set_color(COLOR_P)
        self.play(Write(texto))
        self.wait(3)

class FormulaColor1(Scene): 
    def construct(self):¿
        texto = TexMobject("x","=","{a","\\over","b}")
        texto[0].set_color(RED)
        texto[1].set_color(BLUE)
        texto[2].set_color(GREEN)
        texto[3].set_color(ORANGE)
        texto[4].set_color("#DC28E2")
        self.play(Write(texto))
        self.wait(3)

class FormulaColor2(Scene): 
    def construct(self): 
        texto = TexMobject("x","=","\\frac{a}{b}")
        texto[0].set_color(RED)
        texto[1].set_color(BLUE)
        texto[2].set_color(GREEN)
        self.play(Write(texto))
        self.wait(3)

class FormulaColor3(Scene): 
    def construct(self):
        texto = TexMobject("\\sqrt{","\\int_{","a}^","{b}","\\left(","\\frac{x}{y}","\\right)","dx}")
        texto[0].set_color(RED)
        texto[1].set_color(BLUE)
        texto[2].set_color(GREEN)
        texto[3].set_color(YELLOW)
        texto[4].set_color(PINK)
        texto[5].set_color(ORANGE)
        texto[6].set_color(PURPLE)
        texto[7].set_color(MAROON)
        self.play(Write(texto))
        self.wait(3)

class FormulaColor3Mejorada(Scene): 
    def construct(self): 
        texto = TexMobject("\\sqrt{","\\int_{","a}^","{b}","\\left(","\\frac{x}{y}","\\right)","dx.}")
        texto[0].set_color(RED)
        texto[1].set_color(BLUE)
        texto[2].set_color(GREEN)
        texto[3].set_color(YELLOW)
        texto[4].set_color(PINK)
        texto[5].set_color(ORANGE)
        texto[6].set_color(PURPLE)
        texto[7].set_color(MAROON)
        self.play(Write(texto))
        self.wait(3)

class FormulaColor3Mejorada2(Scene): 
    def construct(self): 
        texto = TexMobject("\\sqrt{","\\int_","{a}^","{b}","{\\left(","{x","\\over","y}","\\right)}","d","x",".}")
        texto[0].set_color(RED)
        texto[1].set_color(BLUE)
        texto[2].set_color(GREEN)
        texto[3].set_color(YELLOW)
        texto[4].set_color(PINK)
        texto[5].set_color(ORANGE)
        texto[6].set_color(PURPLE)
        texto[7].set_color(MAROON)
        texto[8].set_color(TEAL)
        texto[9].set_color(GOLD)
        self.play(Write(texto))
        self.wait(3)

class FormulaColor4(Scene): 
    def construct(self): 
        texto = TexMobject("\\sqrt{","\\int_","{a","+","c}^","{b}","{\\left(","{x","\\over","y}","\\right)}","d","x",".}")
        texto[0].set_color(RED)
        texto[1].set_color(BLUE)
        texto[2].set_color(GREEN)
        texto[3].set_color(YELLOW)
        texto[4].set_color(PINK)
        texto[5].set_color(ORANGE)
        texto[6].set_color(PURPLE)
        texto[7].set_color(MAROON)
        texto[8].set_color(TEAL)
        texto[9].set_color(GOLD)
        texto[10].set_color(GRAY)
        texto[11].set_color(RED)
        self.play(Write(texto))
        self.wait(3)

class ColorPorCaracter1(Scene):
	def construct(self):
		texto = TexMobject("{d","\\over","d","x","}","\\int_","{a}^","{","x","}","f(","t",")d","t","=","f(","x",")")
		texto.set_color_by_tex("x",RED)
		self.play(Write(texto))
		self.wait(2)

class ColorPorCaracter2(Scene): #explicar y modificar x por {x}
	def construct(self):
		texto = TexMobject("{d","\\over","d","x","}","\\int_","{a}^","{","x","}","f(","t",")d","t","=","f(","x",")")
		texto.set_color_by_tex("x",RED)
		texto[6].set_color(RED)
		texto[8].set_color(WHITE)
		self.play(Write(texto))
		self.wait(2)
	
class ForLista(Scene): 
    def construct(self): #no usar siempre frac
        texto = TexMobject("[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]")
        for i in [0,1,3,4]:
        	texto[i].set_color(RED)
        self.play(Write(texto))
        self.wait(3)

class ForRango1(Scene): 
    def construct(self): #no usar siempre frac
        texto = TexMobject("[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]")
        for i in range(3):
        	texto[i].set_color(RED)
        self.play(Write(texto))
        self.wait(3)

class ForRango2(Scene): 
    def construct(self): #no usar siempre frac
        texto = TexMobject("[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]")
        for i in range(2,6):
        	texto[i].set_color(RED)
        self.play(Write(texto))
        self.wait(3)

class For2Variables(Scene): 
    def construct(self): #no usar siempre frac
        texto = TexMobject("[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]")
        for i,color in [(2,RED),(4,PINK)]:
        	texto[i].set_color(color)
        self.play(Write(texto))
        self.wait(3)

class ResaltadoV1(Scene): 
    def construct(self):
    	texto = TexMobject("\\lim_{","x","\\to","\\infty}","{1","\\over","x}","=","0")
    	self.play(Write(texto))
    	self.wait(0.5)
    	self.play(
    			texto[0].set_color, YELLOW,
    			texto[0].scale_in_place, 1.2,
    			rate_func = there_and_back,
    		)
    	self.wait(3)

class ResaltadoV2(Scene): 
    def construct(self):
        texto = TexMobject("\\lim_{","x","\\to","\\infty}","{1","\\over","x}","=","0")
        self.play(Write(texto))
        self.wait(0.5)
        for i in [0,8]:
            self.play(
                    texto[i].set_color, YELLOW,
                    texto[i].scale_in_place, 1.2,
                    rate_func = there_and_back,
                )
        self.wait(3)

class ResaltadoV3(Scene): 
    def construct(self):
    	texto = TexMobject("\\lim_{","x","\\to","\\infty}","{1","\\over","x}","=","0")
    	self.play(Write(texto))
    	self.wait(0.5)
    	self.play(
    			texto[0].set_color, YELLOW,
    			texto[0].scale_in_place, 1.2,
    			run_time =0.3
    		)
    	self.wait(2)
    	self.play(
    			texto[0].set_color, WHITE,
    			texto[0].scale_in_place, 1/1.2,
    			run_time =0.3
    		)
    	self.wait(3)

class ResaltadoV4(Scene): 
    def construct(self):
    	texto = TexMobject("\\lim_{","x","\\to","\\infty}","{1","\\over","x}","=","0")
    	self.play(Write(texto))
    	self.wait(0.5)
    	self.play(
    			texto[0].set_color, YELLOW,
    			texto[0].scale_in_place, 1.2,
    			texto[3].set_color, YELLOW,
    			texto[3].scale_in_place, 1.2,
    			texto[7].set_color, YELLOW,
    			texto[7].scale_in_place, 1.2,
    			rate_func = there_and_back,
    		)
    	self.wait(3)

class ResaltadoV5(Scene): 
    def construct(self):
    	texto = TexMobject("\\lim_{","x","\\to","\\infty}","{1","\\over","x}","=","0")
    	self.play(Write(texto))
    	self.wait(0.5)
    	for i,j,k,l,m in [(0,3,4,4,4),(5,3,3,3,3),(0,2,4,6,8)]:
	    	self.play(
	    			texto[i].set_color, YELLOW,
	    			texto[i].scale_in_place, 1.2,
	    			texto[j].set_color, YELLOW,
	    			texto[j].scale_in_place, 1.2,
	    			texto[k].set_color, YELLOW,
	    			texto[k].scale_in_place, 1.2,
	    			texto[l].set_color, YELLOW,
	    			texto[l].scale_in_place, 1.2,
	    			texto[m].set_color, YELLOW,
	    			texto[m].scale_in_place, 1.2,
	    			run_time =0.3
	    		)
	    	self.wait(2)
	    	self.play(
	    			texto[i].set_color, WHITE,
	    			texto[i].scale_in_place, 1/1.2,
	    			texto[j].set_color, WHITE,
	    			texto[j].scale_in_place, 1/1.2,
	    			texto[k].set_color, WHITE,
	    			texto[k].scale_in_place, 1/1.2,
	    			texto[l].set_color, WHITE,
	    			texto[l].scale_in_place, 1/1.2,
	    			texto[m].set_color, WHITE,
	    			texto[m].scale_in_place, 1/1.2,
	    			run_time =0.3
	    		)
    	self.wait(3)

class Tachado(Scene):
    def construct(self):
        texto = TexMobject("\\sum_{i=1}^{\infty}i","=","-\\frac{1}{2}")
        tache = Cross(texto[2])
        tache.set_stroke(RED, 6)
        self.play(Write(formula))
        self.wait(.5)
        self.play(ShowCreation(tache))
        self.wait(2)

class Tachado2(Scene):
    def construct(self):
        texto = TexMobject("\\sum_{i=1}^{\infty}i","=","-\\frac{1}{2}")
        eq=VGroup(texto[1],texto[2])
        tache = Cross(eq)
        tache.set_stroke(RED, 6)
        self.play(Write(texto))
        self.wait(.5)
        self.play(ShowCreation(tache))
        self.wait(2)

class Encuadre1(Scene):
    def construct(self):
        texto=TexMobject(
            "\\hat g(", "f", ")", "=", "\\int", "_{t_1}", "^{t_{2}}",
            "g(", "t", ")", "e", "^{-2\\pi i", "f", "t}", "dt"
        )
        marco = SurroundingRectangle(texto[4], buff = 0.5*SMALL_BUFF)
        self.play(Write(texto))
        self.wait(.5)
        self.play(ShowCreation(texto))
        self.wait(2)

class Encuadre2(Scene):
    def construct(self):
        texto=TexMobject(
            "\\hat g(", "f", ")", "=", "\\int", "_{t_1}", "^{t_{2}}",
            "g(", "t", ")", "e", "^{-2\\pi i", "f", "t}", "dt"
        )
        seleccion=VGroup(texto[4],texto[5],texto[6])
        marco = SurroundingRectangle(seleccion, buff = 0.5*SMALL_BUFF)
        self.play(Write(texto))
        self.wait(.5)
        self.play(ShowCreation(marco))
        self.wait(2)