#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int Priority(char op)
{
    if (op=='#') {
        return 0;
    }
    if (op=='+' || op=='-') {
        return 1;
    }
    if (op=='*' || op=='/') {
        return 2;
    }
    return -1;
}

double Operate(double x,double y,char op)
{
    if (op=='+') {
        return x+y;
    }
    if (op=='-') {
        return x-y;
    }
    if (op=='*') {
        return x*y;
    }
    if (op=='/') {
        return x/y;
    }
    return -1;
}

double Calc(char* compute_str)
{
    double stDit[300];
    char stOp[300];
    int top1;
    int top2;

    double x;
    double y;
    double tmp;
    char op;
    int i;
    int n = strlen(compute_str);

    top1 = -1;
    top2 = -1;
    top2++;
    stOp[top2] = '#';
    compute_str[n] = '#';
    n++;
    for(i=0; i < n; i++)
    {
        if (compute_str[i]==' ' || compute_str[i] == '\n' || compute_str[i] == '\t') {

        }
        else if (isdigit(compute_str[i]))
        {
            tmp = (int)(compute_str[i]) - (int)('0');
            while(isdigit(compute_str[i+1])) {
                i ++;
                tmp = tmp * 10 + (int)(compute_str[i]) - (int)('0');
            }
            top1++;
            stDit[top1] = tmp;
        }
        else if(compute_str[i] == '(') {
            top2++;
            stOp[top2] = compute_str[i];
        }
        else if (compute_str[i] == ')') {
            while(stOp[top2] != '(')  {
                y = stDit[top1];
                top1--;
                x = stDit[top1];
                top1--;
                op = stOp[top2];
                top2--;
                top1++;
                stDit[top1] = Operate(x,y,op);
            }
            top2 --;
        }
        else
        {
            while (Priority(stOp[top2]) >= Priority(compute_str[i]))
            {
                if (compute_str[i]=='#' && stOp[top2]=='#') {
                    return stDit[top1];
                }
                y = stDit[top1];
                top1--;
                x = stDit[top1];
                top1--;
                op = stOp[top2];
                top2--;
                top1++;
                stDit[top1] = Operate(x,y,op);
            }
            top2++;
            char temp = compute_str[i];
            stOp[top2] = (char)temp;
        }
    }
    return stDit[top1];
}

int main()
{
    char compute_str[100];
    printf("Please enter an arithmetic expression, less than 100 characters:\n");
    gets(compute_str);
    printf("%.2lf\n", Calc(compute_str));
    return 0;
}
