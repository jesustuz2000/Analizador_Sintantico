
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightIFELSEleftSEMIleftCOMMAleftEQUALleftSEMIleftDEQUALleftLESSLESSEQUALGREATERGREATEREQUALISEQUALleftPLUSMINUSleftTIMESDIVIDEleftLBLOCKRBLOCKleftLPARENRPARENAPOSTROPHE BREAK CASE CLASS CLOSETAG COLON COMMA COMMENTS COMMENTS_C99 CONST DEQUAL DISTINT DIVIDE DO DOT ELSE EQUAL FALSE FOR GREATER GREATEREQUAL ID IF INT ISEQUAL LBLOCK LBRACKET LESS LESSEQUAL LPAREN MAIN MINUS MINUSEQUAL MINUSMINUS NUM OPENTAG PLUS PLUSEQUAL PLUSPLUS PRINT QUOTES RBLOCK RBRACKET RETURN RPAREN SEMI STATIC STRING SWITCH TIMES TRUE VAR VOID WHILEdeclaracion : IF LPAREN expresion GREATER expresion RPAREN LBLOCK expresion SEMI RBLOCKdeclaracion : ELSE LBLOCK expresion SEMI RBLOCKdeclaracion : VAR expresion EQUAL expresion SEMIdeclaracion : OPENTAGdeclaracion :  CLOSETAGdeclaracion : expresion SEMI\n    expresion  :   expresion PLUS expresion\n                |   expresion MINUS expresion\n                |   expresion TIMES expresion\n                |   expresion DIVIDE expresion\n\n    \n    expresion : expresion addop NUM\n    | NUM addop expresion\n    addop : PLUS\n    | MINUS\n    | TIMES\n    | DIVIDE\n    expresion : MINUS expresion %prec MINUS\n    expresion  : LPAREN expresion RPAREN\n                | LBLOCK expresion RBLOCK\n    \n    expresion   :  expresion LESS expresion\n                |  expresion GREATER expresion\n                |  expresion LESSEQUAL expresion\n                |   expresion GREATEREQUAL expresion\n                |   expresion EQUAL expresion\n                |   expresion ISEQUAL expresion\n                |  LPAREN expresion LESS expresion RPAREN\n                |  LPAREN expresion GREATER expresion RPAREN\n                |  LPAREN expresion LESSEQUAL expresion RPAREN\n                |  LPAREN expresion GREATEREQUAL expresion RPAREN\n                |  LPAREN expresion EQUAL expresion RPAREN\n                |  LPAREN expresion ISEQUAL expresion RPAREN\n    expresion : NUMexpresion : ID'
    
