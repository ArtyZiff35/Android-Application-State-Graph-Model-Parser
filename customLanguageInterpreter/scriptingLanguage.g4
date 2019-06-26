/*
 * Name of the Grammar (must be the same as the file name)
 */
grammar scriptingLanguage;

/*
 * Parser Rules
 */

// Test suite declaration
suite       :   WHEN apptype APP COL testlist;
apptype     :   APPCAT1 | APPCAT2 | APPCAT3 | APPCAT4 | APPCAT5 | APPCAT6 | APPCAT7 | APPCAT8 | APPCAT9 | APPCAT10;

// Specific test declaration
testlist    :   (testtype1 | testtype2 | testtype3 | testtype4 | testtype5 | testtype6 | testtype7 | testtype8)+;
testtype1   :   (testsame1 | testdiff1);
testtype2   :   (testsame2 | testdiff2);
testtype3   :   (testsame3 | testdiff3);
testtype4   :   (testsame4 | testdiff4);
testtype5   :   (testsame5 | testdiff5);
testtype6   :   (testsame6 | testdiff6);
testtype7   :   (testsame7 | testdiff7);
testtype8   :   (testsame8 | testdiff8);

testsame1   :   IN ACTTYPE1 CHECK FOR SAME STATE COL commandlist1;
testdiff1   :   IN ACTTYPE1 CHECK FOR DIFFERENT STATE activitytype COL commandlist1;
testsame2   :   IN ACTTYPE2 CHECK FOR SAME STATE COL commandlist2;
testdiff2   :   IN ACTTYPE2 CHECK FOR DIFFERENT STATE activitytype COL commandlist2;
testsame3   :   IN ACTTYPE3 CHECK FOR SAME STATE COL commandlist3;
testdiff3   :   IN ACTTYPE3 CHECK FOR DIFFERENT STATE activitytype COL commandlist3;
testsame4   :   IN ACTTYPE4 CHECK FOR SAME STATE COL commandlist4;
testdiff4   :   IN ACTTYPE4 CHECK FOR DIFFERENT STATE activitytype COL commandlist4;
testsame5   :   IN ACTTYPE5 CHECK FOR SAME STATE COL commandlist5;
testdiff5   :   IN ACTTYPE5 CHECK FOR DIFFERENT STATE activitytype COL commandlist5;
testsame6   :   IN ACTTYPE6 CHECK FOR SAME STATE COL commandlist6;
testdiff6   :   IN ACTTYPE6 CHECK FOR DIFFERENT STATE activitytype COL commandlist6;
testsame7   :   IN ACTTYPE7 CHECK FOR SAME STATE COL commandlist7;
testdiff7   :   IN ACTTYPE7 CHECK FOR DIFFERENT STATE activitytype COL commandlist7;
testsame8   :   IN ACTTYPE8 CHECK FOR SAME STATE COL commandlist8;
testdiff8   :   IN ACTTYPE8 CHECK FOR DIFFERENT STATE activitytype COL commandlist8;

activitytype    :   ACTTYPE1 | ACTTYPE2 | ACTTYPE3 | ACTTYPE4 | ACTTYPE5 | ACTTYPE6 | ACTTYPE7 | ACTTYPE8;

// Definition of commands for tests related to a specific Activity type
// To-do screen
commandlist1    :   (command1 SEMICOL)+;
command1        :   SAME DIFFERENT;
// Ads screen
commandlist2    :   (command2 SEMICOL)+;
command2        :   SAME DIFFERENT;
// Login screen
commandlist3    :   (command3 SEMICOL)+;
command3        :   INPUT NAME QUOTEDSTRING | INPUT PASSWORD QUOTEDSTRING | CLICK NEXT;
// List screen
commandlist4    :   (command4 SEMICOL)+;
command4        :   SAME DIFFERENT;
// Portal screen
commandlist5    :   (command5 SEMICOL);
command5        :   SAME DIFFERENT;
// Browser screen
commandlist6    :   (command6 SEMICOL)+;
command6        :   SAME DIFFERENT;
// Map screen
commandlist7    :   (command7 SEMICOL)+;
command7        :   SAME DIFFERENT;
// Messages screen
commandlist8    :   (command8 SEMICOL)+;
command8        :   SAME DIFFERENT;

/*
 * Lexer Rules
 */

// Fragments are used for case-insensitivity
fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];

// Declaration of words with fragments
WHEN        :   W H E N;
APP         :   A P P;
COL         :   ':';
SEMICOL     :   ';';
IN          :   I N;
CHECK       :   C H E C K;
FOR         :   F O R;
SAME        :   S A M E;
DIFFERENT   :   D I F F E R E N T;
STATE       :   S T A T E;
INPUT       :   I N P U T;
NAME        :   N A M E;
PASSWORD    :   P A S S W O R D;
CLICK       :   C L I C K;
NEXT        :   N E X T;

// Application APK categories
APPCAT1     :   N E W S;
APPCAT2     :   S H O P P I N G;
APPCAT3     :   S O C I A L;
APPCAT4     :   V I D E O;
APPCAT5     :   W E A T H E R;
APPCAT6     :   C O M M U N I C A T I O N;
APPCAT7     :   E D U C A T I O N;
APPCAT8     :   F O O D;
APPCAT9     :   M E D I C A L;
APPCAT10    :   A U D I O;

// Activity type categories
ACTTYPE1    :   T O D O;
ACTTYPE2    :   A D;
ACTTYPE3    :   L O G I N;
ACTTYPE4    :   L I S T;
ACTTYPE5    :   P O R T A L;
ACTTYPE6    :   B R O W S E R;
ACTTYPE7    :   M A P;
ACTTYPE8    :   M E S S A G E S;



QUOTEDSTRING        : '"'[-a-zA-Z0-9!@#$&()`.+,]*'"';
WHITESPACE          : (' ' | '\t')+ -> skip;
NEWLINE             : ('\r'? '\n' | '\r')+ -> skip;



