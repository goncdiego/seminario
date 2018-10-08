from antlr4 import CommonTokenStream, ParseTreeWalker, InputStream
from ConjuntosLexer import ConjuntosLexer
from ConjuntosParser import ConjuntosParser
from ConjuntosListener import ConjuntosListener
import antlr4

# TODO:
# Asignar sets a variables
# Seguir con el resto de las funciones de set


class RealListener(ConjuntosListener):
    
    def __init__(self):
        self.variables = {}

    def enterProgram(self, ctx:ConjuntosParser.ProgramContext):
        for node in ctx.children:
            self.visitStatement(node)

    def exitProgram(self, ctx:ConjuntosParser.ProgramContext):
        print('Program ended. :)')


    def visitStatement(self, ctx:ConjuntosParser.StatementContext):
        for node in ctx.children:
            if type(node) == ConjuntosParser.ExpressionContext:
                result = self.visitExpression(node)
                print(result)
            
            elif type(node) == ConjuntosParser.AssignStatementContext:
                self.visitAssignStatement(node)

            elif type(node) == antlr4.tree.Tree.TerminalNodeImpl:   # VARNAME
                result = self.variables[node.symbol.text]
                print(node.symbol.text + ' = ' + str(result))

            elif type(node) == ConjuntosParser.BooleanExpressionContext:
                result = self.visitBooleanExpresion(node)
                print(result)

            elif type(node) == ConjuntosParser.IfStatementContext:
                condition = self.visitBooleanExpresion(node.children[1])
                if condition:
                    i = 3
                    while i < len(node.children) - 1 and type(node.children[i]) != antlr4.tree.Tree.TerminalNodeImpl:
                        self.visitStatement(node.children[i])
                        i += 1
                else:
                    i = 3
                    while i < len(node.children) - 1 and type(node.children[i]) != antlr4.tree.Tree.TerminalNodeImpl:
                        i += 1
                        # sale del while cuando encuentra el ELSE
                    
                    i += 1      # Para saltear el ELSE
                    while i < len(node.children) - 1:
                        self.visitStatement(node.children[i])
                        i += 1
            
            elif type(node) == ConjuntosParser.SetElementContext:
                self.visitSetElement(node)

    
    def visitSetElement(self, ctx:ConjuntosParser.SetElementContext):
        conjunto = []
        a_start = int(ctx.a_start.text)
        a_end = int(ctx.a_end.text)
        
        #Si el conjunto establecido no tiene saltos, voy de 1en1
        if (ctx.a_step != None):
            a_step = int(ctx.a_step.text)
        else:
            a_step = 1

        for x in range(a_start, a_end + 1, a_step):
            conjunto.append(x)
        
        #devuelvo el set
        return conjunto

    def visitSetFunction(self, ctx:ConjuntosParser.SetFunctionContext):
        child = ctx.children[0]

        #si es la funcion .Belong(N), visito el setBelongs
        if type(child) == ConjuntosParser.SetBelongsContext:
            return self.visitSetBelongs(child)
        #si es la funcion N.sum, visito el setElementSum    
        elif type(child) == ConjuntosParser.SetElementSumContext:
            return self.visitSetElementSum(child)

        elif type(child) == ConjuntosParser.SetElementPromContext:
            return self.visitSetElementProm(child)
        
        elif type(child) == ConjuntosParser.SetElementLongContext:
            return self.visitSetElementLong(child)     

        elif type(child) == ConjuntosParser.SetElementCompContext:
            return self.visitSetElementComp(child)
        
        elif type(child) == ConjuntosParser.SetElementUnionContext:
            return self.visitSetElementUnion(child)

        elif type(child) == ConjuntosParser.SetElementInterContext:
            return self.visitSetElementInter(child)

        elif type(child) == ConjuntosParser.SetElementDiffContext:
            return self.visitSetElementDiff(child)                     

    def visitSetBelongs(self, ctx:ConjuntosParser.SetBelongsContext):
        #si el numero conjunto pertenece al conjunto
        print('Funcion Belongs...')
        if int(ctx.a_numero.text) in self.variables[ctx.a_name.text]:
            return True
        #si el numero no pertenece al conjunto    
        else:
            return False

    def visitSetElementSum(self, ctx:ConjuntosParser.SetElementSumContext):
        print('Funcion Suma...')
        return sum(self.variables[ctx.a_name.text])

    def visitSetElementProm(self, ctx:ConjuntosParser.SetElementPromContext):
        print('Funcion Promedio...')
        return sum(self.variables[ctx.a_name.text]) / len((self.variables[ctx.a_name.text]))   

    def visitSetElementLong(self, ctx:ConjuntosParser.SetElementLongContext):
        print('Funcion Longitud...')
        return len(self.variables[ctx.a_name.text])

    def visitSetElementComp(self, ctx:ConjuntosParser.SetElementCompContext):
        print('Funcion Complemento...')
        Neglist = []
        Neglist = self.variables[ctx.a_name.text]
        Neglist = [-abs(x) for x in Neglist]

        return Neglist

    def visitSetElementUnion(self, ctx:ConjuntosParser.SetElementUnionContext):
        print('Funcion Union...')
        lista1 = self.variables[ctx.a_name1.text]
        lista2 = self.variables[ctx.a_name2.text]
        return list(set().union(lista1,lista2))

    def visitSetElementInter(self, ctx:ConjuntosParser.SetElementInterContext):
        print('Funcion Interseccion...')
        lista3 = self.variables[ctx.a_name1.text]
        lista4 = self.variables[ctx.a_name2.text]
        listaresult  = list(set().intersection(lista3,lista4))    
        if len(listaresult)==0:
           print('La lista esta vacia...')
           return 'no_hay_interseccion'
        else:
           print('La lista no esta vacia...')
           return listaresult
    
    def visitSetElementDiff(self, ctx:ConjuntosParser.SetElementDiffContext):
        print('Funcion Diferencia..')
        lista1 = self.variables[ctx.a_name1.text]
        lista2 = self.variables[ctx.a_name2.text]
        temp = set(lista1) - set(lista2) | set(lista1) -set(lista2)

        if len(temp)==0:
           return 'no_hay_diferencia'
        else:
           return temp
           
    def visitWhileStatement(self, ctx:ConjuntosParser.WhileStatementContext):
        
        while self.visitBooleanExpresion(ctx.children[1]):
            print('en el while!!!')
            i = 3
            while i < len(ctx.children) - 1 and type(ctx.children[i]) != antlr4.tree.Tree.TerminalNodeImpl:
                self.visitStatement(ctx.children[i])
                i += 1
    # Ok
    def visitBooleanExpresion(self, ctx:ConjuntosParser.BooleanExpressionContext):
        if ctx.op.text == 'and':
            be_left = self.visitBooleanExpresion(ctx.children[0])
            be_right = self.visitBooleanExpresion(ctx.children[2])
            return be_left and be_right

        if ctx.op.text == 'or':
            be_left = self.visitBooleanExpresion(ctx.children[0])
            be_right = self.visitBooleanExpresion(ctx.children[2])
            return be_left or be_right

        left =  self.visitOperand(ctx.children[0])
        right = self.visitOperand(ctx.children[2])
        op = ctx.children[1].symbol.text

        return eval(str(left) + op + str(right))

    # Ok
    def visitOperand(self, ctx:ConjuntosParser.OperandContext):
        node = ctx.children[0]
        if type(node) == ConjuntosParser.ExpressionContext:
            return self.visitExpression(node)

        if type(node) == antlr4.tree.Tree.TerminalNodeImpl:
            return self.variables[node.symbol.text]
        
        return ''   # No deberia pasar

    # Ok
    def visitAssignStatement(self, ctx:ConjuntosParser.AssignStatementContext):
        name = ctx.children[0].symbol.text
        value = None

        if type(ctx.children[2]) == ConjuntosParser.ExpressionContext:
            value = self.visitExpression(ctx.children[2])
        elif type(ctx.children[2]) == ConjuntosParser.SetElementContext:
            value = self.visitSetElement(ctx.children[2])
        elif type(ctx.children[2]) == ConjuntosParser.SetFunctionContext:
            value = self.visitSetFunction(ctx.children[2])

        self.variables[name] = value

    # Ok
    def visitExpression(self, ctx:ConjuntosParser.ExpressionContext):
        # Es un Term
        if type(ctx.children[0]) == ConjuntosParser.TermContext:
            return self.visitTerm(ctx.children[0])
        
        # Es un Set
        if type(ctx.children[0]) == ConjuntosParser.SetElementContext:
            return self.visitSetElement(ctx.children[0])
        
        # Es una Expression con +/- Term
        sign = 1
        if ctx.children[1].symbol.text == '-':
            sign = -1

        value1 = self.visitExpression(ctx.children[0])
        value2 = self.visitTerm(ctx.children[2])

        return value1 + sign * value2

    # Ok
    def visitTerm(self, ctx:ConjuntosParser.TermContext):
        if type(ctx.children[0]) == ConjuntosParser.FactorContext:
            # Es un factor
            return self.visitFactor(ctx.children[0])

        # Es un term * / factor
        value1 = self.visitTerm(ctx.children[0])
        value2 = self.visitFactor(ctx.children[2])

        if ctx.children[1].symbol.text == '*':
            return value1 * value2

        return value1 / value2

    # Ok
    def visitFactor(self, ctx:ConjuntosParser.FactorContext):
        
        if ctx.n != None:
            return int(ctx.n.text)

        if ctx.vn != None:
            return self.variables[ctx.vn.text]

        if ctx.children[0].symbol.text != '(':
            nodo = ctx.children[0]
            return int(nodo.symbol.text)

        return self.visitExpression(ctx.children[1])
        

def main():
  
    program =   "a = 37 \n"
    program +=  "b = a+3 \n"

    program +=  "j = set[5 10 1] \n"
    program +=  "c = set[10 15 1] \n"
    program +=  "c \n"
    program +=  "d = c.belongs(19)"
    program +=  "e = c.sum"
    program +=  "f = c.prom"
    program +=  "g = c.long"
    program +=  "h = c.comp"
    #program +=  "i = j union c"
    #program +=  "m = c inter j"
    program +=  "k = c diff j"

    input = InputStream(program)
    lexer = ConjuntosLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ConjuntosParser(stream)

    tree = parser.program()
    
    listener = RealListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
 
    print(listener.variables)

if __name__ == '__main__':
    main()