_lr_action_items = {'IF':([0,],[2,]),'ELSE':([0,],[6,]),'VAR':([0,],[7,]),'OPENTAG':([0,],[8,]),'CLOSETAG':([0,],[9,]),'NUM':([0,3,5,7,10,13,16,17,18,19,20,21,22,23,24,25,26,28,31,32,33,34,35,38,39,40,41,42,43,57,59,78,],[11,11,11,11,11,11,-13,-14,-15,-16,48,11,11,11,11,11,11,11,11,-13,-14,-15,-16,11,11,11,11,11,11,11,11,11,]),'MINUS':([0,3,4,5,7,10,11,12,13,14,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,78,79,],[10,10,17,10,10,10,33,-33,10,17,10,10,10,10,10,10,10,10,10,10,17,10,17,-17,10,-13,-14,-15,-16,17,-18,10,10,10,10,10,10,-7,-8,-9,-10,-11,17,17,17,17,17,17,-19,17,10,17,10,17,17,17,17,17,17,17,17,-26,-27,-28,-29,-30,-31,10,17,]),'LPAREN':([0,2,3,5,7,10,13,16,17,18,19,21,22,23,24,25,26,28,31,32,33,34,35,38,39,40,41,42,43,57,59,78,],[3,13,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,-13,-14,-15,-16,3,3,3,3,3,3,3,3,3,]),'LBLOCK':([0,3,5,6,7,10,13,16,17,18,19,21,22,23,24,25,26,28,31,32,33,34,35,38,39,40,41,42,43,57,59,77,78,],[5,5,5,28,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,-13,-14,-15,-16,5,5,5,5,5,5,5,5,78,5,]),'ID':([0,3,5,7,10,13,16,17,18,19,21,22,23,24,25,26,28,31,32,33,34,35,38,39,40,41,42,43,57,59,78,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,-13,-14,-15,-16,12,12,12,12,12,12,12,12,12,]),'$end':([1,8,9,15,75,76,81,],[0,-4,-5,-6,-2,-3,-1,]),'SEMI':([4,11,12,30,37,44,45,46,47,48,49,50,51,52,53,54,55,56,58,67,69,70,71,72,73,74,79,],[15,-32,-33,-17,-18,-7,-8,-9,-10,-11,-20,-21,-22,-23,-24,-25,-19,66,-12,76,-26,-27,-28,-29,-30,-31,80,]),'PLUS':([4,11,12,14,27,29,30,36,37,44,45,46,47,48,49,50,51,52,53,54,55,56,58,60,61,62,63,64,65,67,68,69,70,71,72,73,74,79,],[16,32,-33,16,16,16,-17,16,-18,-7,-8,-9,-10,-11,16,16,16,16,16,16,-19,16,16,16,16,16,16,16,16,16,16,-26,-27,-28,-29,-30,-31,16,]),'TIMES':([4,11,12,14,27,29,30,36,37,44,45,46,47,48,49,50,51,52,53,54,55,56,58,60,61,62,63,64,65,67,68,69,70,71,72,73,74,79,],[18,34,-33,18,18,18,18,18,-18,18,18,-9,-10,-11,18,18,18,18,18,18,-19,18,18,18,18,18,18,18,18,18,18,-26,-27,-28,-29,-30,-31,18,]),'DIVIDE':([4,11,12,14,27,29,30,36,37,44,45,46,47,48,49,50,51,52,53,54,55,56,58,60,61,62,63,64,65,67,68,69,70,71,72,73,74,79,],[19,35,-33,19,19,19,19,19,-18,19,19,-9,-10,-11,19,19,19,19,19,19,-19,19,19,19,19,19,19,19,19,19,19,-26,-27,-28,-29,-30,-31,19,]),'LESS':([4,11,12,14,27,29,30,36,37,44,45,46,47,48,49,50,51,52,53,54,55,56,58,60,61,62,63,64,65,67,68,69,70,71,72,73,74,79,],[21,-32,-33,38,21,21,-17,21,-18,-7,-8,-9,-10,-11,-20,-21,-22,-23,21,-25,-19,21,21,-20,-21,-22,-23,21,-25,21,-21,-26,-27,-28,-29,-30,-31,21,]),'GREATER':([4,11,12,14,27,29,30,36,37,44,45,46,47,48,49,50,51,52,53,54,55,56,58,60,61,62,63,64,65,67,68,69,70,71,72,73,74,79,],[22,-32,-33,39,22,22,-17,59,-18,-7,-8,-9,-10,-11,-20,-21,-22,-23,22,-25,-19,22,22,-20,-21,-22,-23,22,-25,22,-21,-26,-27,-28,-29,-30,-31,22,]),'LESSEQUAL':([4,11,12,14,27,29,30,36,37,44,45,46,47,48,49,50,51,52,53,54,55,56,58,60,61,62,63,64,65,67,68,69,70,71,72,73,74,79,],[23,-32,-33,40,23,23,-17,23,-18,-7,-8,-9,-10,-11,-20,-21,-22,-23,23,-25,-19,23,23,-20,-21,-22,-23,23,-25,23,-21,-26,-27,-28,-29,-30,-31,23,]),'GREATEREQUAL':([4,11,12,14,27,29,30,36,37,44,45,46,47,48,49,50,51,52,53,54,55,56,58,60,61,62,63,64,65,67,68,69,70,71,72,73,74,79,],[24,-32,-33,41,24,24,-17,24,-18,-7,-8,-9,-10,-11,-20,-21,-22,-23,24,-25,-19,24,24,-20,-21,-22,-23,24,-25,24,-21,-26,-27,-28,-29,-30,-31,24,]),'EQUAL':([4,11,12,14,27,29,30,36,37,44,45,46,47,48,49,50,51,52,53,54,55,56,58,60,61,62,63,64,65,67,68,69,70,71,72,73,74,79,],[25,-32,-33,42,25,57,-17,25,-18,-7,-8,-9,-10,-11,-20,-21,-22,-23,-24,-25,-19,25,25,-20,-21,-22,-23,-24,-25,-24,-21,-26,-27,-28,-29,-30,-31,25,]),'ISEQUAL':([4,11,12,14,27,29,30,36,37,44,45,46,47,48,49,50,51,52,53,54,55,56,58,60,61,62,63,64,65,67,68,69,70,71,72,73,74,79,],[26,-32,-33,43,26,26,-17,26,-18,-7,-8,-9,-10,-11,-20,-21,-22,-23,26,-25,-19,26,26,-20,-21,-22,-23,26,-25,26,-21,-26,-27,-28,-29,-30,-31,26,]),'RPAREN':([11,12,14,30,37,44,45,46,47,48,49,50,51,52,53,54,55,58,60,61,62,63,64,65,68,69,70,71,72,73,74,],[-32,-33,37,-17,-18,-7,-8,-9,-10,-11,-20,-21,-22,-23,-24,-25,-19,-12,69,70,71,72,73,74,77,-26,-27,-28,-29,-30,-31,]),'RBLOCK':([11,12,27,30,37,44,45,46,47,48,49,50,51,52,53,54,55,58,66,69,70,71,72,73,74,80,],[-32,-33,55,-17,-18,-7,-8,-9,-10,-11,-20,-21,-22,-23,-24,-25,-19,-12,75,-26,-27,-28,-29,-30,-31,81,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaracion':([0,],[1,]),'expresion':([0,3,5,7,10,13,16,17,18,19,21,22,23,24,25,26,28,31,38,39,40,41,42,43,57,59,78,],[4,14,27,29,30,36,44,45,46,47,49,50,51,52,53,54,56,58,60,61,62,63,64,65,67,68,79,]),'addop':([4,11,14,27,29,30,36,44,45,46,47,49,50,51,52,53,54,56,58,60,61,62,63,64,65,67,68,79,],[20,31,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaracion","S'",1,None,None,None),
  ('declaracion -> IF LPAREN expresion GREATER expresion RPAREN LBLOCK expresion SEMI RBLOCK','declaracion',10,'p_declaracion_coditionif','sintantico.py',31),
  ('declaracion -> ELSE LBLOCK expresion SEMI RBLOCK','declaracion',5,'p_declaracion_coditionelse','sintantico.py',38),
  ('declaracion -> VAR expresion EQUAL expresion SEMI','declaracion',5,'p_declaracion_asignar','sintantico.py',46),
  ('declaracion -> OPENTAG','declaracion',1,'p_declaracion_inicio','sintantico.py',53),
  ('declaracion -> CLOSETAG','declaracion',1,'p_declaracion_final','sintantico.py',60),
  ('declaracion -> expresion SEMI','declaracion',2,'p_declaracion_expr','sintantico.py',67),
  ('expresion -> expresion PLUS expresion','expresion',3,'p_expresion_operaciones','sintantico.py',76),
  ('expresion -> expresion MINUS expresion','expresion',3,'p_expresion_operaciones','sintantico.py',77),
  ('expresion -> expresion TIMES expresion','expresion',3,'p_expresion_operaciones','sintantico.py',78),
  ('expresion -> expresion DIVIDE expresion','expresion',3,'p_expresion_operaciones','sintantico.py',79),
  ('expresion -> expresion addop NUM','expresion',3,'p_expresion_operaciones1','sintantico.py',95),
  ('expresion -> NUM addop expresion','expresion',3,'p_expresion_operaciones1','sintantico.py',96),
  ('addop -> PLUS','addop',1,'p_addop','sintantico.py',102),
  ('addop -> MINUS','addop',1,'p_addop','sintantico.py',103),
  ('addop -> TIMES','addop',1,'p_addop','sintantico.py',104),
  ('addop -> DIVIDE','addop',1,'p_addop','sintantico.py',105),
  ('expresion -> MINUS expresion','expresion',2,'p_expresion_minus','sintantico.py',112),
  ('expresion -> LPAREN expresion RPAREN','expresion',3,'p_expresion_grupo','sintantico.py',120),
  ('expresion -> LBLOCK expresion RBLOCK','expresion',3,'p_expresion_grupo','sintantico.py',121),
  ('expresion -> expresion LESS expresion','expresion',3,'p_expresion_logicas','sintantico.py',130),
  ('expresion -> expresion GREATER expresion','expresion',3,'p_expresion_logicas','sintantico.py',131),
  ('expresion -> expresion LESSEQUAL expresion','expresion',3,'p_expresion_logicas','sintantico.py',132),
  ('expresion -> expresion GREATEREQUAL expresion','expresion',3,'p_expresion_logicas','sintantico.py',133),
  ('expresion -> expresion EQUAL expresion','expresion',3,'p_expresion_logicas','sintantico.py',134),
  ('expresion -> expresion ISEQUAL expresion','expresion',3,'p_expresion_logicas','sintantico.py',135),
  ('expresion -> LPAREN expresion LESS expresion RPAREN','expresion',5,'p_expresion_logicas','sintantico.py',136),
  ('expresion -> LPAREN expresion GREATER expresion RPAREN','expresion',5,'p_expresion_logicas','sintantico.py',137),
  ('expresion -> LPAREN expresion LESSEQUAL expresion RPAREN','expresion',5,'p_expresion_logicas','sintantico.py',138),
  ('expresion -> LPAREN expresion GREATEREQUAL expresion RPAREN','expresion',5,'p_expresion_logicas','sintantico.py',139),
  ('expresion -> LPAREN expresion EQUAL expresion RPAREN','expresion',5,'p_expresion_logicas','sintantico.py',140),
  ('expresion -> LPAREN expresion ISEQUAL expresion RPAREN','expresion',5,'p_expresion_logicas','sintantico.py',141),
  ('expresion -> NUM','expresion',1,'p_expresion_num','sintantico.py',174),
  ('expresion -> ID','expresion',1,'p_expresion_id','sintantico.py',180),
]