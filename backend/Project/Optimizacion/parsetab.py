
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftIGUALDADDIFERENTEleftMENORMAYORMAYORIMENORIleftMASMENOSCOMAleftPORDIVMODleftPARIPARDleftPOTAND CADENA COMA CORD CORI DECIMAL DIFERENTE DIV DPUNTOS ENTERO ID IGUAL IGUALDAD LLD LLI MAS MAYOR MAYORI MENOR MENORI MENOS MOD OR PARD PARI POR POT PUNTO PUNTOCOMA RFLOAT RFMT RFUNC RGOTO RIF RIMPORT RINT RMATH RMOD RPACKAGE RPRINTF RRETURN RVARinit : RPACKAGE ID PUNTOCOMA imports declaraciones L_codigoinit : RPACKAGE ID PUNTOCOMA declaraciones L_codigoimports : imports importimports : importimport : RIMPORT PARI CADENA PARD PUNTOCOMAimport : RIMPORT PARI CADENA PARDdeclaraciones : declaraciones declaraciondeclaraciones : declaraciondeclaracion : RVAR temp_list CORI ENTERO CORD RFLOAT PUNTOCOMAdeclaracion : RVAR temp_list CORI ENTERO CORD RFLOATdeclaracion : RVAR temp_list tipo PUNTOCOMAdeclaracion : RVAR temp_list tipotemp_list : temp_list COMA IDtemp_list : IDtipo : RINT\n            | RFLOATL_codigo : L_codigo codigoL_codigo : codigocodigo : codecode : RFUNC ID PARI PARD instruccionesinstrucciones : LLI instrucciones_2 LLDinstrucciones_2 : instrucciones_2 instruccion\n                        | instruccioninstruccion  : asignacion PUNTOCOMA\n                    | label DPUNTOS\n                    | gotoS PUNTOCOMA\n                    | llamada_funcion PUNTOCOMA\n                    | cond_if\n                    | returnE PUNTOCOMA\n                    | printF PUNTOCOMA\n                    label : IDgotoS : RGOTO IDreturnE : RRETURNprintF : RFMT PUNTO RPRINTF PARI CADENA COMA valor PARDvalor : RINT PARI expresion PARD\n            |   expresioncond_if : RIF expresion LLI RGOTO ID PUNTOCOMA LLDaccess :   ID CORI RINT PARI expresion PARD CORD\n                | ID CORI expresion CORDasignacion : access IGUAL expresionasignacion :   ID IGUAL expresion\n                | ID IGUAL accessllamada_funcion : ID PARI PARDexpresion : expresion MAS expresion\n                  | expresion MENOS expresion\n                  | expresion POR expresion\n                  | expresion DIV expresion\n                  | expresion OR expresion\n                  | expresion AND expresion\n                  | expresion IGUALDAD expresion\n                  | expresion DIFERENTE expresion\n                  | expresion MAYOR expresion\n                  | expresion MENOR expresion\n                  | expresion MAYORI expresion\n                  | expresion MENORI expresion\n                  | expresion POT expresion\n                  | expresion MOD expresionexpresion : PARI expresion PARDexpresion : ENTERO\n                |   ID\n                |   MENOS ENTERO\n                |   DECIMALexpresion : RMATH PUNTO RMOD PARI expresion COMA expresion PARD'
    
