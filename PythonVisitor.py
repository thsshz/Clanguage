# Generated from Clanguage.g4 by ANTLR 4.7.1
from ClanguageVisitor import ClanguageVisitor
from ClanguageParser import ClanguageParser

# This class defines a complete generic visitor for a parse tree produced by ClanguageParser.

class PythonVisitor(ClanguageVisitor):
    def __init__(self):
        self.currSpace = 0
        self.res_code = ''
        self.assign_flag = False
        self.assign_char = ''
        self.array_assign_index = ''

    # Visit a parse tree produced by ClanguageParser#root.
    def visitRoot(self, ctx:ClanguageParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#include.
    def visitInclude(self, ctx:ClanguageParser.IncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#statement.
    def visitStatement(self, ctx:ClanguageParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#id_valuable.
    def visitId_valuable(self, ctx:ClanguageParser.Id_valuableContext):
        self.res_code += ctx.ID().getText()


    # Visit a parse tree produced by ClanguageParser#not_id_valuable.
    def visitNot_id_valuable(self, ctx:ClanguageParser.Not_id_valuableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#const_int.
    def visitConst_int(self, ctx:ClanguageParser.Const_intContext):
        self.res_code += ctx.INT().getText()


    # Visit a parse tree produced by ClanguageParser#const_float.
    def visitConst_float(self, ctx:ClanguageParser.Const_floatContext):
        self.res_code += ctx.FLOAT().getText()


    # Visit a parse tree produced by ClanguageParser#char_element.
    def visitChar_element(self, ctx:ClanguageParser.Char_elementContext):
        self.res_code += ctx.Char().getText()


    # Visit a parse tree produced by ClanguageParser#array_element.
    def visitArray_element(self, ctx:ClanguageParser.Array_elementContext):
        array_str = ctx.ID().getText() + '['
        self.res_code += array_str
        self.visit(ctx.valuable_statement())
        self.res_code += ']'

    # Visit a parse tree produced by ClanguageParser#control_unval.
    def visitControl_unval(self, ctx:ClanguageParser.Control_unvalContext):
        length = len(ctx.CONTROL().getText())
        self.res_code += ctx.CONTROL().getText()[0: length - 1]

    # Visit a parse tree produced by ClanguageParser#not_control_unval.
    def visitNot_control_unval(self, ctx:ClanguageParser.Not_control_unvalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#no_const_arr_sta.
    def visitNo_const_arr_sta(self, ctx:ClanguageParser.No_const_arr_staContext):
        if ctx.TYPE().getText() != 'char': # 不是字符串数组
            self.res_code += ctx.ID().getText() + ' = [0] * ' + ctx.INT().getText()
        else: # 字符串数组
            self.res_code += ctx.ID().getText() + " = ' ' * " + ctx.INT().getText()


    # Visit a parse tree produced by ClanguageParser#const_arr_sta.
    def visitConst_arr_sta(self, ctx:ClanguageParser.Const_arr_staContext):
        type_str = ctx.TYPE().getText()
        temp_str = ctx.ID().getText() + ' = ['
        init_num_count = len(ctx.constant())
        for i in range(init_num_count):
            if i != 0:
                temp_str += ', '
            temp_str += ctx.constant(i).getText()
        else:
            temp_str += ']'
        remain_count = int(ctx.INT().getText()) - len(ctx.constant())
        if remain_count > 0:
            temp_str += ' + [0] * ' + str(remain_count)

        self.res_code += temp_str


    # Visit a parse tree produced by ClanguageParser#str_arr_sta.
    def visitStr_arr_sta(self, ctx:ClanguageParser.Str_arr_staContext):
        self.res_code += ctx.ID().getText() + " = " + ctx.STRING().getText()


    # Visit a parse tree produced by ClanguageParser#normal_assign.
    def visitNormal_assign(self, ctx:ClanguageParser.Normal_assignContext):
        self.res_code += ctx.ID().getText() + ' = '
        self.assign_flag = True
        self.visit(ctx.valuable_statement())
        self.assign_flag = False


    # Visit a parse tree produced by ClanguageParser#op_assign.
    def visitOp_assign(self, ctx:ClanguageParser.Op_assignContext):
        self.res_code += ctx.ID().getText() + ' ' + ctx.ASSIGN_OP().getText() + ' '
        self.assign_flag = True
        self.visit(ctx.valuable_statement())
        self.assign_flag = False

    # Visit a parse tree produced by ClanguageParser#array_assign.
    def visitArray_assign(self, ctx:ClanguageParser.Array_assignContext):
        self.visit(ctx.array_element())
        self.res_code += ' = '
        self.assign_flag = True
        self.visit(ctx.valuable_statement())
        self.assign_flag = False

    # Visit a parse tree produced by ClanguageParser#string_assign.
    def visitString_assign(self, ctx:ClanguageParser.String_assignContext):
        self.assign_char = ctx.Char().getText()
        self.visit(ctx.string_element())

    # Visit a parse tree produced by ClanguageParser#string_assign_id.
    def visitString_assign_id(self, ctx:ClanguageParser.String_assign_idContext):
        self.assign_char = ctx.ID().getText()
        self.visit(ctx.string_element())

    # Visit a parse tree produced by ClanguageParser#logic_deny.
    def visitLogic_deny(self, ctx:ClanguageParser.Logic_denyContext):
        self.res_code += 'not '
        self.visit(ctx.logic_statement())

    # Visit a parse tree produced by ClanguageParser#logic_deny_bracket.
    def visitLogic_deny_bracket(self, ctx: ClanguageParser.Logic_deny_bracketContext):
        self.res_code += 'not ('
        self.visit(ctx.logic_statement())
        self.res_code += ')'

    # Visit a parse tree produced by ClanguageParser#logic_compute.
    def visitLogic_compute(self, ctx:ClanguageParser.Logic_computeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#logic_relation.
    def visitLogic_relation(self, ctx:ClanguageParser.Logic_relationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#logic_with_bracket.
    def visitLogic_with_bracket(self, ctx:ClanguageParser.Logic_with_bracketContext):
        self.res_code += '('
        self.visit(ctx.logic_statement(0))
        raw_op = ctx.LOGIC_OP().getText()
        op = ''
        if raw_op == '&&':
            op = 'and'
        elif raw_op == '||':
            op = 'or'
        self.res_code += ' ' + op + ' '
        self.visit(ctx.logic_statement(1))
        self.res_code += ')'


    # Visit a parse tree produced by ClanguageParser#logic_normal.
    def visitLogic_normal(self, ctx:ClanguageParser.Logic_normalContext):
        self.visit(ctx.logic_statement(0))
        raw_op = ctx.LOGIC_OP().getText()
        op = ''
        if raw_op == '&&':
            op = 'and'
        elif raw_op == '||':
            op = 'or'
        self.res_code += ' ' + op + ' '
        self.visit(ctx.logic_statement(1))


    # Visit a parse tree produced by ClanguageParser#normal_relation.
    def visitNormal_relation(self, ctx:ClanguageParser.Normal_relationContext):
        self.visit(ctx.compute_statement(0))
        self.res_code += ' ' + ctx.RELATION_OP().getText() + ' '
        self.visit(ctx.compute_statement(1))

    # Visit a parse tree produced by ClanguageParser#char_relation.
    def visitChar_relation(self, ctx:ClanguageParser.Char_relationContext):
        self.visit(ctx.compute_statement())
        self.res_code += ' ' + ctx.RELATION_OP().getText() + ' ' + ctx.Char().getText()


    # Visit a parse tree produced by ClanguageParser#comp_is_arr.
    def visitComp_is_arr(self, ctx:ClanguageParser.Comp_is_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#comp_is_comp.
    def visitComp_is_comp(self, ctx:ClanguageParser.Comp_is_compContext):
        self.visit(ctx.compute_statement(0))
        self.res_code += ' ' + ctx.COMPUTE_OP().getText() + ' '
        self.visit(ctx.compute_statement(1))


    # Visit a parse tree produced by ClanguageParser#comp_is_id.
    def visitComp_is_id(self, ctx:ClanguageParser.Comp_is_idContext):
        self.res_code += ctx.ID().getText()


    # Visit a parse tree produced by ClanguageParser#comp_with_bracket.
    def visitComp_with_bracket(self, ctx:ClanguageParser.Comp_with_bracketContext):
        self.res_code += '('
        self.visit(ctx.compute_statement(0))
        self.res_code += ' ' + ctx.COMPUTE_OP().getText() + ' '
        self.visit(ctx.compute_statement(1))
        self.res_code += ')'


    # Visit a parse tree produced by ClanguageParser#comp_is_constant.
    def visitComp_is_constant(self, ctx:ClanguageParser.Comp_is_constantContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClanguageParser#comp_casting.
    def visitComp_casting(self, ctx:ClanguageParser.Comp_castingContext):
        type = ctx.TYPE().getText()
        py_type = ''
        if type == 'float' or type == 'double':
            py_type = 'double'
        else:
            py_type = type

        self.res_code += py_type + '('
        self.visit(ctx.compute_statement())
        self.res_code += ')'

    # Visit a parse tree produced by ClanguageParser#comp_casting_char.
    def visitComp_casting_char(self, ctx:ClanguageParser.Comp_casting_charContext):
        self.res_code += ctx.TYPE().getText() + '(' + ctx.Char().getText() + ')'

    # Visit a parse tree produced by ClanguageParser#comp_casting_bracket.
    def visitComp_casting_bracket(self, ctx:ClanguageParser.Comp_casting_bracketContext):
        type = ctx.TYPE().getText()
        py_type = ''
        if type == 'float' or type == 'double':
            py_type = 'double'
        else:
            py_type = type

        self.res_code += py_type + '('
        self.visit(ctx.compute_statement())
        self.res_code += ')'

    # Visit a parse tree produced by ClanguageParser#front_unit_id.
    def visitFront_unit_id(self, ctx:ClanguageParser.Front_unit_idContext):
        if self.assign_flag:
            op = ''
            if ctx.UNITARY_OP().getText() == '++':
                op = '+'
            else:
                op = '-'
            self.res_code += ctx.ID().getText() + ' ' + op + ' 1\n'
            for i in range(self.currSpace):
                self.res_code += ' '
            self.res_code += ctx.ID().getText() + ' ' + op + '= 1'
        else:
            if ctx.UNITARY_OP().getText() == '++':
                self.res_code += ctx.ID().getText() + ' += 1'
            else:
                self.res_code += ctx.ID().getText() + ' -= 1'


    # Visit a parse tree produced by ClanguageParser#front_unit_arr.
    def visitFront_unit_arr(self, ctx:ClanguageParser.Front_unit_arrContext):
        if self.assign_flag:
            op = ''
            if ctx.UNITARY_OP().getText() == '++':
                op = '+'
            else:
                op = '-'
            self.visit(ctx.array_element())
            self.res_code += ' ' + op + ' 1\n'
            for i in range(self.currSpace):
                self.res_code += ' '
            self.visit(ctx.array_element())
            self.res_code += ' ' + op + '= 1'
        else:
            self.visit(ctx.array_element())
            if ctx.UNITARY_OP().getText() == '++':
                self.res_code += ' += 1'
            else:

                self.res_code += ' -= 1'


    # Visit a parse tree produced by ClanguageParser#back_unit_id.
    def visitBack_unit_id(self, ctx:ClanguageParser.Back_unit_idContext):
        if self.assign_flag:
            op = ''
            if ctx.UNITARY_OP().getText() == '++':
                op = '+'
            else:
                op = '-'
            self.res_code += ctx.ID().getText() + '\n'
            for i in range(self.currSpace):
                self.res_code += ' '
            self.res_code += ctx.ID().getText() + ' ' + op + '= 1'
        else:
            if ctx.UNITARY_OP().getText() == '++':
                self.res_code += ctx.ID().getText() + ' += 1'
            else:
                self.res_code += ctx.ID().getText() + ' -= 1'


    # Visit a parse tree produced by ClanguageParser#back_unit_arr.
    def visitBack_unit_arr(self, ctx:ClanguageParser.Back_unit_arrContext):
        if self.assign_flag:
            op = ''
            if ctx.UNITARY_OP().getText() == '++':
                op = '+'
            else:
                op = '-'
            self.visit(ctx.array_element())
            self.res_code += '\n'
            for i in range(self.currSpace):
                self.res_code += ' '
            self.visit(ctx.array_element())
            self.res_code += ' ' + op + '= 1'
        else:
            self.visit(ctx.array_element())
            if ctx.UNITARY_OP().getText() == '++':
                self.res_code += ' += 1'
            else:

                self.res_code += ' -= 1'

    # Visit a parse tree produced by ClanguageParser#no_param_call.
    def visitNo_param_call(self, ctx:ClanguageParser.No_param_callContext):
        self.res_code += ctx.ID().getText() + '()'


    # Visit a parse tree produced by ClanguageParser#param_call.
    def visitParam_call(self, ctx:ClanguageParser.Param_callContext):
        function_name = ctx.ID().getText()
        if function_name == 'strlen':
            self.res_code += 'len('
            self.visit(ctx.param(0))
            self.res_code += ')'
        elif function_name == 'gets':
            self.visit(ctx.param(0))
            self.res_code += ' = input()'
        elif function_name == 'printf':
            param_count = len(ctx.param())
            if param_count > 1:
                self.res_code += 'print('
                self.visit(ctx.param(0))
                self.res_code += ' % ('
                for i in range(1, param_count):
                    if i > 1:
                        self.res_code += ', '
                    self.visit(ctx.param(i))
                self.res_code += '), end="")'
            else:
                self.res_code += 'print('
                self.visit(ctx.param(0))
                self.res_code += ', end="")'
        elif function_name == 'atoi':
            self.res_code += 'int('
            self.visit(ctx.param(0))
            self.res_code += ')'
        elif function_name == 'isdigit':
            self.visit(ctx.param(0))
            self.res_code += '.isdigit()'
        elif function_name == 'strcmp':
            self.visit(ctx.param(0))
            self.res_code += ' == '
            self.visit(ctx.param(1))
        else:
            self.res_code += ctx.ID().getText() + '('
            if (len(ctx.param()) == 1):
                self.visit(ctx.param(0))
            if (len(ctx.param()) > 1):
                for i in range(0, len(ctx.param())):
                    if i != 0:
                        self.res_code += ', '
                    self.visit(ctx.param(i))
            self.res_code += ')'


    # Visit a parse tree produced by ClanguageParser#param_id.
    def visitParam_id(self, ctx:ClanguageParser.Param_idContext):
        self.res_code += ctx.ID().getText()


    # Visit a parse tree produced by ClanguageParser#param_const.
    def visitParam_const(self, ctx:ClanguageParser.Param_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#param_str.
    def visitParam_str(self, ctx:ClanguageParser.Param_strContext):
        self.res_code += ctx.STRING().getText()


    # Visit a parse tree produced by ClanguageParser#param_arr.
    def visitParam_arr(self, ctx:ClanguageParser.Param_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#return_statement.
    def visitReturn_statement(self, ctx:ClanguageParser.Return_statementContext):
        self.res_code += 'return '
        self.visit(ctx.valuable_statement())


    # Visit a parse tree produced by ClanguageParser#variate_empty.
    def visitVariate_empty(self, ctx:ClanguageParser.Variate_emptyContext):
        self.res_code += ctx.ID().getText() + ' = None'
        if self.currSpace == 0:
            self.res_code += '\n'


    # Visit a parse tree produced by ClanguageParser#variate_normal.
    def visitVariate_normal(self, ctx:ClanguageParser.Variate_normalContext):
        self.res_code += ctx.ID().getText() + ' = '
        self.visit(ctx.valuable_statement())
        if self.currSpace == 0:
            self.res_code += '\n'


    # Visit a parse tree produced by ClanguageParser#variate_casting.
    def visitVariate_casting(self, ctx:ClanguageParser.Variate_castingContext):
        self.res_code += ctx.ID().getText() + ' = ' + ctx.TYPE(1).getText() + '('
        self.visit(ctx.valuable_statement())
        self.res_code += ')'
        if self.currSpace == 0:
            self.res_code += '\n'


    # Visit a parse tree produced by ClanguageParser#variate_char.
    def visitVariate_char(self, ctx:ClanguageParser.Variate_charContext):
        self.res_code += ctx.ID().getText() + ' = ' + ctx.Char().getText()
        if self.currSpace == 0:
            self.res_code += '\n'


    # Visit a parse tree produced by ClanguageParser#only_if.
    def visitOnly_if(self, ctx:ClanguageParser.Only_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#if_else.
    def visitIf_else(self, ctx:ClanguageParser.If_elseContext):
        self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#if_elseif.
    def visitIf_elseif(self, ctx:ClanguageParser.If_elseifContext):
        self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#if_elseif_else.
    def visitIf_elseif_else(self, ctx:ClanguageParser.If_elseif_elseContext):
        self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#if_sentence.
    def visitIf_sentence(self, ctx:ClanguageParser.If_sentenceContext):
        self.res_code += 'if '
        self.visit(ctx.valuable_statement())
        self.res_code += ':\n'
        self.currSpace += 4
        if (len(ctx.statement()) == 1):
            for i in range(0, self.currSpace):
                self.res_code += ' '
            self.visit(ctx.statement(0))
            self.res_code += '\n'
        elif (len(ctx.statement()) > 1):
            for i in range(0, len(ctx.statement())):
                for j in range(0, self.currSpace):
                    self.res_code += ' '
                self.visit(ctx.statement(i))
                self.res_code += '\n'
        else:
            for i in range(0, self.currSpace):
                self.res_code += ' '
            self.res_code += 'pass\n'
        self.currSpace -= 4


    # Visit a parse tree produced by ClanguageParser#elseif_sentence.
    def visitElseif_sentence(self, ctx:ClanguageParser.Elseif_sentenceContext):
        for k in range(0, self.currSpace):
            self.res_code += ' '
        self.res_code += 'elif '
        self.visit(ctx.valuable_statement())
        self.res_code += ':\n'
        self.currSpace += 4
        if (len(ctx.statement()) == 1):
            for i in range(0, self.currSpace):
                self.res_code += ' '
            self.visit(ctx.statement(0))
            self.res_code += '\n'
        if (len(ctx.statement()) > 1):
            for i in range(0, len(ctx.statement())):
                for j in range(0, self.currSpace):
                    self.res_code += ' '
                self.visit(ctx.statement(i))
                self.res_code += '\n'
        self.currSpace -= 4


    # Visit a parse tree produced by ClanguageParser#else_sentence.
    def visitElse_sentence(self, ctx:ClanguageParser.Else_sentenceContext):
        for k in range(0, self.currSpace):
            self.res_code += ' '
        self.res_code += 'else:\n'
        self.currSpace += 4
        if (len(ctx.statement()) == 1):
            for i in range(0, self.currSpace):
                self.res_code += ' '
            self.visit(ctx.statement(0))
            self.res_code += '\n'
        if (len(ctx.statement()) > 1):
            for i in range(0, len(ctx.statement())):
                for j in range(0, self.currSpace):
                    self.res_code += ' '
                self.visit(ctx.statement(i))
                self.res_code += '\n'
        self.currSpace -= 4


    # Visit a parse tree produced by ClanguageParser#while_statement.
    def visitWhile_statement(self, ctx:ClanguageParser.While_statementContext):
        self.res_code += 'while '
        self.visit(ctx.valuable_statement())
        self.res_code += ':\n'
        self.currSpace += 4
        if (len(ctx.statement()) == 1):
            for i in range(0, self.currSpace):
                self.res_code += ' '
            self.visit(ctx.statement(0))
            self.res_code += '\n'
        if (len(ctx.statement()) > 1):
            for i in range(0, len(ctx.statement())):
                for j in range(0, self.currSpace):
                    self.res_code += ' '
                self.visit(ctx.statement(i))
                self.res_code += '\n'
        self.currSpace -= 4


    # Visit a parse tree produced by ClanguageParser#for_statement.
    def visitFor_statement(self, ctx:ClanguageParser.For_statementContext):
        self.visit(ctx.for_init())
        for j in range(self.currSpace):
            self.res_code += ' '
        self.res_code += 'while '
        for i in range(0, len(ctx.relation_statement())):
            if i > 0:
                self.res_code += ' and '
            self.visit(ctx.relation_statement(i))
        else:
            self.res_code += ':\n'
        self.currSpace += 4
        for i in range(0, len(ctx.statement())):
            for j in range(0, self.currSpace):
                self.res_code += ' '
            self.visit(ctx.statement(i))
            self.res_code += '\n'
        self.visit(ctx.for_change())
        self.currSpace -= 4


    # Visit a parse tree produced by ClanguageParser#for_init.
    def visitFor_init(self, ctx: ClanguageParser.For_initContext):
        for i in range(len(ctx.assign_statement())):
            if i > 0:
                for j in range(self.currSpace):
                    self.res_code += ' '
            self.visit(ctx.assign_statement(i))
            self.res_code += '\n'

    # Visit a parse tree produced by ClanguageParser#for_change.
    def visitFor_change(self, ctx: ClanguageParser.For_changeContext):
        for i in range(len(ctx.assign_statement())):
            for j in range(self.currSpace):
                self.res_code += ' '
            self.visit(ctx.assign_statement(i))
            self.res_code += '\n'

    # Visit a parse tree produced by ClanguageParser#function_statement.
    def visitFunction_statement(self, ctx:ClanguageParser.Function_statementContext):
        str = ''
        if (len(ctx.ID()) > 1):
            for i in range(1, len(ctx.ID())):
                str += ctx.ID(i).getText()
                if (i != len(ctx.ID()) - 1):
                    str += ', '
        self.res_code += 'def ' + ctx.ID(0).getText() + '(' + str + '):\n'
        self.currSpace += 4
        if (len(ctx.statement()) == 1):
            for i in range(0, self.currSpace):
                self.res_code += ' '
            self.visit(ctx.statement(0))
            self.res_code += '\n'
        if (len(ctx.statement()) > 1):
            for i in range(0, len(ctx.statement())):
                for j in range(0, self.currSpace):
                    self.res_code += ' '
                self.visit(ctx.statement(i))
                self.res_code += '\n'
        self.currSpace -= 4
        self.res_code += '\n'

    # Visit a parse tree produced by ClanguageParser#str_id.
    def visitStr_id(self, ctx:ClanguageParser.Str_idContext):
        self.res_code += ctx.ID(0).getText() + ' = ' + ctx.ID(0).getText() + '[:' + ctx.ID(1).getText() + '] + ' + self.assign_char + \
                        ' + ' + ctx.ID(0).getText() + '[' + ctx.ID(1).getText() + ' + 1:]'


    # Visit a parse tree produced by ClanguageParser#str_int.
    def visitStr_int(self, ctx:ClanguageParser.Str_intContext):
        self.res_code += ctx.ID().getText() + ' = ' + ctx.ID().getText() + '[:' + ctx.INT().getText() + '] + ' + self.assign_char + \
                         ' + ' + ctx.ID().getText() + '[' + ctx.INT().getText() + ' + 1:]'



del ClanguageParser