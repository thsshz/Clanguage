grammar Clanguage;
root:  (include)* (statement)*;

include:
  '#' 'include' STRING
| '#' 'include' HEADER
;

statement:
  unvaluable_statement
| return_statement
| valuable_statement
;

valuable_statement:
  ID #id_valuable
| array_element #not_id_valuable
| constant #not_id_valuable
| char_element #not_id_valuable
| assign_statement #not_id_valuable //要考虑强制转化
| relation_statement #not_id_valuable
| compute_statement #not_id_valuable
| logic_statement #not_id_valuable
| function_call #not_id_valuable
;

constant: INT #const_int
| FLOAT #const_float
;

char_element: Char ;

array_element:
  ID '[' valuable_statement ']';

string_element:
  ID '[' ID ']' #str_id
| ID '[' INT ']'#str_int
;

unvaluable_statement:
  CONTROL #control_unval
| variate_statement #not_control_unval
| if_statement #not_control_unval
| for_statement #not_control_unval
| while_statement #not_control_unval
| function_statement #not_control_unval
| array_statement #not_control_unval
;

array_statement: TYPE ID '[' INT ']' ';' #no_const_arr_sta
| TYPE ID '[' INT ']' '=' '{' constant (',' constant)* '}' ';' #const_arr_sta
| TYPE ID '[' INT ']' '=' STRING ';' #str_arr_sta
;

assign_statement:
  ID '=' valuable_statement #normal_assign
| ID '=' valuable_statement ';' #normal_assign
| ID ASSIGN_OP valuable_statement #op_assign
| ID ASSIGN_OP valuable_statement ';' #op_assign
| string_element '=' Char ';' #string_assign
| string_element '=' '(char)' ID ';' #string_assign_id
| array_element '=' valuable_statement ';' #array_assign
| unitary_statement #unitary_assign
;

ASSIGN_OP:
  '+=' | '-=' | '*=' | '/=' | '&=' | '^=' ;

TYPE:
'int' | 'float' | 'double' | 'char' | 'char*' | 'int*';

logic_statement:
  logic_statement LOGIC_OP logic_statement #logic_normal
| '(' logic_statement LOGIC_OP logic_statement ')' #logic_with_bracket
| relation_statement #logic_relation
| compute_statement #logic_compute
| NOT_OP logic_statement #logic_deny
| NOT_OP '(' logic_statement ')' #logic_deny_bracket
;

LOGIC_OP:
  '&&' | '||' ;

NOT_OP:
  '!' ;

relation_statement:
compute_statement RELATION_OP compute_statement #normal_relation
| compute_statement RELATION_OP Char #char_relation
;

RELATION_OP:
'>' | '>=' | '<' | '<=' | '==' | '!=' ;

compute_statement:
  array_element #comp_is_arr
| ID #comp_is_id
| constant #comp_is_constant
| compute_statement COMPUTE_OP compute_statement #comp_is_comp
| '(' compute_statement COMPUTE_OP compute_statement ')' #comp_with_bracket
| '(' TYPE ')' compute_statement #comp_casting
| '(' TYPE ')' '(' compute_statement ')' #comp_casting_bracket
| '(' TYPE ')' '(' Char ')' #comp_casting_char
| function_call #comp_func
;

COMPUTE_OP:
'+' | '-' | '*' | '/' | '|' | '&' | '^' ;

unitary_statement:
  ID UNITARY_OP #back_unit_id
| array_element UNITARY_OP #back_unit_arr
| UNITARY_OP ID #front_unit_id
| UNITARY_OP array_element #front_unit_arr
| ID UNITARY_OP ';' #back_unit_id
| array_element UNITARY_OP ';' #back_unit_arr
| UNITARY_OP ID ';' #front_unit_id
| UNITARY_OP array_element ';' #front_unit_arr
;

UNITARY_OP:
'++' | '--';

function_call:
  ID '(' ')' #no_param_call
| ID '(' ')' ';' #no_param_call
| ID '(' param (',' param)* ')' #param_call
| ID '(' param (',' param)* ')' ';'  #param_call
;

param:
  ID #param_id
| constant #param_const
| STRING #param_str
| array_element #param_arr
| function_call #param_func
;

return_statement:
  'return' valuable_statement ';' ;

variate_statement:
  TYPE ID ';' #variate_empty
| TYPE ID '=' valuable_statement ';' #variate_normal
| TYPE ID '=' '(' TYPE ')' valuable_statement ';' #variate_casting
| TYPE ID '=' Char ';' #variate_char
;

if_statement:
  if_sentence #only_if
| if_sentence else_sentence #if_else
| if_sentence (elseif_sentence)+ #if_elseif
| if_sentence (elseif_sentence)+ else_sentence #if_elseif_else
;

if_sentence:
  'if' '(' valuable_statement ')' '{' (statement)* '}' ;

elseif_sentence:
  'else if' '(' valuable_statement ')' '{' (statement)* '}' ;

else_sentence:
  'else' '{' (statement)* '}' ;

while_statement:
  'while' '(' valuable_statement ')' '{' (statement)* '}' ;

for_statement:
  'for' '(' for_init ';' (relation_statement)? (',' relation_statement)* ';' for_change ')' '{' (statement)* '}' ;

for_init:
  (assign_statement)? (',' assign_statement)* ;

for_change:
  (assign_statement)? (',' assign_statement)* ;

function_statement:
  'void' ID '(' ')' '{' (statement)* '}'
| 'void' ID '(' TYPE ID (',' TYPE ID)* ')' '{' (statement)* '}'
| TYPE ID '(' ')' '{' (statement)* '}'
| TYPE ID '(' TYPE ID (',' TYPE ID)* ')' '{' (statement)* '}'
;

ID: [A-Za-z_][A-Za-z_0-9]* ;
INT: ('-')?[0-9]+;
FLOAT: [0-9]*'.'[0-9]+ ;
STRING: '"' ~["]* '"' ;
HEADER: '<' ID ('.h')? '>';
Char: '\'' ('\\')?. '\'' ;
WS  : [ \t\r\n]+ -> skip ;
CONTROL: 'continue' ';' | 'break' ';' ;