_lr_action_items = {'RPACKAGE':([0,],[2,]),'$end':([1,13,15,16,21,22,38,57,],[0,-2,-18,-19,-1,-17,-20,-21,]),'ID':([2,10,17,28,39,41,42,47,52,53,58,59,60,61,62,63,64,65,66,68,73,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,106,126,131,133,134,140,],[3,20,23,34,51,51,-23,-28,69,71,-22,-24,-25,-26,-27,-29,-30,71,79,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,125,71,71,-37,71,71,]),'PUNTOCOMA':([3,26,27,29,31,40,43,45,46,48,49,54,69,71,74,75,78,79,80,81,82,100,105,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,125,132,139,141,],[4,-16,33,-15,36,56,59,61,62,63,64,-33,-32,-60,-59,-62,-40,-60,-41,-42,-43,-61,-39,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,129,-38,-34,-63,]),'RIMPORT':([4,5,7,12,31,36,],[9,9,-4,-3,-6,-5,]),'RVAR':([4,5,6,7,8,11,12,14,26,27,29,31,33,36,40,56,],[10,10,10,-4,-8,10,-3,-7,-16,-12,-15,-6,-11,-5,-10,-9,]),'RFUNC':([6,8,11,13,14,15,16,21,22,26,27,29,33,38,40,56,57,],[17,-8,17,17,-7,-18,-19,17,-17,-16,-12,-15,-11,-20,-10,-9,-21,]),'PARI':([9,23,51,53,65,66,68,73,83,86,87,88,89,90,91,92,93,94,95,96,97,98,99,103,104,122,126,131,134,136,140,],[18,30,67,73,73,73,73,73,104,73,73,73,73,73,73,73,73,73,73,73,73,73,73,123,73,126,73,73,73,140,73,]),'CADENA':([18,123,],[24,127,]),'CORI':([19,20,34,51,79,],[25,-14,-13,68,68,]),'COMA':([19,20,34,71,74,75,100,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,127,130,141,],[28,-14,-13,-60,-59,-62,-61,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,131,134,-63,]),'RINT':([19,20,34,68,131,],[29,-14,-13,83,136,]),'RFLOAT':([19,20,34,37,],[26,-14,-13,40,]),'PARD':([24,30,67,71,74,75,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,135,137,138,141,142,143,],[31,35,82,-60,-59,-62,-61,121,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,128,139,-36,141,-63,143,-35,]),'ENTERO':([25,53,65,66,68,72,73,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,126,131,134,140,],[32,74,74,74,74,100,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'CORD':([32,71,74,75,84,100,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,128,141,],[37,-60,-59,-62,105,-61,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,132,-63,]),'LLI':([35,70,71,74,75,100,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,141,],[39,85,-60,-59,-62,-61,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-63,]),'RGOTO':([39,41,42,47,58,59,60,61,62,63,64,85,133,],[52,52,-23,-28,-22,-24,-25,-26,-27,-29,-30,106,-37,]),'RIF':([39,41,42,47,58,59,60,61,62,63,64,133,],[53,53,-23,-28,-22,-24,-25,-26,-27,-29,-30,-37,]),'RRETURN':([39,41,42,47,58,59,60,61,62,63,64,133,],[54,54,-23,-28,-22,-24,-25,-26,-27,-29,-30,-37,]),'RFMT':([39,41,42,47,58,59,60,61,62,63,64,133,],[55,55,-23,-28,-22,-24,-25,-26,-27,-29,-30,-37,]),'LLD':([41,42,47,58,59,60,61,62,63,64,129,133,],[57,-23,-28,-22,-24,-25,-26,-27,-29,-30,133,-37,]),'DPUNTOS':([44,51,],[60,-31,]),'IGUAL':([50,51,105,132,],[65,66,-39,-38,]),'MENOS':([53,65,66,68,70,71,73,74,75,78,79,80,84,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,126,130,131,134,137,138,140,141,142,],[72,72,72,72,87,-60,72,-59,-62,87,-60,87,87,72,72,72,72,72,72,72,72,72,72,72,72,72,72,-61,87,72,-44,-45,-46,-47,87,87,87,87,87,87,87,87,-56,-57,-58,87,72,87,72,72,87,87,72,-63,87,]),'DECIMAL':([53,65,66,68,73,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,126,131,134,140,],[75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'RMATH':([53,65,66,68,73,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,126,131,134,140,],[76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,]),'PUNTO':([55,76,],[77,102,]),'MAS':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[86,-60,-59,-62,86,-60,86,86,-61,86,-44,-45,-46,-47,86,86,86,86,86,86,86,86,-56,-57,-58,86,86,86,86,-63,86,]),'POR':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[88,-60,-59,-62,88,-60,88,88,-61,88,88,88,-46,-47,88,88,88,88,88,88,88,88,-56,-57,-58,88,88,88,88,-63,88,]),'DIV':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[89,-60,-59,-62,89,-60,89,89,-61,89,89,89,-46,-47,89,89,89,89,89,89,89,89,-56,-57,-58,89,89,89,89,-63,89,]),'OR':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[90,-60,-59,-62,90,-60,90,90,-61,90,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,90,90,90,90,-63,90,]),'AND':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[91,-60,-59,-62,91,-60,91,91,-61,91,-44,-45,-46,-47,91,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,91,91,91,91,-63,91,]),'IGUALDAD':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[92,-60,-59,-62,92,-60,92,92,-61,92,-44,-45,-46,-47,92,92,-50,-51,-52,-53,-54,-55,-56,-57,-58,92,92,92,92,-63,92,]),'DIFERENTE':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[93,-60,-59,-62,93,-60,93,93,-61,93,-44,-45,-46,-47,93,93,-50,-51,-52,-53,-54,-55,-56,-57,-58,93,93,93,93,-63,93,]),'MAYOR':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[94,-60,-59,-62,94,-60,94,94,-61,94,-44,-45,-46,-47,94,94,94,94,-52,-53,-54,-55,-56,-57,-58,94,94,94,94,-63,94,]),'MENOR':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[95,-60,-59,-62,95,-60,95,95,-61,95,-44,-45,-46,-47,95,95,95,95,-52,-53,-54,-55,-56,-57,-58,95,95,95,95,-63,95,]),'MAYORI':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[96,-60,-59,-62,96,-60,96,96,-61,96,-44,-45,-46,-47,96,96,96,96,-52,-53,-54,-55,-56,-57,-58,96,96,96,96,-63,96,]),'MENORI':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[97,-60,-59,-62,97,-60,97,97,-61,97,-44,-45,-46,-47,97,97,97,97,-52,-53,-54,-55,-56,-57,-58,97,97,97,97,-63,97,]),'POT':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[98,-60,-59,-62,98,-60,98,98,-61,98,98,98,98,98,98,98,98,98,98,98,98,98,-56,98,-58,98,98,98,98,-63,98,]),'MOD':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[99,-60,-59,-62,99,-60,99,99,-61,99,99,99,-46,-47,99,99,99,99,99,99,99,99,-56,-57,-58,99,99,99,99,-63,99,]),'RPRINTF':([77,],[103,]),'RMOD':([102,],[122,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'imports':([4,],[5,]),'declaraciones':([4,5,],[6,11,]),'import':([4,5,],[7,12,]),'declaracion':([4,5,6,11,],[8,8,14,14,]),'L_codigo':([6,11,],[13,21,]),'codigo':([6,11,13,21,],[15,15,22,22,]),'code':([6,11,13,21,],[16,16,16,16,]),'temp_list':([10,],[19,]),'tipo':([19,],[27,]),'instrucciones':([35,],[38,]),'instrucciones_2':([39,],[41,]),'instruccion':([39,41,],[42,58,]),'asignacion':([39,41,],[43,43,]),'label':([39,41,],[44,44,]),'gotoS':([39,41,],[45,45,]),'llamada_funcion':([39,41,],[46,46,]),'cond_if':([39,41,],[47,47,]),'returnE':([39,41,],[48,48,]),'printF':([39,41,],[49,49,]),'access':([39,41,66,],[50,50,81,]),'expresion':([53,65,66,68,73,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,126,131,134,140,],[70,78,80,84,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,124,130,137,138,142,]),'valor':([131,],[135,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> RPACKAGE ID PUNTOCOMA imports declaraciones L_codigo','init',6,'p_init','Optimizador_Sintactico.py',187),
  ('init -> RPACKAGE ID PUNTOCOMA declaraciones L_codigo','init',5,'p_init_2','Optimizador_Sintactico.py',191),
  ('imports -> imports import','imports',2,'p_imports','Optimizador_Sintactico.py',195),
  ('imports -> import','imports',1,'p_imports2','Optimizador_Sintactico.py',200),
  ('import -> RIMPORT PARI CADENA PARD PUNTOCOMA','import',5,'p_import3','Optimizador_Sintactico.py',204),
  ('import -> RIMPORT PARI CADENA PARD','import',4,'p_import4','Optimizador_Sintactico.py',208),
  ('declaraciones -> declaraciones declaracion','declaraciones',2,'p_declaraciones','Optimizador_Sintactico.py',212),
  ('declaraciones -> declaracion','declaraciones',1,'p_declaraciones2','Optimizador_Sintactico.py',217),
  ('declaracion -> RVAR temp_list CORI ENTERO CORD RFLOAT PUNTOCOMA','declaracion',7,'p_declaraciones3','Optimizador_Sintactico.py',221),
  ('declaracion -> RVAR temp_list CORI ENTERO CORD RFLOAT','declaracion',6,'p_declaraciones5','Optimizador_Sintactico.py',225),
  ('declaracion -> RVAR temp_list tipo PUNTOCOMA','declaracion',4,'p_declaraciones4','Optimizador_Sintactico.py',229),
  ('declaracion -> RVAR temp_list tipo','declaracion',3,'p_declaraciones6','Optimizador_Sintactico.py',233),
  ('temp_list -> temp_list COMA ID','temp_list',3,'p_Lista_Temps','Optimizador_Sintactico.py',237),
  ('temp_list -> ID','temp_list',1,'p_Lista_Temps2','Optimizador_Sintactico.py',241),
  ('tipo -> RINT','tipo',1,'p_tipo','Optimizador_Sintactico.py',245),
  ('tipo -> RFLOAT','tipo',1,'p_tipo','Optimizador_Sintactico.py',246),
  ('L_codigo -> L_codigo codigo','L_codigo',2,'p_codigo_1','Optimizador_Sintactico.py',253),
  ('L_codigo -> codigo','L_codigo',1,'p_codigo_2','Optimizador_Sintactico.py',258),
  ('codigo -> code','codigo',1,'p_codigo_3','Optimizador_Sintactico.py',262),
  ('code -> RFUNC ID PARI PARD instrucciones','code',5,'p_codigo_4','Optimizador_Sintactico.py',266),
  ('instrucciones -> LLI instrucciones_2 LLD','instrucciones',3,'p_codigo_5','Optimizador_Sintactico.py',270),
  ('instrucciones_2 -> instrucciones_2 instruccion','instrucciones_2',2,'p_codigo_6','Optimizador_Sintactico.py',274),
  ('instrucciones_2 -> instruccion','instrucciones_2',1,'p_codigo_6','Optimizador_Sintactico.py',275),
  ('instruccion -> asignacion PUNTOCOMA','instruccion',2,'p_codigo_7','Optimizador_Sintactico.py',283),
  ('instruccion -> label DPUNTOS','instruccion',2,'p_codigo_7','Optimizador_Sintactico.py',284),
  ('instruccion -> gotoS PUNTOCOMA','instruccion',2,'p_codigo_7','Optimizador_Sintactico.py',285),
  ('instruccion -> llamada_funcion PUNTOCOMA','instruccion',2,'p_codigo_7','Optimizador_Sintactico.py',286),
  ('instruccion -> cond_if','instruccion',1,'p_codigo_7','Optimizador_Sintactico.py',287),
  ('instruccion -> returnE PUNTOCOMA','instruccion',2,'p_codigo_7','Optimizador_Sintactico.py',288),
  ('instruccion -> printF PUNTOCOMA','instruccion',2,'p_codigo_7','Optimizador_Sintactico.py',289),
  ('label -> ID','label',1,'p_label','Optimizador_Sintactico.py',294),
  ('gotoS -> RGOTO ID','gotoS',2,'p_goto','Optimizador_Sintactico.py',298),
  ('returnE -> RRETURN','returnE',1,'p_return','Optimizador_Sintactico.py',302),
  ('printF -> RFMT PUNTO RPRINTF PARI CADENA COMA valor PARD','printF',8,'p_printF','Optimizador_Sintactico.py',306),
  ('valor -> RINT PARI expresion PARD','valor',4,'p_valor','Optimizador_Sintactico.py',310),
  ('valor -> expresion','valor',1,'p_valor','Optimizador_Sintactico.py',311),
  ('cond_if -> RIF expresion LLI RGOTO ID PUNTOCOMA LLD','cond_if',7,'p_if','Optimizador_Sintactico.py',320),
  ('access -> ID CORI RINT PARI expresion PARD CORD','access',7,'p_access','Optimizador_Sintactico.py',324),
  ('access -> ID CORI expresion CORD','access',4,'p_access','Optimizador_Sintactico.py',325),
  ('asignacion -> access IGUAL expresion','asignacion',3,'p_assign','Optimizador_Sintactico.py',333),
  ('asignacion -> ID IGUAL expresion','asignacion',3,'p_assign2','Optimizador_Sintactico.py',337),
  ('asignacion -> ID IGUAL access','asignacion',3,'p_assign2','Optimizador_Sintactico.py',338),
  ('llamada_funcion -> ID PARI PARD','llamada_funcion',3,'p_llamada_funcion','Optimizador_Sintactico.py',344),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',348),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',349),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',350),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',351),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',352),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',353),
  ('expresion -> expresion IGUALDAD expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',354),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',355),
  ('expresion -> expresion MAYOR expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',356),
  ('expresion -> expresion MENOR expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',357),
  ('expresion -> expresion MAYORI expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',358),
  ('expresion -> expresion MENORI expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',359),
  ('expresion -> expresion POT expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',360),
  ('expresion -> expresion MOD expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',361),
  ('expresion -> PARI expresion PARD','expresion',3,'p_expresion_agrupacion','Optimizador_Sintactico.py',365),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','Optimizador_Sintactico.py',369),
  ('expresion -> ID','expresion',1,'p_expresion_entero','Optimizador_Sintactico.py',370),
  ('expresion -> MENOS ENTERO','expresion',2,'p_expresion_entero','Optimizador_Sintactico.py',371),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_entero','Optimizador_Sintactico.py',372),
  ('expresion -> RMATH PUNTO RMOD PARI expresion COMA expresion PARD','expresion',8,'p_expresion_mod','Optimizador_Sintactico.py',379),
]
