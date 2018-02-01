# Generated from Clanguage.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ClanguageParser import ClanguageParser
else:
    from ClanguageParser import ClanguageParser

# This class defines a complete generic visitor for a parse tree produced by ClanguageParser.

class ClanguageVisitor(ParseTreeVisitor):

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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#not_id_valuable.
    def visitNot_id_valuable(self, ctx:ClanguageParser.Not_id_valuableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#const_int.
    def visitConst_int(self, ctx:ClanguageParser.Const_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#const_float.
    def visitConst_float(self, ctx:ClanguageParser.Const_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#char_element.
    def visitChar_element(self, ctx:ClanguageParser.Char_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#array_element.
    def visitArray_element(self, ctx:ClanguageParser.Array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#str_id.
    def visitStr_id(self, ctx:ClanguageParser.Str_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#str_int.
    def visitStr_int(self, ctx:ClanguageParser.Str_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#control_unval.
    def visitControl_unval(self, ctx:ClanguageParser.Control_unvalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#not_control_unval.
    def visitNot_control_unval(self, ctx:ClanguageParser.Not_control_unvalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#no_const_arr_sta.
    def visitNo_const_arr_sta(self, ctx:ClanguageParser.No_const_arr_staContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#const_arr_sta.
    def visitConst_arr_sta(self, ctx:ClanguageParser.Const_arr_staContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#str_arr_sta.
    def visitStr_arr_sta(self, ctx:ClanguageParser.Str_arr_staContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#normal_assign.
    def visitNormal_assign(self, ctx:ClanguageParser.Normal_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#op_assign.
    def visitOp_assign(self, ctx:ClanguageParser.Op_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#string_assign.
    def visitString_assign(self, ctx:ClanguageParser.String_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#string_assign_id.
    def visitString_assign_id(self, ctx:ClanguageParser.String_assign_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#array_assign.
    def visitArray_assign(self, ctx:ClanguageParser.Array_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#unitary_assign.
    def visitUnitary_assign(self, ctx:ClanguageParser.Unitary_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#logic_deny.
    def visitLogic_deny(self, ctx:ClanguageParser.Logic_denyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#logic_compute.
    def visitLogic_compute(self, ctx:ClanguageParser.Logic_computeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#logic_relation.
    def visitLogic_relation(self, ctx:ClanguageParser.Logic_relationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#logic_deny_bracket.
    def visitLogic_deny_bracket(self, ctx:ClanguageParser.Logic_deny_bracketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#logic_with_bracket.
    def visitLogic_with_bracket(self, ctx:ClanguageParser.Logic_with_bracketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#logic_normal.
    def visitLogic_normal(self, ctx:ClanguageParser.Logic_normalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#normal_relation.
    def visitNormal_relation(self, ctx:ClanguageParser.Normal_relationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#char_relation.
    def visitChar_relation(self, ctx:ClanguageParser.Char_relationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#comp_is_arr.
    def visitComp_is_arr(self, ctx:ClanguageParser.Comp_is_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#comp_is_comp.
    def visitComp_is_comp(self, ctx:ClanguageParser.Comp_is_compContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#comp_casting_bracket.
    def visitComp_casting_bracket(self, ctx:ClanguageParser.Comp_casting_bracketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#comp_is_id.
    def visitComp_is_id(self, ctx:ClanguageParser.Comp_is_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#comp_with_bracket.
    def visitComp_with_bracket(self, ctx:ClanguageParser.Comp_with_bracketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#comp_casting_char.
    def visitComp_casting_char(self, ctx:ClanguageParser.Comp_casting_charContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#comp_casting.
    def visitComp_casting(self, ctx:ClanguageParser.Comp_castingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#comp_is_constant.
    def visitComp_is_constant(self, ctx:ClanguageParser.Comp_is_constantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#comp_func.
    def visitComp_func(self, ctx:ClanguageParser.Comp_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#back_unit_id.
    def visitBack_unit_id(self, ctx:ClanguageParser.Back_unit_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#back_unit_arr.
    def visitBack_unit_arr(self, ctx:ClanguageParser.Back_unit_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#front_unit_id.
    def visitFront_unit_id(self, ctx:ClanguageParser.Front_unit_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#front_unit_arr.
    def visitFront_unit_arr(self, ctx:ClanguageParser.Front_unit_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#no_param_call.
    def visitNo_param_call(self, ctx:ClanguageParser.No_param_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#param_call.
    def visitParam_call(self, ctx:ClanguageParser.Param_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#param_id.
    def visitParam_id(self, ctx:ClanguageParser.Param_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#param_const.
    def visitParam_const(self, ctx:ClanguageParser.Param_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#param_str.
    def visitParam_str(self, ctx:ClanguageParser.Param_strContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#param_arr.
    def visitParam_arr(self, ctx:ClanguageParser.Param_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#param_func.
    def visitParam_func(self, ctx:ClanguageParser.Param_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#return_statement.
    def visitReturn_statement(self, ctx:ClanguageParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#variate_empty.
    def visitVariate_empty(self, ctx:ClanguageParser.Variate_emptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#variate_normal.
    def visitVariate_normal(self, ctx:ClanguageParser.Variate_normalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#variate_casting.
    def visitVariate_casting(self, ctx:ClanguageParser.Variate_castingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#variate_char.
    def visitVariate_char(self, ctx:ClanguageParser.Variate_charContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#only_if.
    def visitOnly_if(self, ctx:ClanguageParser.Only_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#if_else.
    def visitIf_else(self, ctx:ClanguageParser.If_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#if_elseif.
    def visitIf_elseif(self, ctx:ClanguageParser.If_elseifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#if_elseif_else.
    def visitIf_elseif_else(self, ctx:ClanguageParser.If_elseif_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#if_sentence.
    def visitIf_sentence(self, ctx:ClanguageParser.If_sentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#elseif_sentence.
    def visitElseif_sentence(self, ctx:ClanguageParser.Elseif_sentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#else_sentence.
    def visitElse_sentence(self, ctx:ClanguageParser.Else_sentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#while_statement.
    def visitWhile_statement(self, ctx:ClanguageParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#for_statement.
    def visitFor_statement(self, ctx:ClanguageParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#for_init.
    def visitFor_init(self, ctx:ClanguageParser.For_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#for_change.
    def visitFor_change(self, ctx:ClanguageParser.For_changeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClanguageParser#function_statement.
    def visitFunction_statement(self, ctx:ClanguageParser.Function_statementContext):
        return self.visitChildren(ctx)



del ClanguageParser