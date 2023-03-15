start: entity
entity: IDENTIFIER
       | enclosed_expr
       | or_expr
       | and_expr
       | not_expr
or_expr: entity "|" entity
and_expr: entity "&" entity
not_expr: "!" entity
enclosed_expr: "(" entity ")"
IDENTIFIER: ("_"|LETTER) ("_"|LETTER|DIGIT)*
LCASE_LETTER: "a".."z"
UCASE_LETTER: "A".."Z"
LETTER: UCASE_LETTER | LCASE_LETTER
DIGIT: "0".."9"
%import common.WS
%ignore WS
