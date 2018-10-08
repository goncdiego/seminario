# Generated from Conjuntos.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ConjuntosParser import ConjuntosParser
else:
    from ConjuntosParser import ConjuntosParser

# This class defines a complete listener for a parse tree produced by ConjuntosParser.
class ConjuntosListener(ParseTreeListener):

    # Enter a parse tree produced by ConjuntosParser#program.
    def enterProgram(self, ctx:ConjuntosParser.ProgramContext):
        pass

    # Exit a parse tree produced by ConjuntosParser#program.
    def exitProgram(self, ctx:ConjuntosParser.ProgramContext):
        pass


    # Enter a parse tree produced by ConjuntosParser#statement.
    def enterStatement(self, ctx:ConjuntosParser.StatementContext):
        pass

    # Exit a parse tree produced by ConjuntosParser#statement.
    def exitStatement(self, ctx:ConjuntosParser.StatementContext):
        pass


    # Enter a parse tree produced by ConjuntosParser#setElement.
    def enterSetElement(self, ctx:ConjuntosParser.SetElementContext):
        pass

    # Exit a parse tree produced by ConjuntosParser#setElement.
    def exitSetElement(self, ctx:ConjuntosParser.SetElementContext):
        pass


    # Enter a parse tree produced by ConjuntosParser#setFunction.
    def enterSetFunction(self, ctx:ConjuntosParser.SetFunctionContext):
        pass

    # Exit a parse tree produced by ConjuntosParser#setFunction.
    def exitSetFunction(self, ctx:ConjuntosParser.SetFunctionContext):
        pass


    # Enter a parse tree produced by ConjuntosParser#setBelongs.
    def enterSetBelongs(self, ctx:ConjuntosParser.SetBelongsContext):
        pass

    # Exit a parse tree produced by ConjuntosParser#setBelongs.
    def exitSetBelongs(self, ctx:ConjuntosParser.SetBelongsContext):
        pass


    # Enter a parse tree produced by ConjuntosParser#setElementSum.
    def enterSetElementSum(self, ctx:ConjuntosParser.SetElementSumContext):
        pass

    # Exit a parse tree produced by ConjuntosParser#setElementSum.
    def exitSetElementSum(self, ctx:ConjuntosParser.SetElementSumContext):
        pass


    # Enter a parse tree produced by ConjuntosParser#setElementProm.
    def enterSetElementProm(self, ctx:ConjuntosParser.SetElementPromContext):
        pass

    # Exit a parse tree produced by ConjuntosParser#setElementProm.
    def exitSetElementProm(self, ctx:ConjuntosParser.SetElementPromContext):
        pass


    # Enter a parse tree produced by ConjuntosParser#setElementComp.
    def enterSetElementComp(self, ctx:ConjuntosParser.SetElementCompContext):
        pass

    # Exit a parse tree produced by ConjuntosParser#setElementComp.
    def exitSetElementComp(self, ctx:ConjuntosParser.SetElementCompContext):
        pass


    # Enter a parse tree produced by ConjuntosParser#setElementLong.
    def enterSetElementLong(self, ctx:ConjuntosParser.SetElementLongContext):
        pass

    # Exit a parse tree produced by ConjuntosParser#setElementLong.
    def exitSetElementLong(self, ctx:ConjuntosParser.SetElementLongContext):
        pass


    # Enter a parse tree produced by ConjuntosParser#setElementUnion.
    def enterSetElementUnion(self, ctx:ConjuntosParser.SetElementUnionContext):
        pass

    # Exit a parse tree produced by ConjuntosParser#setElementUnion.
    def exitSetElementUnion(self, ctx:ConjuntosParser.SetElementUnionContext):
        pass


    # Enter a parse tree produced by ConjuntosParser#setElementInter.
    def enterSetElementInter(self, ctx:ConjuntosParser.SetElementInterContext):
        pass

    # Exit a parse tree produced by ConjuntosParser#setElementInter.
    def exitSetElementInter(self, ctx:ConjuntosParser.SetElementInterContext):
        pass


    # Enter a parse tree produced by ConjuntosParser#setElementDiff.
    def enterSetElementDiff(self, ctx:ConjuntosParser.SetElementDiffContext):
        pass

    # Exit a parse tree produced by ConjuntosParser#setElementDiff.
    def exitSetElementDiff(self, ctx:ConjuntosParser.SetElementDiffContext):
        pass


    # Enter a parse tree produced by ConjuntosParser#assignStatement.
    def enterAssignStatement(self, ctx:ConjuntosParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by ConjuntosParser#assignStatement.
    def exitAssignStatement(self, ctx:ConjuntosParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by ConjuntosParser#ifStatement.
    def enterIfStatement(self, ctx:ConjuntosParser.IfStatementContext):
        pass

    # Exit a parse tree produced by ConjuntosParser#ifStatement.
    def exitIfStatement(self, ctx:ConjuntosParser.IfStatementContext):
        pass


    # Enter a parse tree produced by ConjuntosParser#whileStatement.
    def enterWhileStatement(self, ctx:ConjuntosParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by ConjuntosParser#whileStatement.
    def exitWhileStatement(self, ctx:ConjuntosParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by ConjuntosParser#booleanExpression.
    def enterBooleanExpression(self, ctx:ConjuntosParser.BooleanExpressionContext):
        pass

    # Exit a parse tree produced by ConjuntosParser#booleanExpression.
    def exitBooleanExpression(self, ctx:ConjuntosParser.BooleanExpressionContext):
        pass


    # Enter a parse tree produced by ConjuntosParser#operand.
    def enterOperand(self, ctx:ConjuntosParser.OperandContext):
        pass

    # Exit a parse tree produced by ConjuntosParser#operand.
    def exitOperand(self, ctx:ConjuntosParser.OperandContext):
        pass


    # Enter a parse tree produced by ConjuntosParser#expression.
    def enterExpression(self, ctx:ConjuntosParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ConjuntosParser#expression.
    def exitExpression(self, ctx:ConjuntosParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ConjuntosParser#term.
    def enterTerm(self, ctx:ConjuntosParser.TermContext):
        pass

    # Exit a parse tree produced by ConjuntosParser#term.
    def exitTerm(self, ctx:ConjuntosParser.TermContext):
        pass


    # Enter a parse tree produced by ConjuntosParser#factor.
    def enterFactor(self, ctx:ConjuntosParser.FactorContext):
        pass

    # Exit a parse tree produced by ConjuntosParser#factor.
    def exitFactor(self, ctx:ConjuntosParser.FactorContext):
        pass


