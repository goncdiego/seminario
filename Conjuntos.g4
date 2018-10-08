grammar Conjuntos;

program:
    (statement)+
    ;

//defino las operaciones que va a tener mi gramatica
statement:
      expression                
    | assignStatement  
    | VARNAME                   
    | booleanExpression          
    | ifStatement
    | setElement 
    | setFunction
    ;

//a_start ; a_end ; a_step son los alias para acceder a NUMBER
setElement:
      'set[' a_start=NUMBER a_end=NUMBER a_step=NUMBER ']'
    | 'set[' a_start=NUMBER a_end=NUMBER ']'
    ;

//defino todas las funciones que voy a tener en mi gramatica
setFunction:
      setBelongs
    | setElementSum
    | setElementProm
    | setElementLong
    | setElementComp
    | setElementUnion
    | setElementInter
    | setElementDiff
    ;

setBelongs:
    a_name=VARNAME '.belongs(' a_numero=NUMBER ')'
    ;

setElementSum:
    a_name=VARNAME '.sum'
    ;

setElementProm:
    a_name=VARNAME '.prom'
    ;

setElementComp:
    a_name=VARNAME '.comp'
    ;    

setElementLong:
    a_name=VARNAME '.long'
    ;

setElementUnion:
    a_name1=VARNAME 'union' a_name2=VARNAME
    ;

setElementInter:
    a_name1=VARNAME 'inter' a_name2=VARNAME
    ;   

setElementDiff:
    a_name1=VARNAME 'diff' a_name2=VARNAME
    ;   

assignStatement:
      VARNAME '=' expression
    | VARNAME '=' setElement
    | VARNAME '=' setFunction
    ;

ifStatement:
      'if' booleanExpression 
      'then ' (statement)+ 
      ('else ' (statement)+ )?
      'fi'
    ;

whileStatement:
      'while' booleanExpression 'do'
        (statement)+
      'done'
    ;

booleanExpression:
      operand           op=COMPARATION_OPERATOR operand
    | booleanExpression op=AND_OPERATOR booleanExpression
    | booleanExpression op=OR_OPERATOR booleanExpression
    ;

//defino los operandos puedo tener una expresion o una variable
operand:
      expression
    | VARNAME
    ;

//defino una expresion
expression: 
      setElement
    | term
    | expression '+' term   
    | expression '-' term   
    ;

term:   
    factor                    
    | term '*' factor       
    | term '/' factor       
    ;

factor: 
      n=NUMBER      
    | vn=VARNAME               
    | '(' expression ')'     
    ;

//defino todos los operadores de mi gramatica
AND_OPERATOR : 'and';
OR_OPERATOR : 'or';
COMPARATION_OPERATOR : '=='|'<='|'>='|'<'|'>'|'!=';

//defino que VARNAME, puede ser cualquier caracter entre a-z
VARNAME : [a-z]+;

//defino que NUMBER va ser un digito
NUMBER : DIGIT+;

//defino que digito estara comprendido entre 0-9
DIGIT  : [0-9];
WS : [ \r\n\t] -> skip;